CC = g++

CPPFILE = $(wildcard *.cpp)
OBJS = $(patsubst %.cpp,%.so,$(CPPFILE))
PYFILE = $(patsubst %.cpp, %.py, $(CPPFILE))

all:  $(PYFILE) $(OBJS) 

%.so : %.cpp %.py
	$(CC) -I/home/erbiaoger/miniconda3/include/python3.9/ -shared -fPIC $< -o $@
	python $*.py


clean: 
	rm $(OBJS)