import pandas as pd
from PIL import Image

class Model:
    def __init__(self , csv_file_name, image_name):

        self.df = self.load_pickle_file(csv_file_name)
        self.objs = self.get_objs()
        self.df_by_obj = self.get_df_by_obj()
        self.img = Image.open(image_name)

    def load_pickle_file(self, file_name):
        return pd.read_pickle(file_name)

    def get_objs(self):
        self.df.groupby([
            "filename",
            "obj"]
        ).size().sort_values(ascending=False)

    def get_df_by_obj(self):
        return self.df.set_index(['filename', 'obj']).sort_index()

