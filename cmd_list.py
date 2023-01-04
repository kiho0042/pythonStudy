import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--list_data', type = list, default = [0, 0, 0, 0])

args = parser.parse_args()

list_data = args.list_data

print(list_data)