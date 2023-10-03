"""Takes in arguments and passes them to function.
"""
import my_utils as utils
import argparse
import sys

# parse in arguments
parser = argparse.ArgumentParser(
            description="Take in command line arguments",
            prog="HW#3")

# handles errors if correct type is not entered in for each argument
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
parser.add_argument('--operation',
                    type=str,
                    help = 'Operation to be performed on returned values',
                    required=False)
args = parser.parse_args()


def main():
    # pass in arguments to function
    fires = utils.get_column(file_name=args.file_name,
                             query_column=args.country_column,
                             query_value=args.country,
                             result_column=args.fires_column)

    # perform operation on values  
    if arg.operation.lower() == 'mean':
        print(utils.find_mean(fires))
    else if arg.operation.lower() == 'median':
        print(utils.find_median(fires))
    else if arg.operation.lower() == 'stdev':
        print(utils.find_sd(fires))
    else:
        print(fires)

    sys.exit(1)


if __name__ == '__main__':
    main()
