import numpy as np
from csv_data import CSVData
from scipy import signal
import matplotlib.pyplot as plt


def data_nomalization(data):
        stress_data = data.get_data("stress")
        start_point = np.where(stress_data > 100)[0][0]
        end_point = np.where(stress_data > 100)[0][-1]
        margin = int(len(stress_data) * 0.1)
        data.start_point = max(start_point - margin, 0)
        data.end_point = min(end_point + margin, len(stress_data))

def make_graph(test_path, ans_path):
    test_data = CSVData(test_path)
    ans_data = CSVData(ans_path)

    data_nomalization(test_data)
    data_nomalization(ans_data)

    stress_test = test_data.get_data("stress")
    shearX_test = test_data.get_data("shearX")
    shearY_test = test_data.get_data("shearY")
    grip_test = test_data.get_data("grip")
    angle_test = test_data.get_data("angle")
    stress_ans = ans_data.get_data("stress")
    shearX_ans = ans_data.get_data("shearX")
    shearY_ans = ans_data.get_data("shearY")
    grip_ans = ans_data.get_data("grip")
    angle_ans = ans_data.get_data("angle")
    
    fig = plt.figure(figsize=(10,10))
    fig.subplots_adjust(hspace=1)

    ax1 = fig.add_subplot(5,1,1)
    ax1.plot(np.linspace(0,99,100), signal.resample(stress_ans, 100), marker="None", label="answer")
    ax1.plot(np.linspace(0,99,100), signal.resample(stress_test, 100), marker="None", label="result", lw=3)
    ax1.set_title("stress", fontsize=20)
    ax1.legend()
    
    ax2 = fig.add_subplot(5,1,2)
    ax2.plot(np.linspace(0,99,100), signal.resample(shearX_ans, 100), marker="None", label="answer")
    ax2.plot(np.linspace(0,99,100), signal.resample(shearX_test, 100), marker="None", label="result", lw=3)
    ax2.set_title("shearX", fontsize=20)
    ax2.legend()

    ax3 = fig.add_subplot(5,1,3)
    ax3.plot(np.linspace(0,99,100), signal.resample(shearY_ans, 100), marker="None", label="answer")
    ax3.plot(np.linspace(0,99,100), signal.resample(shearY_test, 100), marker="None", label="result", lw=3)
    ax3.set_title("shearY", fontsize=20)
    ax3.legend()

    ax4 = fig.add_subplot(5,1,4)
    ax4.plot(np.linspace(0,99,100), signal.resample(grip_ans, 100), marker="None", label="answer")
    ax4.plot(np.linspace(0,99,100), signal.resample(grip_test, 100), marker="None", label="result", lw=3)
    ax4.set_title("grip", fontsize=20)
    ax4.legend()

    ax5 = fig.add_subplot(5,1,5)
    ax5.plot(np.linspace(0,99,100), signal.resample(angle_ans, 100), marker="None", label="answer")
    ax5.plot(np.linspace(0,99,100), signal.resample(angle_test, 100), marker="None", label="result", lw=3)
    ax5.set_title("angle", fontsize=20)
    ax5.legend()

    return fig
    
if __name__ == "__main__":
    make_graph("log/2022_02_25_14_59.csv", "log/2022_02_25_15_00.csv")
    plt.show()