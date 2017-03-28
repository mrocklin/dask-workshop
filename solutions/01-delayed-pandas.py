spreads = []
days = []
for fn in filenames:
    df = dask.delayed(pd.read_csv)(fn, parse_dates=['timestamp'], index_col='timestamp')
    spread = df.high.max() - df.low.min()
    day = df.index[0].date()
    
    spreads.append(spread)
    days.append(day)
    
spreads, days = dask.compute(spreads, days)
