from array import array

def get_column(file_name, query_column, query_value, result_column):
    
    file = open(file_name, 'r')
    col_vals = []
    
    for line in file:
        l = line.split(',')
        if l[query_column] == query_value:
            col_vals = col_vals.append(l[result_column])
        
    file.close()
    
    return col_vals
