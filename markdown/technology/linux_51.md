- [一、安装交叉编译工具](#一安装交叉编译工具)
- [二、建立烧写环境](#二建立烧写环境)
- [三、提升USB访问权限](#三提升usb访问权限)
- [四、代码编译](#四代码编译)
- [五、烧写](#五烧写)

## 一、安装交叉编译工具
（1）安装SDCC（shell下编译工具）
方法1（shell）：sudo apt-get install sdcc
方法2（软件管理器）：搜索sdcc并安装
（2）或安装MCU8051 IDE
方法（软件管理器）：搜索MCU8051并安装

## 二、建立烧写环境
安装烧写工具
（1）安装stcflash
下载stcflash： 网址(http://github.com/laborer/stcflash)，用python写的向单片机烧写bin文件的脚本
解压进入stcflash的目录，shell执行以下命令
vi stcflash.py
然后将首行#!/usr/bin/env python修改为#!/usr/bin/env python3
mv stcflash.py stcflash
sudo mv stcflash /usr/local/bin


1、检测系统是否安装python（ubuntu默认装的是3）终端命令解释器：python3 --version
2、检测通过跳到下一步，否则终端命令解释器安装python3：sudo apt install python3
3、检测系统是否安装pip3（pip3是 Python3包管理工具，该工具提供了对Python3包的查找、下载、安装、卸载的功能，shell）：pip3 --version
4、检测通过跳到下一步，否则shell安装pip3：sudo apt install python3-pip
5、shell安装pyserial库：pip3 install pyserial
6、检测USB转串口设备的支持：lsmod | grep usbserial
7、USB转串口不通过则安装CH340驱动：

    CH340LINUX驱动下载地址：http://www.wch.cn/download/CH341SER_LINUX_ZIP.html
    下载后进行解压，得到ch34x.c,makefile,readme三个文件

    cd CH341SER_LINUX 跳转文件夹下编译

    sudo make 进行编译，会出现一大堆文件，有.ko,.o等
    sudo make load 到这里就完成了，然后通过

如直接make之后显示两个错误：

1. ch34x.c:591:2: error: unknown type name ‘wait_queue_t’ 2. error: implicit declaration of function ‘signal_pending’ [-Werror=implicit-function-declaration]

第591行 wait_queue_t wait 这个变量没有用到，直接注释即可，然后缺少一个头文件，添加 #include <linux/sched/signal.h> 。

make load 加载驱动即可。

## 三、提升USB访问权限
使用USB口,串口之类启动时容易出现:/dev/ttyUSB0 permission denied.原因为不是root用户，对端口没有权限．
用下面这条指令：
sudo usermod -a -G dialout user_name
用户名加入dialout用户组，然后注销电脑．这样以后不用修改权限了
*实测不好用，改为 chmod 666 /dev/ttyS4*

## 四、代码编译
方法1：
SDCC（shell）：sdcc text.c

生成的文件：
test.lk test.map test.rel test.sym test.asm test.ihx test.lst test.mem test.rst

*.asm – 由编译器产生的汇编源文件。
*.lst – 由汇编器产生的汇编列表文件。
*.rst – 由连接器产生的汇编列表文件，里面含有连接信息记录。
*.sym – 源文件的符号列表，由汇编器产生。
*.rel 或 *.o – 由汇编器产生的目标文件，供连接器来使用。
*.map – 读入模块的内存映射表，由连接器产生。
*.mem – 记录存储器使用的摘要。
*.ihx – intel hex格式的文件（可以使用--out-fmts19选项来选择Motorola S19输出格式）。
*.adb – 一个包含调试信息的中间文件，产生.cdb文件必须依赖这些中间文件来实现（使用--debug选项）。
*.cdb – 一个可选的包含调试信息的调试文件，在链接时使用选项--debug就会产生这个文件。
* – 一个可选的包含调试信息的AOMF或者AOMF51文件（由选项--debug产生）。整个目标模块格式是OMF51格式的子格式并且一般被第三方工具使用（调试器，模拟器）。
*.dump* -- 打印文件调试编译器本身（选项为 –dumpall）

只需要其中的 test.ihx

packihx file.ihx >file.hex 转换为hex文件

接着下载hex2bin文件，网址(http://sourceforge.net/projects/hex2bin/files/latest/download)
命令：hex2bin test.hex  转换为bin文件

## 五、烧写
1、shell查看本机的串口：python3 -m serial.tools.list_ports
2、shell读取单片机信息：stcflash

启动时出现:Connect to /dev/ttyUSB0 at baudrate 2400
Detecting target...
断电再上电无相应，则指定芯片类型
shell读取单片机信息：stcflash --protocol 12c52

Protocol	                                                       MCUs
89         
	                              STC89C52RC (v4.3C), STC89C54RD+ (v4.3C), STC90C52RC (v4.3C)
12cx052	                              STC12C2052 (v5.8D)
12c52	                              STC12C5608AD (v6.0G), STC12C5204AD (v6.0H)
12c5a	                              STC10F04XE (v6.5J), STC12C5A16S2 (v6.2I), STC11F02E (v6.5K)
 
3、shell烧写：sudo stcflash test.bin


