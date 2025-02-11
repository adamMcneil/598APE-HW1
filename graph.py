import matplotlib.pyplot as plt
import numpy as np

data_set_1 = [4.458084, 4.507959, 4.421250]
data_set_2 = [4.397300, 4.308150, 4.211561]

all_data = [data_set_1, data_set_2]

# Calculate the means and standard deviations
means = [np.mean(data) for data in all_data]
std_devs = [np.std(data) for data in all_data]

# Define categorical x-axis labels
x_labels = ["Baseline", "getLight", ]
x = np.arange(len(x_labels))  # Numeric positions for categorical labels

plt.errorbar(x, means, yerr=std_devs, capsize=5, linestyle='None', marker='^', color='red')

plt.xticks(x, x_labels)  # Set the categorical labels
plt.xlabel('Optimization Stage')
plt.ylabel('Time (sec)')
plt.title('Speed Increase')

plt.legend()
plt.grid(True)

plt.show()
