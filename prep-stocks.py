import dask.dataframe as dd
import dask.multiprocessing
import os
import shutil

if not os.path.exists('data'):
    os.mkdir('data')

dirname = os.path.join('data', 'stocks')
if os.path.exists(dirname):
    shutil.rmtree(dirname)

os.mkdir(dirname)

for symbol in ['GOOG', 'YHOO', 'AAPL', 'MSFT']:
    df = dd.demo.daily_stock(symbol, '2015', '2016', freq='1s')
    dirname = os.path.join('data', 'stocks', symbol)
    os.mkdir(dirname)
    names = [str(ts.date()) for ts in df.divisions]
    df.to_csv(os.path.join('data', 'stocks', symbol, '*.csv'),
              name_function=names.__getitem__,
              get=dask.multiprocessing.get)
