CC = g++

CPPFILE = $(wildcard *.cpp)
OBJS = $(patsubst %.cpp,%,$(CPPFILE))

all:  $(OBJS)

% : %.cpp
	$(CC) -o $@ $< -I/usr/local/include -L/usr/local/lib -lgsl -lcblas -latlas -lm
	
clean: 
	rm $(OBJS)