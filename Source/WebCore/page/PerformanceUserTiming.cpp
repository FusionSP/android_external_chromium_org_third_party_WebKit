/*
 * Copyright (C) 2012 Intel Inc. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY APPLE INC. ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE INC. OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include "config.h"
#include "PerformanceUserTiming.h"

#if ENABLE(USER_TIMING)

#include "Performance.h"
#include "PerformanceMark.h"
#include "PerformanceMeasure.h"
#include <wtf/dtoa/utils.h>
#include <wtf/text/WTFString.h>

namespace WebCore {

HashMap<String, NavigationTimingFunction> UserTiming::m_restrictedKeyMap;

UserTiming::UserTiming(Performance* performance)
    : m_performance(performance)
{
    static const struct RestrictedField {
        String key;
        NavigationTimingFunction navigationTimingFunction;
    } defaultRestrictions[] = {
        {"navigationStart", &PerformanceTiming::navigationStart},
        {"unloadEventStart", &PerformanceTiming::unloadEventStart},
        {"unloadEventEnd", &PerformanceTiming::unloadEventEnd},
        {"redirectStart", &PerformanceTiming::redirectStart},
        {"redirectEnd", &PerformanceTiming::redirectEnd},
        {"fetchStart", &PerformanceTiming::fetchStart},
        {"domainLookupStart", &PerformanceTiming::domainLookupStart},
        {"domainLookupEnd", &PerformanceTiming::domainLookupEnd},
        {"connectStart", &PerformanceTiming::connectStart},
        {"connectEnd", &PerformanceTiming::connectEnd},
        {"secureConnectionStart", &PerformanceTiming::secureConnectionStart},
        {"requestStart", &PerformanceTiming::requestStart},
        {"responseStart", &PerformanceTiming::responseStart},
        {"responseEnd", &PerformanceTiming::responseEnd},
        {"domLoading", &PerformanceTiming::domLoading},
        {"domInteractive", &PerformanceTiming::domInteractive},
        {"domContentLoadedEventStart", &PerformanceTiming::domContentLoadedEventStart},
        {"domContentLoadedEventEnd", &PerformanceTiming::domContentLoadedEventEnd},
        {"domComplete", &PerformanceTiming::domComplete},
        {"loadEventStart", &PerformanceTiming::loadEventStart},
        {"loadEventEnd", &PerformanceTiming::loadEventEnd}
    };

    if (!m_restrictedKeyMap.isEmpty())
        return;

    for (const struct RestrictedField* restriction = defaultRestrictions;
        static_cast<unsigned>(restriction - defaultRestrictions) < ARRAY_SIZE(defaultRestrictions);
        ++restriction) {
        m_restrictedKeyMap.add(restriction->key, restriction->navigationTimingFunction);
    }
}

static void insertPerformanceEntry(PerformanceEntryMap& performanceEntryMap, PassRefPtr<PerformanceEntry> performanceEntry)
{
    RefPtr<PerformanceEntry> entry = performanceEntry;
    PerformanceEntryMap::iterator it = performanceEntryMap.find(entry->name());
    if (it != performanceEntryMap.end())
        it->value.append(entry);
    else {
        Vector<RefPtr<PerformanceEntry> > v(1);
        v[0] = entry;
        performanceEntryMap.set(entry->name(), v);
    }
}

static void clearPeformanceEntries(PerformanceEntryMap& performanceEntryMap, const String& name)
{
    if (name.isNull()) {
        performanceEntryMap.clear();
        return;
    }

    if (performanceEntryMap.contains(name))
        performanceEntryMap.remove(name);
}

void UserTiming::mark(const String& markName, ExceptionCode& ec)
{
    ec = 0;
    if (m_restrictedKeyMap.contains(markName)) {
        ec = SYNTAX_ERR;
        return;
    }

    double startTime = m_performance->now();
    insertPerformanceEntry(m_marksMap, PerformanceMark::create(markName, startTime));
}

void UserTiming::clearMarks(const String& markName)
{
    clearPeformanceEntries(m_marksMap, markName);
}

double UserTiming::findExistingMarkStartTime(const String& markName, ExceptionCode& ec)
{
    ec = 0;

    if (m_marksMap.contains(markName))
        return m_marksMap.get(markName).last()->startTime();

    if (m_restrictedKeyMap.contains(markName))
        return static_cast<double>((m_performance->timing()->*(m_restrictedKeyMap.get(markName)))()) - m_performance->timing()->navigationStart();

    ec = SYNTAX_ERR;
    return 0.0;
}

void UserTiming::measure(const String& measureName, const String& startMark, const String& endMark, ExceptionCode& ec)
{
    double startTime = 0.0;
    double endTime = 0.0;

    if (startMark.isNull())
        endTime = m_performance->now();
    else if (endMark.isNull()) {
        endTime = m_performance->now();
        startTime = findExistingMarkStartTime(startMark, ec);
        if (ec)
            return;
    } else {
        endTime = findExistingMarkStartTime(endMark, ec);
        if (ec)
            return;
        startTime = findExistingMarkStartTime(startMark, ec);
        if (ec)
            return;
    }

    insertPerformanceEntry(m_measuresMap, PerformanceMeasure::create(measureName, startTime, endTime - startTime));
}

void UserTiming::clearMeasures(const String& measureName)
{
    clearPeformanceEntries(m_measuresMap, measureName);
}

static Vector<RefPtr<PerformanceEntry> > convertToEntrySequence(const PerformanceEntryMap& performanceEntryMap)
{
    Vector<RefPtr<PerformanceEntry> > entries;

    for (PerformanceEntryMap::const_iterator it = performanceEntryMap.begin(); it != performanceEntryMap.end(); ++it)
        entries.append(it->value);

    return entries;
}

static Vector<RefPtr<PerformanceEntry> > getEntrySequenceByName(const PerformanceEntryMap& performanceEntryMap, const String& name)
{
    Vector<RefPtr<PerformanceEntry> > entries;

    PerformanceEntryMap::const_iterator it = performanceEntryMap.find(name);
    if (it != performanceEntryMap.end())
        entries.append(it->value);

    return entries;
}

Vector<RefPtr<PerformanceEntry> > UserTiming::getMarks() const
{
    return convertToEntrySequence(m_marksMap);
}

Vector<RefPtr<PerformanceEntry> > UserTiming::getMarks(const String& name) const
{
    return getEntrySequenceByName(m_marksMap, name);
}

Vector<RefPtr<PerformanceEntry> > UserTiming::getMeasures() const
{
    return convertToEntrySequence(m_measuresMap);
}

Vector<RefPtr<PerformanceEntry> > UserTiming::getMeasures(const String& name) const
{
    return getEntrySequenceByName(m_measuresMap, name);
}

} // namespace WebCore

#endif // ENABLE(USER_TIMING)
