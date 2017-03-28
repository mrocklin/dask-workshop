dfs = []
for dir in sorted(glob.glob(os.path.join('data', 'messy', '*'))):
    for fn in sorted(glob.glob(os.path.join(dir, '*'))):
        _, _, date, symbol = fn.split(os.path.sep)
        symbol = symbol[:-len('.feather')]
        date = pd.Timestamp(date)
        df = dask.delayed(feather.read_dataframe)(fn)
        df = df.assign(timestamp=df.timestamp.astype('m8[s]') + date,
                       symbol=symbol)
        dfs.append(df)
        
ddf = dd.from_delayed(dfs)
