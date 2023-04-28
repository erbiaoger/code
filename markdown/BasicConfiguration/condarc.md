```bash
auto_activate_base: true

# channels:
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/fastai/
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
#   - conda-forge
# show_channel_urls: true
# ssl_verify: false

channels:
  - conda-forge
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.bfsu.edu.cn/anaconda
default_channels:
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/main
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/free
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/r
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/pro
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud
  msys2: https://mirrors.bfsu.edu.cn/anaconda/cloud
  bioconda: https://mirrors.bfsu.edu.cn/anaconda/cloud
  menpo: https://mirrors.bfsu.edu.cn/anaconda/cloud
  pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.bfsu.edu.cn/anaconda/cloud

# channels:
#   - conda-forge
#   - defaults
#   - defaults
# show_channel_urls: true
# default_channels:
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
#   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
# custom_channels:
#   conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
#   msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
#   bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
#   menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
#   pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
#   pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
#   simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

```



```shell
>>>$	conda create -n Python2 python=2.7

<<<$ PackagesNotFoundError: The following packages are not available from current channels:

  - python=2.7
```



#### 原因定位

- python 2 官方已经停止维护与更新。
- 官方仓库中已没有python2相关包
- conda默认channel检索不到python2.7导致

#### 解决方案

- 从anaconda2的配置中，查找到可用channel：`https://repo.continuum.io/pkgs/free/osx-64`
- 指定channel url更新环境即可

```shell
conda create -c 'https://repo.continuum.io/pkgs/free/osx-64' -n py2 python=2.7

```

### 使用 2to3 转换

