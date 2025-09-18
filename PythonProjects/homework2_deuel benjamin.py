import numpy as np

np.random.seed(1350)

def problem1():
    arr1 = np.arange(10, 55, 5)
    arr2 = np.zeros((3, 4))
    identity = np.identity(3)
    linspace_arr = np.linspace(0, 5, 10)
    random_arr = np.random.random((2, 5))
    return arr1, arr2, identity, linspace_arr, random_arr

def problem2():
    arr_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    arr_b = np.array([10, 20, 30])
    result_add = arr_a + arr_b
    result_multiply = arr_a * arr_b
    result_square = arr_a ** 2
    column_means = np.mean(arr_a, axis=0)
    centered_arr = arr_a - column_means.T
    return result_add, result_multiply, result_square, column_means, centered_arr

def problem3():
    arr = np.arange(1, 26).reshape(5, 5)
    third_row = arr[2]
    last_column = arr[:, :-1]
    center_subarray = arr[1:3, 1:3]