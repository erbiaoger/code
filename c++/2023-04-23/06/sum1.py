import ctypes

# Load the shared library
lib = ctypes.CDLL("./sum1.so")

# Define the argument and return types of the function
lib.sum.argtypes = [ctypes.c_int, ctypes.c_int]
lib.sum.restype = ctypes.c_int

# Call the C++ function and get the result
x = 10
y = 20
result = lib.sum(x, y)

# Print the result
print(result)
