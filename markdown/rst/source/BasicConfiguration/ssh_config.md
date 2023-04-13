# ssh config

> 在 .ssh 文件夹下makedir config

```bash
Host erbiaoger
	HostName 192.168.124.9
	User erbiaoger
	Port 22 

Host zhangzhiyu
	HostName 222.27.79.19
	User zhangzhiyu
	Port 22 


```

## 1. 生成密钥和公钥

```shell
ssh-keygen -t rsa
```

## 2. 上传公钥

```shell
ssh-copy-id -i ~/.ssh/id_rsa.pub zhangzhiyu@222.27.79.19
```

