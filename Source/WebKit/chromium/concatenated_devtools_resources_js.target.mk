# This file is generated by gyp; do not edit.

include $(CLEAR_VARS)

LOCAL_MODULE_CLASS := GYP
LOCAL_MODULE := third_party_WebKit_Source_WebKit_chromium_concatenated_devtools_resources_js_gyp
LOCAL_MODULE_STEM := concatenated_devtools_resources_js
LOCAL_MODULE_SUFFIX := .stamp
LOCAL_MODULE_TAGS := optional
gyp_intermediate_dir := $(call local-intermediates-dir)
gyp_shared_intermediate_dir := $(call intermediates-dir-for,GYP,shared)

# Make sure our deps are built first.
GYP_TARGET_DEPENDENCIES :=

### Rules for action "concatenate_devtools_resources_js":
$(gyp_shared_intermediate_dir)/resources/inspector/ResourcesPanel.js: gyp_local_path := $(LOCAL_PATH)
$(gyp_shared_intermediate_dir)/resources/inspector/ResourcesPanel.js: gyp_intermediate_dir := $(GYP_ABS_ANDROID_TOP_DIR)/$(gyp_intermediate_dir)
$(gyp_shared_intermediate_dir)/resources/inspector/ResourcesPanel.js: gyp_shared_intermediate_dir := $(GYP_ABS_ANDROID_TOP_DIR)/$(gyp_shared_intermediate_dir)
$(gyp_shared_intermediate_dir)/resources/inspector/ResourcesPanel.js: $(LOCAL_PATH)/third_party/WebKit/Source/WebKit/chromium/scripts/inline_js_imports.py $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/front-end/ApplicationCacheItemsView.js $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/front-end/DOMStorageItemsView.js $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/front-end/DatabaseQueryView.js $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/front-end/DatabaseTableView.js $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/front-end/DirectoryContentView.js $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/front-end/FileContentView.js $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/front-end/FileSystemView.js $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/front-end/IndexedDBViews.js $(LOCAL_PATH)/third_party/WebKit/Source/WebCore/inspector/front-end/ResourcesPanel.js $(GYP_TARGET_DEPENDENCIES)
	@echo "Gyp action: _usr_local_google_code_clank_master_ab_external_chromium_org_third_party_WebKit_Source_WebKit_chromium_WebKit_gyp_concatenated_devtools_resources_js_target_concatenate_devtools_resources_js ($@)"
	$(hide)cd $(gyp_local_path)/third_party/WebKit/Source/WebKit/chromium; mkdir -p $(gyp_shared_intermediate_dir)/resources/inspector; python scripts/inline_js_imports.py ../../WebCore/inspector/front-end/ResourcesPanel.js ../../WebCore/inspector/front-end "$(gyp_shared_intermediate_dir)/resources/inspector/ResourcesPanel.js"



GYP_GENERATED_OUTPUTS := \
	$(gyp_shared_intermediate_dir)/resources/inspector/ResourcesPanel.js

# Make sure our deps and generated files are built first.
LOCAL_ADDITIONAL_DEPENDENCIES := $(GYP_TARGET_DEPENDENCIES) $(GYP_GENERATED_OUTPUTS)

### Rules for final target.
# Add target alias to "gyp_all_modules" target.
.PHONY: gyp_all_modules
gyp_all_modules: third_party_WebKit_Source_WebKit_chromium_concatenated_devtools_resources_js_gyp

# Alias gyp target name.
.PHONY: concatenated_devtools_resources_js
concatenated_devtools_resources_js: third_party_WebKit_Source_WebKit_chromium_concatenated_devtools_resources_js_gyp

LOCAL_MODULE_PATH := $(PRODUCT_OUT)/gyp_stamp
LOCAL_UNINSTALLABLE_MODULE := true

include $(BUILD_SYSTEM)/base_rules.mk

$(LOCAL_BUILT_MODULE): $(LOCAL_ADDITIONAL_DEPENDENCIES)
	$(hide) echo "Gyp timestamp: $@"
	$(hide) mkdir -p $(dir $@)
	$(hide) touch $@
