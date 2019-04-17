import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetRecalib import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.JetSysColl import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.muonScaleResProducer import *

from PhysicsTools.MonoZ.MonoZProducer import *
from PhysicsTools.MonoZ.MonoZWSProducer import *
from PhysicsTools.MonoZ.GlobalWeightProducer import *
import argparse


isMC = True
era = "2017"
dataRun = ""

parser = argparse.ArgumentParser("")
parser.add_argument('-isMC'   , '--isMC'   , type=int, default=1     , help="")
parser.add_argument('-jobNum' , '--jobNum' , type=int, default=1     , help="")
parser.add_argument('-era'    , '--era'    , type=str, default="2017", help="")
parser.add_argument('-doSyst' , '--doSyst' , type=int, default=0     , help="")
parser.add_argument('-dataset', '--dataset', type=str, default="X"   , help="")
parser.add_argument('-catalog', '--catalog', type=str, default="../data/catalogue_2017.yaml", help="")

options  = parser.parse_args()
print "---------------------------"
print " -- options  = ", options 
print " -- is MC    = ", options.isMC
print " -- jobNum   = ", options.jobNum
print " -- era      = ", options.era
print " -- dataset  = ", options.dataset
print " -- catalog  = ", options.catalog
print "---------------------------"

files = [
"root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/ZZTo2L2Nu_13TeV_powheg_pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/D6F99CDC-D6A4-E811-A6E9-0CC47A166D66.root"
#"root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/2E8841C2-4B42-E811-84CD-008CFAE4503C.root"
]

weightRaw  = 1.0
lumiWeight = 1.0
if isMC:
    from PhysicsTools.NanoAODTools.postprocessing.monoZ.catalog_2017 import catalog
    condtag_ = "NANOAODSIM"
    if options.dataset == "X":
        options.dataset = files[0] #inputFiles().value()[0]
        options.dataset = options.dataset.split('store/mc/RunIIFall17NanoAOD/')[1]
        condtag_ = options.dataset.split('/')[2]
        options.dataset = options.dataset.split('/NANOAODSIM/')[0]

    for ds, m in catalog.items():
        if options.dataset == m.get("sample", "") and condtag_ in ds:
            weightRaw = 1000.0 * m.get("xsec")
            weightRaw *= m.get("br", 1.0)
            weightRaw *= m.get("kf", 1.0)
            lumiWeight = weightRaw / float(m.get("nevents", 1))
            print "---------------------------"
            print "sample     == ", m.get("sample", "")
            print "dataset    == ", ds
            print "xsection   == ", m.get("xsec"), " [pb]"
            print "nevents    == ", m.get("nevents", 1)
            print "lumiWeight == ", lumiWeight
            break
    else:
        lumiWeight = 1.0
        print "---------------------------"
        print "lumiWeight  == ", lumiWeight
        print "sample name == ", sample_name.split("_")[0]
    
print "---------------------------"
from PhysicsTools.MonoZ.HLT_NotIn_2017 import HLT_paths, HLT_not_in
if options.dataset in HLT_not_in:
   HLT_paths = [ HLT for HLT in HLT_paths if HLT not in HLT_not_in[options.dataset] ]

pre_selection = "( ( Sum$(Electron_pt>20&&abs(Electron_eta)<2.5) + Sum$(Muon_pt>20&&abs(Muon_eta)<2.5) )>=1 )"
pre_selection = pre_selection + " && (" + "||".join(HLT_paths) + ")"
pre_selection = " && ".join([pre_selection, "(Entry$ < 5000)"])
print("pre_selection : ", pre_selection)

modules_2017 = [
    GlobalWeightProducer(options.isMC, lumiWeight, weightRaw),
]

pro_syst = [ "ElectronEn", "MuonEn", "MuonSF", "jesTotal", "jer", "unclustEn"]
ext_syst = [ "puWeight" ]

if options.isMC:
   modules_2017.append(puAutoWeight())
   modules_2017.append(jetmetUncertainties2017All())
   modules_2017.append(btagSFProducer("2017", "deepcsv"))
   modules_2017.append(muonScaleRes2017())
   # Nominal 
   modules_2017.append(MonoZProducer  (isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))
   modules_2017.append(MonoZWSProducer(isMC=options.isMC, era=str(options.era), 
                                       do_syst=1, syst_var='', sample=""))
   # for variation-based systematics
   for sys in pro_syst:
       for var in ["Up", "Down"]:
           modules_2017.append(MonoZProducer  (options.isMC, str(options.era), do_syst=1, syst_var=sys+var))
           modules_2017.append(MonoZWSProducer(options.isMC, str(options.era), do_syst=1, 
                                               syst_var=sys+var, sample=""))
   # for weight-based systematics
   for sys in ext_syst:
       for var in ["Up", "Down"]:
           modules_2017.append(
               MonoZWSProducer(options.isMC, str(options.era), do_syst=1, syst_var=sys+var, weight_syst=True, sample="")
           )
print "---------------------------"

print modules_2017
p = PostProcessor(
    ".", files, cut=pre_selection,
    branchsel="../data/keep_and_drop.txt",
    outputbranchsel="../data/drop_all.txt",
    modules=modules_2017,
    provenance=True,
    noOut=False,
    histFileName="histfilename.root",
    histDirName=m.get("sample", ""),
    fwkJobReport=False,
)

p.run()
