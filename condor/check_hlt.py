import yaml
import uproot
import os
import re
import ROOT

try:
    combineHLT = yaml.load(open("combineHLT_test.yaml"))
except yaml.YAMLError as exc:
    print(exc)


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



def check_paths(file, hlt_soupe):
    infile = inputfile(file)
    upfile = uproot.open(infile)
    for hlt in hlt_soupe:
        if hlt in upfile["Events"].keys():
            print hlt, " : good"
        else:
            print hlt, " : bad"


def getHLT(name, isMC=True):
    name = name.split('/store')[1].split("/")
    if isMC:
        condtag = name[5]
        dataset = name[3]
    else:
        condtag = name[2]
        dataset = name[3]

    path_cut = ""
    if "Run2016" in condtag:
        path_cut = combineHLT.get("Run2016All.%s" % dataset, 1)
    elif "Run2017" in condtag:
        if 'Run2017B' in condtag:
            path_cut = combineHLT.get("Run2017CF.%s" % dataset, 1)
        elif 'Run2017C' in condtag:
            path_cut = combineHLT.get("Run2017CF.%s" % dataset, 1)
        else:
            path_cut = combineHLT.get("Run2017CF.%s" % dataset, 1)
    else:
        path_cut = combineHLT.get("Run2018All.%s" % dataset, 1)

    oprs = ["(", ")", "||", "&&", "!"]
    for opr in oprs:
        path_cut = path_cut.replace(opr, " %s " % opr)
    soupe = []
    for h in path_cut.split():
        if "HLT" in h: soupe.append(h)
    return soupe


files  = [
    #"/store/data/Run2017B/SingleElectron/NANOAOD/Nano1June2019-v1/30000/501CA18F-562E-F74B-BFCA-3A9DBD7CB1D6.root",
    #"/store/data/Run2017C/SingleElectron/NANOAOD/Nano1June2019-v1/30000/EBEF93A5-F0C2-8D44-8680-405361B507AE.root"
    "/store/data/Run2017F/SingleElectron/NANOAOD/Nano1June2019-v1/40000/9EC26AA8-46FD-844A-89E8-2DCB9F629E31.root"
]


for f in files:
    print "file : ", f
    check_paths(inputfile(f), getHLT(f, False))

