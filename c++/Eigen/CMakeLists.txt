# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)

# 添加Eigen头文件
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIR})

# 项目信息
project (Demo1)

# 单个源文件的情况
# 指定生成目标
add_executable(hello_Eigen hello_Eigen.cpp)
add_executable(Matrices_Vectors Matrices_Vectors.cpp)
add_executable(comma-initializer comma-initializer.cpp)



# 多个源文件的情况
# # 查找当前目录下的所有源文件
# # 并将名称保存到 DIR_SRCS 变量
# aux_source_directory(. DIR_SRCS)
# # 指定生成目标
# add_executable(Demo ${DIR_SRCS})

