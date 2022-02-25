import pandas as pd
import numpy as np
from scipy import signal

class CSVData():

    def __init__(self, csvPath:str):

        self.start_point:int = 0
        self.end_point:int = -1
        self.df = pd.read_csv(csvPath, encoding="SHIFT_JIS", usecols=[1,5])

    def get_data(self, key:str):
        range_idx = slice(self.start_point, self.end_point)
        return np.array(self.df[key].tolist())[range_idx]

class Scoring():
    def __init__(self, test_path, ans_path):
        self.stress_min = 100.0
        self.params = {"stress": 0.02, "angle": 0.01}
        self.test_data = CSVData(test_path)
        self.ans_data = CSVData(ans_path)

    def data_nomalization(self, data):
        start_point = np.where(data.get_data("stress") < self.stress_min)[0][0]
        end_point = np.where(data.get_data("stress") > self.stress_min)[0][-1]
        data.start_point = start_point
        data.end_point = end_point

    def calculate(self):
        self.data_nomalization(self.test_data)
        self.data_nomalization(self.ans_data)

        diff_all = 0.0
        for key in ["stress", "angle"]:
            test_key_data = signal.resample(self.test_data.get_data(key), 100)
            ans_key_data = signal.resample(self.ans_data.get_data(key), 100)

            diff = 0.0
            for i in range(100):
                diff += abs(test_key_data[i] - ans_key_data[i])

            print(diff)
            diff_all += diff * self.params[key]

        point = 100.0 - diff_all
        return point


if __name__ == "__main__":
    score = Scoring("log/2022_02_25_14_18.csv", "log/2022_02_25_14_19.csv")
    print(score.calculate())



