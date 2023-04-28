[TOC]

## C++ 编译

### 有两个以上源文件应该一下编译

```shell
g++   foo1.cpp   foo2.cpp   -o   foo
```

也可以分步实现:

```shell
g++   -c   foo1.cpp  -o   foo1.o
g++   -c    foo2.cpp  -o   foo2.o
g++   foo1.o  foo2.o    -o    foo
```

### GCC一些常用选项

1、产生警告信息的选项大多数以`-W`开头  其中有`-Wall`

```shell
g++  -Wall  hello.cpp   -o   hello
```

2、将所有的警告当成错误的选项`-Werror`

```shell
g++ -Werror  hello.cpp  -o  hello
```

3、寻找头文件选项 

- ```
  -I
  ```

   (linux默认路径：头文件在 `/usr/include/` 下)，不在这个路径下就要用`-I`指定。

  ```shell
  gcc  foo.cpp  -I/home/include   -o  foo
  ```

  4、 库依赖选项 

- ```
  -L
  ```

   (linux默认路径：库文件在 `/usr/lib/` 下)，不在这个路径下就要用`-L`指定。

  ```shell
  g++  foo.cpp  -L/home/lib  -lfoo  -o   foo
  ```

库就是将源文件编译之后生成的目标文件的集合。库命名以lib开头。库有静态库(通常以`.a`结尾)和动态库(通常以`.so`结尾)默认情况下，g++以动态库形式连接。如果要静态库连接则要用`-static`指定(`g++ foo.cpp  -L/home/lib  -static  -lfoo  -o  foo`)

### 编译预处理

选项 `-E` 使 g++ 将源代码用编译预处理器处理后不再执行其他动作。下面的命令预处理源码文件 `helloworld.cpp` 并将结果显示在标准输出中：

```shell
$ g++ -E helloworld.cpp
```

本文前面所列出的 `helloworld.cpp` 的源代码，仅仅有六行，而且该程序除了显示一行文字外什么都不做，但是，预处理后的版本将超过 `1200` 行。这主要是因为头文件 iostream 被包含进来，而且它又包含了其他的头文件，除此之外，还有若干个处理输入和输出的类的定义。
预处理过的文件的 GCC 后缀为`.ii`，它可以通过`-o` 选项来生成，例如：
```shell
$ gcc -E helloworld.cpp -o helloworld.ii
```

### 生成汇编代码

选项 -S指示编译器将程序编译成汇编语言，输出汇编语言代码而后结束。下面的命令将由 C++ 源码文件生成汇编语言文件 `helloworld.s`：
```shell
$ g++ -S helloworld.cpp
```

生成的汇编语言依赖于编译器的目标平台。

### 创建静态库


GCC(GNU Compiler Collection)是Linux下最主要的编译工具，GCC不仅功能非常强大，结构也异常灵活。它可以通过不同的前端模块来支持各种语言，如：Java、Fortran、Pascal、Modula-3和Ada。

**安装Gcc和g++：**
```shell
yum -y install gcc automake autoconf libtool make
```

**安装g++:**
```shell
yum install gcc gcc-c++
```

g++是GCC中的一个工具，专门来编译C++语言的。
GCC的参数有：( 也是分步实现)
- ```
  -E
  ```

    让GCC在预处理结束后停止编译。

  ```shell
  g++ -E hello.cpp  -o  hello.i
  ```

`-c`将`hello.i`编译成目标代码
  ```shell
  g++  -c  hello.i  -o  hello.o
  ```
  
  将目标文件连接成可执行文件
  ```shell
  g++ hell.o   -o   hello
  ```
  
  可以一步实现
  ```shell
  g++  hello.cpp  -o  hello
  ```


### 多个源文件生成可执行程序

如果多于一个的源码文件在 g++ 命令中指定，它们都将被编译并被链接成一个单一的可执行文件。下面是一个名为 `speak.h` 的头文件；它包含一个仅含有一个函数的类的定义：

```cpp
/* speak.h */
#include <iostream>
class Speak
{
    public:
        void sayHello(const char *);
};
```

