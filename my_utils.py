"""Grabbing column values
    * get_column - returns a list of values based on the inputted arguments
    * file_access - returns the name of the file if it's valid
"""


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
        # get the desired numbers based on the inputted arguments for columns
        if ln[query_column] == query_value:
            col_vals.append(ln[result_column])

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
