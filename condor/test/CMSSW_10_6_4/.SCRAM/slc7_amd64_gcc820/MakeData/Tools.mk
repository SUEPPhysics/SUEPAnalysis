ALL_TOOLS      += alpgen

ALL_TOOLS      += blackhat
blackhat_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/blackhat/0.9.9-pafccj/include
blackhat_EX_LIB := Ampl_eval BG BH BHcore CutPart Cut_wCI Cuteval Integrals Interface OLA RatPart Rateval Spinors assembly ratext
blackhat_EX_USE := qd

ALL_TOOLS      += boost
boost_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/boost/1.67.0-pafccj/include
boost_EX_LIB := boost_thread boost_signals boost_date_time
boost_EX_USE := root_cxxdefaults sockets
boost_EX_FLAGS_CPPDEFINES  := -DBOOST_SPIRIT_THREADSAFE -DPHOENIX_THREADSAFE
boost_EX_FLAGS_CXXFLAGS  := -Wno-error=unused-variable

ALL_TOOLS      += boost_chrono
boost_chrono_EX_LIB := boost_chrono
boost_chrono_EX_USE := boost_system boost

ALL_TOOLS      += boost_filesystem
boost_filesystem_EX_LIB := boost_filesystem
boost_filesystem_EX_USE := boost_system boost

ALL_TOOLS      += boost_header
boost_header_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/boost/1.67.0-pafccj/include
boost_header_EX_USE := root_cxxdefaults

ALL_TOOLS      += boost_iostreams
boost_iostreams_EX_USE := boost

ALL_TOOLS      += boost_mpi
boost_mpi_EX_LIB := boost_mpi
boost_mpi_EX_USE := boost boost_serialization

ALL_TOOLS      += boost_program_options
boost_program_options_EX_LIB := boost_program_options
boost_program_options_EX_USE := boost

ALL_TOOLS      += boost_python
boost_python_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/boost/1.67.0-pafccj/include
boost_python_EX_LIB := boost_python27
boost_python_EX_USE := root_cxxdefaults python

ALL_TOOLS      += boost_regex
boost_regex_EX_LIB := boost_regex
boost_regex_EX_USE := boost

ALL_TOOLS      += boost_serialization
boost_serialization_EX_LIB := boost_serialization
boost_serialization_EX_USE := boost

ALL_TOOLS      += boost_signals
boost_signals_EX_LIB := boost_signals
boost_signals_EX_USE := boost

ALL_TOOLS      += boost_system
boost_system_EX_LIB := boost_system
boost_system_EX_USE := boost

ALL_TOOLS      += boost_test
boost_test_EX_LIB := boost_unit_test_framework
boost_test_EX_USE := boost

ALL_TOOLS      += bz2lib
bz2lib_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/bz2lib/1.0.6-pafccj/include
bz2lib_EX_LIB := bz2
bz2lib_EX_USE := root_cxxdefaults

ALL_TOOLS      += cascade
cascade_EX_LIB := cascade_merged
cascade_EX_USE := f77compiler cascade_headers

ALL_TOOLS      += cascade_headers
cascade_headers_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cascade/2.2.04-pafccj3/include
cascade_headers_EX_USE := root_cxxdefaults

ALL_TOOLS      += catch2
catch2_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/catch2/2.2.2-pafccj/include

ALL_TOOLS      += ccache-ccompiler
ccache-ccompiler_EX_USE := gcc-ccompiler

ALL_TOOLS      += ccache-cxxcompiler
ccache-cxxcompiler_EX_USE := gcc-cxxcompiler

ALL_TOOLS      += ccache-f77compiler
ccache-f77compiler_EX_USE := gcc-f77compiler

ALL_TOOLS      += cgal
cgal_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cgal/4.2-pafccj/include
cgal_EX_LIB := CGAL_Core CGAL
cgal_EX_USE := root_cxxdefaults zlib boost_system gmp mpfr

ALL_TOOLS      += cgalimageio
cgalimageio_EX_LIB := CGAL_ImageIO
cgalimageio_EX_USE := zlib boost_system cgal

ALL_TOOLS      += charybdis
charybdis_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/charybdis/1.003-pafccj3/include
charybdis_EX_LIB := charybdis
charybdis_EX_USE := root_cxxdefaults f77compiler herwig pythia6

ALL_TOOLS      += classlib
classlib_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/classlib/3.1.3-pafccj/include
classlib_EX_LIB := classlib
classlib_EX_USE := zlib bz2lib pcre openssl root_cxxdefaults
classlib_EX_FLAGS_CPPDEFINES  := -D__STDC_LIMIT_MACROS -D__STDC_FORMAT_MACROS

ALL_TOOLS      += clhep
clhep_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/clhep/2.4.0.0-pafccj/include
clhep_EX_LIB := CLHEP
clhep_EX_USE := root_cxxdefaults
clhep_EX_FLAGS_CXXFLAGS  := -Wno-error=unused-variable

ALL_TOOLS      += clhepheader
clhepheader_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/clhep/2.4.0.0-pafccj/include
clhepheader_EX_USE := root_cxxdefaults
clhepheader_EX_FLAGS_CXXFLAGS  := -Wno-error=unused-variable

ALL_TOOLS      += cmsswdata
cmsswdata_EX_FLAGS_CMSSW_DATA_PACKAGE  := CalibCalorimetry/CaloMiscalibTools=V01-00-00 CalibCalorimetry/EcalTrivialCondModules=V00-02-00 CalibPPS/ESProducers=V01-00-00 CalibTracker/SiPixelESProducers=V02-00-00 CalibTracker/SiStripDCS=V01-00-00 Calibration/Tools=V01-00-00 CondFormats/JetMETObjects=V01-00-03 CondTools/SiPhase2Tracker=V00-01-00 Configuration/Generator=V01-00-03 DQM/DTMonitorClient=V00-01-00 DQM/PhysicsHWW=V01-00-00 DQM/SiStripMonitorClient=V01-00-00 DataFormats/PatCandidates=V01-00-01 DetectorDescription/Schema=V02-02-01 EgammaAnalysis/ElectronTools=V00-01-04 EventFilter/L1TRawToDigi=V01-00-00 FWCore/Modules=V00-01-00 FastSimulation/MaterialEffects=V05-00-00 FastSimulation/TrackingRecHitProducer=V01-00-03 Fireworks/Geometry=V07-05-04 GeneratorInterface/EvtGenInterface=V02-00-11 GeneratorInterface/ReggeGribovPartonMCInterface=V00-00-02 HLTrigger/JetMET=V01-00-00 IOPool/Input=V00-01-00 L1Trigger/L1TCalorimeter=V01-00-22 L1Trigger/L1TGlobal=V00-00-07 L1Trigger/L1THGCal=V01-00-12 L1Trigger/L1TMuon=V01-01-03 L1Trigger/RPCTrigger=V00-15-00 MagneticField/Interpolation=V01-00-02 PhysicsTools/NanoAOD=V01-00-05 PhysicsTools/PatUtils=V00-01-00 RecoBTag/CTagging=V01-00-03 RecoBTag/Combined=V01-01-04 RecoBTag/SecondaryVertex=V02-00-04 RecoBTag/SoftLepton=V01-00-01 RecoCTPPS/TotemRPLocal=V00-02-00 RecoEgamma/ElectronIdentification=V01-01-03 RecoEgamma/PhotonIdentification=V01-00-06 RecoHI/HiJetAlgos=V01-00-01 RecoJets/JetProducers=V05-10-20 RecoLocalCalo/EcalDeadChannelRecoveryAlgos=V01-00-00 RecoMET/METPUSubtraction=V01-00-03 RecoMuon/MuonIdentification=V01-12-05 RecoParticleFlow/PFBlockProducer=V02-04-02 RecoParticleFlow/PFProducer=V16-00-00 RecoParticleFlow/PFTracking=V13-01-00 RecoTauTag/TrainingFiles=V00-01-01 RecoTracker/FinalTrackSelectors=V01-00-07 SLHCUpgradeSimulations/Geometry=V01-00-10 SimG4CMS/Calo=V03-01-00 SimG4CMS/Forward=V02-03-18 SimTracker/SiStripDigitizer=V01-00-00 SimTransport/HectorProducer=V01-00-01 SimTransport/PPSProtonTransport=V00-01-00 SimTransport/TotemRPProtonTransportParametrization=V00-01-00 Validation/Geometry=V00-07-00

