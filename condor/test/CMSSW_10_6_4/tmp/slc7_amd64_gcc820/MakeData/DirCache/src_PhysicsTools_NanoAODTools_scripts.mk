src_PhysicsTools_NanoAODTools_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/PhysicsTools/NanoAODTools/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_PhysicsTools_NanoAODTools_scripts,src/PhysicsTools/NanoAODTools/scripts,$(SCRAMSTORENAME_BIN),*))
