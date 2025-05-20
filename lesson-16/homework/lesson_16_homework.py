import numpy as np

# 1. Convert List to 1D Array
lst = [12.23, 13.32, 100, 36.32]
arr1 = np.array(lst)
print("1. Convert List to 1D Array:", arr1)

# 2. Create 3x3 Matrix (2 to 10)
arr2 = np.arange(2, 11).reshape(3, 3)
print("\n2. 3x3 Matrix (2 to 10):\n", arr2)

# 3. Null Vector (10) & Update Sixth Value
arr3 = np.zeros(10)
arr3[5] = 11
print("\n3. Null Vector with Sixth Value Updated:", arr3)

# 4. Array from 12 to 38
arr4 = np.arange(12, 38)
print("\n4. Array from 12 to 38:", arr4)

# 5. Convert Array to Float Type
arr5 = np.array([1, 2, 3, 4])
arr5_float = arr5.astype(float)
print("\n5. Convert Array to Float:", arr5_float)

# 6. Celsius to Fahrenheit Conversion
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = (celsius * 9/5) + 32
print("\n6. Celsius to Fahrenheit:")
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
# Reverse conversion for verification
celsius_back = (fahrenheit - 32) * 5/9
print("Back to Celsius:", celsius_back)

# 7. Append Values to Array
arr7 = np.array([10, 20, 30])
arr7 = np.append(arr7, [40, 50, 60, 70, 80, 90])
print("\n7. Append Values to Array:", arr7)

# 8. Array Statistical Functions
arr8 = np.random.rand(10)
mean = np.mean(arr8)
median = np.median(arr8)
std_dev = np.std(arr8)
print("\n8. Array Statistics:")
print("Array:", arr8)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# 9. Find Min and Max
arr9 = np.random.rand(10)
min_val = np.min(arr9)
max_val = np.max(arr9)
print("\n9. Find Min and Max:")
print("Array:", arr9)
print("Min:", min_val)
print("Max:", max_val)

# 10. Create 3x3x3 Array with Random Values
arr10 = np.random.rand(3, 3, 3)
print("\n10. 3x3x3 Array with Random Values:\n", arr10)