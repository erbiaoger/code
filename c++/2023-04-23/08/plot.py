import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('plot.dat')

for i in range(data.shape[1]):
    plt.plot(data[:, i])

plt.savefig('plot.svg', dpi=800, format='svg', bbox_inches='tight')