import pandas as pd
import numpy as np

class CSVData():

    def __init__(self, csvPath:str):

        self.start_point:int = 0
        self.end_point:int = -1
        self.df = pd.read_csv(csvPath, encoding="SHIFT_JIS")

    def get_data(self, key:str):
        range_idx = slice(self.start_point, self.end_point)
        return np.array(self.df[key].tolist())[range_idx]