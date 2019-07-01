import yaml
import uproot
import os
import re
import ROOT
from termcolor import colored

try:
    combineHLT = yaml.load(open("combineHLT_Run2.yaml"))
except yaml.YAMLError as exc:
    print(exc)


def inputfile(nanofile):
    tested   = False
    forceaaa = False
    pfn=os.popen("edmFileUtil -d %s"%(nanofile)).read()
    pfn=re.sub("\n","",pfn)
    if (os.getenv("GLIDECLIENT_Group","") != "overflow" and
        os.getenv("GLIDECLIENT_Group","") != "overflow_conservative" and not
        forceaaa ):
        if not tested:
            testfile=ROOT.TFile.Open(pfn)
            if testfile and testfile.IsOpen() :
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



def check_paths(file, hlt_soupe, path):
    infile = inputfile(file)
    upfile = uproot.open(infile)
    for hlt in hlt_soupe:
        if hlt in upfile["Events"].keys():
            print colored(path +": "+ hlt + " : good",  "blue")
        else:
            print colored(path +": "+ hlt + " : bad",  "red")


def getHLT(name, isMC=True):
    name = name.split('/store')[1].split("/")
    if isMC:
        condtag = name[5]
        dataset = name[3]
    else:
        condtag = name[2]
        dataset = name[3]

    path_cut = ""
    path = ""
    if "Run2016" in condtag:
        path_cut = combineHLT.get("Run2016All.%s" % dataset, 1)
        path = "Run2016All.%s" % dataset
    elif "Run2017" in condtag:
        if 'Run2017B' in condtag:
            path_cut = combineHLT.get("Run2017B.%s" % dataset, 1)
            path = "Run2017CF.%s" % dataset
        elif 'Run2017C' in condtag:
            path_cut = combineHLT.get("Run2017C.%s" % dataset, 1)
            path = "Run2017CF.%s" % dataset
        else:
            path_cut = combineHLT.get("Run2017CF.%s" % dataset, 1)
            path = "Run2017CF.%s" % dataset
    else:
        path_cut = combineHLT.get("Run2018All.%s" % dataset, 1)
        path = "Run2018All.%s" % dataset

    oprs = ["(", ")", "||", "&&", "!"]
    for opr in oprs:
        path_cut = path_cut.replace(opr, " %s " % opr)
    soupe = []
    for h in path_cut.split():
        if "HLT" in h: soupe.append(h)
    return soupe, path 


