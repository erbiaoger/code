代码变成可执行文件，叫做编译（compile）；先编译这个，还是先编译那个（即编译的安排），叫做构建（build）。

## 一、Make 的格式

Makefile文件由一系列**规则**（rules）构成。每条规则的形式如下。
```bash
<target> : <prerequisites> 
[tab]  <commands>
```

上面第一行冒号前面的部分，叫做"目标"（target），冒号后面的部分叫做"前置条件"（prerequisites）；第二行必须由一个tab键起首，后面跟着"命令"（commands）。

每条规则就明确两件事：构建目标的前置条件是什么，以及如何构建。

### 2.2 目标(target)

一个目标（target）就构成一条规则。目标通常是文件名，指明Make命令所要构建的对象。目标可以是一个文件名，也可以是多个文件名，之间用空格分隔。

除了文件名，目标还可以是某个操作的名字，这称为"伪目标"（phony target）。
```bash
clean:
      rm *.o
```

上面代码的目标是clean，它不是文件名，而是一个操作的名字，属于"伪目标 "，作用是删除对象文件。
```bash
$ make  clean
```

但是，如果当前目录中，正好有一个文件叫做clean，那么这个命令不会执行。因为Make发现clean文件已经存在，就认为没有必要重新构建了，就不会执行指定的rm命令。

为了避免这种情况，可以明确声明clean是"伪目标"，写法如下。
```bash
.PHONY: clean
clean:
        rm *.o temp
```

如果Make命令运行时没有指定目标，默认会执行Makefile文件的第一个目标。

### 2.3 前置条件（prerequisites）

前置条件通常是**一组文件名**(也可以是目标)，之间用空格分隔。它指定了"目标"是否重新构建的判断标准：只要有一个前置文件不存在，或者有过更新（前置文件的last-modification时间戳比目标的时间戳新），"目标"就需要重新构建。
```shell
result.txt: source.txt
	cp source.txt result.txt
```

上面代码中，构建 result.txt 的前置条件是 source.txt 。如果当前目录中，source.txt 已经存在，那么`make result.txt`可以正常运行，否则必须再写一条规则，来生成 source.txt 。
```bash
source.txt:
    echo "this is the source" > source.txt
```

### 2.4 命令（commands）

命令（commands）表示如何更新目标文件，由一行或多行的Shell命令组成

需要注意的是，每行命令在一个单独的shell中执行。这些Shell之间没有继承关系。
```bash
var-lost:
    export foo=bar
    echo "foo=[$$foo]"
```

上面代码执行后（`make var-lost`），取不到foo的值。因为两行命令在两个不同的进程执行。一个解决办法是将两行命令写在一行，中间用分号分隔。
```bash
var-kept:
    export foo=bar; echo "foo=[$$foo]"
```

另一个解决办法是在换行符前加反斜杠转义。
```bash
var-kept:
    export foo=bar; \
    echo "foo=[$$foo]"
```

最后一个方法是加上`.ONESHELL:`命令。
```bash
.ONESHELL:
var-kept:
    export foo=bar; 
    echo "foo=[$$foo]"
```

## 三、Makefile文件的语法

### 3.2 回声（echoing）

正常情况下，make会打印每条命令，然后再执行，这就叫做回声（echoing）
```bash
test:
    # 这是测试
```

在命令的前面加上@，就可以关闭回声。
```bash
test:
    @# 这是测试
```

### 3.4 模式匹配

Make命令允许对文件名，进行类似正则运算的匹配，主要用到的匹配符是%。比如，假定当前目录下有 f1.c 和 f2.c 两个源码文件，需要将它们编译为对应的对象文件。
```bash
%.o: %.c
```

### 3.5 变量和赋值符

Makefile 允许使用等号自定义变量。
```bash
txt = Hello World
test:
    @echo $(txt)
```
上面代码中，变量 txt 等于 Hello World。调用时，变量需要放在 $( ) 之中。

调用Shell变量，需要在美元符号前，再加一个美元符号，这是因为Make命令会对美元符号转义。
```bash
test:
    @echo $$HOME
```

### 3.6 内置变量（Implicit Variables）

Make命令提供一系列内置变量，比如，$(CC) 指向当前使用的编译器，$(MAKE) 指向当前使用的Make工具。这主要是为了跨平台的兼容性

```bash
output:
    $(CC) -o output input.c
```

