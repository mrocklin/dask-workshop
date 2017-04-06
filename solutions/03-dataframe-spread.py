high = df.groupby(df.timestamp.dt.round('1d')).high.max()
low = df.groupby(df.timestamp.dt.round('1d')).low.min()
spread = high - low
spread = spread.compute()  # convert from dask.dataframe to pandas
spread.plot(figsize=(10, 5), title='Daily High-Low Spread')