ALL_TOOLS      += codechecker

ALL_TOOLS      += coral
ALL_SCRAM_PROJECTS += coral
coral_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/coral/CORAL_2_3_21-pafccj5/include/LCG
coral_EX_USE := root_cxxdefaults
coral_ORDER := 98000

ALL_TOOLS      += cppunit
cppunit_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cppunit/1.40.1-pafccj/include
cppunit_EX_LIB := cppunit
cppunit_EX_USE := root_cxxdefaults sockets

ALL_TOOLS      += csctrackfinderemulation
csctrackfinderemulation_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/CSCTrackFinderEmulation/1.2-pafccj/include
csctrackfinderemulation_EX_LIB := CSCTrackFinderEmulation

ALL_TOOLS      += cub
cub_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cub/1.8.0-pafccj4/include
cub_EX_USE := cuda
cub_EX_FLAGS_CXXFLAGS  := -DCUB_STDERR

ALL_TOOLS      += cuda-api-wrappers
cuda-api-wrappers_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cuda-api-wrappers/20180504-pafccj4/include
cuda-api-wrappers_EX_LIB := cuda-api-wrappers
cuda-api-wrappers_EX_USE := cuda
cuda-api-wrappers_EX_FLAGS_CXXFLAGS  := -DCUDA_ENABLE_DEPRECATED

ALL_TOOLS      += cuda-cublas
cuda-cublas_EX_LIB := cublas
cuda-cublas_EX_USE := cuda

ALL_TOOLS      += cuda-cufft
cuda-cufft_EX_LIB := cufft cufftw
cuda-cufft_EX_USE := cuda

ALL_TOOLS      += cuda-curand
cuda-curand_EX_LIB := curand
cuda-curand_EX_USE := cuda

ALL_TOOLS      += cuda-cusolver
cuda-cusolver_EX_LIB := cusolver
cuda-cusolver_EX_USE := cuda

ALL_TOOLS      += cuda-cusparse
cuda-cusparse_EX_LIB := cusparse
cuda-cusparse_EX_USE := cuda

ALL_TOOLS      += cuda-gcc-support

ALL_TOOLS      += cuda-npp
cuda-npp_EX_LIB := nppial nppicc nppicom nppidei nppif nppig nppim nppist nppisu nppitc npps nppc
cuda-npp_EX_USE := cuda

ALL_TOOLS      += cuda-nvgraph
cuda-nvgraph_EX_LIB := nvgraph
cuda-nvgraph_EX_USE := cuda

ALL_TOOLS      += cuda-nvjpeg
cuda-nvjpeg_EX_LIB := nvjpeg
cuda-nvjpeg_EX_USE := cuda

ALL_TOOLS      += cuda-nvml
cuda-nvml_EX_LIB := nvidia-ml
cuda-nvml_EX_USE := cuda

ALL_TOOLS      += cuda-nvrtc
cuda-nvrtc_EX_LIB := nvrtc
cuda-nvrtc_EX_USE := cuda

ALL_TOOLS      += cuda-stubs
cuda-stubs_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cuda/10.1.105-pafccj2/include
cuda-stubs_EX_LIB := cuda
cuda-stubs_EX_LIBDIR := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cuda/10.1.105-pafccj2/lib64/stubs
cuda-stubs_EX_FLAGS_SKIP_TOOL_SYMLINKS  := 1

ALL_TOOLS      += cuda
ALL_LIB_TYPES += CUDA_LIB
cuda_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/cuda/10.1.105-pafccj2/include
cuda_EX_LIB := cudart cudadevrt nvToolsExt
cuda_EX_CUDA_LIB := cudadevrt
cuda_EX_USE := cuda-stubs
cuda_EX_FLAGS_CUDA_HOST_CXXFLAGS  := -std=c++14
cuda_EX_FLAGS_CUDA_FLAGS  := -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -O3 -std=c++14 --expt-relaxed-constexpr --expt-extended-lambda --generate-line-info --source-in-ptx --cudart=shared
cuda_EX_FLAGS_CUDA_HOST_REM_CXXFLAGS  := -std=% %potentially-evaluated-expression

ALL_TOOLS      += curl
curl_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/curl/7.59.0-pafccj/include
curl_EX_LIB := curl
curl_EX_USE := root_cxxdefaults

ALL_TOOLS      += cvs2git

ALL_TOOLS      += dablooms
dablooms_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-dablooms/0.9.1-pafccj/include
dablooms_EX_LIB := dablooms

ALL_TOOLS      += das_client
das_client_EX_USE := python

ALL_TOOLS      += davix
davix_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/davix/0.6.7-pafccj/include/davix
davix_EX_LIB := davix
davix_EX_USE := boost_system openssl libxml2

ALL_TOOLS      += db6
db6_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/db6/6.2.32-pafccj/include
db6_EX_LIB := db

ALL_TOOLS      += dcap
dcap_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dcap/2.47.8-pafccj/include
dcap_EX_LIB := dcap
dcap_EX_USE := root_cxxdefaults

ALL_TOOLS      += dd4hep-core
dd4hep-core_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dd4hep/v01-10x-pafccj4/include
dd4hep-core_EX_LIB := DDCore DDParsers
dd4hep-core_EX_USE := root_cxxdefaults root boost xerces-c clhep

ALL_TOOLS      += dd4hep-geant4
dd4hep-geant4_EX_LIB := DDG4-static
dd4hep-geant4_EX_USE := geant4core dd4hep-core

ALL_TOOLS      += dd4hep
dd4hep_EX_LIB := DDAlign DDCond
dd4hep_EX_USE := dd4hep-core

ALL_TOOLS      += dire
dire_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dire/2.003-pafccj4/include
dire_EX_LIB := dire
dire_EX_USE := root_cxxdefaults pythia8

ALL_TOOLS      += distcc-ccompiler
distcc-ccompiler_EX_USE := gcc-ccompiler

ALL_TOOLS      += distcc-cxxcompiler
distcc-cxxcompiler_EX_USE := gcc-cxxcompiler

ALL_TOOLS      += distcc-f77compiler
distcc-f77compiler_EX_USE := gcc-f77compiler

ALL_TOOLS      += dmtcp

ALL_TOOLS      += doxygen

ALL_TOOLS      += dpm
dpm_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dpm/1.8.0.1-pafccj/include
dpm_EX_LIB := dpm
dpm_EX_LIBDIR := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/dpm/1.8.0.1-pafccj/lib
dpm_EX_USE := root_cxxdefaults

ALL_TOOLS      += eigen
eigen_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/eigen/e4c107b451c52c9ab2d7b7fa4194ee35332916ec-pafccj/include/eigen3
eigen_EX_FLAGS_CPPDEFINES  := -DEIGEN_DONT_PARALLELIZE

ALL_TOOLS      += evtgen
evtgen_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/evtgen/1.6.0-pafccj4/include
evtgen_EX_LIB := EvtGen EvtGenExternal
evtgen_EX_USE := hepmc pythia8 tauolapp photospp

ALL_TOOLS      += expat
expat_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/expat/2.1.0-pafccj/include
expat_EX_LIB := expat
expat_EX_USE := root_cxxdefaults

ALL_TOOLS      += fastjet-contrib-archive
fastjet-contrib-archive_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fastjet-contrib/1.033-pafccj/include
fastjet-contrib-archive_EX_LIB := EnergyCorrelator GenericSubtractor JetCleanser JetFFMoments Nsubjettiness ScJet SubjetCounting VariableR

ALL_TOOLS      += fastjet-contrib
fastjet-contrib_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fastjet-contrib/1.033-pafccj/include
fastjet-contrib_EX_LIB := fastjetcontribfragile