下面列出的是文件 `speak.cpp` 的内容：包含 `sayHello()`函数的函数体：

```cpp
/* speak.cpp */
#include "speak.h"
void Speak::sayHello(const char *str)
{
    std::cout << "Hello " << str << "\n";
}
```

文件`hellospeak.cpp`内是一个使用 `Speak` 类的程序：

```cpp
/* hellospeak.cpp */
#include "speak.h"
int main(int argc,char *argv[])
{
    Speak speak;
    speak.sayHello("world");
    return(0);
}
```

下面这条命令将上述两个源码文件编译链接成一个单一的可执行程序：

```shell
$ g++ hellospeak.cpp speak.cpp -o hellospeak
```

> 提示： 这里说一下为什么在命令中没有提到“`speak.h`“文件(原因是：在“`speak.cpp`“中包含有”`#include"speak.h`““这句代码，它的意思是搜索系统头文件目录之前将先在当前目录中搜索文件“`speak.h`“。而”`speak.h`“正在该目录中，不用再在命令中指定了)。

### 源文件生成对象文件

选项 `-c` 用来告诉编译器编译源代码但不要执行链接，输出结果为对象文件。文件默认名与源码文件名相同，只是将其后缀变为`.o`。例如，下面的命令将编译源码文件 `hellospeak.cpp`并生成对象文件 `hellospeak.o`：

```shell
$ g++ -c hellospeak.cpp
```

命令 g++ 也能识别 `.o` 文件并将其作为输入文件传递给链接器。下列命令将编译源码文件为对象文件并将其链接成单一的可执行程序：

```shell
$ g++ -c hellospeak.cpp 
$ g++ -c speak.cpp 
$ g++ hellospeak.o speak.o -o hellospeak
```

选项 `-o` 不仅仅能用来命名可执行文件。它也用来命名编译器输出的其他文件。例如：除了中间的对象文件有不同的名字外，下列命令生将生成和上面完全相同的可执行文件：

```shell
$ g++ -c hellospeak.cpp -o hspk1.o 
$ g++ -c speak.cpp -o hspk2.o 
$ g++ hspk1.o hspk2.o -o hellospeak
```

### 编译预处理

选项 `-E` 使 g++ 将源代码用编译预处理器处理后不再执行其他动作。下面的命令预处理源码文件 `helloworld.cpp` 并将结果显示在标准输出中：

```shell
$ g++ -E helloworld.cpp
```

本文前面所列出的 `helloworld.cpp` 的源代码，仅仅有六行，而且该程序除了显示一行文字外什么都不做，但是，预处理后的版本将超过 `1200` 行。这主要是因为头文件 iostream 被包含进来，而且它又包含了其他的头文件，除此之外，还有若干个处理输入和输出的类的定义。
预处理过的文件的 GCC 后缀为`.ii`，它可以通过`-o` 选项来生成，例如：

```shell
$ gcc -E helloworld.cpp -o helloworld.ii
```

### 生成汇编代码

选项 -S指示编译器将程序编译成汇编语言，输出汇编语言代码而后结束。下面的命令将由 C++ 源码文件生成汇编语言文件 `helloworld.s`：

```shell
$ g++ -S helloworld.cpp
```

生成的汇编语言依赖于编译器的目标平台。

### 创建静态库

静态库是编译器生成的一系列对象文件的集合。链接一个程序时用库中的对象文件还是目录中的对象文件都是一样的。库中的成员包括普通函数，类定义，类的对象实例等等。静态库的另一个名字叫归档文件(archive)，管理这种归档文件的工具叫 `ar` 

在下面的例子中，我们先创建两个对象模块，然后用其生成静态库。
头文件 `say.h`包含函数 `sayHello()`的原型和类 `Say` 的定义：

```cpp
/* say.h */
#include <iostream>
void sayhello(void);
class Say {
    private:
        char *string;
    public:
        Say(char *str)
        {
            string = str;
        }
        void sayThis(const char *str)
        {
            std::cout << str << " from a static library\n";
        }
        void sayString(void);
};
```

