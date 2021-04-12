LIB :=
INCLUDE :=
USE :=
USE += self 
$(foreach f,$(ALL_COMPILER_FLAGS),$(eval $f += $(cxxcompiler_EX_FLAGS_$f_ALL)))
$(foreach f,$(ALL_COMPILER_FLAGS),$(eval REM_$f += $(cxxcompiler_EX_FLAGS_REM_$f_ALL)))
$(foreach f,$(ALL_COMPILER_FLAGS),$(eval $f += $(ccompiler_EX_FLAGS_$f_ALL)))
$(foreach f,$(ALL_COMPILER_FLAGS),$(eval REM_$f += $(ccompiler_EX_FLAGS_REM_$f_ALL)))
$(foreach f,$(ALL_COMPILER_FLAGS),$(eval $f += $(f77compiler_EX_FLAGS_$f_ALL)))
$(foreach f,$(ALL_COMPILER_FLAGS),$(eval REM_$f += $(f77compiler_EX_FLAGS_REM_$f_ALL)))
LCGDICT_DEPS := rootrflx
GENREFLEX_CPPFLAGS := $(rootrflx_EX_FLAGS_GENREFLEX_CPPFLAGS)
GENREFLEX_GCCXMLOPT := $(if $(strip $(rootrflx_EX_FLAGS_GENREFLEX_GCCXMLOPT)),--gccxmlopt=\"$(rootrflx_EX_FLAGS_GENREFLEX_GCCXMLOPT)\")
GENREFLEX_ARGS := $(rootrflx_EX_FLAGS_GENREFLEX_ARGS)
self_EX_FLAGS_BIGOBJ_CXXFLAGS+=-flto -Wl,--exclude-libs,ALL
LLVM_PLUGIN+=UtilitiesStaticAnalyzers
self_EX_FLAGS_REM_LCGDICT_CPPFLAGS+=-O%
self_EX_FLAGS_CXXFLAGS+=-DBOOST_DISABLE_ASSERTS
LLVM_CHECKERS+=-enable-checker threadsafety
self_EX_FLAGS_LCGDICT_CXXFLAGS+=-Os -Wno-unused-variable
self_EX_FLAGS_LCGDICT_CPPFLAGS+=-DCMSSW_REFLEX_DICT
self_EX_FLAGS_MISSING_SYMBOL_FLAGS+=-Wl,-z,defs
self_EX_FLAGS_REM_LCGDICT_CXXFLAGS+=-O% -fipa%
self_EX_FLAGS_ROOTDICT_CXXFLAGS+=-Wno-unknown-pragmas
self_EX_FLAGS_REM_ROOTDICT_CXXFLAGS+=-pedantic
PYTHON_PACKAGE_SYMLINK+=YES


ifeq ($(strip $(GENREFLEX)),)
GENREFLEX:=$(ROOTRFLX_BASE)/bin/genreflex
endif
ifeq ($(strip $(GENREFLEX_CPPFLAGS)),)
GENREFLEX_CPPFLAGS:=-DCMS_DICT_IMPL -D_REENTRANT -DGNU_SOURCE
endif
ifeq ($(strip $(GENREFLEX_ARGS)),)
GENREFLEX_ARGS:=--deep
endif
ifeq ($(strip $(ROOTCINT)),)
ROOTCINT:=$(ROOTRFLX_BASE)/bin/rootcint
endif

LIBDIR+=$(self_EX_LIBDIR)
ifdef RELEASETOP
ifeq ($(strip $(wildcard $(RELEASETOP)/$(PUB_DIRCACHE_MKDIR)/DirCache.mk)),)
$(error Release area has been removed/modified as $(RELEASETOP)/$(PUB_DIRCACHE_MKDIR)/DirCache.mk is missing.)
endif
endif
LIBTYPE:= 

subdirs_src+=$(filter-out Documentation, src_PhysicsTools)

COND_SERIALIZATION:=$(SCRAM_SOURCEDIR)/CondFormats/Serialization/python/condformats_serialization_generate.py
ALL_EXTRA_PRODUCT_RULES+=LCG
EDM_WRITE_CONFIG:=edmWriteConfigs
EDM_CHECK_CLASS_VERSION:=$(SCRAM_SOURCEDIR)/FWCore/Utilities/scripts/edmCheckClassVersion
EDM_CHECK_CLASS_TRANSIENTS=$(SCRAM_SOURCEDIR)/FWCore/Utilities/scripts/edmCheckClassTransients
COMPILE_PYTHON_SCRIPTS:=yes
self_EX_FLAGS_CPPDEFINES+=-DCMSSW_GIT_HASH='"$(CMSSW_GIT_HASH)"' -DPROJECT_NAME='"$(SCRAM_PROJECTNAME)"' -DPROJECT_VERSION='"$(SCRAM_PROJECTVERSION)"'
ifeq ($(strip $(RELEASETOP)$(IS_PATCH)),yes)
CMSSW_SEARCH_PATH:=${CMSSW_SEARCH_PATH}:$($(SCRAM_PROJECTNAME)_BASE_FULL_RELEASE)/$(SCRAM_SOURCEDIR)
endif
.PHONY: dependencies
dependencies:
	@cd $(LOCALTOP); \
	mkdir -p $(LOCALTOP)/doc/deps/$(SCRAM_ARCH); \
	cd $(LOCALTOP)/doc/deps/$(SCRAM_ARCH); \
	ignominy -f -i -A -g all $(LOCALTOP)
.PHONY: userguide referencemanual doc doxygen
doc: referencemanual
	@echo "Documentation/release notes built for $(SCRAM_PROJECTNAME) v$(SCRAM_PROJECTVERSION)"
userguide:
	@if [ -f $(LOCALTOP)/src/Documentation/UserGuide/scripts/makedoc ]; then \
	  doctop=$(LOCALTOP); \
	else \
	  doctop=$(RELEASETOP); \
	fi; \
	cd $$doctop/src; \
	Documentation/UserGuide/scripts/makedoc $(LOCALTOP)/src $(LOCALTOP)/doc/UserGuide $(RELEASETOP)/src
referencemanual:
	@cd $(LOCALTOP)/src/Documentation/ReferenceManualScripts/config; \
	sed -e 's|@PROJ_NAME@|$(SCRAM_PROJECTNAME)|g' \
	-e 's|@PROJ_VERS@|$(SCRAM_PROJECTVERSION)|g' \
	-e 's|@CMSSW_BASE@|$(LOCALTOP)|g' \
	-e 's|@INC_PATH@|$(LOCALTOP)/src|g' \
	doxyfile.conf.in > doxyfile.conf; \
	cd $(LOCALTOP); \
	ls -d src/*/*/doc/*.doc | sed 's|(.*).doc|mv "&" "\1.dox"|' | /bin/sh; \
	if [ `expr substr $(SCRAM_PROJECTVERSION) 1 1` = "2" ]; then \
	  ./config/fixdocs.sh $(SCRAM_PROJECTNAME)"_"$(SCRAM_PROJECTVERSION); \
	else \
	  ./config/fixdocs.sh $(SCRAM_PROJECTVERSION); \
	fi; \
	ls -d src/*/*/doc/*.doy |  sed 's/(.*).doy/sed "s|@PROJ_VERS@|$(SCRAM_PROJECTVERSION)|g" "&" > "\1.doc"/' | /bin/sh; \
	rm -rf src/*/*/doc/*.doy; \
	cd $(LOCALTOP)/src/Documentation/ReferenceManualScripts/config; \
	doxygen doxyfile.conf; \
	cd $(LOCALTOP); \
	ls -d src/*/*/doc/*.dox | sed 's|(.*).dox|mv "&" "\1.doc"|' | /bin/sh;
doxygen:
	@rm -rf $(LOCALTOP)/$(WORKINGDIR)/doxygen &&\
	mkdir -p $(LOCALTOP)/$(WORKINGDIR)/doxygen &&\
	scriptdir=$(LOCALTOP)/$(SCRAM_SOURCEDIR)/Documentation/ReferenceManualScripts/doxygen/utils &&\
	[ -d $$scriptdir ] || scriptdir=$(RELEASETOP)/$(SCRAM_SOURCEDIR)/Documentation/ReferenceManualScripts/doxygen/utils &&\
	cd $$scriptdir/doxygen &&\
	cp -t $(LOCALTOP)/$(WORKINGDIR)/doxygen cfgfile footer.html header.html doxygen.css DoxygenLayout.xml doxygen ../../script_launcher.sh &&\
	cd $(LOCALTOP)/$(WORKINGDIR)/doxygen &&\
	chmod +rwx doxygen script_launcher.sh &&\
	sed -e 's|@CMSSW_BASE@|$(LOCALTOP)|g' cfgfile > cfgfile.conf &&\
	./doxygen cfgfile.conf &&\
	./script_launcher.sh $(SCRAM_PROJECTVERSION) $$scriptdir $(LOCALTOP) &&\
	echo "Reference Manual is generated."
.PHONY: gindices
gindices:
	@cd $(LOCALTOP); \
	rm -rf  .glimpse_*; mkdir .glimpse_full; \
	find $(LOCALTOP)/src $(LOCALTOP)/cfipython/$(SCRAM_ARCH) -follow -mindepth 3 -type f | grep -v '.pyc$$' | sed 's|^./||' | glimpseindex -F -H .glimpse_full; \
	chmod 0644 .glimpse_full/.glimpse_*; \
	mv .glimpse_full/.glimpse_filenames .; \
	for  x in `ls -A1 .glimpse_full` ; do \
	  ln -s .glimpse_full/$$x $$x; \
	done; \
	cp .glimpse_filenames .glimpse_full/.glimpse_filenames; \
	sed -i -e "s|$(LOCALTOP)/||" .glimpse_filenames
.PHONY: productmap
productmap:
	@cd $(LOCALTOP); \
	mkdir -p src; rm -f src/ReleaseProducts.list; echo ">> Generating Product Map in src/ReleaseProducts.list.";\
	(RelProducts.pl $(LOCALTOP) > $(LOCALTOP)/src/ReleaseProducts.list || exit 0)
.PHONY: depscheck
depscheck:
	@ReleaseDepsChecks.pl --detail
CONFIGDEPS += $(COMMON_WORKINGDIR)/cache/project_links
$(COMMON_WORKINGDIR)/cache/project_links: FORCE_TARGET
	@echo '>> Creating project symlinks';\
	[ -d $(@D) ] ||  $(CMD_mkdir) -p $(@D) &&\
	config/SCRAM/createSymLinks.pl src/LCG include/LCG 1 . '' &&\
	if [ ! -f $@ ] ; then touch $@; fi

PLUGIN_REFRESH_CMDS += DD4HepPluginRefresh
define do_DD4HepPluginRefresh
  echo "@@@@ Refreshing Plugins:DD4HepPluginRefresh" &&\
$(EDM_TOOLS_PREFIX) DD4HepPluginRefresh $(1)
endef
$(SCRAMSTORENAME_LIB)/.dd4hepcache: $(SCRAM_INTwork)/cache/dd4hep_DD4HepPluginRefresh $(SCRAM_INTwork)/cache/prod/DD4HepPluginRefresh
	$(call run_plugin_refresh_cmd,DD4HepPluginRefresh)
DD4HepPluginRefresh_cache := $(SCRAMSTORENAME_LIB)/.dd4hepcache
$(SCRAM_INTwork)/cache/dd4hep_DD4HepPluginRefresh: 
	@:
-include $(SCRAM_CONFIGDIR)/SCRAM/GMake/Makefile.dd4hepplugin
PLUGIN_REFRESH_CMDS += RivetPluginRefresh
define do_RivetPluginRefresh
  echo "@@@@ Refreshing Plugins:RivetPluginRefresh" &&\
$(EDM_TOOLS_PREFIX) RivetPluginRefresh $(1)
endef
$(SCRAMSTORENAME_LIB)/.rivetcache: $(SCRAM_INTwork)/cache/rivet_RivetPluginRefresh $(SCRAM_INTwork)/cache/prod/RivetPluginRefresh
	$(call run_plugin_refresh_cmd,RivetPluginRefresh)
RivetPluginRefresh_cache := $(SCRAMSTORENAME_LIB)/.rivetcache
$(SCRAM_INTwork)/cache/rivet_RivetPluginRefresh: 
	@:
-include $(SCRAM_CONFIGDIR)/SCRAM/GMake/Makefile.rivetplugin
PLUGIN_REFRESH_CMDS += edmPluginRefresh
define do_edmPluginRefresh
  echo "@@@@ Refreshing Plugins:edmPluginRefresh" &&\
$(EDM_TOOLS_PREFIX) edmPluginRefresh $(1)
endef
$(SCRAMSTORENAME_LIB)/.edmplugincache: $(SCRAM_INTwork)/cache/edm_edmPluginRefresh $(SCRAM_INTwork)/cache/prod/edmPluginRefresh
	$(call run_plugin_refresh_cmd,edmPluginRefresh)
edmPluginRefresh_cache := $(SCRAMSTORENAME_LIB)/.edmplugincache
$(SCRAM_INTwork)/cache/edm_edmPluginRefresh: 
	@:
-include $(SCRAM_CONFIGDIR)/SCRAM/GMake/Makefile.edmplugin
###############################################################################