ALL_TOOLS      += fastjet
fastjet_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fastjet/3.3.0-pafccj/include
fastjet_EX_LIB := fastjetplugins fastjettools siscone siscone_spherical fastjet
fastjet_EX_USE := root_cxxdefaults

ALL_TOOLS      += fftjet
fftjet_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fftjet/1.5.0-pafccj/include
fftjet_EX_LIB := fftjet
fftjet_EX_USE := root_cxxdefaults

ALL_TOOLS      += fftw3
fftw3_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/fftw3/3.3.2-pafccj/include
fftw3_EX_LIB := fftw3
fftw3_EX_USE := root_cxxdefaults

ALL_TOOLS      += freetype
freetype_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/freetype/2.5.3-pafccj/include
freetype_EX_LIB := freetype-cms
freetype_EX_USE := root_cxxdefaults

ALL_TOOLS      += frontier_client
frontier_client_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/frontier_client/2.8.20-pafccj/include
frontier_client_EX_LIB := frontier_client
frontier_client_EX_USE := root_cxxdefaults zlib openssl expat python

ALL_TOOLS      += gbl
gbl_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gbl/V02-01-03-pafccj/include
gbl_EX_LIB := GBL
gbl_EX_USE := eigen

ALL_TOOLS      += gcc-analyzer-ccompiler
gcc-analyzer-ccompiler_EX_FLAGS_CFLAGS  := -fplugin=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc-checker-plugin/1.2-pafccj/lib/libchecker_gccplugins.so -fplugin-arg-libchecker_gccplugins-checkers=all -fsyntax-only

ALL_TOOLS      += gcc-analyzer-cxxcompiler
gcc-analyzer-cxxcompiler_EX_FLAGS_CXXFLAGS  := -fplugin=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc-checker-plugin/1.2-pafccj/lib/libchecker_gccplugins.so -fplugin-arg-libchecker_gccplugins-checkers=all -fsyntax-only

ALL_TOOLS      += gcc-atomic
gcc-atomic_EX_LIB := atomic

ALL_TOOLS      += gcc-ccompiler
gcc-ccompiler_EX_FLAGS_CFLAGS  := -O2 -pthread
gcc-ccompiler_EX_FLAGS_CSHAREDOBJECTFLAGS  := -fPIC

ALL_TOOLS      += gcc-checker-plugin
gcc-checker-plugin_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc-checker-plugin/1.2-pafccj/include

ALL_TOOLS      += gcc-cxxcompiler
gcc-cxxcompiler_EX_FLAGS_CXXSHAREDFLAGS  := -shared -Wl,-E
gcc-cxxcompiler_EX_FLAGS_CXXSHAREDOBJECTFLAGS  := -fPIC
gcc-cxxcompiler_EX_FLAGS_LDFLAGS  := -Wl,-E -Wl,--hash-style=gnu
gcc-cxxcompiler_EX_FLAGS_CPPDEFINES  := -DGNU_GCC -D_GNU_SOURCE
gcc-cxxcompiler_EX_FLAGS_CXXFLAGS  := -O2 -pthread -pipe -Werror=main -Werror=pointer-arith -Werror=overlength-strings -Wno-vla -Werror=overflow -std=c++1z -ftree-vectorize -Wstrict-overflow -Werror=array-bounds -Werror=format-contains-nul -Werror=type-limits -fvisibility-inlines-hidden -fno-math-errno --param vect-max-version-for-alias-checks=50 -Xassembler --compress-debug-sections -msse3 -felide-constructors -fmessage-length=0 -Wall -Wno-non-template-friend -Wno-long-long -Wreturn-type -Wunused -Wparentheses -Wno-deprecated -Werror=return-type -Werror=missing-braces -Werror=unused-value -Werror=address -Werror=format -Werror=sign-compare -Werror=write-strings -Werror=delete-non-virtual-dtor -Werror=strict-aliasing -Werror=narrowing -Werror=unused-but-set-variable -Werror=reorder -Werror=unused-variable -Werror=conversion-null -Werror=return-local-addr -Wnon-virtual-dtor -Werror=switch -fdiagnostics-show-option -Wno-unused-local-typedefs -Wno-attributes -Wno-psabi
gcc-cxxcompiler_EX_FLAGS_LD_UNIT  := -r -z muldefs

ALL_TOOLS      += gcc-f77compiler
gcc-f77compiler_EX_LIB := gfortran m
gcc-f77compiler_EX_FLAGS_FFLAGS  := -fno-second-underscore -Wunused -Wuninitialized -O2 -cpp
gcc-f77compiler_EX_FLAGS_FOPTIMISEDFLAGS  := -O2
gcc-f77compiler_EX_FLAGS_FSHAREDOBJECTFLAGS  := -fPIC

ALL_TOOLS      += gcc-plugin
gcc-plugin_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/lib/gcc/x86_64-unknown-linux-gnu/8.3.1/plugin/include
gcc-plugin_EX_LIB := cc1plugin cp1plugin

ALL_TOOLS      += gdb

ALL_TOOLS      += gdbm
gdbm_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gdbm/1.10-pafccj/include
gdbm_EX_LIB := gdbm
gdbm_EX_USE := root_cxxdefaults

ALL_TOOLS      += geant4-parfullcms

ALL_TOOLS      += geant4
geant4_EX_USE := geant4core geant4vis xerces-c

ALL_TOOLS      += geant4core
geant4core_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/geant4/10.4.3-pafccj/include/Geant4
geant4core_EX_LIB := G4digits_hits G4error_propagation G4event G4geometry G4global G4graphics_reps G4intercoms G4interfaces G4materials G4parmodels G4particles G4persistency G4physicslists G4processes G4readout G4run G4tracking G4track G4analysis
geant4core_EX_USE := clhep vecgeom root_cxxdefaults
geant4core_EX_FLAGS_CXXFLAGS  := -DG4MULTITHREADED -DG4USE_STD11 -DG4GEOM_USE_USOLIDS -ftls-model=global-dynamic -pthread
geant4core_EX_FLAGS_CPPDEFINES  := -DGNU_GCC -DG4V9

ALL_TOOLS      += geant4data

ALL_TOOLS      += geant4static
geant4static_EX_LIB := geant4-static
geant4static_EX_USE := vecgeom clhep xerces-c
geant4static_EX_FLAGS_CXXFLAGS  := -DG4MULTITHREADED -DG4USE_STD11 -ftls-model=global-dynamic -pthread

ALL_TOOLS      += geant4vis
geant4vis_EX_LIB := G4FR G4modeling G4RayTracer G4Tree G4visHepRep G4vis_management G4visXXX G4VRML G4GMocren G4zlib
geant4vis_EX_USE := geant4core

ALL_TOOLS      += geneva
geneva_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/geneva/1.0-RC3-pafccj4/include/Geneva
geneva_EX_USE := root_cxxdefaults python py2-numpy hepmc lhapdf openloops gsl boost pythia8

ALL_TOOLS      += giflib
giflib_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/giflib/4.2.3-pafccj/include
giflib_EX_LIB := gif
giflib_EX_USE := root_cxxdefaults

ALL_TOOLS      += git

ALL_TOOLS      += glibc

ALL_TOOLS      += glimpse

ALL_TOOLS      += gmake

ALL_TOOLS      += gmp
gmp_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gmp-static/6.1.0-pafccj/include
gmp_EX_LIB := gmp
gmp_EX_USE := mpfr

ALL_TOOLS      += gnuplot

ALL_TOOLS      += google-benchmark-main
google-benchmark-main_EX_LIB := benchmark_main
google-benchmark-main_EX_USE := google-benchmark

ALL_TOOLS      += google-benchmark
google-benchmark_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/google-benchmark/1.4.x-pafccj/include
google-benchmark_EX_LIB := benchmark
google-benchmark_EX_USE := sockets

ALL_TOOLS      += gosam

ALL_TOOLS      += gosamcontrib
gosamcontrib_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gosamcontrib/2.0-20150803-pafccj/include

ALL_TOOLS      += graphviz
graphviz_EX_USE := expat zlib libjpeg-turbo libpng

