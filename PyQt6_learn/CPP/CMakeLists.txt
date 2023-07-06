project(Main)
#add_executable(signal signal.cpp)
add_library(forA SHARED forA.cpp)
add_executable(main main.cpp forA.h)
add_library(forB SHARED forB.cpp)
# 添加链接库
target_link_libraries(main forA)