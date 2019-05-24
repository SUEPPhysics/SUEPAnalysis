import argparse
from dbs.apis.dbsClient import DbsApi
import json


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", type=str, default='../Samples/MC_2017.txt',help="directory config")
options = parser.parse_args()
json_out = 'test.json'

def das_files(dataset):
    dataset_split = dataset.split('/')
    dataset_split[2] = 'RunIIFall17NanoAODv4*'
    datasetv4 = '/'.join( dataset_split )

    dbs = DbsApi('https://cmsweb.cern.ch/dbs/prod/global/DBSReader')
    return dbs.listDatasets(dataset = datasetv4 )

def get_v4():
    data_file = open(options.config, "r")
    data = data_file.read()

    dict_dataset = {}
    for dataset in data.split('\n'):
        if len(dataset) <= 5: continue
        if "#" in dataset: continue

        dataset = dataset.rstrip()
        dict_dataset[dataset] = das_files(dataset)

    with open(json_out, 'w') as f:
        json.dump(dict_dataset, f, indent=4)

def json_to_txt():
    datasets_txt = []
    with open(json_out) as json_file:
        dict_dataset = json.load(json_file)
        for key in dict_dataset:
            for item in dict_dataset[key]:
                datasets_txt.append(item['dataset'])

        datasets_txt.sort()
        with open('AllMCSamples_v4.txt', 'w') as outfile:
            for datset in datasets_txt:
                outfile.write(datset+'\n')

get_v4()
json_to_txt()
