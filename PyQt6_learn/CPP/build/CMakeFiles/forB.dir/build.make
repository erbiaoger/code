# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/Cellar/cmake/3.26.4/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/Cellar/cmake/3.26.4/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build

# Include any dependencies generated for this target.
include CMakeFiles/forB.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/forB.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/forB.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/forB.dir/flags.make

CMakeFiles/forB.dir/forB.cpp.o: CMakeFiles/forB.dir/flags.make
CMakeFiles/forB.dir/forB.cpp.o: forB.cpp
CMakeFiles/forB.dir/forB.cpp.o: CMakeFiles/forB.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/forB.dir/forB.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/forB.dir/forB.cpp.o -MF CMakeFiles/forB.dir/forB.cpp.o.d -o CMakeFiles/forB.dir/forB.cpp.o -c /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build/forB.cpp

CMakeFiles/forB.dir/forB.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/forB.dir/forB.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build/forB.cpp > CMakeFiles/forB.dir/forB.cpp.i

CMakeFiles/forB.dir/forB.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/forB.dir/forB.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build/forB.cpp -o CMakeFiles/forB.dir/forB.cpp.s

# Object files for target forB
forB_OBJECTS = \
"CMakeFiles/forB.dir/forB.cpp.o"

# External object files for target forB
forB_EXTERNAL_OBJECTS =

libforB.dylib: CMakeFiles/forB.dir/forB.cpp.o
libforB.dylib: CMakeFiles/forB.dir/build.make
libforB.dylib: CMakeFiles/forB.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libforB.dylib"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/forB.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/forB.dir/build: libforB.dylib
.PHONY : CMakeFiles/forB.dir/build

CMakeFiles/forB.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/forB.dir/cmake_clean.cmake
.PHONY : CMakeFiles/forB.dir/clean

CMakeFiles/forB.dir/depend:
	cd /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build /Users/zhiyuzhang/MyProjects/code/PyQt6_learn/CPP/build/CMakeFiles/forB.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/forB.dir/depend

