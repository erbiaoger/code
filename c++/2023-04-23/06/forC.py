from ctypes import *

# 使用CXX加载库文件
forC = CDLL('./forC.o', RTLD_GLOBAL, use_errno=True, use_last_error=True)

forC.forC()