ALL_TOOLS      += gsl
gsl_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gsl/2.2.1-pafccj/include
gsl_EX_LIB := gsl gslcblas
gsl_EX_USE := root_cxxdefaults

ALL_TOOLS      += hdf5
hdf5_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hdf5/1.8.17-pafccj/include
hdf5_EX_LIB := hdf5 hdf5_cpp hdf5_hl hdf5_hl_cpp

ALL_TOOLS      += hector
hector_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hector/1.3.4_patch1-pafccj4/include
hector_EX_LIB := Hector
hector_EX_USE := root_cxxdefaults

ALL_TOOLS      += hepmc
hepmc_EX_LIB := HepMCfio HepMC
hepmc_EX_USE := hepmc_headers

ALL_TOOLS      += hepmc_headers
hepmc_headers_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hepmc/2.06.07-pafccj/include
hepmc_headers_EX_USE := root_cxxdefaults

ALL_TOOLS      += heppdt
heppdt_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/heppdt/3.03.00-pafccj/include
heppdt_EX_LIB := HepPDT HepPID
heppdt_EX_USE := root_cxxdefaults

ALL_TOOLS      += herwig
herwig_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/herwig/6.521-pafccj3/include
herwig_EX_LIB := herwig herwig_dummy
herwig_EX_USE := root_cxxdefaults f77compiler lhapdf photos

ALL_TOOLS      += herwigpp
herwigpp_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/herwigpp/7.1.4-pafccj5/include
herwigpp_EX_LIB := HerwigAPI
herwigpp_EX_USE := root_cxxdefaults lhapdf thepeg madgraph5amcatnlo openloops

ALL_TOOLS      += histfactory
histfactory_EX_LIB := HistFactory
histfactory_EX_USE := roofitcore roofit roostats rootcore roothistmatrix rootgpad rootxml rootfoam

ALL_TOOLS      += hls
hls_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hls/2019.08/include
hls_EX_USE := root_cxxdefaults

ALL_TOOLS      += igprof

ALL_TOOLS      += intel-license

ALL_TOOLS      += ittnotify
ittnotify_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/ittnotify/16.06.18-pafccj/include
ittnotify_EX_LIB := ittnotify

ALL_TOOLS      += iwyu-cxxcompiler
iwyu-cxxcompiler_EX_USE := llvm-cxxcompiler

ALL_TOOLS      += jemalloc
jemalloc_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/jemalloc/5.1.0-pafccj/include
jemalloc_EX_LIB := jemalloc
jemalloc_EX_USE := root_cxxdefaults

ALL_TOOLS      += jimmy
jimmy_EX_LIB := jimmy
jimmy_EX_USE := f77compiler herwig jimmy_headers

ALL_TOOLS      += jimmy_headers
jimmy_headers_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/jimmy/4.2-pafccj3/include
jimmy_headers_EX_USE := root_cxxdefaults

ALL_TOOLS      += ktjet
ktjet_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/ktjet/1.06-pafccj/include
ktjet_EX_LIB := KtEvent
ktjet_EX_USE := root_cxxdefaults
ktjet_EX_FLAGS_CPPDEFINES  := -DKTDOUBLEPRECISION

ALL_TOOLS      += lapack

ALL_TOOLS      += lcov

ALL_TOOLS      += lhapdf
lhapdf_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lhapdf/6.2.1-pafccj3/include
lhapdf_EX_LIB := LHAPDF
lhapdf_EX_USE := yaml-cpp root_cxxdefaults

ALL_TOOLS      += libffi
libffi_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libffi/3.2.1-pafccj/include
libffi_EX_LIB := ffi

ALL_TOOLS      += libhepml
libhepml_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libhepml/0.2.1-pafccj/interface
libhepml_EX_LIB := hepml
libhepml_EX_USE := root_cxxdefaults

ALL_TOOLS      += libjpeg-turbo
libjpeg-turbo_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libjpeg-turbo/2.0.1-pafccj/include
libjpeg-turbo_EX_LIB := jpeg turbojpeg
libjpeg-turbo_EX_USE := root_cxxdefaults

ALL_TOOLS      += libpng
libpng_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libpng/1.6.16-pafccj/include
libpng_EX_LIB := png
libpng_EX_USE := root_cxxdefaults zlib

ALL_TOOLS      += libtiff
libtiff_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libtiff/4.0.3-pafccj/include
libtiff_EX_LIB := tiff
libtiff_EX_USE := root_cxxdefaults libjpeg-turbo zlib

ALL_TOOLS      += libungif
libungif_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libungif/4.1.4-pafccj/include
libungif_EX_LIB := ungif
libungif_EX_USE := root_cxxdefaults zlib

ALL_TOOLS      += libuuid
libuuid_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libuuid/2.22.2-pafccj/include
libuuid_EX_LIB := uuid
libuuid_EX_USE := root_cxxdefaults sockets

ALL_TOOLS      += libxml2
libxml2_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libxml2/2.9.1-pafccj/include/libxml2
libxml2_EX_LIB := xml2
libxml2_EX_USE := root_cxxdefaults

ALL_TOOLS      += libxslt
libxslt_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libxslt/1.1.28-pafccj/include/libxslt
libxslt_EX_LIB := xslt

ALL_TOOLS      += llvm-analyzer-ccompiler
llvm-analyzer-ccompiler_EX_USE := llvm-ccompiler

ALL_TOOLS      += llvm-analyzer-cxxcompiler
llvm-analyzer-cxxcompiler_EX_USE := llvm-cxxcompiler

ALL_TOOLS      += llvm-ccompiler
llvm-ccompiler_EX_USE := gcc-ccompiler

ALL_TOOLS      += llvm-cxxcompiler
llvm-cxxcompiler_EX_USE := gcc-cxxcompiler
llvm-cxxcompiler_EX_FLAGS_CXXFLAGS  := -Wno-c99-extensions -Wno-c++11-narrowing -D__STRICT_ANSI__ -Wno-unused-private-field -Wno-unknown-pragmas -Wno-unused-command-line-argument -Wno-unknown-warning-option -ftemplate-depth=512 -Wno-error=potentially-evaluated-expression
llvm-cxxcompiler_EX_FLAGS_REM_CXXFLAGS  := -Wno-non-template-friend -Werror=format-contains-nul -Werror=maybe-uninitialized -Werror=unused-but-set-variable -Werror=return-local-addr -fipa-pta -frounding-math -mrecip -Wno-psabi -fno-crossjumping -fno-aggressive-loop-optimizations -mlong-double-64

ALL_TOOLS      += llvm-f77compiler
llvm-f77compiler_EX_USE := gcc-f77compiler

ALL_TOOLS      += llvm
llvm_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/llvm/7.1.0/include
llvm_EX_LIB := clang
llvm_EX_FLAGS_LDFLAGS  := -Wl,-undefined -Wl,suppress
llvm_EX_FLAGS_CXXFLAGS  := -D_DEBUG -D_GNU_SOURCE -D__STDC_CONSTANT_MACROS -D__STDC_FORMAT_MACROS -D__STDC_LIMIT_MACROS -O3 -fomit-frame-pointer -fPIC -Wno-enum-compare -Wno-strict-aliasing -fno-rtti

ALL_TOOLS      += lwtnn
lwtnn_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lwtnn/2.4-pafccj/include
lwtnn_EX_LIB := lwtnn
lwtnn_EX_USE := root_cxxdefaults eigen boost_system

ALL_TOOLS      += madgraph5amcatnlo
madgraph5amcatnlo_EX_USE := root_cxxdefaults gosamcontrib

ALL_TOOLS      += mcdb
mcdb_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mcdb/1.0.3-pafccj/interface
mcdb_EX_LIB := mcdb
mcdb_EX_USE := root_cxxdefaults xerces-c

ALL_TOOLS      += mctester
mctester_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mctester/1.25.0a-pafccj4/include
mctester_EX_LIB := HEPEvent HepMCEvent MCTester
mctester_EX_USE := root_cxxdefaults root hepmc

ALL_TOOLS      += md5
md5_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/md5/1.0.0-pafccj/include
md5_EX_LIB := cms-md5

