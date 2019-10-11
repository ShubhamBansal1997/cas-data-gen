import argparse

from data_gen.data.generator import generate_data

parser = argparse.ArgumentParser(description='Generate fake CAS data.')
parser.add_argument('multiplier', type=int,
                    help='Number of items of each data type to generate')

args = parser.parse_args()

generate_data(args.multiplier)
