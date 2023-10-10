[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

# Code
The main goal of the code is to search for certain values in the file depending on the input from the user and calculate either the mean, median, or standard deviation from those values. In my assignment, I am looking for number of fires for say a country like Afghanistan. The program takes in arguments for a file to search, the country to look for, what column country is in, and the column that fires can be found. In order to run the program type this command within the src folder and make sure the file is in the same folder:

```
bash run.sh
```

## run.sh
This shell script runs print_fires.py with one error free example and two error prone examples.
The input for the error free example is as follows (file can be found in class Google Drive):
- file_name = Agrofood_co2_emission.csv
- country = Afghanistan
- country_column = 0
- fires_column = 3

In the examples with errors, use the exact same variables but one example does not provide the arguments and the other example inputs the wrong type of parameter.

## print_fires.py
This python file takes in the arguments inputted by the user and passes them to the function in my_utils.py in the main function. The user needs to enter arguments of these types for each argument:
- file_name = string
- country = string
- country_column = integer
- fires_column = integer 
- operation = string

## my_utils.py 
This python file is a library for the functions used in print_fires.py. It consists of three functions: 
1. get_column which gets the values from the column
2. file_access which checks whether the file is valid to pass into get_column
3. convert_value which converts values from the file to integer and float types
4. find_mean which finds the mean of a list of values
5. find_median which finds the median of a list of values
6. find_sd which finds the standard deviation of a list of values 

## Testing
### Unit Tests
Unit tests have been added to test each of the operation functions inside the test_my_utils.py file. Tests have been both randomized and accounts for positive, random, and edge cases. To run this test file, it needs to be run from within the unit_test directory with the command:
```
python -m unittest test_my_utils.py
```

### Functional Tests
Functional tests have also been added to test both the operations and also the arguments that get read in inside the test_print_fires.sh script. To run this test file, it needs to be run from within the functional_tests directory with the command:
```
bash test_print_fires.sh
```

## Continuous Integration
In the .github/workflows directory, is a file named tests.yml which has a simple continuous integration workflow for the code. It runs for style checks, unit tests, and functional tests. 