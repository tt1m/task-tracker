import argparse
parser = argparse.ArgumentParser()

parser.add_argument("number", help="displays the square of a given number.", type=int)

args = parser.parse_args()

print(args.number**2)