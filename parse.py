import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--data', default='default_data',type=str,help='Dataset to load.')
parser.add_argument('--apii', action='store_true', help='appi')



opt = parser.parse_args()

print(opt.apii)

print(opt.data)
