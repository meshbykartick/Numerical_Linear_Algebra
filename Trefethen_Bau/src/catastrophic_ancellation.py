import numpy as np
import matplotlib.pyplot as plt

# Very small x values to see cancellation effect
x_values = np.array([1e-1, 1e-3, 1e-5, 1e-7, 1e-9, 1e-11, 1e-13])

# Direct computation
direct = np.sqrt(1 + x_values) - 1

# Stable computation using conjugate
stable = x_values / (np.sqrt(1 + x_values) + 1)

# Absolute error
abs_error = np.abs(direct - stable)

# Table
print(f"{'x':>12} | {'Direct':>20} | {'Stable':>20} | {'Abs Error':>20}")
print("-"*80)
for i, x in enumerate(x_values):
    print(f"{x:12.1e} | {direct[i]:20.15e} | {stable[i]:20.15e} | {abs_error[i]:20.15e}")

# Plot
plt.figure(figsize=(8,5))
plt.loglog(x_values, abs_error, 'o-', color='red')
plt.xlabel('x (log scale)')
plt.ylabel('Absolute Error (log scale)')
plt.title('Catastrophic Cancellation: sqrt(1+x) - 1')
plt.grid(True, which="both", ls="--")
plt.show()
