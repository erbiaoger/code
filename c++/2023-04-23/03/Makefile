CC = g++

CPPFILE = $(wildcard *.cpp)
OBJS = $(patsubst %.cpp,%,$(CPPFILE))

all:  $(OBJS)

%.o : %.cpp
	$(CC) $< -o $@

clean: 
	rm $(OBJS)