下面是文件`say.cpp`是我们要加入到静态库中的两个对象文件之一的源码。它包含 `Say` 类中 `sayString()`函数的定义体；类 `Say` 的一个实例 `librarysay`的声明也包含在内：

```cpp
/* say.cpp */
#include "say.h"
void Say::sayString()
{
    std::cout << string << "\n";
}
```

`Say librarysay("Library instance of Say");`
源码文件 `syshello.cpp` 是我们要加入到静态库中的第二个对象文件的源码。它包含函数 `sayhello()` 的定义：

```cpp
/* sayhello.cpp */
#include "say.h"
void sayhello()
{
    std::cout << "hello from a static library\n";
}


C++
```

下面的命令序列将源码文件编译成对象文件，命令 ar 将其存进库中：

```shell
$ g++ -c sayhello.cpp
$ g++ -c say.cpp
$ ar -r libsay.a sayhello.o say.o
```

程序 `ar` 配合参数 `-r` 创建一个新库 `libsay.a` 并将命令行中列出的对象文件插入。采用这种方法，如果库不存在的话，参数 `-r` 将创建一个新的库，而如果库存在的话，将用新的模块替换原来的模块。
下面是主程序 `saymain.cpp`，它调用库 `libsay.a` 中的代码：

```cpp
/* saymain.cpp */
#include "say.h"
int main(int argc,char *argv[])
{
    extern Say librarysay;
    Say localsay = Say("Local instance of Say");
    sayhello();
    librarysay.sayThis("howdy");
    librarysay.sayString();
    localsay.sayString();
    return(0);
}
```

该程序可以下面的命令来编译和链接：

```
$ g++ saymain.cpp libsay.a -o saymain
```

程序运行时，产生以下输出：

```
hello from a static library
howdy from a static library
Library instance of SayLocal instance of Say
```

## C++变量

