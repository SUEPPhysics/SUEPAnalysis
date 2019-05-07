#ifndef PhysicsTools_ChickenChicken_CombineHLTCppWorker_H
#define PhysicsTools_ChickenChicken_CombineHLTCppWorker_H

#include <memory>
#include <string>
#include <vector>
#include <array>
#include <TTree.h>
#include <TTreeReaderValue.h>
#include <TTreeReaderArray.h>
#include <TLorentzVector.h>
#include <TFormula.h>

class CombineHLTCppWorker {
public:
  typedef TTreeReaderValue<bool>* TRB;
  typedef TTreeReaderValue<unsigned char>* TRUC;
  typedef TTreeReaderValue<unsigned int>* TRUI;

  CombineHLTCppWorker(const std::string formulaExpr, const std::string outName="HLT");
  ~CombineHLTCppWorker() = default;

  void reset();
  void addHLT(TRB flag);
  void addHLT(TRUC flag);
  void addHLT(TRUI flag);
  bool analyze();

private:
  std::map<int, TRB> in_HLTFlags;
  std::map<int, TRUC> in_HLTFlagsUC;
  std::map<int, TRUI> in_HLTFlagsUI;

  int nHLT_;
  const std::string outName_;
  TFormula formula_;

};

#endif
