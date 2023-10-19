"""Utility library for getting values, graphing, and operations
    * get_column - returns a list of values based on the inputted arguments
    * file_access - returns the name of the file if it's valid
    * convert_value - returns a converted list of floats from str values
    * find_mean - returns the mean of an array
    * find_median - returns the median of an array
    * find_sd - returns the sample standard deviation of an array
    * graph_hist - graphs histogram and saves it as png
"""
import math
import matplotlib.pyplot as plt


def get_column(file_name, query_column, query_value, result_column=1):
    """Read file by line and get information desired on the arguments inputted.

    Parameters
    ----------
    file_name : str
                Name of the file to be searched.
    query_column : int
                   Column to search.
    query_value : str
                  Value to search for in query_column.
    result_column : int
                    Column values to output.

    Returns
    -------
    col_vals
        A list of values user is searching for.
    """

    # check for valid file
    file = file_access(file_name)

    # create empty list to append values
    col_vals = []

    # loop through each line in the file
    for line in file:
        ln = line.split(',')
        # convert number values to integers/floats
        parsed_ln = convert_value(ln)
        # exceptions for indexes out of range
        try:
            # get numbers based on the inputted arguments for columns
            if parsed_ln[query_column] == query_value:
                col_vals.append(parsed_ln[result_column])
        except IndexError:
            print("Index out of bounds.")
            break

    file.close()
    return col_vals


def file_access(file):
    """Checks is file exists or accessible.

    Parameters
    ----------
    file : str
           Name of the file.

    Returns
    -------
    f
        File name if it's valid.
    """

    # exceptions for handling files
    f = None
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        print('Could not find ' + file)
    except PermissionError:
        print('Could not open ' + file)
    finally:
        return f


def convert_value(line):
    """Makes sure each value in the line is read as the correct type.

    Parameters
    ----------
    line : list of str
           Line from the file.

    Returns
    -------
    converted_line
        A list of all elements in the line as the correct type.
    """

    # exceptions for handling integers
    converted_line = []
    for val in line:
        try:
            val_convert = int(val)
        except ValueError:
            try:
                val_convert = float(val)
            except ValueError:
                val_convert = val

        converted_line.append(val_convert)

    return converted_line


def find_mean(arr):
    """Finds the mean of an array of integers.

    Parameters
    ----------
    arr : array of int
           Array of integers.

    Returns
    -------
    mean
        The mean value of an array of integers.
    """

    mean = sum(arr)/len(arr)
    return mean


def find_median(arr):
    """Finds the median of an array of integers.

    Parameters
    ----------
    arr : array of int
           Array of integers.

    Returns
    -------
    median
        The median value of an array of integers.
    """

    arr.sort()
    midpt = len(arr) // 2

    if len(arr) % 2 == 0:
        median = (arr[midpt-1] + arr[midpt]) / 2
        return median
    else:
        median = arr[midpt]
        return median


def find_sd(arr):
    """Finds the standard deviation of an array of integers.

    Parameters
    ----------
    arr : array of int
           Array of integers.

    Returns
    -------
    sd
        The standard deviation value of an array of integers.
    """

    mean = find_mean(arr)
    summation = 0

    if len(arr) > 1:
        for x in arr:
            summation += (x - mean) ** 2

        sd = math.sqrt(summation/(len(arr)-1))
    else:
        sd = 0

    return sd


def graph_hist(data, xlab, title):
    """Plots the histogram of a list of numbers.

    Parameters
    ----------
    data : array of floats
           Values to be plotted
    xlab : str
           X-axis label
    title : str
           Title of plot

    Returns
    -------
    Saved png file of the plot.
    """

    plt.hist(data, bins='auto', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel('Frequency')

    # write out to doc directory 
    out_file = f"../../../doc/{title}_{xlab}.png"
    plt.savefig(out_file, bbox_inches='tight')
