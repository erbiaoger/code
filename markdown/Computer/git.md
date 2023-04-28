# Learn Git
<!--
![git 结构](https://raw.githubusercontent.com/erbiaoger/PicGo/main/image/202303192139836.jpg)

![git 工作流程](https://raw.githubusercontent.com/erbiaoger/PicGo/main/image/202303192139707.png)
-->
- [ Learn Git](#-learn-git)
  - [基础操作](#基础操作)
    - [创建仓库命令](#创建仓库命令)
  - [提交与修改](#提交与修改)
    - [提交日志](#提交日志)
    - [远程操作](#远程操作)
    - [初始化仓库](#初始化仓库)
    - [提交文件到缓存区](#提交文件到缓存区)
    - [提交文件到](#提交文件到)
    - [查看提交状态](#查看提交状态)
  - [查看提交记录](#查看提交记录)
    - [查看提交记录](#查看提交记录-1)
    - [查看历史命令](#查看历史命令)
  - [版本回退](#版本回退)
    - [**--soft** ](#--soft)
    - [**--hard** ](#--hard)
    - [**HEAD 说明：**](#head-说明)
    - [git reset HEAD](#git-reset-head)


## 基础操作


### 创建仓库命令

下表列出了 git 创建仓库的命令：

|命令|说明|
|--|--|
|git init|初始化仓库|
|git clone|拷贝一份远程仓库，也就是下载一个项目。|

---

## 提交与修改

Git 的工作就是创建和保存你的项目的快照及与之后的快照进行对比。

下表列出了有关创建与提交你的项目的快照的命令：

|命令|说明|
|--|--|
|git add | 添加文件到暂存区|
|git status|查看仓库当前的状态，显示有变更的文件。|
|git diff|比较文件的不同，即暂存区和工作区的差异。|
|git commit|提交暂存区到本地仓库。|
|git reset|回退版本。|
|git rm|将文件从暂存区和工作区中删除。|
|git mv|移动或重命名工作区文件。

---
### 提交日志

|命令|说明|
|--|--|
|git log|查看历史提交记录|
|git blame|以列表形式查看指定文件的历史修改记录|

---
### 远程操作

|命令|说明|
|--|--|
|git remote|远程仓库操作|
|git fetch|从远程获取代码库|
|git pull|下载远程代码并合并|
|git push|上传远程代码并合并|

---

### 初始化仓库
```shell
>>> git init
```
### 提交文件到缓存区
```shell
>>> git add Readme.md
```
### 提交文件到
```shell
>>> git commit -m "提交 Readme.md"
```
### 查看提交状态
```shell
>>> git status
```
## 查看提交记录
### 查看提交记录
```shell
>>> git log

commit dc6c15dd9ab48f2d2bc220621c6a857af9e7502b (HEAD -> master)
Author: zhangzhiyu <zhangzhiyu@zhangzhiyudeMac-mini.local>
Date:   Sun Mar 19 21:20:14 2023 +0800

    添加 utils.py 一些工具

commit 54dcd9d458c96e33d575adc0c95433c54df7b758
Author: zhangzhiyu <zhangzhiyu@zhangzhiyudeMac-mini.local>
Date:   Sun Mar 19 21:17:46 2023 +0800

    添加 ellipticity.ipynb 椭圆率

commit 13624c975d5048e59114df70c53a5d97c067b7ab
Author: zhangzhiyu <zhangzhiyu@zhangzhiyudeMac-mini.local>
Date:   Sun Mar 19 21:15:02 2023 +0800

    添加 InSight_Data_Processing.ipynb

commit 29dfd24f6d73fa74e4cb583e5853220936a7402c
Author: zhangzhiyu <zhangzhiyu@zhangzhiyudeMac-mini.local>
Date:   Sun Mar 19 20:52:57 2023 +0800

    新建 InSight 数据处理仓库
```
### 查看历史命令
```shell
>>> git reflog

dc6c15d (HEAD -> master) HEAD@{0}: commit: 添加 utils.py 一些工具
54dcd9d HEAD@{1}: commit (amend): 添加 ellipticity.ipynb 椭圆率
1460265 HEAD@{2}: commit: 添加 ellipticity.ipynb 椭圆率
13624c9 HEAD@{3}: commit (amend): 添加 InSight_Data_Processing.ipynb
24b730a HEAD@{4}: commit: 添加 InSight_Data_Processing.ipynb
29dfd24 HEAD@{5}: commit (initial): 新建 InSight 数据处理仓库
```

## 版本回退
```shell
>>> git reset [--soft | --mixed | --hard] [HEAD]
```

### **--soft** 
	参数用于回退到某个版本
```shell
>>> git reset --soft HEAD~3   # 回退上上上一个版本
```

### **--hard** 
	参数撤销工作区中所有未提交的修改内容，将暂存区与工作区都回到上一次版本，并删除之前的所有信息提交：
```shell
>>> git reset --hard HEAD~3  # 回退上上上一个版本 
>>> git reset –-hard bae128  # 回退到某个版本回退点之前的所有信息。
>>> git reset --hard origin/master    # 将本地的状态回退到和远程的一样
```
**注意：**谨慎使用 **–-hard** 参数，它会删除回退点之前的所有信息。

### **HEAD 说明：**

-   HEAD 表示当前版本
    
-   HEAD^ 上一个版本
    
-   HEAD^^ 上上一个版本
    
-   HEAD^^^ 上上上一个版本
    
-   以此类推...
    

可以使用 ～数字表示

-   HEAD~0 表示当前版本
    
-   HEAD~1 上一个版本
    
-   HEAD^2 上上一个版本
    
-   HEAD^3 上上上一个版本
    
-   以此类推...

### git reset HEAD

git reset HEAD 命令用于取消已缓存的内容
