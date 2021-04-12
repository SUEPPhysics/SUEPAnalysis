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
