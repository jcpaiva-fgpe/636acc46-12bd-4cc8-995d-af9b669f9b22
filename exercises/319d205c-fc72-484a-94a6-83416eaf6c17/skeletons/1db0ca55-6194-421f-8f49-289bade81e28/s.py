data = [ [ 1, 7, 2, None, None, 5],
         [ 3, 3, 5, None, 1, 8 ],
         [ 2, 4, None, 5, 7, 6 ] ]

def impute(data):
    for i, row in enumerate(data):
        r = [x for x in row if x is not None]
        avg = sum(r) / len(r)
        data[i] = list(map(lambda x: {{gap}}, row))
        
impute(data)
print(data)

# exp output
# [[1, 7, 2, 3.75, 3.75, 5], [3, 3, 5, 4.0, 1, 8], [2, 4, 4.8, 5, 7, 6]]
