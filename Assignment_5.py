# Q1
# import numpy as np
# arr = np.array([1, 2, 3, 4,5])
# print("Original array: ", arr)

# print("Addition in array: ", arr + 2)
# print("Multiplication in array: ", arr * 3)
# print("dividion in array: ", arr / 2)

# Q2(a)
# import numpy as np
# arr = np.array([1, 2, 3, 6, 4, 5])
# print(arr[::-1])

# Q2(b)
# import numpy as np
# x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
# values, counts = np.unique(x, return_counts=True)
# most_frequent = values[np.argmax(counts)]
# indices = np.where(x == most_frequent)[0]
# print("Most frequent value:", most_frequent)
# print("Indices:", indices)


# Q3
# import numpy as np
# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])
# print("Array: ", arr)
# print("first row 2nd column: ", arr[0,1])
# print("third row second column: ", arr[2,0])

# Q4
# import numpy as np
# Harshita = np.linspace(10, 100, 25)
# print("Array:")
# print(Harshita)
# print("Dimensions:", Harshita.ndim)
# print("Shape:", Harshita.shape)
# print("Total elements:", Harshita.size)
# print("Data type:", Harshita.dtype)
# print("Total bytes:", Harshita.nbytes)
# transpose_array = Harshita.reshape(25, 1)
# print("Transpose using reshape:")
# print(transpose_array)
# transpose_T = Harshita.reshape(25, 1).T
# print("Transpose using T:")
# print(transpose_T)



# Q5
# import numpy as np
# arr = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 15, 20, 35]
# ])
# print("Original Array:")
# print(arr)
# print("Mean:", np.mean(arr))
# print("Median:", np.median(arr))
# print("Maximum:", np.max(arr))
# print("Minimum:", np.min(arr))
# print("Unique Elements:", np.unique(arr))
# reshaped_arr = arr.reshape(4, 3)
# print("Reshaped Array:")
# print(reshaped_arr)
# resized_arr = np.resize(arr, (2, 3))
# print("Resized Array:")
# print(resized_arr)