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
parser.add_argument('-dataRun', '--dataRun', type=str, default="X"   , help="")
parser.add_argument('-c'      , '--catalog', type=str, default="../data/catalogue_2017.yaml", help="")
options  = parser.parse_args()
print(" -- options = ", options)
isMC = options.isMC
era = options.era
dataRun = options.dataRun

print("isMC = ", isMC, "era = ", era, "dataRun = ", dataRun)

files = [
    "root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/ZZTo4L_13TeV_powheg_pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/04664F82-5F43-E811-808C-0025905A48C0.root"
]

pre_selection = " || ".join([
    "Sum$(Electron_pt>20&&abs(Electron_eta)<2.5) + Sum$(Muon_pt>20&&abs(Muon_eta)<2.5)>=1"
])

pre_selection = " && ".join([pre_selection, "(Entry$ < 2000)"])
print("pre_selection : ", pre_selection)

lumiWeight  = 1.0
if isMC:
    sample_name = files[0].split('store/mc/RunIIFall17NanoAOD/')[1].split('/NANOAODSIM/')[0]
    import yaml
    with open(options.catalog, 'r') as stream:
        try:
            catalog = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    for ds, m in catalog.items():
        if sample_name == m.get("sample", ""):
            print m.get("sample", "")
            lumiWeight = 1000.0 * m.get("xsec") * m.get("br", 1.0) * m.get("kf",1.0) / float(m.get("nevents", 1))
            print "---------------------------"
            print "xsection   == ", m.get("xsec"), " [pb]"
            print "nevents    == ", m.get("nevents", 1)
            print "lumiWeight == ", lumiWeight
            break
    
else:
    lumiWeight = 1.0
    print "---------------------------"
    print "lumiWeight == ", lumiWeight


print "---------------------------"

modules_2017 = [
    GlobalWeightProducer(options.isMC, lumiWeight),
]

pro_syst = [ "ElectronEn", "MuonEn", "MuonSF", "jes", "jer", "unclustEn"]
ext_syst = [ "puWeight" ]

if options.isMC:
   modules_2017.append(puAutoWeight())
   modules_2017.append(jetmetUncertainties2017All())
   modules_2017.append(btagSFProducer("2017", "deepcsv"))
   modules_2017.append(muonScaleRes2017())
   # Nominal 
   modules_2017.append(MonoZProducer  (isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))
   modules_2017.append(MonoZWSProducer(isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))
   # for variation-based systematics
   for sys in pro_syst:
       for var in ["Up", "Down"]:
           modules_2017.append(MonoZProducer  (options.isMC, str(options.era), do_syst=1, syst_var=sys+var))
           modules_2017.append(MonoZWSProducer(options.isMC, str(options.era), do_syst=1, syst_var=sys+var))
   # for weight-based systematics
   for sys in ext_syst:
       for var in ["Up", "Down"]:
           modules_2017.append(
               MonoZWSProducer(options.isMC, str(options.era), do_syst=1, syst_var=sys+var)
           )
   	


print "---------------------------"

print modules_2017
p = PostProcessor(
    ".", files, cut=pre_selection,
    branchsel="../data/keep_and_drop.txt",
    outputbranchsel="../data/drop_all.txt",# if options.doSyst else "../data/keep_and_drop.txt",
    modules=modules_2017,
    provenance=True,
    noOut=False,
    fwkJobReport=False,
    # jsonInput=runsAndLumis()
)

p.run()
