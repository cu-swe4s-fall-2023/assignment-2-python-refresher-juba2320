test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# functional tests for mean operation
run basic_mean python ../../src/print_fires.py --file_name Sample_Data.csv --country Afghanistan --country_column 0 --fires_column 3 --operation Mean
assert_in_stdout 0.12991667
assert_exit_code 0

run mean_with_file_exception python ../../src/print_fires.py --file_name sample_data.csv --country Afghanistan --country_column 0 --fires_column 3 --operation mean
assert_stderr
assert_exit_code 1

run mean_with_out_of_bounds_index python ../../src/print_fires.py --file_name Sample_Data.csv --country Afghanistan --country_column 0 --fires_column 20 --operation mean 
assert_stderr
assert_exit_code 1

run mean_with_nonexisting_country python ../../src/print_fires.py --file_name Sample_Data.csv --country China --country_column 0 --fires_column 3 --operation mean 
assert_no_stdout
assert_exit_code 1

run mean_with_one_value python ../../src/print_fires.py --file_name Sample_Data.csv --country "American Samoa" --country_column 0 --fires_column 10 --operation mean 
assert_in_stdout 0.5665
assert_exit_code 0


# functional tests for median operation
run basic_median python ../../src/print_fires.py --file_name Sample_Data.csv --country Afghanistan --country_column 0 --fires_column 3 --operation Median
assert_in_stdout 0.0557
assert_exit_code 0

run median_with_invalid_index python ../../src/print_fires.py --file_name Sample_Data.csv --country Afghanistan --country_column 0.2 --fires_column 3 --operation Median
assert_stderr
assert_exit_code 2

run median_with_zeroes python ../../src/print_fires.py --file_name Sample_Data.csv --country Albania --country_column 0 --fires_column 6 --operation Median
assert_in_stdout 0
assert_exit_code 0

run median_with_one_value python ../../src/print_fires.py --file_name Sample_Data.csv --country "American Samoa" --country_column 0 --fires_column 10 --operation Median
assert_in_stdout 0.5665
assert_exit_code 0


# functional tests for stdev operation
run basic_stdev python ../../src/print_fires.py --file_name Sample_Data.csv --country Afghanistan --country_column 0 --fires_column 3 --operation Stdev
assert_in_stdout 0.20858931
assert_exit_code 0

run stdev_with_negatives python ../../src/print_fires.py --file_name Sample_Data.csv --country Afghanistan --country_column 0 --fires_column 5 --operation Stdev
assert_in_stdout 1292.83373159
assert_exit_code 0

run stdev_with_zeros python ../../src/print_fires.py --file_name Sample_Data.csv --country Albania --country_column 0 --fires_column 6 --operation Stdev
assert_in_stdout 0
assert_exit_code 0
