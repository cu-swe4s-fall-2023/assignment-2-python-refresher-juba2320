"""Takes in arguments and passes them to function.
"""
import my_utils as utils
import argparse
import sys

# parse in arguments
parser = argparse.ArgumentParser(
            description="Take in command line arguments",
            prog="HW#3")

parser.add_argument('--file_name',
                    type=str,
                    help='Name of file',
                    required=True)
parser.add_argument('--country',
                    type=str,
                    help='Country name to look up',
                    required=True)
parser.add_argument('--country_column',
                    type=int,
                    help='Country column number from index 0',
                    required=True)
parser.add_argument('--fires_column',
                    type=int,
                    help='Fires column number from index 0',
                    required=False)
args = parser.parse_args()

# pass in arguments to function
fires = utils.get_column(file_name=args.file_name,
                         query_column=args.country_column,
                         query_value=args.country,
                         result_column=args.fires_column)
print(fires)
sys.exit(1)
