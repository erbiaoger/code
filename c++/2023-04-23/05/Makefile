CC = g++

CPPFILE = $(wildcard *.cpp)
OBJS = $(patsubst %.cpp,%.so,$(CPPFILE))

all:  $(OBJS)

%.so : %.cpp
	$(CC) -shared -fPIC $< -o $@

clean: 
	rm $(OBJS)