[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

# Assignment 3
The main goal of the code is to search for certain values in the file depending on the input from the user. In my assignment, I am looking for number of fires for say a country like Afghanistan. The program takes in arguments for a file to search, the country to look for, what column country is in, and the column that fires can be found. 

## run.sh
This shell script runs print_fires.py with one error free example and two error prone examples.
The input for the error free example is as follows:
- file_name = Agrofood_co2_emission.csv
- country = Afghanistan
- country_column = 0
- fires_column = 3
In the examples with errors, one example does not provide the arguments and the other example inputs the wrong type of parameter.

## print_fires.py
This python file takes in the arguments inputted by the user and passes them to the function in my_utils.py 

## my_utils.py 
This python file is a library for the functions used in print_fires.py. It consists of two functions: get_column which gets the values from the column and file_access which checks whether the file is valid to pass into get_column. 