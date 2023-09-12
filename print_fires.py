import my_utils as utils

country='United States of America'
county_column = 0
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
fires = utils.get_column(file_name = file_name, query_column = county_column , query_value = country, result_column = fires_column)
print(fires)
