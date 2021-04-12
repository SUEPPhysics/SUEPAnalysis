ALL_TOOLS      += gcc-analyzer-cxxcompiler
gcc-analyzer-cxxcompiler_EX_FLAGS_CXXFLAGS  := -fplugin=/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gcc-checker-plugin/1.2-pafccj/lib/libchecker_gccplugins.so -fplugin-arg-libchecker_gccplugins-checkers=all -fsyntax-only

