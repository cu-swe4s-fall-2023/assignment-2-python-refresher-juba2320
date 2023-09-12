country='United States of America'
county_column = 1
fires_column = 4
file_name = 'Agrofood_co2_emission.csv'
fires = get_column(file_name, county_column ,country, fires_column)
print(fires)
