"""Takes in arguments and plots a histogram using the data.
"""
import my_utils as utils
import argparse
import sys

# parse in arguments
parser = argparse.ArgumentParser(
            description="Take in command line arguments to plot data",
            prog="HW#6")

parser.add_argument('--file_name',
                    type=str,
                    help='Name of file',
                    required=True)
parser.add_argument('--filter',
                    type=str,
                    help='Filter to look up (ex. specific country)',
                    required=True)
parser.add_argument('--filter_column',
                    type=int,
                    help='Filter column number from index 0',
                    required=True)
parser.add_argument('--data_name',
                    type=str,
                    help='Name of the data values to get(ex. savannah fires)',
                    required=True)
parser.add_argument('--data_column',
                    type=int,
                    help='Data value column number from index 0',
                    required=True)
args = parser.parse_args()


def main():
    # get data
    data = utils.get_column(file_name=args.file_name,
                            query_column=args.filter_column,
                            query_value=args.filter,
                            result_column=args.data_column)
    # plot data
    if len(data) != 0:
        utils.graph_hist(data, args.data_name, args.filter)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
