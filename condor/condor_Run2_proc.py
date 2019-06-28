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
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *

from PhysicsTools.MonoZ.MonoZProducer import *
from PhysicsTools.MonoZ.MonoZWSProducer import *
from PhysicsTools.MonoZ.GenWeightProducer import *
from PhysicsTools.MonoZ.EWProducer import *
from PhysicsTools.MonoZ.NvtxPUreweight import *

import argparse

parser = argparse.ArgumentParser("")
parser.add_argument('-isMC'   , '--isMC'   , type=int, default=1     , help="")
parser.add_argument('-jobNum' , '--jobNum' , type=int, default=1     , help="")
parser.add_argument('-era'    , '--era'    , type=str, default="2018", help="")
parser.add_argument('-doSyst' , '--doSyst' , type=int, default=1     , help="")
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
nevents = 1
if options.isMC:
   if options.era=="2016":
      from PhysicsTools.MonoZ.catalog_2016 import catalog
   if options.era=="2017":
      from PhysicsTools.MonoZ.catalog_2017 import catalog
   else:#for 2018
      from PhysicsTools.MonoZ.catalog_2018 import catalog
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
         nevents = m.get("nevents", 1)
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
pre_selection += "&& Flag_METFilters"

if float(options.nevt) > 0:
   print " passing this cut and : ", options.nevt
   pre_selection += ' && (Entry$ < {})'.format(options.nevt)

modules_era   = [
    GenWeightProducer(
       isMC = options.isMC,
       xsec = xsection,
       nevt = nevents,
       dopdf = False if ("ADDMonoZ" in options.dataset or
                         "Unpart"          in options.dataset or
                         "DMSimp"          in options.dataset ) else True
    )
]
print "start simple"
pro_syst = [ "ElectronEn", "MuonEn", "MuonSF", "jesTotal", "jer", "unclustEn"]
ext_syst = [ "puWeight", "PDF", "MuonSFEff", "ElecronSFEff", "EWK","PrefireWeight","nvtxWeight"]

if options.isMC:
   if options.era=="2016":
        modules_era.append(puAutoWeight_2016())
        modules_era.append(PrefCorr())
        modules_era.append(jetmetUncertainties2016All())
        modules_era.append(btagSFProducer("Legacy2016", "deepcsv"))
        modules_era.append(muonScaleRes2016())
        modules_era.append(lepSF_2016())
	modules_era.append(nvtxWeight_2016())
   if options.era=="2017":
   	modules_era.append(puAutoWeight_2017())
        modules_era.append(PrefCorr())
   	modules_era.append(jetmetUncertainties2017All())
   	modules_era.append(btagSFProducer("2017", "deepcsv"))
   	modules_era.append(muonScaleRes2017())
   	modules_era.append(lepSF_2017())
        modules_era.append(nvtxWeight_2017())
   if options.era=="2018":
        modules_era.append(puAutoWeight_2018())
        modules_era.append(jetmetUncertainties2018All())
        modules_era.append(btagSFProducer("2018", "deepcsv"))
        modules_era.append(muonScaleRes2018())
        modules_era.append(lepSF_2018())
        modules_era.append(nvtxWeight_2018())
   modules_era.append(MonoZProducer(isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))
   modules_era.append(MonoZWSProducer(
      isMC=options.isMC, era=str(options.era),
      do_syst=1, syst_var='', sample=m.get("sample", "")
   ))
   # WW or ZZ sample
   if "ZZTo" in m.get("sample", "") and "GluGluToContin" not in m.get("sample", ""):
      modules_era.append(EWProducer(1, True))
   if "WZTo" in m.get("sample", ""):
      modules_era.append(EWProducer(2, False))
   # for variation-based systematics
   for sys in pro_syst:
      for var in ["Up", "Down"]:
           modules_era.append(MonoZProducer(options.isMC, str(options.era), do_syst=1, syst_var=sys+var))
           modules_era.append(MonoZWSProducer(options.isMC, str(options.era), do_syst=1,
                                               syst_var=sys+var, sample=m.get("sample", "")))
   # for weight-based systematics
   for sys in ext_syst:
      if ("ADDMonoZ" in options.dataset or
          "Unpart"          in options.dataset  ) and "PDF" in sys:
         continue
      for var in ["Up", "Down"]:
          modules_era.append(
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
      combineHLT = yaml.load(open("combineHLT_Run2.yaml"))
   except yaml.YAMLError as exc:
      print(exc)

   ##specifically for private NanoAOD production!!
   #options.dataset2 = options.infile
   #options.dataset2 = options.dataset2.split('/store')[1].split("/")
   #condtag_ = options.dataset2[6]
   #options.dataset = options.dataset2[5]
   #print options.dataset
   #print condtag_
   ##specifically for private NanoAOD production!!

   if options.era=="2016":
        pre_selection = pre_selection + " && (" + combineHLT.get("Run2016All.%s" % options.dataset, 1) + ")"
	print "still need to add 2016 HLT"
   if options.era=="2017":
	if 'Run2017B' in condtag_:
		pre_selection = pre_selection + " && (" + combineHLT.get("Run2017B.%s" % options.dataset, 1) + ")"
	elif 'Run2017C' in condtag_:
		pre_selection = pre_selection + " && (" + combineHLT.get("Run2017C.%s" % options.dataset, 1) + ")"
	else:
		pre_selection = pre_selection + " && (" + combineHLT.get("Run2017CF.%s" % options.dataset, 1) + ")"
   if options.era=="2018":
	pre_selection = pre_selection + " && (" + combineHLT.get("Run2018All.%s" % options.dataset, 1) + ")"
   print " -- era : ",
   if options.era=="2016":
      modules_era.append(getattr(jetRecalib, 'jetRecalib2016%s' % condtag_.split(options.era)[1])() )
   if options.era=="2017":
      modules_era.append(getattr(jetRecalib, 'jetRecalib2017%s' % condtag_.split(options.era)[1])() )
   if options.era=="2018":
      modules_era.append(getattr(jetRecalib, 'jetRecalib2018%s' % condtag_.split(options.era)[1][:1])() )
   modules_era.append(MonoZProducer  (isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))
   modules_era.append(MonoZWSProducer(isMC=options.isMC, era=str(options.era),
                                       do_syst=1, syst_var='', sample="data"))


   if options.era=="2016":
	options.json = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
   if options.era=="2017":
	options.json = "Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"
   if options.era=="2018":
	options.json = "Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"
   print options.json

for i in modules_era:
   print "modules : ", i

print "Selection : ", pre_selection

p = PostProcessor(
   ".", [options.infile],
   cut=pre_selection,
   #branchsel="keep_and_drop.txt",
   #outputbranchsel="drop_all.txt",
   haddFileName="tree_%s.root" % str(options.jobNum),
   modules=modules_era,
   provenance=True,
   noOut=False,
   fwkJobReport=True,
   jsonInput=options.json
)
p.run()