ALL_TOOLS      += meschach
meschach_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/meschach/1.2.pCMS1-pafccj/include
meschach_EX_LIB := meschach
meschach_EX_USE := root_cxxdefaults

ALL_TOOLS      += millepede
millepede_EX_USE := sockets pcre zlib

ALL_TOOLS      += mpfr
mpfr_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mpfr-static/4.0.1-pafccj/include
mpfr_EX_LIB := mpfr

ALL_TOOLS      += mxnet-predict
mxnet-predict_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/mxnet-predict/1.2.1-pafccj2/include
mxnet-predict_EX_LIB := mxnetpredict
mxnet-predict_EX_USE := openblas

ALL_TOOLS      += numpy-c-api
numpy-c-api_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-numpy/1.16.2-pafccj/c-api/core/include
numpy-c-api_EX_LIB := npymath
numpy-c-api_EX_USE := root_cxxdefaults

ALL_TOOLS      += ofast-flag
ofast-flag_EX_FLAGS_CXXFLAGS  := -Ofast
ofast-flag_EX_FLAGS_NO_RECURSIVE_EXPORT  := 1

ALL_TOOLS      += openblas
openblas_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/OpenBLAS/0.3.5/include
openblas_EX_LIB := openblas

ALL_TOOLS      += opengl
opengl_EX_LIB := GL GLU
opengl_EX_USE := x11

ALL_TOOLS      += openldap
openldap_EX_USE := openssl db6

ALL_TOOLS      += openloops

ALL_TOOLS      += openmpi
openmpi_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/openmpi/2.1.5-pafccj/include
openmpi_EX_LIB := mpi mpi_cxx

ALL_TOOLS      += openssl
openssl_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/openssl/1.0.2d-pafccj/include
openssl_EX_LIB := ssl crypto
openssl_EX_USE := root_cxxdefaults

ALL_TOOLS      += oracle
oracle_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/oracle/12.1.0.2.0-pafccj2/include
oracle_EX_LIB := clntsh
oracle_EX_USE := root_cxxdefaults sockets

ALL_TOOLS      += oracleocci
oracleocci_EX_LIB := occi
oracleocci_EX_USE := oracle

ALL_TOOLS      += pacparser
pacparser_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pacparser/1.3.5-pafccj/include
pacparser_EX_LIB := pacparser
pacparser_EX_USE := root_cxxdefaults

ALL_TOOLS      += pcre
pcre_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pcre/8.37-pafccj/include
pcre_EX_LIB := pcre
pcre_EX_USE := root_cxxdefaults zlib bz2lib

ALL_TOOLS      += photos
photos_EX_LIB := photos
photos_EX_USE := photos_headers f77compiler

ALL_TOOLS      += photos_headers
photos_headers_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/photos/215.5-pafccj/include
photos_headers_EX_USE := root_cxxdefaults

ALL_TOOLS      += photospp
photospp_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/photospp/3.61-pafccj/include
photospp_EX_LIB := Photospp PhotosppHepMC PhotosppHEPEVT
photospp_EX_USE := hepmc

ALL_TOOLS      += professor

ALL_TOOLS      += professor2
professor2_EX_USE := py2-numpy py2-sympy root yoda eigen

ALL_TOOLS      += protobuf
protobuf_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/protobuf/3.5.2-pafccj/include
protobuf_EX_LIB := protobuf
protobuf_EX_USE := root_cxxdefaults

ALL_TOOLS      += py2-absl-py

ALL_TOOLS      += py2-appdirs

ALL_TOOLS      += py2-argparse

ALL_TOOLS      += py2-asn1crypto

ALL_TOOLS      += py2-atomicwrites

ALL_TOOLS      += py2-attrs

ALL_TOOLS      += py2-autopep8

ALL_TOOLS      += py2-avro

ALL_TOOLS      += py2-awkward

ALL_TOOLS      += py2-backcall

ALL_TOOLS      += py2-backports-functools_lru_cache

ALL_TOOLS      += py2-backports

ALL_TOOLS      += py2-backports_abc

ALL_TOOLS      += py2-beautifulsoup4

ALL_TOOLS      += py2-bleach

ALL_TOOLS      += py2-bokeh

ALL_TOOLS      += py2-bottleneck

ALL_TOOLS      += py2-cachetools

ALL_TOOLS      += py2-certifi

ALL_TOOLS      += py2-cffi

ALL_TOOLS      += py2-chardet

ALL_TOOLS      += py2-click

ALL_TOOLS      += py2-climate

ALL_TOOLS      += py2-colorama

ALL_TOOLS      += py2-contextlib2

ALL_TOOLS      += py2-cryptography

ALL_TOOLS      += py2-cx-oracle

ALL_TOOLS      += py2-cycler

ALL_TOOLS      += py2-cython

ALL_TOOLS      += py2-dablooms

ALL_TOOLS      += py2-decorator

ALL_TOOLS      += py2-defusedxml

ALL_TOOLS      += py2-docopt

ALL_TOOLS      += py2-downhill

ALL_TOOLS      += py2-dxr

ALL_TOOLS      += py2-entrypoints

ALL_TOOLS      += py2-enum34

ALL_TOOLS      += py2-flake8

ALL_TOOLS      += py2-flawfinder

ALL_TOOLS      += py2-fs

ALL_TOOLS      += py2-funcsigs

ALL_TOOLS      += py2-functools32

ALL_TOOLS      += py2-future

ALL_TOOLS      += py2-futures

ALL_TOOLS      += py2-gast

ALL_TOOLS      += py2-gitdb2

ALL_TOOLS      += py2-gitpython

ALL_TOOLS      += py2-google-common

ALL_TOOLS      += py2-googlepackages

ALL_TOOLS      += py2-grpcio

ALL_TOOLS      += py2-h5py-cache

ALL_TOOLS      += py2-h5py

ALL_TOOLS      += py2-hep_ml

ALL_TOOLS      += py2-histbook

ALL_TOOLS      += py2-histogrammar

ALL_TOOLS      += py2-html5lib

ALL_TOOLS      += py2-hyperas

ALL_TOOLS      += py2-hyperopt

ALL_TOOLS      += py2-idna

ALL_TOOLS      += py2-ipaddress

ALL_TOOLS      += py2-ipykernel

ALL_TOOLS      += py2-ipython

ALL_TOOLS      += py2-ipython_genutils

ALL_TOOLS      += py2-ipywidgets

ALL_TOOLS      += py2-jedi

ALL_TOOLS      += py2-jinja2

ALL_TOOLS      += py2-jsonpickle

ALL_TOOLS      += py2-jsonschema

ALL_TOOLS      += py2-jupyter

ALL_TOOLS      += py2-jupyter_client

ALL_TOOLS      += py2-jupyter_console

ALL_TOOLS      += py2-jupyter_core

ALL_TOOLS      += py2-keras-applications

ALL_TOOLS      += py2-keras-preprocessing

ALL_TOOLS      += py2-keras

ALL_TOOLS      += py2-kiwisolver

ALL_TOOLS      += py2-lint

ALL_TOOLS      += py2-lizard

ALL_TOOLS      += py2-llvmlite

ALL_TOOLS      += py2-lxml

ALL_TOOLS      += py2-lz4

ALL_TOOLS      += py2-markdown

ALL_TOOLS      += py2-markupsafe

ALL_TOOLS      += py2-matplotlib

ALL_TOOLS      += py2-mccabe

ALL_TOOLS      += py2-mistune

ALL_TOOLS      += py2-mock

ALL_TOOLS      += py2-more-itertools

ALL_TOOLS      += py2-mpld3

ALL_TOOLS      += py2-mpmath

ALL_TOOLS      += py2-nbconvert

ALL_TOOLS      += py2-nbdime

ALL_TOOLS      += py2-nbformat

ALL_TOOLS      += py2-networkx

ALL_TOOLS      += py2-neurolab

ALL_TOOLS      += py2-nose-parameterized

ALL_TOOLS      += py2-nose

ALL_TOOLS      += py2-notebook

ALL_TOOLS      += py2-numba

ALL_TOOLS      += py2-numexpr

ALL_TOOLS      += py2-numpy

