import os, sys, re
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
# import PSet
import yaml
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme import jetRecalib
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.JetSysColl import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.muonScaleResProducer import *
#from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles, runsAndLumis


from PhysicsTools.MonoZ.MonoZProducer import *
from PhysicsTools.MonoZ.MonoZWSProducer import *
from PhysicsTools.MonoZ.GlobalWeightProducer import *
#from PhysicsTools.MonoZ.CombineHLT import *

import argparse

parser = argparse.ArgumentParser("")
parser.add_argument('-isMC'   , '--isMC'   , type=int, default=1     , help="")
parser.add_argument('-jobNum' , '--jobNum' , type=int, default=1     , help="")
parser.add_argument('-era'    , '--era'    , type=str, default="2017", help="")
parser.add_argument('-doSyst' , '--doSyst' , type=int, default=0     , help="")
parser.add_argument('-infile' , '--infile' , type=str, default=None  , help="")
parser.add_argument('-dataset', '--dataset', type=str, default="X"   , help="")
parser.add_argument('-catalog', '--catalog', type=str, default="configs/catalogue_2017.yaml", help="")

options  = parser.parse_args()

def inputfile(nanofile):
   tested   = False
   forceaaa = False
   pfn=os.popen("edmFileUtil -d %s"%(nanofile)).read()
   pfn=re.sub("\n","",pfn)
   print nanofile," -> ",pfn
   if (os.getenv("GLIDECLIENT_Group","") != "overflow" and  
       os.getenv("GLIDECLIENT_Group","") != "overflow_conservative" and not 
       forceaaa ):
      if not tested:
         print "Testing file open"
         testfile=ROOT.TFile.Open(pfn)
         if testfile and testfile.IsOpen() :
            print "Test OK"
            nanofile=pfn
            testfile.Close()
         else:
            nanofile = "root://cms-xrd-global.cern.ch/" + nanofile if "root://cms-xrd-global.cern.ch/" not in nanofile else nanofile
            forceaaa=True
      else:
         nanofile = pfn
   else:
      nanofile = "root://cms-xrd-global.cern.ch/" + nanofile if "root://cms-xrd-global.cern.ch/" not in nanofile else nanofile
   return nanofile

options.infile = inputfile(options.infile)

print "---------------------------"
print " -- options  = ", options
print " -- is MC    = ", options.isMC
print " -- jobNum   = ", options.jobNum
print " -- era      = ", options.era
print " -- in file  = ", options.infile
print " -- dataset  = ", options.dataset
print " -- catalog  = ", options.catalog
print "---------------------------"


weightRaw  = 1.0
lumiWeight  = 1.0
if options.isMC:
   from PhysicsTools.NanoAODTools.postprocessing.monoZ.catalog_2017 import catalog
   condtag_ = "NANOAODSIM"
   if options.dataset == "X":
      options.dataset = options.infile
      options.dataset = options.dataset.split('/store')[1].split("/")
      condtag_ = options.dataset[5]
      options.dataset = options.dataset[3]
   for ds, m in catalog.items():
      if options.dataset in m.get("sample", "") and condtag_ in ds:
         # -----
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
      print "lumiWeight == ", lumiWeight
else:
   if options.dataset == "X":
      options.dataset = options.infile
      options.dataset = options.dataset.split('/store')[1].split("/")
      condtag_ = options.dataset[2]
      options.dataset = options.dataset[3]
   else:
      options.dataset = options.dataset.split("/")
      condtag_ = options.dataset[2]
      options.dataset = options.dataset[1]

# This has only been tested on 2017 samples
from PhysicsTools.NanoAODTools.postprocessing.monoZ.HLT_NotIn_2017 import HLT_paths, HLT_not_in
if options.dataset in HLT_not_in:
   HLT_paths = [ HLT for HLT in HLT_paths if HLT not in HLT_not_in[options.dataset] ]

pre_selection  = "((Sum$(Electron_pt>20 & &abs(Electron_eta)<2.5) + Sum$(Muon_pt>20 && abs(Muon_eta)<2.5) )>=1)"
#pre_selection += '&& (Entry$ < 100)'
modules_2017   = [
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
                                       do_syst=1, syst_var='', sample=m.get("sample", "")))
   # for variation-based systematics
   for sys in pro_syst:
       for var in ["Up", "Down"]:
           modules_2017.append(MonoZProducer  (options.isMC, str(options.era), do_syst=1, syst_var=sys+var))
           modules_2017.append(MonoZWSProducer(options.isMC, str(options.era), do_syst=1,
                                               syst_var=sys+var, sample=m.get("sample", "")))
   # for weight-based systematics
   for sys in ext_syst:
       for var in ["Up", "Down"]:
           modules_2017.append(
               MonoZWSProducer(options.isMC, str(options.era), do_syst=1, syst_var=sys+var, weight_syst=True)
           )

else:
   print "sample : ", options.dataset, " candtag : ", condtag_
   try:
      combineHLT = yaml.load(open("combineHLT_2017.yaml"))
   except yaml.YAMLError as exc:
      print(exc)
   if 'Run2017B' in condtag_:
      pre_selection = pre_selection + " && (" + combineHLT.get("Run2017B.%s" % options.dataset, 1) + ")"
   else:
      pre_selection = pre_selection + " && (" + combineHLT.get("Run2017CF.%s" % options.dataset, 1) + ")"
   # ---
   print " -- era : ",
   modules_2017.append(getattr(jetRecalib, 'jetRecalib2017%s' % condtag_.split(options.era)[1])() )
   modules_2017.append(MonoZProducer  (isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))
   modules_2017.append(MonoZWSProducer(isMC=options.isMC, era=str(options.era),
                                       do_syst=1, syst_var='', sample="data"))
p = PostProcessor(
   ".", [options.infile],
   cut=pre_selection,
   branchsel="keep_and_drop.txt",
   outputbranchsel="drop_all.txt",
   haddFileName="tree_%s.root" % str(options.jobNum),
   modules=modules_2017,
   provenance=True,
   noOut=False,
   fwkJobReport=True,
   #jsonInput=runsAndLumis()
)

p.run()
