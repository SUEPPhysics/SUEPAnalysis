import os, sys, re
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
# import PSet
import yaml
#Import the NanoAOD-tools that we will need
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
#Import the MonoZ analysis tools
from PhysicsTools.MonoZ.MonoZProducer import *
from PhysicsTools.MonoZ.GenWeightProducer import *
from PhysicsTools.MonoZ.EWProducer import *
from PhysicsTools.MonoZ.ADDProducer import *
from PhysicsTools.MonoZ.NvtxPUreweight import *
from PhysicsTools.MonoZ.BtagEventWeightProducer import *
from PhysicsTools.MonoZ.TriggerSFProducer import *
from PhysicsTools.MonoZ.GenMonoZProducer import *
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
   condtag_ = "NANOAODSIM"
   if options.dataset == "X":
      options.dataset = options.infile
      options.dataset = options.dataset.split('/store')[1].split("/")
      condtag_ = options.dataset[5]
      options.dataset = options.dataset[3]
   print "[check] condtag_ == ", condtag_
   print "[check] dataset  == ", options.dataset
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

pre_selection  = "((Sum$(Electron_pt>20 & &abs(Electron_eta)<2.5) + Sum$(Muon_pt>20 && abs(Muon_eta)<2.5) )>=2)"
pre_selection += "&& Flag_METFilters"

if float(options.nevt) > 0:
   print " passing this cut and : ", options.nevt
   pre_selection += ' && (Entry$ < {})'.format(options.nevt)

modules_era   = [
    GenWeightProducer(
       isMC = options.isMC,
       dopdf = False if ("ADD" in options.dataset or "Unpart" in options.dataset) else True
    )
]

pro_syst = [ "ElectronEn", "MuonEn", "jesTotal", "jer"]
ext_syst = [ "puWeight", "PDF", "MuonSF", "ElecronSF", "EWK", "nvtxWeight","TriggerSFWeight","btagEventWeight", "QCDScale0w", "QCDScale1w", "QCDScale2w"]

if options.isMC:
   if options.era=="2016":
      modules_era.append(puAutoWeight_2016())
      modules_era.append(PrefCorr())
      modules_era.append(jetmetUncertainties2016All())
      modules_era.append(btagSFProducer("Legacy2016", "deepcsv"))
      modules_era.append(muonScaleRes2016())
      modules_era.append(lepSF_2016())
      modules_era.append(nvtxWeight_2016())
      ext_syst.append("PrefireWeight")
   if options.era=="2017":
      modules_era.append(puAutoWeight_2017())
      modules_era.append(PrefCorr())
      modules_era.append(jetmetUncertainties2017All())
      modules_era.append(btagSFProducer("2017", "deepcsv"))
      modules_era.append(muonScaleRes2017())
      modules_era.append(lepSF_2017())
      modules_era.append(nvtxWeight_2017())
      ext_syst.append("PrefireWeight")
   if options.era=="2018":
      modules_era.append(puAutoWeight_2018())
      modules_era.append(jetmetUncertainties2018All())
      modules_era.append(btagSFProducer("2018", "deepcsv"))
      modules_era.append(muonScaleRes2018())
      modules_era.append(lepSF_2018())
      modules_era.append(nvtxWeight_2018())

   modules_era.append(MonoZProducer(isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))

   if options.era=="2016":
      modules_era.append(TriggerSF_2016())
      modules_era.append(BtagEventWeight_2016())
   if options.era=="2017":
      modules_era.append(TriggerSF_2017())
      modules_era.append(BtagEventWeight_2017())
   if options.era=="2018":
      modules_era.append(TriggerSF_2018())
      modules_era.append(BtagEventWeight_2018())

   modules_era.append(GenMonoZProducer())
   # WZ or ZZ sample for ewk corrections and ADD for EFT weights
   if "ZZTo" in options.dataset and "GluGluToContin" not in options.dataset:
      modules_era.append(EWProducer(1, True))
   if "WZTo" in options.dataset:
      modules_era.append(EWProducer(2, False))
   dim = 0
   if "ADD" in options.dataset:
      if "d_2" in options.dataset or "d-2" in options.dataset: dim = 2
      elif "d_3" in options.dataset or "d-3" in options.dataset: dim = 3
      elif "d_4" in options.dataset or "d-4" in options.dataset: dim = 4
      elif "d_5" in options.dataset or "d-5" in options.dataset: dim = 5
      elif "d_6" in options.dataset or "d-6" in options.dataset: dim = 6
      elif "d_7" in options.dataset or "d-7" in options.dataset: dim = 7
      else: sys.exit('ADD model dimensions does not make sense') 

      if "MD_1" in options.dataset or "MD-1" in options.dataset: MD = 1
      elif "MD_2" in options.dataset or "MD-2" in options.dataset:MD = 2
      elif "MD_3" in options.dataset or "MD-3" in options.dataset: MD = 3
      else: MD=100#number large enough the ADDWeight will be 1

      modules_era.append(ADDProducer(MD,dim,options.era))


   # for shift-based systematics
   for sys in pro_syst:
      for var in ["Up", "Down"]:
         modules_era.append(MonoZProducer(options.isMC, str(options.era), do_syst=1, syst_var=sys+var))

