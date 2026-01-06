import numpy as np
def add_arrays(arr1, arr2):
    return np.add(arr1, arr2)

if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = add_arrays(a, b)
    print("Result of addition:", result)
