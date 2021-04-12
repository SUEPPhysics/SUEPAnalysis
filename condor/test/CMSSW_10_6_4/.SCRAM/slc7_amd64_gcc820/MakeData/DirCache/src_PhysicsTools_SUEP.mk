ifeq ($(strip $(PhysicsTools/SUEP)),)
src_PhysicsTools_SUEP := self/PhysicsTools/SUEP
PhysicsTools/SUEP  := src_PhysicsTools_SUEP
src_PhysicsTools_SUEP_BuildFile    := $(WORKINGDIR)/cache/bf/src/PhysicsTools/SUEP/BuildFile
src_PhysicsTools_SUEP_LOC_USE := roottmva rootphysics self
src_PhysicsTools_SUEP_EX_USE   := $(foreach d,$(src_PhysicsTools_SUEP_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
ALL_EXTERNAL_PRODS += src_PhysicsTools_SUEP
src_PhysicsTools_SUEP_INIT_FUNC += $$(eval $$(call EmptyPackage,src_PhysicsTools_SUEP,src/PhysicsTools/SUEP))
endif

