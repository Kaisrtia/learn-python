import numpy as np

arr_by_list = np.array([1, 2, 3, 4, 5])
# print(arr_by_list[1:4:2])

arr_by_tuple = np.array((1, 2, 3, 4, 5))

arr_0d = np.array(42)

arr_1d = np.array([1, 2, 3, 4, 5])

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr_2d[0, 2])

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr_3d.ndim) 

arr = np.array([1, 2, 3, 4, 5], ndmin=5)

arr = np.array([1, 2, 3, 4], dtype='U') # dtype='S' like char
# print(arr)

arr = np.array([0, 1.2, 2.3, 3.4], dtype='f') # error
# print(arr)

new_arr = arr.astype('i') # convert to int
# print(new_arr)

x = arr.view()
x[0] = 24
# print(arr)
# print(x.base, arr.base) # None if the array owns its data 

arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(arr.reshape(4, 3).base)
new_arr = arr.reshape(4, 3)
# print(new_arr)
new_arr = arr.reshape(3, 2, -1)
# print(new_arr)

# for x in np.nditer(new_arr, flags=['buffered'], op_dtypes=['U']):
#   print(x, end=', ')

# for idx, x in np.ndenumerate(new_arr):
#   print(idx, x)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.stack((arr1, arr2), axis=2)
# print(arr)

arr = np.array([1, 2, 3, 4, 5])
# print(np.array_split(arr, 3))

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# print(np.array_split(arr, 3, axis=1))

arr = np.array([1, 2, 3, 4, 5, 4, 4, 3, 2, 2, 1, 5])
# print(np.where(arr == 4))

arr = np.array([1, 2, 3, 3, 3, 4, 5])
# print(np.searchsorted(arr, 4))

filter_arr = arr > 3
print(filter_arr)
print(arr[filter_arr])