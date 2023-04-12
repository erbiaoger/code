### 自省

`?`的使用

在变量后使用 `?` 可以查看变量信息

```python
b = [1, 2, 3]
?b
```

结果

```python
Type:        list
String form: [1, 2, 3]
Length:      3
Docstring:  
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
```

也可在函数和方法之后使用

```python
def add_numbers(a, b):
    """
    Add two numbers together
    Returns
    -------
    the_sum : type of arguments
    """
    return a + b

add_numbers?
```

结果

```python
Signature: add_numbers(a, b)
Docstring:
Add two numbers together
Returns
-------
the_sum : type of arguments
File:      /var/folders/sl/483mjxsd5wn00k1lbpr591jm0000gn/T/ipykernel_41262/1674744173.py
Type:      function
```

使用 `??` 可以显示源码

```python
add_numbers??
```

结果

```python
Signature: add_numbers(a, b)
Source:   
def add_numbers(a, b):
    """
    Add two numbers together
    Returns
    -------
    the_sum : type of arguments
    """
    return a + b
File:      /var/folders/sl/483mjxsd5wn00k1lbpr591jm0000gn/T/ipykernel_41262/1674744173.py
Type:      function
```



### %run

使用 `%run` 可以像在命令行内执行 python 程序, 如有以下 sum.py 

```python
def sum(a, b):
    return a + b

a = 1
b = 3
c = sum(a, b)
print(c)
```

![](https://raw.githubusercontent.com/erbiaoger/PicGo/main/img202209051006599.png)

文件中所有定义的变量(import、函数和全局变量，除非抛出异常)，都可以在IPython shell中随后访问:

![](https://raw.githubusercontent.com/erbiaoger/PicGo/main/img202209051013607.png)

### 魔术命令

魔术命令可以被看做IPython中运行的命令行。许多魔术命令有“命令行”选项，可以通过?查看:

![](https://raw.githubusercontent.com/erbiaoger/PicGo/main/img202209051023172.png)

如 `%load sum.py`, `%time sum()`

![](https://raw.githubusercontent.com/erbiaoger/PicGo/main/img202209051027514.png)
