## 在服务器端部署 Jupyter Notebook

### 1. 生成配置文件

 ```shell
 jupyter-notebook --generate-config
 ```

### 2. 生成密码

使用 `ipython`

```python 
form notebook.auth import passwd
passwd()
```

### 3. 修改配置文件

```shell
c.NotebookApp.ip='当前服务器IP'
c.NotebookApp.password = u'sha1:......'
c.NotebookApp.notebook_dir = u'/root/jpynotebook'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8899
c.NotebookApp.allow_root = True
```

### 4. 使用`nohup`启动服务

```shell
nohup jupyter-notebook
```

### 5. 在本地浏览器输入`http://服务器地址IP:8899`