![819210326_89576](https://raw.githubusercontent.com/erbiaoger/PicGo/main/20230404/202304231556856.png)

| 类型 | 数据类型 |
| :-: | :-: |
|  基本数据类型(Basic) |`int`, `char`, `float`, `double`等 |
| 派生数据类型(Derived)| 数组, 指针等 |
| 枚举数据类型(Enumeration)| 枚举(`enum`)|
|  用户定义的数据类型(User Defined) |结构体 |

## C++关键字
关键字是保留字。我们不能将其用作变量名称，常量名称等。下面给出了C语言中可用的C++语言中的32个关键字列表。

|auto|break|case|char|const|continue|default|do|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|double|else|enum|extern|float|for|goto|if|
|int|long|register|return|short|signed|sizeof|static|
|struct|switch|typedef|union|unsigned|void|volatile|while|

下面给出了在C语言中不可用的30个C++语言关键字的列表。

|asm|dynamic_cast|namespace|reinterpret_cast|bool|
|:-:|:-:|:-:|:-:|:-:|
|explicit|new|static_cast|false|catch|
|operator|template|friend|private|class|
|this|inline|public|throw|const_cast|
|delete|mutable|protected|true|try|
|typeid|typename|using|virtual|wchar_t|

## C++存储类

存储类用于定义C++程序中变量和/或函数的生命周期和可见性。

寿命是指变量保持活动的时间段，可见性是指可访问变量的程序的模块。

有五种类型的存储类，可以在C++程序中使用

- 自动(Automatic)
- 寄存器(Register)
- 静态(Static)
- 外部(External)
- 可变(Mutable)

| 存储类 | 关键字   | 生命周期 | 可见性 | 初始值 |
| ------ | -------- | -------- | ------ | ------ |
| 自动   | auto     | 函数块   | 局部   | 垃圾   |
| 寄存器 | register | 函数块   | 局部   | 垃圾   |
| 可变   | mutable  | 类       | 局部   | 垃圾   |
| 静态   | static   | 整个程序 | 全局   | 零     |
| 外部   | extern   | 整个程序 | 局部   | 零     |

### 自动存储类

它是所有局部变量的默认存储类。 `auto`关键字自动应用于所有局部变量。

```cpp
{   
    auto int y;  
    float y = 3.45;  
}
```

上面的例子定义了两个具有相同存储类的变量，`auto`只能在函数中使用。

### 注册存储类

寄存器变量在寄存器中分配存储器而不是`RAM`。 其大小与寄存器大小相同。 它比其他变量具有更快的访问速度。
建议仅使用寄存器变量进行快速访问，例如:在计数器中。

> **注意**：我们不能得到寄存器变量的地址。

```cpp
register int counter=0;
```

### 静态存储类

静态变量只初始化一次，直到程序结束。 它保留可在多个函数之间调用的值。
静态变量由编译器提供的一个默认值：`0`。

```cpp
#include <iostream>  
using namespace std;  
void func() {    
    static int i=0; //static variable    
    int j=0; //local variable    
    i++;    
    j++;    
    cout<<"i=" << i<<" and j=" <<j<<endl;    
}    
int main()  
{  
    func();    
    func();    
    func();    
}
```

执行上面代码，得到以下结果 -

```cpp
i= 1 and j= 1
i= 2 and j= 1
i= 3 and j= 1
```

### 外部存储类

`extern`变量对所有程序都可见。 如果两个或多个文件共享相同的变量或函数，则使用它。

```cpp
extern int counter=0;
```

## C++数组 				 				 			
像其他编程语言一样，C++中的数组是一组具有连续内存位置的类似类型的元素。在C++中`std ::array`是一个封装固定大小数组的容器。 在C++中，数组索引从0开始。我们可以在C++数组中只存储固定的元素集合。

![693210322_27822](https://raw.githubusercontent.com/erbiaoger/PicGo/main/20230404/202304232118226.png)

### C++数组示例：使用foreach循环遍历

我们也可以使用foreach循环遍历数组元素。 它一个一个返回数组中的元素。

```cpp
#include <iostream>  
using namespace std;  
int main()  
{  
    int arr[5]={10, 0, 20, 0, 30}; //creating and initializing array    
    //traversing array    
    for (int i: arr)     
    {    
        cout<<i<<"\n";    
    }
    return 0;
}
```

## C++ this指针

​					 				 				 				 			

在C++编程中，`this`是一个引用类的当前实例的关键字。 `this`关键字在C++中可以有`3`个主要用途。

1. 用于将当前对象作为参数传递给另一个方法。
2. 用来引用当前类的实例变量。
3. 用来声明索引器。

```c++
#include <iostream>  
using namespace std;  
class Employee {  
   public:  
       int id; //data member (also instance variable)      
       string name; //data member(also instance variable)  
       float salary;  
       Employee(int id, string name, float salary)    
        {    
             this->id = id;    
            this->name = name;    
            this->salary = salary;   
        }    
       void display()    
        {    
            cout<<id<<"  "<<name<<"  "<<salary<<endl;    
        }    
};  
int main(void) {  
    Employee e1 =Employee(101, "Hema", 890000); //creating an object of Employee   
    Employee e2=Employee(102, "Calf", 59000); //creating an object of Employee  
    e1.display();    
    e2.display();    
    return 0;  
}
```

## C++ static关键字					 				 				 				 		
在C++中，`static`是属于类而不是实例的关键字或修饰符。 因此，不需要实例来访问静态成员。 在C++中，`static`可以是字段，方法，构造函数，类，属性，操作符和事件。

**C++ static关键字的优点**

**内存效率：** 现在我们不需要创建实例来访问静态成员，因此它节省了内存。 此外，它属于一种类型，所以每次创建实例时不会再去获取内存。

使用`static`关键字声明字段称为静态字段。它不像每次创建对象时都要获取内存的实例字段，在内存中只创建一个静态字段的副本。它被共享给所有的对象。

```c++
#include <iostream>  
using namespace std;  
class Account {  
   public:  
       int accno; //data member (also instance variable)      
       string name;   
       static int count;     
       Account(int accno, string name)   
        {    
             this->accno = accno;    
            this->name = name;    
            count++;  
        }    
       void display()    
        {    
            cout<<accno<<" "<<name<<endl;   
        }    
};  
int Account::count=0;  
int main(void) {  
    Account a1 =Account(201, "Sanjay"); //creating an object of Account  
    Account a2=Account(202, "Calf");   
     Account a3=Account(203, "Ranjana");  
    a1.display();    
    a2.display();    
    a3.display();    
    cout<<"Total Objects are: "<<Account::count;  
    return 0;  
}
```

## C++结构体			 				 				 				 			
在C++中，类和结构体(`struct`)是用于创建类的实例的蓝图(或叫模板)。结构体可用于轻量级对象，如矩形，颜色，点等。

## C++枚举

C++中的枚举是一种包含固定常量的数据类型。

枚举可以用于星期几(`SUNDAY`，`MONDAY`，`TUESDAY`，`WEDNESDAY`，`THURSDAY`，`FRIDAY`和`SATURDAY`)，方向(`NORTH`，`SOUTH`，`EAST`和`WEST`等)。C++枚举常量是静态和最终隐式。

C++枚举可以认为是具有固定的常量集合的类。

**C++中枚举注意事项**

- 枚举提高了类型安全性
- 枚举可以很容易地在`switch`语句块中使用
- 枚举可以遍历
- 枚举可以有字段，构造函数和方法
- 枚举可以实现许多接口，但不能扩展任何类，因为它在内部扩展`Enum`类

```c++
#include <iostream>
using namespace std;

enum week {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday};

int main() {
    week day;
    day = Friday;
    cout << "Day: " << day+1 << endl;
    return 0;
}
```

```shell
Day: 5
```

## C++友元函数

如果一个函数在C++中定义为一个友元(使用`friend`作为修辞符)函数，那么可以使用该函数访问类的`protected`和`private`数据。

通过使用`friend`关键字，编译器知道给定的函数是一个友元函数。为了访问数据，友元函数的声明应该在以关键字`friend`开头的类的主体内部进行

```c++
#include <iostream>  
using namespace std;  
class Box  
{  
    private:  
        int length;  
    public:  
        Box(): length(0) { }  
        friend int printLength(Box); //friend function  
};  
int printLength(Box b)  
{  
    b.length += 10;  
    return b.length;  
}  
int main()  
{  
    Box b;  
    cout<<"Length of box: "<< printLength(b)<<endl;  
    return 0;  
}
```

## C++文件和流

在C++编程中，我们使用`iostream`标准库，它提供了`cin`和`cout`方法，分别从输入和输出读取流。

要从文件读取和写入，我们使用名称为`fstream`的标准C++库。 下面来看看看在`fstream`库中定义的数据类型是：

| 数据类型   | 描述                                               |
| ---------- | -------------------------------------------------- |
| `fstream`  | 它用于创建文件，向文件写入信息以及从文件读取信息。 |
| `ifstream` | 它用于从文件读取信息。                             |
| `ofstream` | 它用于创建文件以及写入信息到文件。                 |

## C++ FileStream示例：写入文件

下面来看看看使用C++ FileStream编程写一个定稿文本文件：`testout.txt`的简单例子。

```cpp
#include <iostream>  
#include <fstream>  
using namespace std;  
int main () {  
  ofstream filestream("testout.txt");  
  if (filestream.is_open())  
  {  
    filestream << "Welcome to javaTpoint.\n";  
    filestream << "C++ Tutorial.\n";  
    filestream.close();  
  }  
  else cout <<"File opening is fail.";  
  return 0;  
}
```

执行上面代码，输出结果如下 -

```cpp
The content of a text file testout.txt is set with the data:
Welcome to javaTpoint.
C++ Tutorial.
```

### C++ FileStream示例：从文件读取

下面来看看看使用C++ `FileStream`编程从文本文件`testout.txt`中读取的简单示例。

```cpp
#include <iostream>  
#include <fstream>  
using namespace std;  
int main () {  
  string srg;  
  ifstream filestream("testout.txt");  
  if (filestream.is_open())  
  {  
    while ( getline (filestream,srg) )  
    {  
      cout << srg <<endl;  
    }  
    filestream.close();  
  }  
  else {  
      cout << "File opening is fail."<<endl;   
    }  
  return 0;  
}
```

**注意：**在运行代码之前，需要创建一个名为“`testout.txt`”的文本文件，并且文本文件的内容如下所示：

```bash
Welcome to Yiibai.com.
C++ Tutorial.
```

执行上面代码输出结果如下 -

```cpp
Welcome to Yiibai.com.
C++ Tutorial.
```

### C++读写示例

下面来看看一个简单的例子，将数据写入文本文件：`testout.txt`，然后使用C++ FileStream编程从文件中读取数据。

```cpp
#include <fstream>  
#include <iostream>  
using namespace std;  
int main () {  
   char input[75];  
   ofstream os;  
   os.open("testout.txt");  
   cout <<"Writing to a text file:" << endl;  
   cout << "Please Enter your name: ";   
   cin.getline(input, 100);  
   os << input << endl;  
   cout << "Please Enter your age: ";   
   cin >> input;  
   cin.ignore();  
   os << input << endl;  
   os.close();  
   ifstream is;   
   string line;  
   is.open("testout.txt");   
   cout << "Reading from a text file:" << endl;   
   while (getline (is,line))  
   {  
   cout << line << endl;  
   }      
   is.close();  
   return 0;  
}
```

## C++重载

如果创建两个或多个成员(函数)具有相同的名称，但参数的数量或类型不同，则称为C++重载。 在C++中，我们可以重载：

- 方法
- 构造函数
- 索引属性

这是因为这些成员只有参数。

**C++中的重载类型有：**

- 函数重载
- 运算符重载

### C++函数重载

在C++中，具有两个或更多个具有相同名称但参数不同的函数称为**函数重载**。

函数重载的优点是它增加了程序的可读性，不需要为同一个函数操作功能使用不同的名称。

**C++函数重载示例**

下面来看看看函数重载的简单例子，修改了`add()`方法的参数数量。

```cpp
#include <iostream>  
using namespace std;  
class Cal {  
    public:  
static int add(int a,int b){    
        return a + b;    
    }    
static int add(int a, int b, int c)    
    {    
        return a + b + c;    
    }    
};   
int main(void) {  
    Cal C;  
    cout<<C.add(10, 20)<<endl;    
    cout<<C.add(12, 20, 23);   
   return 0;  
}
```

### C++操作符重载

操作符重载用于重载或重新定义C++中可用的大多数操作符。 它用于对用户定义数据类型执行操作。

运算符重载的优点是对同一操作数执行不同的操作。

**C++操作符重载示例**

下面来看看看在C++中运算符重载的简单例子。 在本示例中，定义了`void operator ++ ()`运算符函数(在`Test`类内部)。

```cpp
#include <iostream>  
using namespace std;  
class Test  
{  
   private:  
      int num;  
   public:  
       Test(): num(8){}  
       void operator ++()   
       {   
          num = num+2;   
       }  
       void Print() {   
           cout<<"The Count is: "<<num;   
       }  
};  
int main()  
{  
    Test tt;  
    ++tt;  // calling of a function "void operator ++()"  
    tt.Print();  
    return 0;  
}
```

## C++命名空间		 				 				 				 			

C++中的命名空间用于组织项目中的类，以方便处理应用程序结构。

对于访问命名空间的类，我们需要使用`namespacename::classname`。 可以使用 `using` 关键字，所以不必一直使用完整的名称。

在C++中，全局命名空间是根命名空间。 `global::std`总是引用C++ 框架的命名空间“`std`”。

### C++命名空间示例

下面来看看看包含变量和函数的命名空间的一个简单例子。

```cpp
#include <iostream>  
using namespace std;  
namespace First {    
    void sayHello() {   
        cout<<"Hello First Namespace"<<endl;          
    }    
}    
namespace Second  {    
    void sayHello() {   
        cout<<"Hello Second Namespace"<<endl;   
    }    
}   
int main()  
{  
    First::sayHello();  
    Second::sayHello();  
    return 0;  
}
```

执行上面代码，得到以下结果 -

```cpp
Hello First Namespace
Hello Second Namespace
```