ALL_TOOLS      += py2-oamap

ALL_TOOLS      += py2-onnx

ALL_TOOLS      += py2-ordereddict

ALL_TOOLS      += py2-packaging

ALL_TOOLS      += py2-pandas

ALL_TOOLS      += py2-pandocfilters

ALL_TOOLS      += py2-parsimonious

ALL_TOOLS      += py2-parso

ALL_TOOLS      += py2-pathlib2

ALL_TOOLS      += py2-pbr

ALL_TOOLS      += py2-pexpect

ALL_TOOLS      += py2-pickleshare

ALL_TOOLS      += py2-pillow

ALL_TOOLS      += py2-pip

ALL_TOOLS      += py2-pkgconfig

ALL_TOOLS      += py2-plac

ALL_TOOLS      += py2-pluggy

ALL_TOOLS      += py2-ply

ALL_TOOLS      += py2-prettytable

ALL_TOOLS      += py2-prometheus_client

ALL_TOOLS      += py2-prompt_toolkit

ALL_TOOLS      += py2-protobuf

ALL_TOOLS      += py2-prwlock

ALL_TOOLS      += py2-psutil

ALL_TOOLS      += py2-ptyprocess

ALL_TOOLS      += py2-py

ALL_TOOLS      += py2-pyasn1-modules

ALL_TOOLS      += py2-pyasn1

ALL_TOOLS      += py2-pybind11
py2-pybind11_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/py2-pybind11/2.2.4-pafccj/include/python2.7

ALL_TOOLS      += py2-pybrain

ALL_TOOLS      += py2-pycodestyle

ALL_TOOLS      += py2-pycparser

ALL_TOOLS      += py2-pycurl

ALL_TOOLS      += py2-pydot

ALL_TOOLS      += py2-pyflakes

ALL_TOOLS      += py2-pygithub

ALL_TOOLS      += py2-pygments

ALL_TOOLS      += py2-pymongo

ALL_TOOLS      += py2-pyopenssl

ALL_TOOLS      += py2-pyparsing

ALL_TOOLS      += py2-pysqlite

ALL_TOOLS      += py2-pytest

ALL_TOOLS      += py2-python-cjson

ALL_TOOLS      += py2-python-dateutil

ALL_TOOLS      += py2-python-ldap

ALL_TOOLS      += py2-pytz

ALL_TOOLS      += py2-pyyaml

ALL_TOOLS      += py2-pyzmq

ALL_TOOLS      += py2-qtconsole

ALL_TOOLS      += py2-rep

ALL_TOOLS      += py2-repoze-lru

ALL_TOOLS      += py2-requests

ALL_TOOLS      += py2-root_numpy

ALL_TOOLS      += py2-root_pandas

ALL_TOOLS      += py2-rootpy

ALL_TOOLS      += py2-scandir

ALL_TOOLS      += py2-schema

ALL_TOOLS      += py2-scikit-learn

ALL_TOOLS      += py2-scipy

ALL_TOOLS      += py2-seaborn

ALL_TOOLS      += py2-send2trash

ALL_TOOLS      += py2-setuptools

ALL_TOOLS      += py2-simplegeneric

ALL_TOOLS      += py2-singledispatch

ALL_TOOLS      += py2-six

ALL_TOOLS      += py2-smmap2

ALL_TOOLS      += py2-soupsieve

ALL_TOOLS      += py2-sqlalchemy

ALL_TOOLS      += py2-stevedore

ALL_TOOLS      += py2-subprocess32

ALL_TOOLS      += py2-sympy

ALL_TOOLS      += py2-tables

ALL_TOOLS      += py2-tensorflow

ALL_TOOLS      += py2-terminado

ALL_TOOLS      += py2-testpath

ALL_TOOLS      += py2-theanets

ALL_TOOLS      += py2-theano

ALL_TOOLS      += py2-thriftpy

ALL_TOOLS      += py2-tornado

ALL_TOOLS      += py2-tqdm

ALL_TOOLS      += py2-traitlets

ALL_TOOLS      += py2-typing

ALL_TOOLS      += py2-typing_extensions

ALL_TOOLS      += py2-uncertainties

ALL_TOOLS      += py2-uproot-methods

ALL_TOOLS      += py2-uproot

ALL_TOOLS      += py2-urllib3

ALL_TOOLS      += py2-virtualenv-clone

ALL_TOOLS      += py2-virtualenv

ALL_TOOLS      += py2-virtualenvwrapper

ALL_TOOLS      += py2-wcwidth

ALL_TOOLS      += py2-webencodings

ALL_TOOLS      += py2-werkzeug

ALL_TOOLS      += py2-wheel

ALL_TOOLS      += py2-widgetsnbextension

ALL_TOOLS      += py2-xgboost

ALL_TOOLS      += py2-xrootdpyfs

ALL_TOOLS      += pyclang
pyclang_EX_USE := python

ALL_TOOLS      += pydata
pydata_EX_FLAGS_LDFLAGS  := $(PYDATA_BASE)/lib/pydata.o
pydata_EX_FLAGS_NO_RECURSIVE_EXPORT  := 1

ALL_TOOLS      += pyminuit2

ALL_TOOLS      += pyqt

ALL_TOOLS      += pyquen
pyquen_EX_LIB := pyquen
pyquen_EX_USE := pythia6 lhapdf

ALL_TOOLS      += pythia6
pythia6_EX_LIB := pythia6 pythia6_dummy pythia6_pdfdummy
pythia6_EX_USE := pythia6_headers f77compiler

ALL_TOOLS      += pythia6_headers
pythia6_headers_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pythia6/426-pafccj/include
pythia6_headers_EX_USE := root_cxxdefaults

ALL_TOOLS      += pythia8
pythia8_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pythia8/240-pafccj4/include
pythia8_EX_LIB := pythia8
pythia8_EX_USE := root_cxxdefaults cxxcompiler hepmc lhapdf

ALL_TOOLS      += python-paths

ALL_TOOLS      += python
python_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/python/2.7.15-pafccj/include/python2.7
python_EX_LIB := python2.7
python_EX_USE := root_cxxdefaults sockets

ALL_TOOLS      += python3
python3_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/python3/3.6.4-pafccj/include/python3.6m
python3_EX_LIB := python3.6m
python3_EX_USE := sockets

ALL_TOOLS      += python_tools

ALL_TOOLS      += qd
qd_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qd/2.3.13-pafccj/include
qd_EX_LIB := qdmod qd

ALL_TOOLS      += qd_f_main
qd_f_main_EX_LIB := qd_f_main
qd_f_main_EX_USE := qd

ALL_TOOLS      += qt
qt_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj/include/QtOpenGL /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj/include/QtGui
qt_EX_LIB := QtOpenGL QtGui
qt_EX_USE := root_cxxdefaults qtbase qt3support x11 opengl

ALL_TOOLS      += qt3support
qt3support_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj/include/Qt3Support
qt3support_EX_LIB := Qt3Support
qt3support_EX_USE := root_cxxdefaults qtbase
qt3support_EX_FLAGS_CPPDEFINES  := -DQT3_SUPPORT

ALL_TOOLS      += qtbase
qtbase_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj/include /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj/include/Qt /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj/include/QtCore /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj/include/QtXml
qtbase_EX_LIB := QtCore QtXml
qtbase_EX_USE := root_cxxdefaults zlib
qtbase_EX_FLAGS_CPPDEFINES  := -DQT_ALTERNATE_QTSMANIP -DQT_CLEAN_NAMESPACE -DQT_THREAD_SUPPORT

ALL_TOOLS      += qtdesigner
qtdesigner_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/qt/4.8.7-pafccj/include/QtDesigner
qtdesigner_EX_LIB := QtDesigner
qtdesigner_EX_USE := root_cxxdefaults qtbase qt

ALL_TOOLS      += rivet
rivet_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/rivet/2.7.0-pafccj3/include
rivet_EX_LIB := Rivet
rivet_EX_USE := hepmc fastjet gsl yoda

ALL_TOOLS      += roofit
roofit_EX_LIB := RooFit
roofit_EX_USE := roofitcore rootcore rootmath roothistmatrix

