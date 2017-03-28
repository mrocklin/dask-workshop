# Parallel code

results = []
for x in data:
    if iseven(x):  # even
        y = dask.delayed(double)(x)
    else:          # odd
        y = dask.delayed(inc)(x)

    results.append(y)
    
total = dask.delayed(sum)(results)
total.compute()
