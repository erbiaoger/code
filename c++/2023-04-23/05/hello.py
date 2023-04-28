import ctypes

# Load the shared library
lib = ctypes.CDLL("./hello.so")

# Define the argument and return types of the function
lib.print_str.argtypes = [ctypes.c_char_p]
lib.print_str.restype = None

# Call the C++ function with a Python string argument
my_string = "Hello from Python"
num = lib.print_str(my_string.encode('utf-8'))
print(num)