ALL_TOOLS      += roofitcore
roofitcore_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09/include
roofitcore_EX_LIB := RooFitCore
roofitcore_EX_USE := rootcore roothistmatrix rootgpad rootminuit root_cxxdefaults

ALL_TOOLS      += roostats
roostats_EX_LIB := RooStats
roostats_EX_USE := roofitcore roofit rootcore roothistmatrix rootgpad

ALL_TOOLS      += root
root_EX_USE := rootphysics
root_EX_FLAGS_NO_CAPABILITIES  := yes

ALL_TOOLS      += root_cxxdefaults

ALL_TOOLS      += root_interface
root_interface_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09/include
root_interface_EX_USE := root_cxxdefaults

ALL_TOOLS      += rootcling
rootcling_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09/include
rootcling_EX_LIB := Core
rootcling_EX_USE := root_interface sockets pcre zlib xz

ALL_TOOLS      += rootcore
rootcore_EX_LIB := Tree Net
rootcore_EX_USE := rootmathcore rootthread

ALL_TOOLS      += rootdataframe
rootdataframe_EX_LIB := ROOTDataFrame
rootdataframe_EX_USE := rootcore rootgraphics roothistmatrix rootrio rootvecops

ALL_TOOLS      += rooteg
rooteg_EX_LIB := EG
rooteg_EX_USE := rootgraphics

ALL_TOOLS      += rooteve
rooteve_EX_LIB := Eve
rooteve_EX_USE := rootgeompainter rootrgl rootged

ALL_TOOLS      += rootfoam
rootfoam_EX_LIB := Foam
rootfoam_EX_USE := roothistmatrix

ALL_TOOLS      += rootged
rootged_EX_LIB := Ged
rootged_EX_USE := rootgui

ALL_TOOLS      += rootgeom
rootgeom_EX_LIB := Geom
rootgeom_EX_USE := rootrio rootmathcore

ALL_TOOLS      += rootgeompainter
rootgeompainter_EX_LIB := GeomPainter
rootgeompainter_EX_USE := rootgeom rootgraphics

ALL_TOOLS      += rootglew
rootglew_EX_LIB := GLEW

ALL_TOOLS      += rootgpad
rootgpad_EX_LIB := Gpad Graf
rootgpad_EX_USE := roothistmatrix

ALL_TOOLS      += rootgraphics
rootgraphics_EX_LIB := TreePlayer Graf3d Postscript
rootgraphics_EX_USE := rootgpad

ALL_TOOLS      += rootgui
rootgui_EX_LIB := Gui
rootgui_EX_USE := rootgpad

ALL_TOOLS      += rootguihtml
rootguihtml_EX_LIB := GuiHtml
rootguihtml_EX_USE := rootgui rootinteractive

ALL_TOOLS      += roothistmatrix
roothistmatrix_EX_LIB := Hist Matrix
roothistmatrix_EX_USE := rootcore

ALL_TOOLS      += roothtml
roothtml_EX_LIB := Html
roothtml_EX_USE := rootgpad

ALL_TOOLS      += rootinteractive
rootinteractive_EX_LIB := Gui
rootinteractive_EX_USE := libjpeg-turbo libpng rootgpad rootrint

ALL_TOOLS      += rootmath
rootmath_EX_LIB := GenVector MathMore
rootmath_EX_USE := rootcore gsl

ALL_TOOLS      += rootmathcore
rootmathcore_EX_LIB := MathCore
rootmathcore_EX_USE := rootcling

ALL_TOOLS      += rootminuit
rootminuit_EX_LIB := Minuit
rootminuit_EX_USE := rootgpad

ALL_TOOLS      += rootminuit2
rootminuit2_EX_LIB := Minuit2
rootminuit2_EX_USE := rootgpad

ALL_TOOLS      += rootmlp
rootmlp_EX_LIB := MLP
rootmlp_EX_USE := rootgraphics

ALL_TOOLS      += rootphysics
rootphysics_EX_LIB := Physics
rootphysics_EX_USE := roothistmatrix

ALL_TOOLS      += rootpy
rootpy_EX_LIB := PyROOT
rootpy_EX_USE := rootgraphics

ALL_TOOLS      += rootpymva
rootpymva_EX_LIB := PyMVA
rootpymva_EX_USE := roottmva numpy-c-api

ALL_TOOLS      += rootrflx
rootrflx_EX_USE := root_interface rootcling
rootrflx_EX_FLAGS_GENREFLEX_CPPFLAGS  := -DCMS_DICT_IMPL -D_REENTRANT -DGNUSOURCE -D__STRICT_ANSI__
rootrflx_EX_FLAGS_GENREFLEX_GCCXMLOPT  := -m64
rootrflx_EX_FLAGS_GENREFLEX_ARGS  := --deep

ALL_TOOLS      += rootrgl
rootrgl_EX_LIB := RGL
rootrgl_EX_USE := rootglew rootgui rootinteractive rootgraphics

ALL_TOOLS      += rootrint
rootrint_EX_LIB := Rint
rootrint_EX_USE := rootcling

ALL_TOOLS      += rootrio
rootrio_EX_LIB := RIO
rootrio_EX_USE := rootcling

ALL_TOOLS      += rootsmatrix
rootsmatrix_EX_LIB := Smatrix
rootsmatrix_EX_USE := rootcling

ALL_TOOLS      += rootspectrum
rootspectrum_EX_LIB := Spectrum
rootspectrum_EX_USE := roothistmatrix

ALL_TOOLS      += rootthread
rootthread_EX_LIB := Thread
rootthread_EX_USE := rootrio

ALL_TOOLS      += roottmva
roottmva_EX_LIB := TMVA
roottmva_EX_USE := rootmlp rootminuit

ALL_TOOLS      += rootvecops
rootvecops_EX_LIB := ROOTVecOps
rootvecops_EX_USE := rootcore

ALL_TOOLS      += rootx11
rootx11_EX_LIB := GCocoa
rootx11_EX_USE := rootcling

ALL_TOOLS      += rootxml
rootxml_EX_LIB := XMLParser
rootxml_EX_USE := rootcore libxml2

ALL_TOOLS      += rootxmlio
rootxmlio_EX_LIB := XMLIO
rootxmlio_EX_USE := rootrio

ALL_TOOLS      += scons

ALL_TOOLS      += self
self_EX_INCLUDE := /home/freerc/Nano_SUEP/CMSSW_10_6_4/src /home/freerc/Nano_SUEP/CMSSW_10_6_4/include/slc7_amd64_gcc820/src /home/freerc/Nano_SUEP/CMSSW_10_6_4/include/LCG /cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_4/src /cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_4/include/slc7_amd64_gcc820/src /cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_4/include/LCG
self_EX_LIBDIR := /home/freerc/Nano_SUEP/CMSSW_10_6_4/lib/slc7_amd64_gcc820 /home/freerc/Nano_SUEP/CMSSW_10_6_4/external/slc7_amd64_gcc820/lib /cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_4/lib/slc7_amd64_gcc820 /cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_4/external/slc7_amd64_gcc820/lib
self_EX_FLAGS_SYMLINK_DEPTH_CMSSW_SEARCH_PATH  := 2
self_EX_FLAGS_LLVM_ANALYZER  := llvm-analyzer
self_EX_FLAGS_SKIP_TOOLS_SYMLINK  := cxxcompiler ccompiler f77compiler gcc-cxxcompiler gcc-ccompiler gcc-f77compiler llvm-cxxcompiler llvm-ccompiler llvm-f77compiler llvm-analyzer-cxxcompiler llvm-analyzer-ccompiler icc-cxxcompiler icc-ccompiler icc-f77compiler x11 dpm
self_EX_FLAGS_DEFAULT_COMPILER  := gcc
self_EX_FLAGS_EXTERNAL_SYMLINK  := PATH LIBDIR CMSSW_SEARCH_PATH
self_EX_FLAGS_NO_EXTERNAL_RUNTIME  := LD_LIBRARY_PATH PATH CMSSW_SEARCH_PATH
TOOLS_OVERRIDABLE_FLAGS  +=CPPDEFINES CXXFLAGS FFLAGS CFLAGS CPPFLAGS LDFLAGS CUDA_FLAGS CUDA_LDFLAGS
self_ORDER := 20000
IS_PATCH:=

