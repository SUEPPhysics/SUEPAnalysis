# SUEP NanoAOD
SUEP analysis using NanoAOD


## Quick start

```bash
cmsrel CMSSW_10_6_4
cd CMSSW_10_6_4/src
cmsenv


mkdir PhysicsTools/
git clone https://github.com/yhaddad/nanoAOD-tools.git PhysicsTools/NanoAODTools
git clone git@github.com:yhaddad/MonoZNanoAOD.git PhysicsTools/SUEP

cd $CMSSW_BASE/src/PhysicsTools/NanoAODTools
git checkout remotes/origin/topic-Run2-Lepton-SF
cd $CMSSW_BASE/src
scram b -j 10

cd $CMSSW_BASE/src/PhysicsTools/SUEP/condor
python condor_Run2_proc.py --isMC=1 --era=2018 --infile=<file>
```

## Running combine

Before generating datacard and running the final fit, we need to fetch [combine](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part2/settinguptheanalysis/) tools.

```bash
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_13
cd CMSSW_10_2_13/src
cmsenv
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit
git fetch origin
git checkout v8.0.1

# fetch CombineTool
cd $CMSSW_BASE/src
bash <(curl -s https://raw.githubusercontent.com/cms-analysis/CombineHarvester/master/CombineTools/scripts/sparse-checkout-https.sh)

cd $CMSSW_BASE/src/
scramv1 b clean; scramv1 b -j 10
```

To run some of the plotting tools, you need third party pakages such as uproot. You can install by 

```
pip install uproot --user
pip install thermcolor --user
```

Then you need to checkout the packages to run the datacrad producer, you need to create a directory where to put the merged root files.

```
cd $CMSSW_BASE/src/
git clone https://github.com/yhaddad/MonoZFinalFit.git
cd $CMSSW_BASE/src/MonoZFinalFit/
cd data/
python filemerger.py --dir=/eos/cms/store/group/phys_exotica/monoZ/DarkNight/
```

`DarkNight` is the latest production to be replaced with the tag that you run with. 

Please make sure to edit `config/merged_inputs.yaml` and make appropriate changes about how the group merging should be done (dont change the group name, only the file names)

to make datacards for all the different control regions you can run: 
```
./run.sh
```

please edit this file and make approperiate changes, such as "python3 to python".
to run the limits, you hit the follwing command

```
combineCards.py -S DMY1000Xd200/card_* > combined_DMY1000Xd200.dat
text2workspace.py combined_DMY1000Xd200.dat
combine -M AsymptoticLimits combined_DMY1000Xd200.dat.root  --run blind
```

Sometimes it complains about "0.000" please changes it to "0.100" if it does. 

the output of such command is :

```
 -- AsymptoticLimits ( CLs ) --
Expected  2.5%: r < 5.1239
Expected 16.0%: r < 7.3816
Expected 50.0%: r < 11.4062
Expected 84.0%: r < 18.0897
Expected 97.5%: r < 27.4244
```
Where 5.1239 is the expected limit using the input signal. 

To run the impact parameters tools check the documentation [here](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/nonstandard/#nuisance-parameter-impacts)

```
combineTool.py -M Impacts -d combined_DMY2000Xd1.dat.root -m 125 --doInitialFit --robustFit 1
combineTool.py -M Impacts -d combined_DMY2000Xd1.dat.root -m 125 --robustFit 1 --doFits
combineTool.py -M Impacts -d combined_DMY2000Xd1.dat.root -m 125 --o impacts.json
plotImpacts.py -i impacts.json -o impacts
```


