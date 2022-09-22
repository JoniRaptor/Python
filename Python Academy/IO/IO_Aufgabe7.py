#  file use_argparse.py

import argparse

#  input
parser = argparse.ArgumentParser(description="IO-Handler")
parser.add_argument("-i", "--input", type=str, help="Input file")
parser.add_argument("-o", "--output", type=str, help="output file")
args = parser.parse_args()

print("Using input file:", args.input)
print("Using output file:", args.output)
