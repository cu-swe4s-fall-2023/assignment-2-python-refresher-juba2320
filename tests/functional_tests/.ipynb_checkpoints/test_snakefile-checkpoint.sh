test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

country0_file_name="Canada_savannah_fires.png"
country1_file_name="Uganda_savannah_fires.png"
country2_file_name="Cambodia_savannah_fires.png"

run basic_snakemake conda install -c conda-forge -c bioconda snakemake graphviz ; cd ../../src/workflow/snakemake ; snakemake --use-conda --cores all 
assert_equal $country0_file_name $( ls $country0_file_name )
assert_equal $country1_file_name $( ls $country1_file_name )
assert_equal $country2_file_name $( ls $country2_file_name )
