// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME tmpdIslc7_amd64_gcc820dIsrcdIPhysicsToolsdINanoAODToolsdIsrcdIPhysicsToolsNanoAODToolsdIadIPhysicsToolsNanoAODTools_xr

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Since CINT ignores the std namespace, we need to do so in this file.
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "src/PhysicsTools/NanoAODTools/src/classes.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static TClass *PyJetResolutionWrapper_Dictionary();
   static void PyJetResolutionWrapper_TClassManip(TClass*);
   static void *new_PyJetResolutionWrapper(void *p = 0);
   static void *newArray_PyJetResolutionWrapper(Long_t size, void *p);
   static void delete_PyJetResolutionWrapper(void *p);
   static void deleteArray_PyJetResolutionWrapper(void *p);
   static void destruct_PyJetResolutionWrapper(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::PyJetResolutionWrapper*)
   {
      ::PyJetResolutionWrapper *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::PyJetResolutionWrapper));
      static ::ROOT::TGenericClassInfo 
         instance("PyJetResolutionWrapper", "PhysicsTools/NanoAODTools/interface/PyJetResolutionWrapper.h", 10,
                  typeid(::PyJetResolutionWrapper), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &PyJetResolutionWrapper_Dictionary, isa_proxy, 4,
                  sizeof(::PyJetResolutionWrapper) );
      instance.SetNew(&new_PyJetResolutionWrapper);
      instance.SetNewArray(&newArray_PyJetResolutionWrapper);
      instance.SetDelete(&delete_PyJetResolutionWrapper);
      instance.SetDeleteArray(&deleteArray_PyJetResolutionWrapper);
      instance.SetDestructor(&destruct_PyJetResolutionWrapper);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::PyJetResolutionWrapper*)
   {
      return GenerateInitInstanceLocal((::PyJetResolutionWrapper*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::PyJetResolutionWrapper*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *PyJetResolutionWrapper_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::PyJetResolutionWrapper*)0x0)->GetClass();
      PyJetResolutionWrapper_TClassManip(theClass);
   return theClass;
   }

   static void PyJetResolutionWrapper_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *PyJetResolutionScaleFactorWrapper_Dictionary();
   static void PyJetResolutionScaleFactorWrapper_TClassManip(TClass*);
   static void *new_PyJetResolutionScaleFactorWrapper(void *p = 0);
   static void *newArray_PyJetResolutionScaleFactorWrapper(Long_t size, void *p);
   static void delete_PyJetResolutionScaleFactorWrapper(void *p);
   static void deleteArray_PyJetResolutionScaleFactorWrapper(void *p);
   static void destruct_PyJetResolutionScaleFactorWrapper(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::PyJetResolutionScaleFactorWrapper*)
   {
      ::PyJetResolutionScaleFactorWrapper *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::PyJetResolutionScaleFactorWrapper));
      static ::ROOT::TGenericClassInfo 
         instance("PyJetResolutionScaleFactorWrapper", "PhysicsTools/NanoAODTools/interface/PyJetResolutionScaleFactorWrapper.h", 10,
                  typeid(::PyJetResolutionScaleFactorWrapper), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &PyJetResolutionScaleFactorWrapper_Dictionary, isa_proxy, 4,
                  sizeof(::PyJetResolutionScaleFactorWrapper) );
      instance.SetNew(&new_PyJetResolutionScaleFactorWrapper);
      instance.SetNewArray(&newArray_PyJetResolutionScaleFactorWrapper);
      instance.SetDelete(&delete_PyJetResolutionScaleFactorWrapper);
      instance.SetDeleteArray(&deleteArray_PyJetResolutionScaleFactorWrapper);
      instance.SetDestructor(&destruct_PyJetResolutionScaleFactorWrapper);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::PyJetResolutionScaleFactorWrapper*)
   {
      return GenerateInitInstanceLocal((::PyJetResolutionScaleFactorWrapper*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::PyJetResolutionScaleFactorWrapper*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *PyJetResolutionScaleFactorWrapper_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::PyJetResolutionScaleFactorWrapper*)0x0)->GetClass();
      PyJetResolutionScaleFactorWrapper_TClassManip(theClass);
   return theClass;
   }

   static void PyJetResolutionScaleFactorWrapper_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *PyJetParametersWrapper_Dictionary();
   static void PyJetParametersWrapper_TClassManip(TClass*);
   static void *new_PyJetParametersWrapper(void *p = 0);
   static void *newArray_PyJetParametersWrapper(Long_t size, void *p);
   static void delete_PyJetParametersWrapper(void *p);
   static void deleteArray_PyJetParametersWrapper(void *p);
   static void destruct_PyJetParametersWrapper(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::PyJetParametersWrapper*)
   {
      ::PyJetParametersWrapper *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::PyJetParametersWrapper));
      static ::ROOT::TGenericClassInfo 
         instance("PyJetParametersWrapper", "PhysicsTools/NanoAODTools/interface/PyJetParametersWrapper.h", 8,
                  typeid(::PyJetParametersWrapper), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &PyJetParametersWrapper_Dictionary, isa_proxy, 4,
                  sizeof(::PyJetParametersWrapper) );
      instance.SetNew(&new_PyJetParametersWrapper);
      instance.SetNewArray(&newArray_PyJetParametersWrapper);
      instance.SetDelete(&delete_PyJetParametersWrapper);
      instance.SetDeleteArray(&deleteArray_PyJetParametersWrapper);
      instance.SetDestructor(&destruct_PyJetParametersWrapper);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::PyJetParametersWrapper*)
   {
      return GenerateInitInstanceLocal((::PyJetParametersWrapper*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::PyJetParametersWrapper*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *PyJetParametersWrapper_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::PyJetParametersWrapper*)0x0)->GetClass();
      PyJetParametersWrapper_TClassManip(theClass);
   return theClass;
   }

   static void PyJetParametersWrapper_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *WeightCalculatorFromHistogram_Dictionary();
   static void WeightCalculatorFromHistogram_TClassManip(TClass*);
   static void *new_WeightCalculatorFromHistogram(void *p = 0);
   static void *newArray_WeightCalculatorFromHistogram(Long_t size, void *p);
   static void delete_WeightCalculatorFromHistogram(void *p);
   static void deleteArray_WeightCalculatorFromHistogram(void *p);
   static void destruct_WeightCalculatorFromHistogram(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::WeightCalculatorFromHistogram*)
   {
      ::WeightCalculatorFromHistogram *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::WeightCalculatorFromHistogram));
      static ::ROOT::TGenericClassInfo 
         instance("WeightCalculatorFromHistogram", "PhysicsTools/NanoAODTools/interface/WeightCalculatorFromHistogram.h", 10,
                  typeid(::WeightCalculatorFromHistogram), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &WeightCalculatorFromHistogram_Dictionary, isa_proxy, 4,
                  sizeof(::WeightCalculatorFromHistogram) );
      instance.SetNew(&new_WeightCalculatorFromHistogram);
      instance.SetNewArray(&newArray_WeightCalculatorFromHistogram);
      instance.SetDelete(&delete_WeightCalculatorFromHistogram);
      instance.SetDeleteArray(&deleteArray_WeightCalculatorFromHistogram);
      instance.SetDestructor(&destruct_WeightCalculatorFromHistogram);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::WeightCalculatorFromHistogram*)
   {
      return GenerateInitInstanceLocal((::WeightCalculatorFromHistogram*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::WeightCalculatorFromHistogram*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *WeightCalculatorFromHistogram_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::WeightCalculatorFromHistogram*)0x0)->GetClass();
      WeightCalculatorFromHistogram_TClassManip(theClass);
   return theClass;
   }

   static void WeightCalculatorFromHistogram_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ReduceMantissaToNbitsRounding_Dictionary();
   static void ReduceMantissaToNbitsRounding_TClassManip(TClass*);
   static void delete_ReduceMantissaToNbitsRounding(void *p);
   static void deleteArray_ReduceMantissaToNbitsRounding(void *p);
   static void destruct_ReduceMantissaToNbitsRounding(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ReduceMantissaToNbitsRounding*)
   {
      ::ReduceMantissaToNbitsRounding *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ReduceMantissaToNbitsRounding));
      static ::ROOT::TGenericClassInfo 
         instance("ReduceMantissaToNbitsRounding", "PhysicsTools/NanoAODTools/interface/ReduceMantissa.h", 4,
                  typeid(::ReduceMantissaToNbitsRounding), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ReduceMantissaToNbitsRounding_Dictionary, isa_proxy, 4,
                  sizeof(::ReduceMantissaToNbitsRounding) );
      instance.SetDelete(&delete_ReduceMantissaToNbitsRounding);
      instance.SetDeleteArray(&deleteArray_ReduceMantissaToNbitsRounding);
      instance.SetDestructor(&destruct_ReduceMantissaToNbitsRounding);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ReduceMantissaToNbitsRounding*)
   {
      return GenerateInitInstanceLocal((::ReduceMantissaToNbitsRounding*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::ReduceMantissaToNbitsRounding*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ReduceMantissaToNbitsRounding_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ReduceMantissaToNbitsRounding*)0x0)->GetClass();
      ReduceMantissaToNbitsRounding_TClassManip(theClass);
   return theClass;
   }

   static void ReduceMantissaToNbitsRounding_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_PyJetResolutionWrapper(void *p) {
      return  p ? new(p) ::PyJetResolutionWrapper : new ::PyJetResolutionWrapper;
   }
   static void *newArray_PyJetResolutionWrapper(Long_t nElements, void *p) {
      return p ? new(p) ::PyJetResolutionWrapper[nElements] : new ::PyJetResolutionWrapper[nElements];
   }
   // Wrapper around operator delete
   static void delete_PyJetResolutionWrapper(void *p) {
      delete ((::PyJetResolutionWrapper*)p);
   }
   static void deleteArray_PyJetResolutionWrapper(void *p) {
      delete [] ((::PyJetResolutionWrapper*)p);
   }
   static void destruct_PyJetResolutionWrapper(void *p) {
      typedef ::PyJetResolutionWrapper current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::PyJetResolutionWrapper

namespace ROOT {
   // Wrappers around operator new
   static void *new_PyJetResolutionScaleFactorWrapper(void *p) {
      return  p ? new(p) ::PyJetResolutionScaleFactorWrapper : new ::PyJetResolutionScaleFactorWrapper;
   }
   static void *newArray_PyJetResolutionScaleFactorWrapper(Long_t nElements, void *p) {
      return p ? new(p) ::PyJetResolutionScaleFactorWrapper[nElements] : new ::PyJetResolutionScaleFactorWrapper[nElements];
   }
   // Wrapper around operator delete
   static void delete_PyJetResolutionScaleFactorWrapper(void *p) {
      delete ((::PyJetResolutionScaleFactorWrapper*)p);
   }
   static void deleteArray_PyJetResolutionScaleFactorWrapper(void *p) {
      delete [] ((::PyJetResolutionScaleFactorWrapper*)p);
   }
   static void destruct_PyJetResolutionScaleFactorWrapper(void *p) {
      typedef ::PyJetResolutionScaleFactorWrapper current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::PyJetResolutionScaleFactorWrapper

namespace ROOT {
   // Wrappers around operator new
   static void *new_PyJetParametersWrapper(void *p) {
      return  p ? new(p) ::PyJetParametersWrapper : new ::PyJetParametersWrapper;
   }
   static void *newArray_PyJetParametersWrapper(Long_t nElements, void *p) {
      return p ? new(p) ::PyJetParametersWrapper[nElements] : new ::PyJetParametersWrapper[nElements];
   }
   // Wrapper around operator delete
   static void delete_PyJetParametersWrapper(void *p) {
      delete ((::PyJetParametersWrapper*)p);
   }
   static void deleteArray_PyJetParametersWrapper(void *p) {
      delete [] ((::PyJetParametersWrapper*)p);
   }
   static void destruct_PyJetParametersWrapper(void *p) {
      typedef ::PyJetParametersWrapper current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::PyJetParametersWrapper

namespace ROOT {
   // Wrappers around operator new
   static void *new_WeightCalculatorFromHistogram(void *p) {
      return  p ? new(p) ::WeightCalculatorFromHistogram : new ::WeightCalculatorFromHistogram;
   }
   static void *newArray_WeightCalculatorFromHistogram(Long_t nElements, void *p) {
      return p ? new(p) ::WeightCalculatorFromHistogram[nElements] : new ::WeightCalculatorFromHistogram[nElements];
   }
   // Wrapper around operator delete
   static void delete_WeightCalculatorFromHistogram(void *p) {
      delete ((::WeightCalculatorFromHistogram*)p);
   }
   static void deleteArray_WeightCalculatorFromHistogram(void *p) {
      delete [] ((::WeightCalculatorFromHistogram*)p);
   }
   static void destruct_WeightCalculatorFromHistogram(void *p) {
      typedef ::WeightCalculatorFromHistogram current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::WeightCalculatorFromHistogram

namespace ROOT {
   // Wrapper around operator delete
   static void delete_ReduceMantissaToNbitsRounding(void *p) {
      delete ((::ReduceMantissaToNbitsRounding*)p);
   }
   static void deleteArray_ReduceMantissaToNbitsRounding(void *p) {
      delete [] ((::ReduceMantissaToNbitsRounding*)p);
   }
   static void destruct_ReduceMantissaToNbitsRounding(void *p) {
      typedef ::ReduceMantissaToNbitsRounding current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ReduceMantissaToNbitsRounding

namespace {
  void TriggerDictionaryInitialization_PhysicsToolsNanoAODTools_xr_Impl() {
    static const char* headers[] = {
0    };
    static const char* includePaths[] = {
"/home/freerc/Nano_SUEP/CMSSW_10_6_4/src",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_4/src",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/coral/CORAL_2_3_21-pafccj5/include/LCG",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/pcre/8.37-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/boost/1.67.0-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/bz2lib/1.0.6-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/clhep/2.4.0.0-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/gsl/2.2.1-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/hepmc/2.06.07-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/libuuid/2.22.2-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/openssl/1.0.2d-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/sigcpp/2.6.2-pafccj/include/sigc++-2.0",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tbb/2019_U3-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/vdt/0.4.0-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xerces-c/3.1.3-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/xz/5.2.2-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/zlib-x86_64/1.2.11-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/md5/1.0.0-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/tinyxml2/6.2.0-pafccj/include",
"/cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.14.09/include",
"/home/freerc/Nano_SUEP/CMSSW_10_6_4/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "PhysicsToolsNanoAODTools_xr dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
class __attribute__((annotate("$clingAutoload$PhysicsTools/NanoAODTools/interface/PyJetResolutionWrapper.h")))  PyJetResolutionWrapper;
class __attribute__((annotate("$clingAutoload$PhysicsTools/NanoAODTools/interface/PyJetResolutionScaleFactorWrapper.h")))  PyJetResolutionScaleFactorWrapper;
class __attribute__((annotate("$clingAutoload$PhysicsTools/NanoAODTools/interface/PyJetParametersWrapper.h")))  PyJetParametersWrapper;
class __attribute__((annotate("$clingAutoload$PhysicsTools/NanoAODTools/interface/WeightCalculatorFromHistogram.h")))  WeightCalculatorFromHistogram;
class __attribute__((annotate("$clingAutoload$PhysicsTools/NanoAODTools/interface/ReduceMantissa.h")))  ReduceMantissaToNbitsRounding;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "PhysicsToolsNanoAODTools_xr dictionary payload"

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif
#ifndef CMS_DICT_IMPL
  #define CMS_DICT_IMPL 1
#endif
#ifndef _REENTRANT
  #define _REENTRANT 1
#endif
#ifndef GNUSOURCE
  #define GNUSOURCE 1
#endif
#ifndef __STRICT_ANSI__
  #define __STRICT_ANSI__ 1
#endif
#ifndef GNU_GCC
  #define GNU_GCC 1
#endif
#ifndef _GNU_SOURCE
  #define _GNU_SOURCE 1
#endif
#ifndef TBB_USE_GLIBCXX_VERSION
  #define TBB_USE_GLIBCXX_VERSION 80301
#endif
#ifndef BOOST_SPIRIT_THREADSAFE
  #define BOOST_SPIRIT_THREADSAFE 1
#endif
#ifndef PHOENIX_THREADSAFE
  #define PHOENIX_THREADSAFE 1
#endif
#ifndef CMSSW_GIT_HASH
  #define CMSSW_GIT_HASH "CMSSW_10_6_4"
#endif
#ifndef PROJECT_NAME
  #define PROJECT_NAME "CMSSW"
#endif
#ifndef PROJECT_VERSION
  #define PROJECT_VERSION "CMSSW_10_6_4"
#endif
#ifndef CMSSW_REFLEX_DICT
  #define CMSSW_REFLEX_DICT 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "PhysicsTools/NanoAODTools/interface/PyJetResolutionWrapper.h"
#include "PhysicsTools/NanoAODTools/interface/PyJetResolutionScaleFactorWrapper.h"
#include "PhysicsTools/NanoAODTools/interface/PyJetParametersWrapper.h"
#include "PhysicsTools/NanoAODTools/interface/WeightCalculatorFromHistogram.h"
#include "PhysicsTools/NanoAODTools/interface/ReduceMantissa.h"

PyJetResolutionWrapper jetRes;
PyJetResolutionScaleFactorWrapper jetResScaleFactor;
PyJetParametersWrapper jetParams;
WeightCalculatorFromHistogram wcalc;
ReduceMantissaToNbitsRounding red(12);

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"PyJetParametersWrapper", payloadCode, "@",
"PyJetResolutionScaleFactorWrapper", payloadCode, "@",
"PyJetResolutionWrapper", payloadCode, "@",
"ReduceMantissaToNbitsRounding", payloadCode, "@",
"WeightCalculatorFromHistogram", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("PhysicsToolsNanoAODTools_xr",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_PhysicsToolsNanoAODTools_xr_Impl, {}, classesHeaders, /*has no C++ module*/false);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_PhysicsToolsNanoAODTools_xr_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_PhysicsToolsNanoAODTools_xr() {
  TriggerDictionaryInitialization_PhysicsToolsNanoAODTools_xr_Impl();
}
