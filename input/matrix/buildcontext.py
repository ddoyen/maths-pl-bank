
matrix = []
for i in range(int(config['num_rows'])):
    matrix.append([])
    for j in range(int(config['num_cols'])): 
        # each matrix entry is a triple, the first item is a string describing the position of the entry
        # the second item is the value displayed in the form, or '', the third item is True if it is an input field, False 
        # if it isn't.
        if 'matrix' in dic:
            entry_value = dic['matrix'][i][j]
        else:
            entry_value = ''
        if 'mask' in dic:
            entry_mask = dic['mask'][i][j]
        else: 
            entry_mask = True
        matrix[i].append([str(i)+str(j), entry_value, entry_mask])
config['matrix']=matrix

