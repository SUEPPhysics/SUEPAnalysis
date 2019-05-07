#include "../interface/CombineHLTCppWorker.h"
#include <iostream>
#include <cmath>

using namespace std;

CombineHLTCppWorker::CombineHLTCppWorker(const std::string formulaExpr, const std::string outName):
  nHLT_(0), outName_(outName), formula_(("CombineHLT_"+outName).c_str(), formulaExpr.c_str())
{
}

void CombineHLTCppWorker::reset() {
  nHLT_ = 0;
  in_HLTFlags.clear();
  in_HLTFlagsUC.clear();
  in_HLTFlagsUI.clear();
}

void CombineHLTCppWorker::addHLT(CombineHLTCppWorker::TRB HLTFlag) {
  in_HLTFlags[nHLT_++] = HLTFlag;
}

void CombineHLTCppWorker::addHLT(CombineHLTCppWorker::TRUC HLTFlag) {
  in_HLTFlagsUC[nHLT_++] = HLTFlag;
}

void CombineHLTCppWorker::addHLT(CombineHLTCppWorker::TRUI HLTFlag) {
  in_HLTFlagsUI[nHLT_++] = HLTFlag;
}

bool CombineHLTCppWorker::analyze() {
  for ( auto key=in_HLTFlags.begin(); key!=in_HLTFlags.end(); ++key ) {
    const int i = key->first;
    auto& flag = key->second;
    formula_.SetParameter(i, static_cast<double>(**flag));
  }
  for ( auto key=in_HLTFlagsUC.begin(); key!=in_HLTFlagsUC.end(); ++key ) {
    const int i = key->first;
    auto& flag = key->second;
    formula_.SetParameter(i, static_cast<double>(**flag));
  }
  for ( auto key=in_HLTFlagsUI.begin(); key!=in_HLTFlagsUI.end(); ++key ) {
    const int i = key->first;
    auto& flag = key->second;
    formula_.SetParameter(i, static_cast<double>(**flag));
  }

  return formula_.Eval(0);
}