### 3.7 自动变量（Automatic Variables）
Make命令还提供一些自动变量，它们的值与当前规则有关。主要有以下几个。
#### 1. $@

``$@`` 指代当前目标，就是Make命令当前构建的那个目标。
```bash
a.txt b.txt: 
    touch $@
```
等同于下面的写法。
```bash
a.txt:
    touch a.txt
b.txt:
    touch b.txt
```

#### 2. $<

`$<` 指代第一个前置条件。比如，规则为 t: p1 p2，那么`$<` 就指代p1。
```bash
a.txt: b.txt c.txt
    cp $< $@ 
```
等同于下面的写法。
```bash
a.txt: b.txt c.txt
    cp b.txt a.txt 
```

**（3）$?**

$? 指代比目标更新的所有前置条件，之间以空格分隔。比如，规则为 t: p1 p2，其中 p2 的时间戳比 t 新，$?就指代p2。

**（4）$^**

$^ 指代所有前置条件，之间以空格分隔。比如，规则为 t: p1 p2，那么 $^ 就指代 p1 p2 。

**（5）$***

`$*`指代匹配符% 匹配的部分， 比如% 匹配 f1.txt 中的f1 ，$* 就表示 f1。

**（6）$(@D) 和 $(@F)**

$(@D) 和 $(@F) 分别指向 $@ 的目录名和文件名。比如，$@是 src/input.c，那么$(@D) 的值为 src ，$(@F) 的值为 input.c。

#### 重点
```shell
objects = *.o
```
上面这个例子，表示了通配符同样可以用在变量中。并不是说 `*.o` 会展开，不！objects的值就是 `*.o` 。Makefile中的变量其实就是C/C++中的宏。如果你要让通配符在变量中展开，也就是让objects的值是所有 `.o` 的文件名的集合，那么，你可以这样：
```shell
objects := $(wildcard *.o)
```

### vpath

在一些大的工程中，有大量的源文件，我们通常的做法是把这许多的源文件分类，并存放在不同的目录中。所以，当make需要去找寻文件的依赖关系时，你可以在文件前加上路径，但最好的方法是把一个路径告诉make，让make在自动去找。

Makefile文件中的特殊变量 `VPATH` 就是完成这个功能的，如果没有指明这个变量，make只会在当前的目录中去找寻依赖文件和目标文件。如果定义了这个变量，那么，make就会在当前目录找不到的情况下，到所指定的目录中去找寻文件了
```shell
VPATH = src
print1: f_array.f90
	@cat src/f_array.f90
```

另一个设置文件搜索路径的方法是使用make的“vpath”关键字（注意，它是全小写的），这不是变量，这是一个make的关键字，这和上面提到的那个VPATH变量很类似，但是它更为灵活。它可以指定不同的文件在不同的搜索目录中
```shell
vpath %.f90 src
print1: f_array.f90
	@cat src/f_array.f90
```

```shell
vpath <pattern> <directories>
# 为符合模式<pattern>的文件指定搜索目录<directories>。

vpath <pattern>
# 清除符合模式<pattern>的文件的搜索目录。

vpath
# 清除所有已被设置好了的文件搜索目录。
```

### 伪目标

“伪目标”并不是一个文件，只是一个**标签**。为了避免和文件重名的这种情况，我们可以使用一个特殊的标记“.PHONY”来显式地指明一个目标是“伪目标”，向make说明，不管是否有这个文件，这个目标就是“伪目标”
```shell
all : prog1 prog2 prog3
.PHONY : all clean

prog1 : prog1.o utils.o
    cc -o prog1 prog1.o utils.o

prog2 : prog2.o
    cc -o prog2 prog2.o

prog3 : prog3.o sort.o utils.o
    cc -o prog3 prog3.o sort.o utils.o

clean :
    rm *.o temp
```

### 多目标

```shell
bigoutput littleoutput : text.g
    generate text.g -$(subst output,,$@) > $@
```
上述规则等价于：
```shell
bigoutput : text.g
    generate text.g -big > bigoutput
littleoutput : text.g
    generate text.g -little > littleoutput
```

其中， `-$(subst output,,$@)` 中的 `$` 表示执行一个Makefile的函数，函数名为subst，后面的为参数。关于函数，将在后面讲述。这里的这个函数是替换字符串的意思， `$@` 表示目标的集合，就像一个数组， `$@` 依次取出目标，并执于命令。