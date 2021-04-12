############## All Tools Variables ################
TOOLS_OVERRIDABLE_FLAGS:=
ALL_LIB_TYPES:=
CUDA_TYPE_COMPILER        := cuda
CUDASRC_FILES_SUFFIXES := cu
CXXSRC_FILES_SUFFIXES     := cxx cc C cpp
CSRC_FILES_SUFFIXES       := c
FORTRANSRC_FILES_SUFFIXES := F f77 f F77
SRC_FILES_SUFFIXES        := $(CXXSRC_FILES_SUFFIXES) $(CSRC_FILES_SUFFIXES) $(FORTRANSRC_FILES_SUFFIXES) $(CUDASRC_FILES_SUFFIXES)
SCRAM_ADMIN_DIR           := .SCRAM/$(SCRAM_ARCH)
SCRAM_TOOLS_DIR           := $(SCRAM_ADMIN_DIR)/timestamps
CFLAGS:=
LIBRARY_CFLAGS:=
TEST_CFLAGS:=
BINARY_CFLAGS:=
EDM_CFLAGS:=
CAPABILITIES_CFLAGS:=
LCGDICT_CFLAGS:=
ROOTDICT_CFLAGS:=
PRECOMPILE_CFLAGS:=
DEV_CFLAGS:=
RELEASE_CFLAGS:=
REM_CFLAGS:=
REM_LIBRARY_CFLAGS:=
REM_TEST_CFLAGS:=
REM_BINARY_CFLAGS:=
REM_EDM_CFLAGS:=
REM_CAPABILITIES_CFLAGS:=
REM_LCGDICT_CFLAGS:=
REM_ROOTDICT_CFLAGS:=
REM_PRECOMPILE_CFLAGS:=
REM_DEV_CFLAGS:=
REM_RELEASE_CFLAGS:=
CPPDEFINES:=
LIBRARY_CPPDEFINES:=
TEST_CPPDEFINES:=
BINARY_CPPDEFINES:=
EDM_CPPDEFINES:=
CAPABILITIES_CPPDEFINES:=
LCGDICT_CPPDEFINES:=
ROOTDICT_CPPDEFINES:=
PRECOMPILE_CPPDEFINES:=
DEV_CPPDEFINES:=
RELEASE_CPPDEFINES:=
REM_CPPDEFINES:=
REM_LIBRARY_CPPDEFINES:=
REM_TEST_CPPDEFINES:=
REM_BINARY_CPPDEFINES:=
REM_EDM_CPPDEFINES:=
REM_CAPABILITIES_CPPDEFINES:=
REM_LCGDICT_CPPDEFINES:=
REM_ROOTDICT_CPPDEFINES:=
REM_PRECOMPILE_CPPDEFINES:=
REM_DEV_CPPDEFINES:=
REM_RELEASE_CPPDEFINES:=
CPPFLAGS:=
LIBRARY_CPPFLAGS:=
TEST_CPPFLAGS:=
BINARY_CPPFLAGS:=
EDM_CPPFLAGS:=
CAPABILITIES_CPPFLAGS:=
LCGDICT_CPPFLAGS:=
ROOTDICT_CPPFLAGS:=
PRECOMPILE_CPPFLAGS:=
DEV_CPPFLAGS:=
RELEASE_CPPFLAGS:=
REM_CPPFLAGS:=
REM_LIBRARY_CPPFLAGS:=
REM_TEST_CPPFLAGS:=
REM_BINARY_CPPFLAGS:=
REM_EDM_CPPFLAGS:=
REM_CAPABILITIES_CPPFLAGS:=
REM_LCGDICT_CPPFLAGS:=
REM_ROOTDICT_CPPFLAGS:=
REM_PRECOMPILE_CPPFLAGS:=
REM_DEV_CPPFLAGS:=
REM_RELEASE_CPPFLAGS:=
CSHAREDOBJECTFLAGS:=
LIBRARY_CSHAREDOBJECTFLAGS:=
TEST_CSHAREDOBJECTFLAGS:=
BINARY_CSHAREDOBJECTFLAGS:=
EDM_CSHAREDOBJECTFLAGS:=
CAPABILITIES_CSHAREDOBJECTFLAGS:=
LCGDICT_CSHAREDOBJECTFLAGS:=
ROOTDICT_CSHAREDOBJECTFLAGS:=
PRECOMPILE_CSHAREDOBJECTFLAGS:=
DEV_CSHAREDOBJECTFLAGS:=
RELEASE_CSHAREDOBJECTFLAGS:=
REM_CSHAREDOBJECTFLAGS:=
REM_LIBRARY_CSHAREDOBJECTFLAGS:=
REM_TEST_CSHAREDOBJECTFLAGS:=
REM_BINARY_CSHAREDOBJECTFLAGS:=
REM_EDM_CSHAREDOBJECTFLAGS:=
REM_CAPABILITIES_CSHAREDOBJECTFLAGS:=
REM_LCGDICT_CSHAREDOBJECTFLAGS:=
REM_ROOTDICT_CSHAREDOBJECTFLAGS:=
REM_PRECOMPILE_CSHAREDOBJECTFLAGS:=
REM_DEV_CSHAREDOBJECTFLAGS:=
REM_RELEASE_CSHAREDOBJECTFLAGS:=
CUDA_FLAGS:=
LIBRARY_CUDA_FLAGS:=
TEST_CUDA_FLAGS:=
BINARY_CUDA_FLAGS:=
EDM_CUDA_FLAGS:=
CAPABILITIES_CUDA_FLAGS:=
LCGDICT_CUDA_FLAGS:=
ROOTDICT_CUDA_FLAGS:=
PRECOMPILE_CUDA_FLAGS:=
DEV_CUDA_FLAGS:=
RELEASE_CUDA_FLAGS:=
REM_CUDA_FLAGS:=
REM_LIBRARY_CUDA_FLAGS:=
REM_TEST_CUDA_FLAGS:=
REM_BINARY_CUDA_FLAGS:=
REM_EDM_CUDA_FLAGS:=
REM_CAPABILITIES_CUDA_FLAGS:=
REM_LCGDICT_CUDA_FLAGS:=
REM_ROOTDICT_CUDA_FLAGS:=
REM_PRECOMPILE_CUDA_FLAGS:=
REM_DEV_CUDA_FLAGS:=
REM_RELEASE_CUDA_FLAGS:=
CUDA_LDFLAGS:=
LIBRARY_CUDA_LDFLAGS:=
TEST_CUDA_LDFLAGS:=
BINARY_CUDA_LDFLAGS:=
EDM_CUDA_LDFLAGS:=
CAPABILITIES_CUDA_LDFLAGS:=
LCGDICT_CUDA_LDFLAGS:=
ROOTDICT_CUDA_LDFLAGS:=
PRECOMPILE_CUDA_LDFLAGS:=
DEV_CUDA_LDFLAGS:=
RELEASE_CUDA_LDFLAGS:=
REM_CUDA_LDFLAGS:=
REM_LIBRARY_CUDA_LDFLAGS:=
REM_TEST_CUDA_LDFLAGS:=
REM_BINARY_CUDA_LDFLAGS:=
REM_EDM_CUDA_LDFLAGS:=
REM_CAPABILITIES_CUDA_LDFLAGS:=
REM_LCGDICT_CUDA_LDFLAGS:=
REM_ROOTDICT_CUDA_LDFLAGS:=
REM_PRECOMPILE_CUDA_LDFLAGS:=
REM_DEV_CUDA_LDFLAGS:=
REM_RELEASE_CUDA_LDFLAGS:=
CXXFLAGS:=
LIBRARY_CXXFLAGS:=
TEST_CXXFLAGS:=
BINARY_CXXFLAGS:=
EDM_CXXFLAGS:=
CAPABILITIES_CXXFLAGS:=
LCGDICT_CXXFLAGS:=
ROOTDICT_CXXFLAGS:=
PRECOMPILE_CXXFLAGS:=
DEV_CXXFLAGS:=
RELEASE_CXXFLAGS:=
REM_CXXFLAGS:=
REM_LIBRARY_CXXFLAGS:=
REM_TEST_CXXFLAGS:=
REM_BINARY_CXXFLAGS:=
REM_EDM_CXXFLAGS:=
REM_CAPABILITIES_CXXFLAGS:=
REM_LCGDICT_CXXFLAGS:=
REM_ROOTDICT_CXXFLAGS:=
REM_PRECOMPILE_CXXFLAGS:=
REM_DEV_CXXFLAGS:=
REM_RELEASE_CXXFLAGS:=
CXXSHAREDFLAGS:=
LIBRARY_CXXSHAREDFLAGS:=
TEST_CXXSHAREDFLAGS:=
BINARY_CXXSHAREDFLAGS:=
EDM_CXXSHAREDFLAGS:=
CAPABILITIES_CXXSHAREDFLAGS:=
LCGDICT_CXXSHAREDFLAGS:=
ROOTDICT_CXXSHAREDFLAGS:=
PRECOMPILE_CXXSHAREDFLAGS:=
DEV_CXXSHAREDFLAGS:=
RELEASE_CXXSHAREDFLAGS:=
REM_CXXSHAREDFLAGS:=
REM_LIBRARY_CXXSHAREDFLAGS:=
REM_TEST_CXXSHAREDFLAGS:=
REM_BINARY_CXXSHAREDFLAGS:=
REM_EDM_CXXSHAREDFLAGS:=
REM_CAPABILITIES_CXXSHAREDFLAGS:=
REM_LCGDICT_CXXSHAREDFLAGS:=
REM_ROOTDICT_CXXSHAREDFLAGS:=
REM_PRECOMPILE_CXXSHAREDFLAGS:=
REM_DEV_CXXSHAREDFLAGS:=
REM_RELEASE_CXXSHAREDFLAGS:=
CXXSHAREDOBJECTFLAGS:=
LIBRARY_CXXSHAREDOBJECTFLAGS:=
TEST_CXXSHAREDOBJECTFLAGS:=
BINARY_CXXSHAREDOBJECTFLAGS:=
EDM_CXXSHAREDOBJECTFLAGS:=
CAPABILITIES_CXXSHAREDOBJECTFLAGS:=
LCGDICT_CXXSHAREDOBJECTFLAGS:=
ROOTDICT_CXXSHAREDOBJECTFLAGS:=
PRECOMPILE_CXXSHAREDOBJECTFLAGS:=
DEV_CXXSHAREDOBJECTFLAGS:=
RELEASE_CXXSHAREDOBJECTFLAGS:=
REM_CXXSHAREDOBJECTFLAGS:=
REM_LIBRARY_CXXSHAREDOBJECTFLAGS:=
REM_TEST_CXXSHAREDOBJECTFLAGS:=
REM_BINARY_CXXSHAREDOBJECTFLAGS:=
REM_EDM_CXXSHAREDOBJECTFLAGS:=
REM_CAPABILITIES_CXXSHAREDOBJECTFLAGS:=
REM_LCGDICT_CXXSHAREDOBJECTFLAGS:=
REM_ROOTDICT_CXXSHAREDOBJECTFLAGS:=
REM_PRECOMPILE_CXXSHAREDOBJECTFLAGS:=
REM_DEV_CXXSHAREDOBJECTFLAGS:=
REM_RELEASE_CXXSHAREDOBJECTFLAGS:=
FFLAGS:=
LIBRARY_FFLAGS:=
TEST_FFLAGS:=
BINARY_FFLAGS:=
EDM_FFLAGS:=
CAPABILITIES_FFLAGS:=
LCGDICT_FFLAGS:=
ROOTDICT_FFLAGS:=
PRECOMPILE_FFLAGS:=
DEV_FFLAGS:=
RELEASE_FFLAGS:=
REM_FFLAGS:=
REM_LIBRARY_FFLAGS:=
REM_TEST_FFLAGS:=
REM_BINARY_FFLAGS:=
REM_EDM_FFLAGS:=
REM_CAPABILITIES_FFLAGS:=
REM_LCGDICT_FFLAGS:=
REM_ROOTDICT_FFLAGS:=
REM_PRECOMPILE_FFLAGS:=
REM_DEV_FFLAGS:=
REM_RELEASE_FFLAGS:=
FOPTIMISEDFLAGS:=
LIBRARY_FOPTIMISEDFLAGS:=
TEST_FOPTIMISEDFLAGS:=
BINARY_FOPTIMISEDFLAGS:=
EDM_FOPTIMISEDFLAGS:=
CAPABILITIES_FOPTIMISEDFLAGS:=
LCGDICT_FOPTIMISEDFLAGS:=
ROOTDICT_FOPTIMISEDFLAGS:=
PRECOMPILE_FOPTIMISEDFLAGS:=
DEV_FOPTIMISEDFLAGS:=
RELEASE_FOPTIMISEDFLAGS:=
REM_FOPTIMISEDFLAGS:=
REM_LIBRARY_FOPTIMISEDFLAGS:=
REM_TEST_FOPTIMISEDFLAGS:=
REM_BINARY_FOPTIMISEDFLAGS:=
REM_EDM_FOPTIMISEDFLAGS:=
REM_CAPABILITIES_FOPTIMISEDFLAGS:=
REM_LCGDICT_FOPTIMISEDFLAGS:=
REM_ROOTDICT_FOPTIMISEDFLAGS:=
REM_PRECOMPILE_FOPTIMISEDFLAGS:=
REM_DEV_FOPTIMISEDFLAGS:=
REM_RELEASE_FOPTIMISEDFLAGS:=
FSHAREDOBJECTFLAGS:=
LIBRARY_FSHAREDOBJECTFLAGS:=
TEST_FSHAREDOBJECTFLAGS:=
BINARY_FSHAREDOBJECTFLAGS:=
EDM_FSHAREDOBJECTFLAGS:=
CAPABILITIES_FSHAREDOBJECTFLAGS:=
LCGDICT_FSHAREDOBJECTFLAGS:=
ROOTDICT_FSHAREDOBJECTFLAGS:=
PRECOMPILE_FSHAREDOBJECTFLAGS:=
DEV_FSHAREDOBJECTFLAGS:=
RELEASE_FSHAREDOBJECTFLAGS:=
REM_FSHAREDOBJECTFLAGS:=
REM_LIBRARY_FSHAREDOBJECTFLAGS:=
REM_TEST_FSHAREDOBJECTFLAGS:=
REM_BINARY_FSHAREDOBJECTFLAGS:=
REM_EDM_FSHAREDOBJECTFLAGS:=
REM_CAPABILITIES_FSHAREDOBJECTFLAGS:=
REM_LCGDICT_FSHAREDOBJECTFLAGS:=
REM_ROOTDICT_FSHAREDOBJECTFLAGS:=
REM_PRECOMPILE_FSHAREDOBJECTFLAGS:=
REM_DEV_FSHAREDOBJECTFLAGS:=
REM_RELEASE_FSHAREDOBJECTFLAGS:=
LDFLAGS:=
LIBRARY_LDFLAGS:=
TEST_LDFLAGS:=
BINARY_LDFLAGS:=
EDM_LDFLAGS:=
CAPABILITIES_LDFLAGS:=
LCGDICT_LDFLAGS:=
ROOTDICT_LDFLAGS:=
PRECOMPILE_LDFLAGS:=
DEV_LDFLAGS:=
RELEASE_LDFLAGS:=
REM_LDFLAGS:=
REM_LIBRARY_LDFLAGS:=
REM_TEST_LDFLAGS:=
REM_BINARY_LDFLAGS:=
REM_EDM_LDFLAGS:=
REM_CAPABILITIES_LDFLAGS:=
REM_LCGDICT_LDFLAGS:=
REM_ROOTDICT_LDFLAGS:=
REM_PRECOMPILE_LDFLAGS:=
REM_DEV_LDFLAGS:=
REM_RELEASE_LDFLAGS:=
LD_UNIT:=
LIBRARY_LD_UNIT:=
TEST_LD_UNIT:=
BINARY_LD_UNIT:=
EDM_LD_UNIT:=
CAPABILITIES_LD_UNIT:=
LCGDICT_LD_UNIT:=
ROOTDICT_LD_UNIT:=
PRECOMPILE_LD_UNIT:=
DEV_LD_UNIT:=
RELEASE_LD_UNIT:=
REM_LD_UNIT:=
REM_LIBRARY_LD_UNIT:=
REM_TEST_LD_UNIT:=
REM_BINARY_LD_UNIT:=
REM_EDM_LD_UNIT:=
REM_CAPABILITIES_LD_UNIT:=
REM_LCGDICT_LD_UNIT:=
REM_ROOTDICT_LD_UNIT:=
REM_PRECOMPILE_LD_UNIT:=
REM_DEV_LD_UNIT:=
REM_RELEASE_LD_UNIT:=
ALL_COMPILER_FLAGS := CFLAGS CPPDEFINES CPPFLAGS CSHAREDOBJECTFLAGS CUDA_FLAGS CUDA_LDFLAGS CXXFLAGS CXXSHAREDFLAGS CXXSHAREDOBJECTFLAGS FFLAGS FOPTIMISEDFLAGS FSHAREDOBJECTFLAGS LDFLAGS LD_UNIT 
SCRAM_MULTIPLE_COMPILERS := yes
SCRAM_DEFAULT_COMPILER    := gcc
SCRAM_COMPILER            := $(SCRAM_DEFAULT_COMPILER)
ifdef COMPILER
SCRAM_COMPILER            := $(COMPILER)
endif
CXX_TYPE_COMPILER := cxxcompiler
C_TYPE_COMPILER := ccompiler
F77_TYPE_COMPILER := f77compiler
ifndef SCRAM_IGNORE_MISSING_COMPILERS
$(if $(wildcard $(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-$(CXX_TYPE_COMPILER)),,$(info ****WARNING: You have selected $(SCRAM_COMPILER) as compiler but there is no $(SCRAM_COMPILER)-$(CXX_TYPE_COMPILER) tool setup. Default compiler $(SCRAM_DEFAULT_COMPILER)-$(CXX_TYPE_COMPILER) will be used to comple CXX files))
$(if $(wildcard $(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-$(C_TYPE_COMPILER)),,$(info ****WARNING: You have selected $(SCRAM_COMPILER) as compiler but there is no $(SCRAM_COMPILER)-$(C_TYPE_COMPILER) tool setup. Default compiler $(SCRAM_DEFAULT_COMPILER)-$(C_TYPE_COMPILER) will be used to comple C files))
$(if $(wildcard $(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-$(F77_TYPE_COMPILER)),,$(info ****WARNING: You have selected $(SCRAM_COMPILER) as compiler but there is no $(SCRAM_COMPILER)-$(F77_TYPE_COMPILER) tool setup. Default compiler $(SCRAM_DEFAULT_COMPILER)-$(F77_TYPE_COMPILER) will be used to comple F77 files))
endif
GCC_CXXCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/c++
GCC_CCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/gcc
GCC_F77COMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj
FC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/gfortran
ALL_TOOLS  += cxxcompiler
cxxcompiler_EX_USE    := $(if $(strip $(wildcard $(LOCALTOP)/$(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-cxxcompiler)),$(SCRAM_COMPILER)-cxxcompiler,$(SCRAM_DEFAULT_COMPILER)-cxxcompiler)
ALL_TOOLS  += ccompiler
ccompiler_EX_USE    := $(if $(strip $(wildcard $(LOCALTOP)/$(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-ccompiler)),$(SCRAM_COMPILER)-ccompiler,$(SCRAM_DEFAULT_COMPILER)-ccompiler)
ALL_TOOLS  += f77compiler
f77compiler_EX_USE    := $(if $(strip $(wildcard $(LOCALTOP)/$(SCRAM_TOOLS_DIR)/$(SCRAM_COMPILER)-f77compiler)),$(SCRAM_COMPILER)-f77compiler,$(SCRAM_DEFAULT_COMPILER)-f77compiler)
CMSSW_BASE:=/home/freerc/Nano_SUEP/CMSSW_10_6_4
PROTOBUF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/protobuf/3.5.2-pafccj
BINDIR:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/protobuf/3.5.2-pafccj/bin
CLHEP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/clhep/2.4.0.0-pafccj
ifeq ($(strip $(SCRAM_COMPILER)),gcc-analyzer)
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/cc
endif
LAPACK_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lapack/3.6.1-pafccj
LIBHEPML_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libhepml/0.2.1-pafccj
BOOST_PYTHON_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/boost/1.67.0-pafccj
DOXYGEN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/doxygen/1.8.11-pafccj
PY2_NUMBA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-numba/0.43.1-pafccj
RIVET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/rivet/2.7.0-pafccj3
DPM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dpm/1.8.0.1-pafccj
MAKE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gmake/4.2.1-pafccj
HEPMC_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hepmc/2.06.07-pafccj
CSCTRACKFINDEREMULATION_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/CSCTrackFinderEmulation/1.2-pafccj
GCC_ATOMIC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj
PY2_JUPYTER_CLIENT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-jupyter_client/5.2.4-pafccj
LIBUUID_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libuuid/2.22.2-pafccj
FREETYPE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/freetype/2.5.3-pafccj
BLACKHAT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/blackhat/0.9.9-pafccj
PY2_THEANO_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-Theano/1.0.4-pafccj2
LIBXSLT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libxslt/1.1.28-pafccj
MCTESTER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mctester/1.25.0a-pafccj4
GIFLIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/giflib/4.2.3-pafccj
PY2_IPYTHON_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-ipython/5.8.0-pafccj2
PY2_PYBIND11_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-pybind11/2.2.4-pafccj
VECGEOM_INTERFACE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/vecgeom/v00.05.00-pafccj
TOPREX_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/toprex/4.23-pafccj
PY2_MARKDOWN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-Markdown/3.1
XTL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xtl/0.6.3
TCMALLOC_MINIMAL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gperftools/2.6.1-pafccj
SIP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sip/4.17-pafccj
ORACLE_ADMINDIR:=/etc
FASTJET_CONTRIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fastjet-contrib/1.033-pafccj
LCOV_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lcov/1.9
PY2_HISTOGRAMMAR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-histogrammar/1.0.9-pafccj
PYMINUIT2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pyminuit2/0.0.1-pafccj4
PY2_CYTHON_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-cython/0.29.7
YAML_CPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/yaml-cpp/0.6.2-pafccj
LLVM_ANALYZER_CXXCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0
ifeq ($(strip $(SCRAM_COMPILER)),llvm-analyzer)
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0/bin/c++-analyzer
endif
XERCES_C_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xerces-c/3.1.3-pafccj
GMP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gmp-static/6.1.0-pafccj
LLVM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0
CUB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cub/1.8.0-pafccj4
PY2_BACKPORTS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-backports/1.0-pafccj2
GEANT4CORE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/geant4/10.4.3-pafccj
G4LIB:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/geant4/10.4.3-pafccj/lib
FASTJET_CONTRIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fastjet-contrib/1.033-pafccj
PY2_PYFLAKES_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-pyflakes/2.1.1
PYQT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pyqt/4.11.4-pafccj
HEPMC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hepmc/2.06.07-pafccj
TAUOLA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tauola/27.121.5-pafccj
LHAPDF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lhapdf/6.2.1-pafccj3
SCONS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/scons/3.0.1-pafccj
ifeq ($(strip $(SCRAM_COMPILER)),ccache)
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/ccache/3.1.8-pafccj/bin/gcc
endif
ifeq ($(strip $(SCRAM_COMPILER)),ccache)
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/ccache/3.1.8-pafccj/bin/c++
export CCACHE_BASEDIR:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_4
endif
ifeq ($(strip $(SCRAM_COMPILER)),llvm)
FC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/gfortran
endif
PY2_PYGMENTS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-Pygments/2.3.1-pafccj
PY2_NBFORMAT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-nbformat/4.4.0-pafccj2
PY2_PYCODESTYLE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-pycodestyle/2.5.0-pafccj
NUMPY_C_API_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-numpy/1.16.2-pafccj
CURL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/curl/7.59.0-pafccj
GNUPLOT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gnuplot/4.6.5-pafccj
MADGRAPH5AMCATNLO_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/madgraph5amcatnlo/2.6.0-pafccj5
GEANT4STATIC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/geant4/10.4.3-pafccj
ifeq ($(strip $(SCRAM_COMPILER)),ccache)
FC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/ccache/3.1.8-pafccj/bin/gfortran
endif
DMTCP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dmtcp/3.0.0-dev-pafccj
PYDATA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pythia6/426-pafccj
PYCLANG_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0
ifeq ($(strip $(SCRAM_COMPILER)),gcc-analyzer)
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/c++
endif
MXNET_PREDICT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mxnet-predict/1.2.1-pafccj2
PY2_NOTEBOOK_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-notebook/5.7.8-pafccj
CATCH2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/catch2/2.2.2-pafccj
PY2_JSONSCHEMA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-jsonschema/2.6.0-pafccj
PY2_FLAKE8_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-flake8/3.7.7
DB6_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/db6/6.2.32-pafccj
CVS2GIT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cvs2git/5419-pafccj
PYTHON_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/python/2.7.15-pafccj
PYTHON_COMPILE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/python/2.7.15-pafccj/lib/python2.7/compileall.py
GENEVA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/geneva/1.0-RC3-pafccj4
PYTHIA8_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pythia8/240-pafccj4
BZ2LIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/bz2lib/1.0.6-pafccj
QD_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qd/2.3.13-pafccj
DD4HEP_CORE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dd4hep/v01-10x-pafccj4
SLOCCOUNT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sloccount/2.26-pafccj
GDBM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gdbm/1.10-pafccj
LWTNN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lwtnn/2.4-pafccj
VINCIA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/vincia/2.2.04-pafccj4
PY2_HYPEROPT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-hyperopt/0.1.2-pafccj
FFTJET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fftjet/1.5.0-pafccj
EXPAT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/expat/2.1.0-pafccj
PROFESSOR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/professor/1.4.0-pafccj4
PY2_AUTOPEP8_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-autopep8/1.4.4
HEPPDT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/heppdt/3.03.00-pafccj
PY2_LINT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-lint/0.25.1-pafccj
DAVIX_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/davix/0.6.7-pafccj
CORAL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/coral/CORAL_2_3_21-pafccj5
PYTHON3_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/python3/3.6.4-pafccj
PYTHON3_COMPILE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/python3/3.6.4-pafccj/lib/python3.6/compileall.py
OPENLDAP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/openldap/2.4.45-pafccj
MPFR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mpfr-static/4.0.1-pafccj
PY2_NOSE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-nose/1.3.7-pafccj
VECGEOM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/vecgeom/v00.05.00-pafccj
LIBFFI_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libffi/3.2.1-pafccj
PY2_CHARDET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-chardet/3.0.4-pafccj
CLHEPHEADER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/clhep/2.4.0.0-pafccj
JIMMY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/jimmy/4.2-pafccj3
DIRE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dire/2.003-pafccj4
CLASSLIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/classlib/3.1.3-pafccj
IGPROF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/igprof/5.9.16-pafccj
TCMALLOC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gperftools/2.6.1-pafccj
ORACLE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/oracle/12.1.0.2.0-pafccj2
PHOTOS_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/photos/215.5-pafccj
CHARYBDIS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/charybdis/1.003-pafccj3
FASTJET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fastjet/3.3.0-pafccj
HLS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hls/2019.08
YODA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/yoda/1.7.4-pafccj4
PY2_AVRO_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-avro/1.8.2-pafccj
GLIBC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/glibc/2.17-78.el7_2.12-1.166.el6_7.3
LIBTIFF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libtiff/4.0.3-pafccj
HERWIG_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/herwig/6.521-pafccj3
PY2_NBDIME_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-nbdime/1.0.5-pafccj
GSL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gsl/2.2.1-pafccj
OPENMPI_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/openmpi/2.1.5-pafccj
UTM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/utm/utm_0.7.1-pafccj
ROOTRFLX_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09
QT3SUPPORT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj
QTDESIGNER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj
PY2_JUPYTER_CONSOLE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-jupyter_console/5.2.0-pafccj2
XROOTD_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xrootd/4.8.5-pafccj
GEANT4DATA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external
ifeq ($(strip $(SCRAM_COMPILER)),distcc)
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/distcc/3.2rc1-pafccj/bin/c++
endif
OPENLOOPS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/openloops/2.0.0
DCAP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dcap/2.47.8-pafccj
JIMMY_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/jimmy/4.2-pafccj3
PY2_TENSORFLOW_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-tensorflow/1.6.0-pafccj3
FRONTIER_CLIENT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/frontier_client/2.8.20-pafccj
PY2_NBCONVERT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-nbconvert/5.4.1-pafccj
LLVM_CCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0
ifeq ($(strip $(SCRAM_COMPILER)),llvm)
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0/bin/clang
endif
PY2_DABLOOMS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-dablooms/0.9.1-pafccj
GOSAMCONTRIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gosamcontrib/2.0-20150803-pafccj
CASCADE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cascade/2.2.04-pafccj3
PACPARSER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pacparser/1.3.5-pafccj
GCC_CHECKER_PLUGIN_ROOT:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc-checker-plugin/1.2-pafccj
BOOSTHEADER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/boost/1.67.0-pafccj
PYTHIA6_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pythia6/426-pafccj
PY2_SYMPY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-sympy/1.4
PROFESSOR2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/professor2/2.2.2-pafccj4
XTENSOR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xtensor/0.20.1
PY2_GOOGLEPACKAGES_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-googlePackages/1.0-pafccj2
PY2_SETUPTOOLS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-setuptools/28.3.0-pafccj
BOOST_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/boost/1.67.0-pafccj
CUDA_API_WRAPPERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cuda-api-wrappers/20180504-pafccj4
OPENBLAS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/OpenBLAS/0.3.5
ifeq ($(strip $(SCRAM_COMPILER)),iwyu)
LLVM_CXXCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0/bin/include-what-you-use
endif
ZLIB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/zlib-x86_64/1.2.11-pafccj
GBL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gbl/V02-01-03-pafccj
XZ_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xz/5.2.2-pafccj
LIBXML2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libxml2/2.9.1-pafccj
STARLIGHT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/starlight/r193-pafccj
ITTNOTIFY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/ittnotify/16.06.18-pafccj
PHOTOSPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/photospp/3.61-pafccj
MCDB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mcdb/1.0.3-pafccj
PYQUEN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pyquen/1.5.3-pafccj
PY2_TABLES_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-tables/3.4.4-pafccj3
SHERPA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sherpa/2.2.6-pafccj3
PYTHIA6_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pythia6/426-pafccj
PY2_VIRTUALENV_CLONE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-virtualenv-clone/0.5.3
ifeq ($(strip $(SCRAM_COMPILER)),distcc)
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/distcc/3.2rc1-pafccj/bin/gcc
endif
PY2_TQDM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-tqdm/4.31.1
FFTW3_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fftw3/3.3.2-pafccj
THEPEG_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/thepeg/2.1.4-pafccj4
LLVM_ANALYZER_CCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0
ifeq ($(strip $(SCRAM_COMPILER)),llvm-analyzer)
CC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0/bin/ccc-analyzer
endif
SIGCPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sigcpp/2.6.2-pafccj
QT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj
GOOGLE_BENCHMARK_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/google-benchmark/1.4.x-pafccj
LIBJPEG_TURBO_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libjpeg-turbo/2.0.1-pafccj
PCRE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pcre/8.37-pafccj
TENSORFLOW_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tensorflow/1.6.0-pafccj3
TFCOMPILE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tensorflow/1.6.0-pafccj3/bin/tfcompile
PY2_JUPYTER_CORE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-jupyter_core/4.4.0-pafccj2
TINYXML2_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tinyxml2/6.2.0-pafccj
MILLEPEDE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/millepede/V04-03-08-pafccj
OPENSSL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/openssl/1.0.2d-pafccj
TBB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tbb/2019_U3-pafccj
PY2_WHEEL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-wheel/0.33.1
HDF5_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hdf5/1.8.17-pafccj
ALPGEN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/alpgen/214-pafccj
PY2_VIRTUALENV_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-virtualenv/16.0.0-pafccj
LIBUNGIF_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libungif/4.1.4-pafccj
PY2_DXR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-dxr/1.0-pafccj4
GRAPHVIZ_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/graphviz/2.38.0-pafccj
CMSSWDATA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms
CMSSW_DATA_PATH:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms
PY2_NUMPY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-numpy/1.16.2-pafccj
PY2_VIRTUALENVWRAPPER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-virtualenvwrapper/4.8.4-pafccj
HECTOR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hector/1.3.4_patch1-pafccj4
QTBASE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj
PY2_LIZARD_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-lizard/1.16.3
GEANT4_PARFULLCMS:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/geant4-parfullcms/2014.01.27-pafccj2
JEMALLOC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/jemalloc/5.1.0-pafccj
TAUOLA_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tauola/27.121.5-pafccj
TKONLINESW_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tkonlinesw/4.2.0-1_gcc7-pafccj4
ROOTCLING_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09
GCC_PLUGIN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/lib/gcc/x86_64-unknown-linux-gnu/8.3.1/plugin
KTJET_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/ktjet/1.06-pafccj
PY2_FUTURE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-future/0.17.1-pafccj
CUDA_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cuda/10.1.105-pafccj2
NVCC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cuda/10.1.105-pafccj2/bin/nvcc
CUDA_STUBS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cuda/10.1.105-pafccj2
VDT_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/vdt/0.4.0-pafccj
VDT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/vdt/0.4.0-pafccj
PY2_PIP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-pip/9.0.3-pafccj
GDB_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gdb/8.1-pafccj
ifeq ($(strip $(SCRAM_COMPILER)),distcc)
FC:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/distcc/3.2rc1-pafccj/bin/gfortran
endif
CASCADE_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cascade/2.2.04-pafccj3
PY2_ONNX_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-onnx/1.5.0
EIGEN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/eigen/e4c107b451c52c9ab2d7b7fa4194ee35332916ec-pafccj
CPPUNIT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cppunit/1.40.1-pafccj
PY2_PLAC_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-plac/1.0.0-pafccj
GOSAM_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gosam/2.0.4-33b41ed-pafccj3
ROOT_INTERFACE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09
HERWIGPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/herwigpp/7.1.4-pafccj5
TAUOLAPP_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tauolapp/1.1.5-pafccj4
PY2_PBR_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-pbr/5.2.0
DAS_CLIENT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/das_client/v03.01.00-pafccj
PY2_FLAWFINDER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-flawfinder/2.0.8-pafccj
LIBPNG_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libpng/1.6.16-pafccj
MD5_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/md5/1.0.0-pafccj
PHOTOS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/photos/215.5-pafccj
SQLITE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sqlite/3.22.0-pafccj
PY2_QTCONSOLE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-qtconsole/4.4.4
CGAL_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cgal/4.2-pafccj
EVTGEN_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/evtgen/1.6.0-pafccj4
GIT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/git/2.19.0-pafccj
PY2_ROOTPY_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-rootpy/1.0.1-pafccj4
PY2_FS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-fs/0.5.5a1-pafccj2
VALGRIND_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/valgrind/3.13.0-pafccj
LLVM_CXXCOMPILER_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0
ifeq ($(strip $(SCRAM_COMPILER)),llvm)
CXX:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0/bin/clang++
endif
MESCHACH_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/meschach/1.2.pCMS1-pafccj
TOPREX_HEADERS_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/toprex/4.23-pafccj
ROOFIT_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09
GLIMPSE_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/glimpse/4.18.5-pafccj
PY2_BOKEH_BASE:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-bokeh/1.1.0-pafccj
############## All SCRAM ENV variables ################
LOCALTOP:=/home/freerc/Nano_SUEP/CMSSW_10_6_4
SCRAM_TMP:=tmp
SCRAM_INIT_LOCALTOP:=/home/freerc/Nano_SUEP/CMSSW_10_6_4
SCRAM_BUILDFILE:=BuildFile
RELEASETOP:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_4
SCRAM_INTlog:=logs
SCRAM_GMAKE_PATH:=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gmake/4.2.1-pafccj/bin/
SCRAM_INTwork:=tmp/slc7_amd64_gcc820
SCRAM_PROJECTNAME:=CMSSW
SCRAM_ARCH:=slc7_amd64_gcc820
SCRAM_SOURCEDIR:=src
SCRAM_RTBOURNE_SET:=CMSSW:CMSSW_10_6_4:slc7_amd64_gcc820:V2_2_9_pre12:SRT_
SCRAM_CONFIGCHKSUM:=V05-08-36
SCRAM_LOOKUPDB_WRITE:=/cvmfs/cms.cern.ch
SCRAM_CXX11_ABI:=1
SCRAM_PROJECTVERSION:=CMSSW_10_6_4
SCRAM_CONFIGDIR:=config
################ ALL SCRAM Stores #######################
ALL_PRODUCT_STORES:=
SCRAMSTORENAME_LOGS:=logs/slc7_amd64_gcc820
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_LOGS)
SCRAMSTORENAME_LIB:=lib/slc7_amd64_gcc820
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_LIB)
SCRAMSTORENAME_INCLUDE:=include
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_INCLUDE)
SCRAMSTORENAME_CFIPYTHON:=cfipython/slc7_amd64_gcc820
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_CFIPYTHON)
SCRAMSTORENAME_STATIC:=static/slc7_amd64_gcc820
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_STATIC)
SCRAMSTORENAME_BIGLIB:=biglib/slc7_amd64_gcc820
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_BIGLIB)
SCRAMSTORENAME_OBJS:=objs/slc7_amd64_gcc820
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_OBJS)
SCRAMSTORENAME_DOC:=doc
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_DOC)
SCRAMSTORENAME_TEST:=test/slc7_amd64_gcc820
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_TEST)
SCRAMSTORENAME_PYTHON:=python
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_PYTHON)
SCRAMSTORENAME_BIN:=bin/slc7_amd64_gcc820
ALL_PRODUCT_STORES+=$(SCRAMSTORENAME_BIN)
