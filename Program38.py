# Generate random temperature data and plot histogram

import numpy as np
import matplotlib.pyplot as plt

# Generate random temperature data (in °C)
# 100 values between 20°C and 40°C
temps = np.random.randint(20, 41, 100)

print("Temperature Data:\n", temps)
# Output: Array of 100 random values between 20 and 40 (values will vary)

# Plot histogram
plt.hist(temps, bins=10)

# Add title and labels
plt.title("Temperature Distribution")   # Output: Title displayed
plt.xlabel("Temperature (°C)")         # Output: X-axis label
plt.ylabel("Frequency")                # Output: Y-axis label

# Show grid
plt.grid()                             # Output: Grid lines shown

# Display plot
plt.show()                             # Output: Histogram displayed