import numpy as np

print("A random 5x5 array:\n")
random = np.random.normal(size=[5, 5])
print(random)

print("\nSwapping the first and last rows of the random 5x5 array:\n")
random[[0, 4]] = random[[4, 0]]
print(random)
