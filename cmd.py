
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--mode', help = 'Run Time : r, Test Mode : t (Default : r)', type = str, default = 'r')

args = parser.parse_args()

print(str(args.mode).lower())