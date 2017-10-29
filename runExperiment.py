import argparse
import importlib
from pathlib2 import Path
import yaml
import time

parser = argparse.ArgumentParser(description='Run AWS experiments.')
parser.add_argument('experimentDir', type=str,
                    help='the experiment you wish to run')


args = parser.parse_args()
experimentName = args.experimentDir.split("/")[1]

experiment = importlib.import_module("experiments.%s" % experimentName)

from troposphere import Ref, Template
t = Template()
t = experiment.fill_template(t)
print (t.to_json())



json_doc = t.to_json()
yml_doc = yaml.dump(yaml.load(json_doc))
# print(json_doc)

now = time.time()
experiment_output_dir="output/%s" % experimentName
Path(experiment_output_dir).mkdir(parents=True, exist_ok=True)

filename_base = "%s/%s" % (experiment_output_dir, experimentName)
filename_with_timestamp = "%s_%d" % (filename_base, now)
with open("%s.json" % filename_base, "w") as text_file:
    text_file.write(json_doc)
with open("%s.json" % filename_with_timestamp, "w") as text_file:
    text_file.write(json_doc)
with open("%s.yml"% filename_with_timestamp, "w") as text_file:
    text_file.write(yml_doc)

#doExperiment experiments/20171029_bootstrap
