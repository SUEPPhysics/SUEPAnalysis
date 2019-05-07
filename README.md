# MonoZNanoAOD
MonoZ analysis using NanoAOD


## Quick start

```bash
cmsrel CMSSW_9_4_9
cd CMSSW_9_4_9/src
cmsenv


mkdir PhysicsTools/
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
git clone git@github.com:yhaddad/MonoZNanoAOD.git PhysicsTools/MonoZ

cd $CMSSW_BASE/src
scram b -j 10

cd $CMSSW_BASE/src/PhysicsTools/MonoZ/scripts/
python postproc_test.py
```

## submitting crab jobs

```bash
voms-proxy-init -voms cms --valid 168:00
source /cvmfs/cms.cern.ch/crab3/crab.sh

cd $CMSSW_BASE/src/PhysicsTools/MonoZ/crab/

echo "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM" > simple_test.dat

python submit_all.py -i simple_test.dat --isMC=1
```

