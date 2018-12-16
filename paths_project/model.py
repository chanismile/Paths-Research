import pandas as pd
from PIL import Image
import fix_csv
import os.path


class Model:
    def __init__(self , csv_file_name, image_name):
        self.df = self.convert_csv_to_pickle(csv_file_name)
        # aa = self.df.head(25)
        # aa.to_pickle('../data/sample1.pkl.xz')
        # aa.to_csv('../data/sample1.csv')
        self.objs = self.get_objs()
        self.df_by_obj = self.get_df_by_obj()
        self.img = Image.open(image_name)

    def load_pickle_file(self, file_name):
        return pd.read_pickle(file_name)

    def convert_csv_to_pickle(self, csv_file_name):
        pickle_file_name = f"{csv_file_name[:csv_file_name.rfind('.')]}.pkl.xz"

        if os.path.isfile(pickle_file_name):
            return pd.read_pickle(pickle_file_name)

        csv_fixed_file_name = fix_csv.fix_csv_file(csv_file_name)[0]
        df = pd.read_csv(csv_fixed_file_name, usecols=[1, 2, 3, 5, 9, 10, 12])
        df.columns = ['x', 'y', 'obj', 'seq', 'filename', 'time', 'delta_time']
        df['time'] = pd.to_datetime(df['time'])
        df['delta_time'] = pd.to_timedelta(df['delta_time'])
        df['time'] += df['delta_time']

        df_int = df.select_dtypes(include=['int64'])
        converted_int = df_int.apply(pd.to_numeric, downcast='unsigned')
        df[converted_int.columns] = converted_int
        df_obj = df.select_dtypes(include=['object']).copy()
        converted_obj = pd.DataFrame()

        for col in df_obj.columns:
            num_unique_values = len(df_obj[col].unique())
            num_total_values = len(df_obj[col])
            if num_unique_values / num_total_values < 0.5:
                converted_obj.loc[:, col] = df_obj[col].astype('category')
            else:
                converted_obj.loc[:, col] = df_obj[col]

        df[converted_obj.columns] = converted_obj

        df = df.drop('delta_time', 1)
        df = df.drop_duplicates()
        df.to_pickle(pickle_file_name)
        return pd.read_pickle(pickle_file_name)

    def get_objs(self):
        self.df.groupby([
            "filename",
            "obj"]
        ).size().sort_values(ascending=False)

    def get_df_by_obj(self):
        return self.df.set_index(['filename', 'obj']).sort_index()

