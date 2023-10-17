COUNTRIES: ["Canada", "Uganda", "Cambodia"]

rule all:
    COUNTRIES + '.png'

for COUNTRY in COUNTRIES:
    rule plot_savannah_fires:
        input: 
            'Agrofood_co2_emission.csv'
        output:
            COUNTRY + '_savannah fires.png'
        conda:
            "env.yml"
        Shell:
            "python plot_data.py --file_name {input} --filter " + COUNTRY + " --filter_column 0 --data_name \"savannah fires\" --data_column 2"
            