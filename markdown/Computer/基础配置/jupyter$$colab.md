# Jupyter && Colab

参照：

https://dummerfu.top/p/64572.html

## $ colab 实现本地连接

### $ 安装 jupyter

```bash
conda install noteboo
```

### $ `启用jupyter_http_over_ws jupyter 扩展程序（连接到本地需要`

```bash
pip install jupyter_http_over_ws jupyter serverextension enable --py jupyter_http_over_ws
```

### $ 启动jupyter 最后一行参数是为了挂载到本地后能打开自己的文件

虽然缺乏安全性，但是是最快解决403的方法，有时间再找找其他替代方案

```bash
jupyter notebook \\
  --NotebookApp.allow_origin='<https://colab.research.google.com>' \\
  --port=8888 \\
  --NotebookApp.port_retries=0 \\
  --NotebookApp.disable_check_xsrf=True
```

## $ 优化

### 生成配置文件

```shell
jupyter notebook --generate-config
cd .jupyter
vim jupyter_config.py
```

### 更改参数

```python
c.NotebookApp.allow_origin='<https://colab.research.google.com>'
c.port=8888
c.NotebookApp.port_retries=0
c.NotebookApp.disable_check_xsrf=True
 
c.Notebook_dir='/Users/erbiaoger/DAS'	# 更改自己的工作路径
```

### 更改token

因为每次连接到本地运行都要输入token，可以将token设置为固定值也相当于password了

不过这样运行的时候命令行里面不会显示token具体值

```python
c.NotebookApp.token='http://localhost:8888/?token=erbiaoger'
```

### 取消自动重定向

每次打开一个new tab很烦人~~我又不用jupyter写代码~~

```python
c.NotebookApp.open_browser = False
```

### 后台运行

```python

# 在上述命令的最后加一个 & ，则该命令产生的进程在后台运行，不会影响当前终端的使用（我们在只有一个bash的环境下）。
# ctrl c之后还在运行，但是关掉窗口就会停止
jupyter notebook &

# 在命令的开头加一个nohup，忽略所有的挂断信号，如果当前bash关闭，则当前进程会挂载到init进程下，成为其子进程，这样即使退出当前bash，其8000端口也可以使用。
nohup jupyter notebook &
```





## Jupyter notebook 插件

### 1. 安装并激活 **jupyter_contrib_nbextensions**，

```shell 
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
pip install jupyter_contrib_nbextensions 
jupyter contrib nbextension install --user
```

### 2. 安装并启用 **Jupyter Nbextensions Configurator**

```shell
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```



```shell
 ssh -NL 8888:localhost:8891 zhangzhiyu
 
 
```

