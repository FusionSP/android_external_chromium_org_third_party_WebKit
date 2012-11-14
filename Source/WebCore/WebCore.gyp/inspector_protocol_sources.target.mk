# This file is generated by gyp; do not edit.

include $(CLEAR_VARS)

LOCAL_MODULE_CLASS := GYP
LOCAL_MODULE := third_party_WebKit_Source_WebCore_WebCore_gyp_inspector_protocol_sources_gyp
LOCAL_MODULE_STEM := inspector_protocol_sources
LOCAL_MODULE_SUFFIX := .stamp
LOCAL_MODULE_TAGS := optional
gyp_intermediate_dir := $(call local-intermediates-dir)
gyp_shared_intermediate_dir := $(call intermediates-dir-for,GYP,shared)

# Make sure our deps are built first.
GYP_TARGET_DEPENDENCIES := \
	$(call intermediates-dir-for,GYP,third_party_WebKit_Source_WebCore_WebCore_gyp_generate_inspector_protocol_version_gyp)/generate_inspector_protocol_version.stamp

### Rules for action "generateInspectorProtocolSources":
$(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp: gyp_local_path := $(LOCAL_PATH)
$(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp: gyp_intermediate_dir := $(GYP_ABS_ANDROID_TOP_DIR)/$(gyp_intermediate_dir)
$(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp: gyp_shared_intermediate_dir := $(GYP_ABS_ANDROID_TOP_DIR)/$(gyp_shared_intermediate_dir)
$(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp: $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/CodeGeneratorInspector.py $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/Inspector.json $(GYP_TARGET_DEPENDENCIES)
	@echo "Gyp action: Generating Inspector protocol sources from Inspector.json ($@)"
	$(hide)cd $(gyp_local_path)/third_party/WebKit/Source/WebCore/WebCore.gyp; mkdir -p $(gyp_shared_intermediate_dir)/webkit $(gyp_shared_intermediate_dir)/webcore; python ../inspector/CodeGeneratorInspector.py ../inspector/Inspector.json --output_h_dir "$(gyp_shared_intermediate_dir)/webkit" --output_cpp_dir "$(gyp_shared_intermediate_dir)/webcore"

$(gyp_shared_intermediate_dir)/webkit/InspectorBackendDispatcher.h: $(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp ;
$(gyp_shared_intermediate_dir)/webcore/InspectorFrontend.cpp: $(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp ;
$(gyp_shared_intermediate_dir)/webkit/InspectorFrontend.h: $(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp ;
$(gyp_shared_intermediate_dir)/webcore/InspectorTypeBuilder.cpp: $(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp ;
$(gyp_shared_intermediate_dir)/webkit/InspectorTypeBuilder.h: $(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp ;
$(gyp_shared_intermediate_dir)/webcore/InspectorBackendCommands.js: $(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp ;


GYP_GENERATED_OUTPUTS := \
	$(gyp_shared_intermediate_dir)/webcore/InspectorBackendDispatcher.cpp \
	$(gyp_shared_intermediate_dir)/webkit/InspectorBackendDispatcher.h \
	$(gyp_shared_intermediate_dir)/webcore/InspectorFrontend.cpp \
	$(gyp_shared_intermediate_dir)/webkit/InspectorFrontend.h \
	$(gyp_shared_intermediate_dir)/webcore/InspectorTypeBuilder.cpp \
	$(gyp_shared_intermediate_dir)/webkit/InspectorTypeBuilder.h \
	$(gyp_shared_intermediate_dir)/webcore/InspectorBackendCommands.js

# Make sure our deps and generated files are built first.
LOCAL_ADDITIONAL_DEPENDENCIES := $(GYP_TARGET_DEPENDENCIES) $(GYP_GENERATED_OUTPUTS)

### Rules for final target.
# Add target alias to "gyp_all_modules" target.
.PHONY: gyp_all_modules
gyp_all_modules: third_party_WebKit_Source_WebCore_WebCore_gyp_inspector_protocol_sources_gyp

# Alias gyp target name.
.PHONY: inspector_protocol_sources
inspector_protocol_sources: third_party_WebKit_Source_WebCore_WebCore_gyp_inspector_protocol_sources_gyp

LOCAL_MODULE_PATH := $(PRODUCT_OUT)/gyp_stamp
LOCAL_UNINSTALLABLE_MODULE := true

include $(BUILD_SYSTEM)/base_rules.mk

$(LOCAL_BUILT_MODULE): $(LOCAL_ADDITIONAL_DEPENDENCIES)
	$(hide) echo "Gyp timestamp: $@"
	$(hide) mkdir -p $(dir $@)
	$(hide) touch $@
