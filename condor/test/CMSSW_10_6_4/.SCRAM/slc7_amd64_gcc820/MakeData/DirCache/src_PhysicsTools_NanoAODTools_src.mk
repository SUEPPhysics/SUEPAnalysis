ifeq ($(strip $(PhysicsTools/NanoAODTools)),)
ALL_COMMONRULES += src_PhysicsTools_NanoAODTools_src
src_PhysicsTools_NanoAODTools_src_parent := PhysicsTools/NanoAODTools
src_PhysicsTools_NanoAODTools_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_PhysicsTools_NanoAODTools_src,src/PhysicsTools/NanoAODTools/src,LIBRARY))
PhysicsToolsNanoAODTools := self/PhysicsTools/NanoAODTools
PhysicsTools/NanoAODTools := PhysicsToolsNanoAODTools
PhysicsToolsNanoAODTools_files := $(patsubst src/PhysicsTools/NanoAODTools/src/%,%,$(wildcard $(foreach dir,src/PhysicsTools/NanoAODTools/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PhysicsToolsNanoAODTools_BuildFile    := $(WORKINGDIR)/cache/bf/src/PhysicsTools/NanoAODTools/BuildFile
PhysicsToolsNanoAODTools_LOC_USE := self  roottmva hepmc CondFormats/JetMETObjects JetMETCorrections/Modules
PhysicsToolsNanoAODTools_LCGDICTS  := x 
PhysicsToolsNanoAODTools_PRE_INIT_FUNC += $$(eval $$(call LCGDict,PhysicsToolsNanoAODTools,src/PhysicsTools/NanoAODTools/src/classes.h,src/PhysicsTools/NanoAODTools/src/classes_def.xml,$(SCRAMSTORENAME_LIB),$(GENREFLEX_ARGS) --fail_on_warnings,))
PhysicsToolsNanoAODTools_EX_LIB   := PhysicsToolsNanoAODTools
PhysicsToolsNanoAODTools_EX_USE   := $(foreach d,$(PhysicsToolsNanoAODTools_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
PhysicsToolsNanoAODTools_PACKAGE := self/src/PhysicsTools/NanoAODTools/src
ALL_PRODS += PhysicsToolsNanoAODTools
PhysicsToolsNanoAODTools_CLASS := LIBRARY
PhysicsTools/NanoAODTools_forbigobj+=PhysicsToolsNanoAODTools
PhysicsToolsNanoAODTools_INIT_FUNC        += $$(eval $$(call Library,PhysicsToolsNanoAODTools,src/PhysicsTools/NanoAODTools/src,src_PhysicsTools_NanoAODTools_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS),))
endif
