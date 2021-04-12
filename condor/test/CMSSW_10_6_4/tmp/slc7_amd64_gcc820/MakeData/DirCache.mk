ALL_PACKAGES += PhysicsTools/NanoAODTools
subdirs_src_PhysicsTools_NanoAODTools := src_PhysicsTools_NanoAODTools_python src_PhysicsTools_NanoAODTools_data src_PhysicsTools_NanoAODTools_scripts src_PhysicsTools_NanoAODTools_src
ALL_SUBSYSTEMS+=PhysicsTools
subdirs_src_PhysicsTools = src_PhysicsTools_SUEP src_PhysicsTools_NanoAODTools
ifeq ($(strip $(PyPhysicsToolsSUEP)),)
PyPhysicsToolsSUEP := self/src/PhysicsTools/SUEP/python
src_PhysicsTools_SUEP_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/PhysicsTools/SUEP/python)
PyPhysicsToolsSUEP_files := $(patsubst src/PhysicsTools/SUEP/python/%,%,$(wildcard $(foreach dir,src/PhysicsTools/SUEP/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyPhysicsToolsSUEP_LOC_USE := self  
PyPhysicsToolsSUEP_PACKAGE := self/src/PhysicsTools/SUEP/python
ALL_PRODS += PyPhysicsToolsSUEP
PyPhysicsToolsSUEP_INIT_FUNC        += $$(eval $$(call PythonProduct,PyPhysicsToolsSUEP,src/PhysicsTools/SUEP/python,src_PhysicsTools_SUEP_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyPhysicsToolsSUEP,src/PhysicsTools/SUEP/python))
endif
ALL_COMMONRULES += src_PhysicsTools_SUEP_python
src_PhysicsTools_SUEP_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_PhysicsTools_SUEP_python,src/PhysicsTools/SUEP/python,PYTHON))
ifeq ($(strip $(PyPhysicsToolsNanoAODTools)),)
PyPhysicsToolsNanoAODTools := self/src/PhysicsTools/NanoAODTools/python
src_PhysicsTools_NanoAODTools_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/PhysicsTools/NanoAODTools/python)
PyPhysicsToolsNanoAODTools_files := $(patsubst src/PhysicsTools/NanoAODTools/python/%,%,$(wildcard $(foreach dir,src/PhysicsTools/NanoAODTools/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyPhysicsToolsNanoAODTools_LOC_USE := self  
PyPhysicsToolsNanoAODTools_PACKAGE := self/src/PhysicsTools/NanoAODTools/python
ALL_PRODS += PyPhysicsToolsNanoAODTools
PyPhysicsToolsNanoAODTools_INIT_FUNC        += $$(eval $$(call PythonProduct,PyPhysicsToolsNanoAODTools,src/PhysicsTools/NanoAODTools/python,src_PhysicsTools_NanoAODTools_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyPhysicsToolsNanoAODTools,src/PhysicsTools/NanoAODTools/python))
endif
ALL_COMMONRULES += src_PhysicsTools_NanoAODTools_python
src_PhysicsTools_NanoAODTools_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_PhysicsTools_NanoAODTools_python,src/PhysicsTools/NanoAODTools/python,PYTHON))
ALL_PACKAGES += PhysicsTools/SUEP
subdirs_src_PhysicsTools_SUEP := src_PhysicsTools_SUEP_condor src_PhysicsTools_SUEP_python src_PhysicsTools_SUEP_data
src_PhysicsTools_NanoAODTools_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/PhysicsTools/NanoAODTools/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_PhysicsTools_NanoAODTools_scripts,src/PhysicsTools/NanoAODTools/scripts,$(SCRAMSTORENAME_BIN),*))
