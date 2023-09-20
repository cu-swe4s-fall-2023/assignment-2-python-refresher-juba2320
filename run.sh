#!/bin/bash

set -u
set -o 

a="Agrofood_co2_emission.csv"
b="Afghanistan"
c=0 
d=3

echo "Running print_fires.py"
python print_fires.py --file_name $a --country $b --country_column $c --fires_column $d

echo "Running print_fires.py again with error" 
python print_fires.py

echo "Running print_fires.py again with error"
python print_fires.py --file_name $a --country $c --country_column $b --fires_column $d