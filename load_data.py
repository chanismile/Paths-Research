import pandas as pd

df = pd.read_csv('data/fixed.csv',usecols=[1,2,3,5,9,10,12])
df.columns = ['x', 'y', 'obj', 'seq', 'filename', 'time' , 'delta_time']


df['time'] = pd.to_datetime(df['time'])
df['delta_time'] = pd.to_timedelta(df['delta_time'])

df['time'] += df['delta_time']

df_int = df.select_dtypes(include=['int64'])
converted_int = df_int.apply(pd.to_numeric, downcast='unsigned')

df[converted_int.columns] = converted_int


df_obj = df.select_dtypes(include = ['object']).copy()
converted_obj = pd.DataFrame()

for col in df_obj.columns:
       num_unique_values = len(df_obj[col].unique())
       num_total_values = len(df_obj[col])
       if num_unique_values / num_total_values < 0.5:
           converted_obj.loc[:,col] = df_obj[col].astype('category')
       else:
           converted_obj.loc[:,col] = df_obj[col]

df[converted_obj.columns] = converted_obj


df = df.drop('delta_time', 1)


df = df.drop_duplicates()


df.to_pickle('data/paths.pkl.xz')



