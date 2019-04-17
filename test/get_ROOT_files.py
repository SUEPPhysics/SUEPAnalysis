import os
import argparse
import multiprocessing as mp
from functools import partial
import yaml
from ROOT import *



parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", type=str, 
   default='/eos/cms/store/group/phys_exotica/monoZ/MonoZAnalysis_BladeRunner_MonoZ_2017/', 
   help="top directory containing all the datasets")
options = parser.parse_args()

gROOT.SetBatch(1)
dir_monoZ = options.dir if options.dir[-1] == '/' else options.dir + '/'
data_samples = ['SingleElectron', 'SingleMuon', 'DoubleEG', 'DoubleMuon', 'MuonEG']


def MergeFiles(file_list, name):
   str_files = " ".join(file_list)
   os.system("../scripts/haddnano.py {}.root ".format(name) + str_files)

def GetGenCorrection(file_list):
   chain = TChain("Runs")
   for file in file_list:
      chain.Add(file)
   dataset = file.split(dir_monoZ)[1].split('/')[0]

   genEventCount = 0
   genEventSumw = 0
   for i in range( chain.GetEntries() ):
      chain.GetEntry(i)
      genEventCount += chain.genEventCount 
      genEventSumw += chain.genEventSumw

   chain.Reset()
   chain.Delete()
   print 'Finished', dataset, 'nFiles:', len(file_list)
   return genEventCount / genEventSumw


def main():
   dict_files = {}
   print 'Walking through directory:', dir_monoZ
   for path, subdirs, files in os.walk(dir_monoZ): 
      sub_path_splited = path.split(dir_monoZ)[1].split('/')
      if len(sub_path_splited) != 4:
         continue
      dataset = sub_path_splited[0]
      if dataset not in dict_files:
         dict_files[dataset] = {'files':[]}
      for name in files:
         if name.split('.')[-1] == 'root':
            dict_files[dataset]['files'].append( os.path.join(path, name) )
   """
   nWorker = mp.cpu_count()
   pool = mp.Pool(processes=nWorker)
   print 'Calculating Gen Weight Corrections with %d CPUs' % nWorker
   def callback_function(GWCorr, dataset):
      dict_files[dataset]['GWCorr'] = GWCorr
   for dataset in sorted( dict_files.keys(), key=lambda _x : len(dict_files[_x]['files']), reverse=True ):
      if dataset in data_samples:
         continue
      file_list = dict_files[dataset]['files']
      if not file_list:
         del dict_files[dataset]
         continue
      partial_callback = partial(callback_function, dataset=dataset)
      pool.apply_async(GetGenCorrection, args=(file_list,), callback=partial_callback)

   pool.close()
   pool.join()
   """
   
   with open('ROOTfiles.yml', 'w') as outfile:
      yaml.dump(dict_files, outfile, default_flow_style=False)

   for name, files in dict_files.items():
      print " ------------------ "
      print "name  : ", name
      MergeFiles(files["files"], name)
      
      
if __name__ == "__main__":
   main()
