from Utilities.General.cmssw_das_client import get_data as das_query
import argparse
import yaml
import ROOT
import os
import os.path

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--config", type=str, default='configs/sample_mc_2017.dat',help="directory config")
parser.add_argument("-d", "--dir"   , type=str, default='/eos/cms/', help="scan this directory")
parser.add_argument("-p", "--use_parent", type=str, default='True',
                    help="use MiniAOD parent instead of NanoAOD")
parser.add_argument("-x", "--xsec"  , type=str, default='configs/xsections.yaml', help="scan this directory")
parser.add_argument("--include_files", "--include_files", type=bool, default=True, help="")
parser.add_argument("--otype", "--otype", type=str, default="python", help="[python,yaml]")

options = parser.parse_args()

def get_nevent(infile):
    rootf= ROOT.TFile.Open(infile, 'READ')
    tree = rootf.Get("Events")
    return tree.GenEntries()

def file_from_das(dataset):
    if options.use_parent:
        format_ = dataset.split("/")[2]
        if 'SIM' in format_:
            dataset.replace("NANOAODSIM", "MINIAODSIM")
        else:
            dataset.replace("NANOAOD", "MINIAOD")
    response = das_query(
        "file dataset=%s | grep file.name,file.nevents" % ( dataset )
    )
    root_file_list = []
    nevents = 0
    for d in response.get("data",[]):
        for jf in d["file"]:
            if "nevents" in jf:
                nevents += jf["nevents"]
                root_file_list.append({
                    "name"    : str(jf["name"]),
                    "nevents" : int(jf["nevents"])
                })
                break
    return root_file_list, nevents

def file_from_eos(dataset):
    files = []
    nevents = 0
    for dirpath, dirnames, filenames in os.walk(options.dir):
        for filename in [f for f in filenames if f.endswith(".root")]:
            # Add Something here to select the sample
            Files.append(os.path.join(dirpath, filename))
            nevents = get_nevent(os.path.join(dirpath, filename))

    return files, nevents

data_file = open(options.config, "r")
data = data_file.read()

catalog = {}
with open(options.xsec, 'r') as stream:
    try:
        xsection = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)


for s in data.split('\n'):
    print "sample : ", s
    if len(s) <= 5: continue
    if "#" in s: continue

    tag = s.split("/")[1].replace(" ", "")
    print len(s), len(s.replace(" ", ""))
    _files, _nevt = file_from_das(s)
    try:
        _xsec = xsection[tag].get("xsec", 1.0)
    except:
        _xsec = 1.0
    catalog[s] = {
        "sample"  : tag,
        "xsec"    : _xsec,                          #
        "nevents" : _nevt
    }

if options.otype == "yaml":
    with open('catalog_2017.yml', 'w') as outfile:
        yaml.dump(catalog, outfile, default_flow_style=False)

elif options.otype == "python":
    _template_ = """
    import os
    dataset = {}
    """
    with open("catalog_2017.py", "w") as outfile:
        outfile.write("# auto-generated \n")
        outfile.write("catalog={} \n")
        for name, c in catalog.items():
            line = "catalog['%s']= {'sample': '%s', 'nevents': %i, 'xsec': %f} \n"
            outfile.write(
                line % (
                    name, c["sample"], c["nevents"], c["xsec"]
                )
            )

elif options.otype == "json":
    print "not implemented yet"
else:
    print "type unknown"