ALL_TOOLS      += sherpa
sherpa_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sherpa/2.2.6-pafccj3/include/SHERPA-MC
sherpa_EX_LIB := SherpaMain ToolsMath ToolsOrg
sherpa_EX_USE := root_cxxdefaults hepmc lhapdf qd blackhat fastjet sqlite openmpi openloops

ALL_TOOLS      += sigcpp
sigcpp_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sigcpp/2.6.2-pafccj/include/sigc++-2.0
sigcpp_EX_LIB := sigc-2.0
sigcpp_EX_USE := root_cxxdefaults

ALL_TOOLS      += sip
sip_EX_USE := python

ALL_TOOLS      += sloccount

ALL_TOOLS      += sockets
sockets_EX_LIB := nsl crypt dl rt

ALL_TOOLS      += sqlite
sqlite_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sqlite/3.22.0-pafccj/include
sqlite_EX_LIB := sqlite3
sqlite_EX_USE := root_cxxdefaults

ALL_TOOLS      += starlight
starlight_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/starlight/r193-pafccj/include
starlight_EX_LIB := Starlib
starlight_EX_USE := root_cxxdefaults clhep

ALL_TOOLS      += tauola
tauola_EX_LIB := pretauola tauola
tauola_EX_USE := f77compiler tauola_headers

ALL_TOOLS      += tauola_headers
tauola_headers_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tauola/27.121.5-pafccj/include
tauola_headers_EX_USE := root_cxxdefaults

ALL_TOOLS      += tauolapp
tauolapp_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tauolapp/1.1.5-pafccj4/include
tauolapp_EX_LIB := TauolaCxxInterface TauolaFortran TauolaTauSpinner
tauolapp_EX_USE := root_cxxdefaults hepmc f77compiler pythia8 lhapdf

ALL_TOOLS      += tbb
tbb_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tbb/2019_U3-pafccj/include
tbb_EX_LIB := tbb
tbb_EX_USE := root_cxxdefaults
tbb_EX_FLAGS_CPPDEFINES  := -DTBB_USE_GLIBCXX_VERSION=80301

ALL_TOOLS      += tcmalloc
tcmalloc_EX_LIB := tcmalloc

ALL_TOOLS      += tcmalloc_minimal
tcmalloc_minimal_EX_LIB := tcmalloc_minimal

ALL_TOOLS      += tensorflow-c
tensorflow-c_EX_LIB := tensorflow
tensorflow-c_EX_USE := tensorflow-framework

ALL_TOOLS      += tensorflow-cc
tensorflow-cc_EX_LIB := tensorflow_cc
tensorflow-cc_EX_USE := tensorflow-framework eigen protobuf

ALL_TOOLS      += tensorflow-framework
tensorflow-framework_EX_LIB := tensorflow_framework
tensorflow-framework_EX_USE := tensorflow

ALL_TOOLS      += tensorflow-runtime
tensorflow-runtime_EX_LIB := tf_aot_runtime
tensorflow-runtime_EX_USE := tensorflow

ALL_TOOLS      += tensorflow-xla_compiled_cpu_function
tensorflow-xla_compiled_cpu_function_EX_LIB := xla_compiled_cpu_function
tensorflow-xla_compiled_cpu_function_EX_USE := tensorflow

ALL_TOOLS      += tensorflow
tensorflow_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tensorflow/1.6.0-pafccj3/include

ALL_TOOLS      += thepeg
thepeg_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/thepeg/2.1.4-pafccj4/include
thepeg_EX_LIB := ThePEG LesHouches
thepeg_EX_USE := root_cxxdefaults lhapdf gsl

ALL_TOOLS      += tinyxml2
tinyxml2_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tinyxml2/6.2.0-pafccj/include
tinyxml2_EX_LIB := tinyxml2

ALL_TOOLS      += tkonlinesw
tkonlinesw_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tkonlinesw/4.2.0-1_gcc7-pafccj4/include
tkonlinesw_EX_LIB := ICUtils Fed9UUtils
tkonlinesw_EX_USE := root_cxxdefaults xerces-c
tkonlinesw_EX_FLAGS_CXXFLAGS  := -DCMS_TK_64BITS

ALL_TOOLS      += tkonlineswdb
tkonlineswdb_EX_LIB := DeviceDescriptions Fed9UDeviceFactory
tkonlineswdb_EX_USE := tkonlinesw oracle oracleocci

ALL_TOOLS      += toprex
toprex_EX_LIB := toprex
toprex_EX_USE := toprex_headers f77compiler

ALL_TOOLS      += toprex_headers
toprex_headers_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/toprex/4.23-pafccj/include
toprex_headers_EX_USE := root_cxxdefaults

ALL_TOOLS      += utm
utm_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/utm/utm_0.7.1-pafccj/include
utm_EX_LIB := tmeventsetup tmtable tmxsd tmgrammar tmutil
utm_EX_USE := root_cxxdefaults

ALL_TOOLS      += valgrind
valgrind_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/valgrind/3.13.0-pafccj/include
valgrind_EX_USE := root_cxxdefaults

ALL_TOOLS      += vdt
vdt_EX_LIB := vdt
vdt_EX_USE := vdt_headers

ALL_TOOLS      += vdt_headers
vdt_headers_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/vdt/0.4.0-pafccj/include
vdt_headers_EX_USE := root_cxxdefaults

ALL_TOOLS      += vecgeom
vecgeom_EX_LIB := vecgeom usolids
vecgeom_EX_USE := vecgeom_interface

ALL_TOOLS      += vecgeom_interface
vecgeom_interface_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/vecgeom/v00.05.00-pafccj/include
vecgeom_interface_EX_USE := root_cxxdefaults
vecgeom_interface_EX_FLAGS_CPPDEFINES  := -DVECGEOM_SCALAR -DVECGEOM_REPLACE_USOLIDS -DVECGEOM_NO_SPECIALIZATION -DVECGEOM_USOLIDS -DVECGEOM_INPLACE_TRANSFORMATIONS -DVECGEOM_USE_INDEXEDNAVSTATES

ALL_TOOLS      += vincia
vincia_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/vincia/2.2.04-pafccj4/include
vincia_EX_LIB := vincia VinciaMG4 VinciaMG5
vincia_EX_USE := root_cxxdefaults pythia8

ALL_TOOLS      += x11
x11_EX_USE := sockets

ALL_TOOLS      += xerces-c
xerces-c_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xerces-c/3.1.3-pafccj/include
xerces-c_EX_LIB := xerces-c
xerces-c_EX_USE := root_cxxdefaults

ALL_TOOLS      += xrootd
xrootd_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xrootd/4.8.5-pafccj/include/xrootd /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xrootd/4.8.5-pafccj/include/xrootd/private
xrootd_EX_LIB := XrdUtils XrdClient
xrootd_EX_USE := root_cxxdefaults

ALL_TOOLS      += xtensor
xtensor_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xtensor/0.20.1/include
xtensor_EX_USE := xtl

ALL_TOOLS      += xtl
xtl_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xtl/0.6.3/include

ALL_TOOLS      += xz
xz_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xz/5.2.2-pafccj/include
xz_EX_LIB := lzma
xz_EX_USE := root_cxxdefaults

ALL_TOOLS      += yaml-cpp
yaml-cpp_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/yaml-cpp/0.6.2-pafccj/include
yaml-cpp_EX_LIB := yaml-cpp
yaml-cpp_EX_USE := boost

ALL_TOOLS      += yoda
yoda_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/yoda/1.7.4-pafccj4/include
yoda_EX_LIB := YODA
yoda_EX_USE := root_cxxdefaults

ALL_TOOLS      += zlib
zlib_EX_INCLUDE := /cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/zlib-x86_64/1.2.11-pafccj/include
zlib_EX_LIB := z
zlib_EX_USE := root_cxxdefaults

