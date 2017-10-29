import argparse
import importlib

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


#doExperiment experiments/20171029_bootstrap