else:
   print "sample : ", options.dataset, " candtag : ", condtag_
   try:
      combineHLT = yaml.load(open("combineHLT_Run2.yaml"))
   except yaml.YAMLError as exc:
      print(exc)
   if options.era=="2016":
        pre_selection = pre_selection + " && (" + combineHLT.get("Run2016All.%s" % options.dataset, "") + ")"
	print "still need to add 2016 HLT"
   if options.era=="2017":
      if 'Run2017B' in condtag_:
         pre_selection = pre_selection + " && (" + combineHLT.get("Run2017B.%s" % options.dataset, "") + ")"
      elif 'Run2017C' in condtag_:
         pre_selection = pre_selection + " && (" + combineHLT.get("Run2017C.%s" % options.dataset, "") + ")"
      else:
         pre_selection = pre_selection + " && (" + combineHLT.get("Run2017CF.%s" % options.dataset, "") + ")"
   if options.era=="2018":
      if ('Run2018A' in condtag_) or ('Run2018B' in condtag_):
         pre_selection = pre_selection + " && (" + combineHLT.get("Run2018AB.%s" % options.dataset, "") + ")"
      else:
         pre_selection = pre_selection + " && (" + combineHLT.get("Run2018CD.%s" % options.dataset, "") + ")"

   print " -- era : ",
   if options.era=="2016":
      modules_era.append(getattr(jetRecalib, 'jetRecalib2016%s' % condtag_.split(options.era)[1][:1])() )
   if options.era=="2017":
      modules_era.append(getattr(jetRecalib, 'jetRecalib2017%s' % condtag_.split(options.era)[1])() )
   if options.era=="2018":
      modules_era.append(getattr(jetRecalib, 'jetRecalib2018%s' % condtag_.split(options.era)[1][:1])() )

   modules_era.append(MonoZProducer  (isMC=options.isMC, era=str(options.era), do_syst=1, syst_var=''))

   if options.era=="2016":
       options.json = "Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt"
   if options.era=="2017":
       options.json = "Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
   if options.era=="2018":
       options.json = "Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"
   print "---- JSON used is : ", options.json


for i in modules_era:
   print "modules : ", i

print "Selection : ", pre_selection

p = PostProcessor(
   ".", [options.infile],
   cut=pre_selection,
   branchsel="keep_and_drop.txt",
   outputbranchsel="keep_and_drop.txt",
   haddFileName="tree_%s.root" % str(options.jobNum),
   modules=modules_era,
   provenance=True,
   noOut=False,
   fwkJobReport=True,
   jsonInput=options.json
)
p.run()
