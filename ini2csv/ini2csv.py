import csv
from argparse import ArgumentParser
from configparser import ConfigParser

# parser = ArgumentParser()
# parser.add_argument('input_file')
# parser.add_argument('output_file')
# args = parser.parse_args()
#
# config = ConfigParser()
# config.read(args.input_file)
#
# with open(args.output_file, 'w', newline='') as f:
#     writer = csv.writer(f)
#     for section in config.sections():
#         for key in config[section].keys():
#             writer.writerow([section, key, config[section][key]])

parser = ArgumentParser()
parser.add_argument('--collapsed', action='store_true')
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

config = ConfigParser()
config.read(args.input_file)
keys = [i for i in config[config.sections()[0]].keys()]

with open(args.output_file, 'w', newline='') as f:
    writer = csv.writer(f)

    if args.collapsed is True:
        writer.writerow(['header'] + keys)
        for section in config.sections():
            writer.writerow([section] + [config[section][key] for key in keys])
    else:
        for section in config.sections():
            for key in config[section].keys():
                writer.writerow([section, key, config[section][key]])
