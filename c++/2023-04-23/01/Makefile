# 指定编译器
CC = g++

# 指定编译选项
FFLAGS = -O2 -Wall

# 指定源代码文件和目标文件所在的目录
SRCDIR = src
BINDIR = bin
DOCDIR = doc
INCDIR = include

# 获取源代码文件和目标文件
SRCS = $(wildcard $(SRCDIR)/*.cpp)
OBJS = $(patsubst $(SRCDIR)/%.cpp,$(BINDIR)/%.o,$(SRCS))

# 指定生成的可执行文件名
EXEC = my_program

# all 为默认的目标，即直接运行 make 命令时执行的目标
all: $(BINDIR)/$(EXEC)

# 可执行文件的生成规则
$(BINDIR)/$(EXEC): $(OBJS)
	$(CC) $(OBJS) -o $@

# 目标文件的生成规则
$(BINDIR)/%.o: $(SRCDIR)/%.cpp
	$(CC) -c $< -I$(INCDIR) -o $@


# 清除中间文件的规则
clean:
	rm -f $(BINDIR)/*.o $(BINDIR)/$(EXEC)


