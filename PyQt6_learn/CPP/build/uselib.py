# from ctypes import *

# # mycalcu = CDLL('./libforA.dylib')

# # #a = mycalcu.add(10)

# # #print(a)

# # print(mycalcu.forA(1))

# forB = CDLL('./libforB.dylib')
# print(forB)
# print(forB.forB())

from ctypes import *

# 使用CXX加载库文件
forB = CDLL('./libforB.dylib', RTLD_GLOBAL, use_errno=True, use_last_error=True)

# 设置函数的返回类型和参数类型
forB.forB.restype = None
forB.forB.argtypes = []

# 调用函数
forB.forB()
