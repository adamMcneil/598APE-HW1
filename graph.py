import matplotlib.pyplot as plt
import numpy as np

data_set_1 = [4.458084, 4.507959, 4.421250]
data_set_2 = [4.397300, 4.308150, 4.211561]
data_set_3 = [3.571864, 3.484238, 3.449706]
data_set_4 = [3.219148, 2.905530, 2.932814]
data_set_5 = [2.970248, 2.89260, 2.941668]
data_set_6 = [2.798702, 2.780181, 2.757088]
macros = [2.652793, 2.621943,2.578901]

all_data = [data_set_1, data_set_2, data_set_3, data_set_4, data_set_5, data_set_6, macros]

# Calculate the means and standard deviations
means = [np.mean(data) for data in all_data]
std_devs = [np.std(data) for data in all_data]

# Define categorical x-axis labels
x_labels = ["Baseline", "getLight", "calcColor", "getIntersection", "solveScaler", "calcColor", "macros"]
x = np.arange(len(x_labels))  # Numeric positions for categorical labels

plt.errorbar(x, means, yerr=std_devs, capsize=5, linestyle='None', marker='^', color='red')

plt.xticks(x, x_labels)  # Set the categorical labels
plt.xlabel('Optimization Stage')
plt.ylabel('Time (sec)')
plt.title('Speed Increase')

plt.legend()
plt.grid(True)

plt.show()
