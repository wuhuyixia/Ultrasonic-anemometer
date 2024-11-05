import numpy as np
from matplotlib import pyplot as plt

# Generate data points with noise
x = np.linspace(1, 100, 100)
y = 0.01 * x**2 - x + 123
y += np.random.randn(len(x))

# Plot original data
plt.plot(x, y, label='original')

# Apply FIR filter
y2 = np.zeros((100))
y2[0] = y[0]
y2[99] = y[99]
for i in range(98):
    y2[i+1] = (y[i] + y[i+1] + y[i+2]) / 3
y2 += 10

# Plot filtered data using FIR
plt.plot(x, y2, label='FIR')

# Apply IIR filter
for i in range(98):
    y[i+1] = (y[i] + y[i+1] + y[i+2]) / 3
y += 20

# Plot filtered data using IIR
plt.plot(x, y, label='IIR')

# Show legend and plot
plt.legend()
plt.show()