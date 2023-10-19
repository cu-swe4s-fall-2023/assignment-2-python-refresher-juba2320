test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

file_name1="../../doc/Afghanistan_fires.png"

run basic_plot_data python ../../src/plot_data.py --file_name Sample_Data.csv --filter Afghanistan --filter_column 0 --data_name savannah_fires --data_column 2 --output_filename ../../doc/Afghanistan_fires.png
assert_equal $file_name1 $( ls $file_name1 )
assert_exit_code 0

run plot_with_file_exception python ../../src/plot_data.py --file_name sample_data.csv --filter Afghanistan --filter_column 0 --data_name savannah_fires --data_column 2 --output_filename ../../doc/Afghanistan_fires.png
assert_stderr
assert_exit_code 1

run plot_with_nonexisting_country python ../../src/plot_data.py --file_name Sample_Data.csv --filter China --filter_column 0 --data_name crop_residues --data_column 4 --output_filename ../../doc/China_crop.png
assert_no_stdout
assert_exit_code 1