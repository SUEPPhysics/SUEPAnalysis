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
from PhysicsTools.NanoAODTools.postprocessing.modules.common.lepSFProducer import *

from PhysicsTools.MonoZ.MonoZProducer import *
from PhysicsTools.MonoZ.MonoZWSProducer import *
from PhysicsTools.MonoZ.GenWeightProducer import *

import argparse

parser = argparse.ArgumentParser("")
parser.add_argument('-isMC'   , '--isMC'   , type=int, default=1     , help="")
parser.add_argument('-jobNum' , '--jobNum' , type=int, default=1     , help="")
parser.add_argument('-era'    , '--era'    , type=str, default="2017", help="")
parser.add_argument('-doSyst' , '--doSyst' , type=int, default=0     , help="")
parser.add_argument('-infile' , '--infile' , type=str, default=None  , help="")
parser.add_argument('-dataset', '--dataset', type=str, default="X"   , help="")
parser.add_argument('-nevt'   , '--nevt'   , type=str, default=-1    , help="")
parser.add_argument('-json'   , '--json'   , type=str, default=None  , help="")

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
            if "root://cms-xrd-global.cern.ch/" not in nanofile:
               nanofile = "root://cms-xrd-global.cern.ch/" + nanofile
            forceaaa=True
      else:
         nanofile = pfn
   else:
       if "root://cms-xrd-global.cern.ch/" not in nanofile:
          nanofile = "root://cms-xrd-global.cern.ch/" + nanofile
   return nanofile

options.infile = inputfile(options.infile)

print "---------------------------"
print " -- options  = ", options
print " -- is MC    = ", options.isMC
print " -- jobNum   = ", options.jobNum
print " -- era      = ", options.era
print " -- in file  = ", options.infile
print " -- dataset  = ", options.dataset
print "---------------------------"

xsection = 1.0
if options.isMC:
   from PhysicsTools.MonoZ.catalog_2017 import catalog
   condtag_ = "NANOAODSIM"
   if options.dataset == "X":
      options.dataset = options.infile
      options.dataset = options.dataset.split('/store')[1].split("/")
      condtag_ = options.dataset[5]
      options.dataset = options.dataset[3]
   for ds, m in catalog.items():
      if options.dataset in m.get("sample", "") and condtag_ in ds:
         # -----
         xsection  = 1000.0 * m.get("xsec")
         xsection *= m.get("br", 1.0)
         xsection *= m.get("kf", 1.0)
         print "---------------------------"
         print "sample     == ", m.get("sample", "")
         print "dataset    == ", ds
         print "xsection   == ", m.get("xsec"), " [pb]"
         print "nevents    == ", m.get("nevents", 1)
         print "new xsec   == ", xsection
         break
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
from PhysicsTools.MonoZ.HLT_NotIn_2017 import HLT_paths, HLT_not_in
if options.dataset in HLT_not_in:
   HLT_paths = [ HLT for HLT in HLT_paths if HLT not in HLT_not_in[options.dataset] ]

pre_selection  = "((Sum$(Electron_pt>20 & &abs(Electron_eta)<2.5) + Sum$(Muon_pt>20 && abs(Muon_eta)<2.5) )>=1)"
if options.nevt > 0:
   pre_selection += '&& (Entry$ < {})'.format(options.nevt)

modules_2017   = [
    GenWeightProducer(
       isMC = options.isMC,
       xsec = xsection,
       nevt = float(m.get("nevents", 1))
    )
]

pro_syst = []#[ "ElectronEn", "MuonEn", "MuonSF", "jesTotal", "jer", "unclustEn"]
ext_syst = []#[ "puWeight" ]

if options.isMC:
   modules_2017.append(puWeight_2017())
   modules_2017.append(jetmetUncertainties2017All())
   modules_2017.append(btagSFProducer("2017", "deepcsv"))
   modules_2017.append(muonScaleRes2017())
   modules_2017.append(lepSF())
   modules_2017.append(MonoZProducer(isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))
   modules_2017.append(MonoZWSProducer(
      isMC=options.isMC, era=str(options.era),
      do_syst=1, syst_var='', sample=m.get("sample", "")
   ))
   # for variation-based systematics
   for sys in pro_syst:
       for var in ["Up", "Down"]:
           modules_2017.append(MonoZProducer(options.isMC, str(options.era), do_syst=1, syst_var=sys+var))
           modules_2017.append(MonoZWSProducer(options.isMC, str(options.era), do_syst=1,
                                               syst_var=sys+var, sample=m.get("sample", "")))
   # for weight-based systematics
   for sys in ext_syst:
       for var in ["Up", "Down"]:
          modules_2017.append(
              MonoZWSProducer(
                 options.isMC, str(options.era),
                 do_syst=1, syst_var=sys+var,
                 weight_syst=True,
                 sample=m.get("sample", "")
              )
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


for i in modules_2017:
   print "modules : ", i

p = PostProcessor(
   ".", [options.infile],
   cut=pre_selection,
   #branchsel="keep_and_drop.txt",
   #outputbranchsel="drop_all.txt",
   haddFileName="tree_%s.root" % str(options.jobNum),
   modules=modules_2017,
   provenance=True,
   noOut=False,
   fwkJobReport=True,
   #jsonInput=options.json
)
p.run()