files  = [
    # "/store/data/Run2017B/DoubleEG/NANOAOD/Nano1June2019-v1/40000/7AF5D4BF-41BD-F54F-9FBD-4F1BF74E7585.root",
    # "/store/data/Run2017C/DoubleEG/NANOAOD/Nano1June2019-v1/70000/15E5DB5F-DA7A-ED46-9E54-42DB3EDCF922.root",
    # "/store/data/Run2017D/DoubleEG/NANOAOD/Nano1June2019-v1/40000/1085C979-C6C1-D245-81E0-14245BAF2540.root",
    # "/store/data/Run2017E/DoubleEG/NANOAOD/Nano1June2019-v1/40000/38571A86-DF79-284B-8293-90C0694440F3.root",
    # "/store/data/Run2017F/DoubleEG/NANOAOD/Nano1June2019-v1/30000/D101991C-3391-4842-95B0-17370BA942C7.root",
    # 
    # "/store/data/Run2017B/MuonEG/NANOAOD/Nano1June2019-v1/70000/969BCC88-6833-1C41-88AE-D81D72E1FCD6.root",
    # "/store/data/Run2017C/MuonEG/NANOAOD/Nano1June2019-v1/30000/029DFAE9-B541-7744-BF01-DE71F8D154BD.root",
    # "/store/data/Run2017D/MuonEG/NANOAOD/Nano1June2019-v1/40000/5C6C2ED4-944E-F742-8F94-55BDA3619D61.root",
    # "/store/data/Run2017E/MuonEG/NANOAOD/Nano1June2019-v1/40000/B155EEC9-472C-994C-8166-A35A2CCDBAE8.root",
    # "/store/data/Run2017F/MuonEG/NANOAOD/Nano1June2019-v1/30000/021952F8-6AF0-AE44-8ACC-44E869FFA3A9.root",
    # 
    # "/store/data/Run2017B/SingleElectron/NANOAOD/Nano1June2019-v1/30000/7269D287-C9F3-8940-BBBB-52309C6011B7.root",
    # "/store/data/Run2017C/SingleElectron/NANOAOD/Nano1June2019-v1/30000/7F3172F0-54F1-EE40-92D5-41BC786C63E3.root",
    # "/store/data/Run2017D/SingleElectron/NANOAOD/Nano1June2019-v1/70000/6BE12F48-717E-3A4A-8ADE-5B316925A84B.root",
    # "/store/data/Run2017E/SingleElectron/NANOAOD/Nano1June2019-v1/70000/4D6173C2-6675-2949-B0A0-2755BBC6FE69.root",
    # "/store/data/Run2017F/SingleElectron/NANOAOD/Nano1June2019-v1/40000/D817CA4F-3FFF-F643-81BB-33955EC5E2F5.root",
    # 
    # "/store/data/Run2017B/DoubleMuon/NANOAOD/Nano1June2019-v1/70000/FD04AF6C-ABBD-FD47-BDD1-67342508781C.root",
    # "/store/data/Run2017C/DoubleMuon/NANOAOD/Nano1June2019-v1/70000/EDFE58C4-2BA4-E543-AE9B-A935FBDA78A7.root",
    # "/store/data/Run2017D/DoubleMuon/NANOAOD/Nano1June2019-v1/30000/78DEB2A5-5DA6-944A-A8E6-5458FEC6D697.root",
    # "/store/data/Run2017E/DoubleMuon/NANOAOD/Nano1June2019-v1/30000/DF7A52FE-9728-5541-B846-B9756C6BFCBE.root"

    "/store/data/Run2018B/DoubleMuon/NANOAOD/Nano1June2019-v1/40000/87EA3C75-83B5-714B-8EFF-4F9C1656B513.root",
    "/store/data/Run2018A/DoubleMuon/NANOAOD/Nano1June2019-v1/60000/8A8F6070-3AF9-6F43-AF27-B10D151AD4BC.root",
    "/store/data/Run2018C/DoubleMuon/NANOAOD/Nano1June2019-v1/40000/92483499-84F4-C440-9318-55BCA9EDE538.root",
    "/store/data/Run2018D/DoubleMuon/NANOAOD/Nano1June2019_ver2-v1/30000/FA738A7B-9639-3846-B1B6-8E210AF27C3F.root",

    "/store/data/Run2018A/SingleMuon/NANOAOD/Nano1June2019-v1/40000/E588896A-DB15-8044-9CB7-7A07E7BAD796.root",
    "/store/data/Run2018B/SingleMuon/NANOAOD/Nano1June2019-v1/40000/C070EEF1-959E-3841-8B5C-F63A2E816006.root",
    "/store/data/Run2018C/SingleMuon/NANOAOD/Nano1June2019-v1/40000/81D2D727-42AD-4E4E-97C5-7C9FDF874828.root",
    "/store/data/Run2018D/SingleMuon/NANOAOD/Nano1June2019-v1/40000/B120BBE4-C003-424E-B430-9B9F2E537C14.root",
    
    "/store/data/Run2018A/EGamma/NANOAOD/Nano1June2019-v1/40000/63D76523-7059-A644-8AB7-C4C357F2876C.root",
    "/store/data/Run2018B/EGamma/NANOAOD/Nano1June2019-v1/40000/47077F9D-A175-CF4E-8030-432E8CF5DEEB.root",
    "/store/data/Run2018C/EGamma/NANOAOD/Nano1June2019-v1/240000/C1197790-7086-B44A-B2FF-3FB26D5E8E33.root",
    "/store/data/Run2018D/EGamma/NANOAOD/Nano1June2019-v1/70000/2850CA7A-8F55-3A4E-BC12-527835BCC4C5.root"

]


for f in files:
    print "DataSet : ", f.split("NANOAOD")[0]
    soupe, path = getHLT(f, False)
    check_paths(inputfile(f), soupe, path)

