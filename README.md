# SUEP NanoAOD
SUEP analysis using NanoAOD


## Quick start

```bash
cmsrel CMSSW_10_6_4
cd CMSSW_10_6_4/src
cmsenv


mkdir PhysicsTools/
git clone https://github.com/yhaddad/nanoAOD-tools.git PhysicsTools/NanoAODTools
git clone git@github.com:chadfreer/Nano_SUEP.git PhysicsTools/SUEP

cd $CMSSW_BASE/src/PhysicsTools/NanoAODTools
git checkout remotes/origin/topic-Run2-Lepton-SF
cd $CMSSW_BASE/src
scram b -j 10

cd $CMSSW_BASE/src/PhysicsTools/SUEP/condor
python condor_Run2_proc.py --isMC=1 --era=2018 --infile=<file>
```
