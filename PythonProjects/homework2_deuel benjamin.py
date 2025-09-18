import numpy as np
import time

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
	last_column = arr[:, -1]
	center_subarray = arr[1:3, 1:3]
	greater_than_15 = arr[arr > 15]
	arr_copy = arr.copy()
	arr_copy -= (arr_copy+1) * (arr_copy%2==1) #if odd, all is multiplied by 0, nothing is changed. if even, subtract by (val + 1) * 1, making -1
	return third_row, last_column, center_subarray, greater_than_15, arr_copy

def problem4():
	#each row is a student's scores
	scores = np.array([[85, 90, 78, 92], [79, 85, 88, 91], [92, 88, 95, 89], [75, 72, 80, 78], [88, 91, 87, 94]])
	student_averages = scores.mean(axis=1)
	test_averages = scores.mean(axis=0)
	student_max_scores = scores.max(axis=1)
	test_std = scores.std(axis=0)
	high_performers = student_averages > 85
	return student_averages, test_averages, student_max_scores, test_std, high_performers

def problem5():
	size = 100000
	python_list = list(range(size))
	numpy_array = np.arange(size)
	
	start_time = time.time()
	list_result = [ x**2 for x in python_list ]
	list_time = time.time() - start_time
	
	start_time = time.time()
	array_result = numpy_array ** 2
	numpy_time = time.time() - start_time
	
	speedup = list_time / numpy_time
	return { 'list_time': list_time, 'numpy_time': numpy_time, 'speedup': speedup, 'conclusion': f"NumPy is {speedup:.1f}x faster than Python lists for this operation" }

def bonus_challenge():
	image = np.random.randint(0, 256, size=(10, 10))
	normalized = image / 255
	brightened = np.clip(image + 50, a_min = 0, a_max = 255)
	negative = image - 255
	thresholded = (image > 128) * 255
	return normalized, brightened, negative, thresholded

if __name__ == "__main__":
	print("Problem 1 Results:")
	print(problem1())
	print("\nProblem 2 Results:")
	print(problem2())
	print("\nProblem 3 Results:")
	print(problem3())
	print("\nProblem 4 Results:")
	print(problem4())
	print("\nProblem 5 Results:")
	print(problem5())
	print("\nBonus Challenge Results:")
	print(bonus_challenge())
	input()