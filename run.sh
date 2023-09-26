#!/bin/bash
"""Runs print_fires.py with and without errors.
"""

set -e
set -u
set -o pipefail

a="Agrofood_co2_emission.csv"
b="Afghanistan"
c=0
d=3

set +e
# run print_fires.py without errors
echo "Running print_fires.py"
python print_fires.py --file_name $a --country $b --country_column $c --fires_column $d

# run print_fires.py with errors: no arguments
echo "Running print_fires.py again with error"
python print_fires.py

# run print_fires.py with errors: wrong type of arguments
echo "Running print_fires.py again with error"
python print_fires.py --file_name $a --country $c --country_column $b --fires_column $d
set -e
