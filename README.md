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
python condor_Run2_proc.py --isMC=1 --era=2018 --dataset=<dataset> --infile=<file>
```

## The code set up

The code is effectively run on top of the NanoAOD-tools which give you the central corrections and systematics for each of the objects that you add.

The code is run from the condor file through the condor_Run2_proc.py which can be called for either MC or data for each year (2016,2017,2018). If you want to add an additional correction/producer it will need to be imported and then the module added in this file.

If you are writing a producer from scratch it can be added in the python directory and will follow the same format as the SUEPProducer.py which creates the kinematic variables used in the SUEP analysis (including the jet clustering).

Additionally, in the condor directory there is the kraken_run.py file which will submit Condor jobs for all the files in specified datasets. This submission currenty uses xrdfs to find the files stored on Kraken. An example submission can be seen below:

```
python kraken_run.py --isMC=1 --era=2018 --tag=<tag name> --input=../data/list_2018_MC.txt 
```
The submission will name a directory in the output directory after the tage name you input. If the tag already exists use the --force option if you are trying to resubmit/overwrite.

Note that this submission will look for the dataset xsec in ../data/xsections_<era>.yaml.
  
## After the code is run

Running this code will leave you an NTuple with the new branches defined through the condor_Run2_proc.py. The branches are also trimmed using the keep_and_drop files so if a Branch is missing check these files first. 

To make histograms from these NTuples move to SUEPPhysics/SUEPCoffea
