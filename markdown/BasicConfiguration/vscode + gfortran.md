<!--
This is a sample markdown to demonstrate how to configurate vscode and gfortran.

Author: Zhang Zhiyu
Email: erbiaoger@gmail.com
Created: 2023/4/10 11:12
Version: 1.0.0
-->
参考：
[My Gfortran in VS Code](https://mp.weixin.qq.com/s/DMZWzNgUJH9oRTX4xnh4lA)
[GDB 入门教程](https://oi.men.ci/gnu-debugger/)
[进击的VS code（一）——对付上古语言Fortran](https://zhuanlan.zhihu.com/p/362664913)

- [环境配置](#环境配置)
- [插件](#插件)
- [插件配置](#插件配置)
- [测试](#测试)


## 环境配置
1. fortran 
```python
sudo apt install build-essential
sudo apt install gdb
```
2. setuptools
```python
pip3 install -U setuptools
```
3. fortran-language-server
```python
pip3 install fortran-language-server
```
4. 找到 `forls`
```sh
which fortls
which gdb

<<< /home/erbiaoger/miniconda3/bin/fortls
<<< /usr/bin/gdb
```

## 插件
1. fortran
2. Modern Fortran
3. My Fortran Setting
4. FORTRAN intelliSense
5. Fortran Breakpoint Support
6. GDB Debugger
7. Code Runner
8. C/C++
![](https://raw.githubusercontent.com/erbiaoger/PicGo/main/20230404/202304101059310.png)

## 插件配置
1. 在 `settings.json` 中设置
```json
"fortran.linter.includePaths": [
	"/Users/zhangzhiyu/miniconda3/bin/"
],
"code-runner.saveFileBeforeRun": true,
"code-runner.defaultLanguage": "fortran",
"code-runner.runInTerminal": true,
"fortran-ls.executablePath": "/home/erbiaoger/miniconda3/bin/fortls",
"files.associations": {
	"*.f90": "fortran-modern"
},
"debug.allowBreakpointsEverywhere": true,
```
![](https://raw.githubusercontent.com/erbiaoger/PicGo/main/20230404/202304101103302.png)
2. `launch.json` 设置
```json
{
	"version": "0.2.0",
	"preLaunchTask": "build",
	"configurations": [
		{
			"name": "Fortran Debug",
			"type": "cppdbg",
			"request": "launch",
			"targetArchitecture": "arm64",
			"program": "${workspaceRoot}/${fileBasenameNoExtension}",
			"miDebuggerPath": "/usr/bin/gdb",
			"cwd": "${workspaceRoot}",
			"preLaunchTask": "gfortran",
		}
	]
}
```
3. `tasks.json`设置
```json
{
	"version": "2.0.0",
	"command": "gfortran",
	"args": [
		"-g",
		"${fileBasenameNoExtension}.f90",
		"-o",
		"${workspaceRoot}/${fileBasenameNoExtension}"
	]
}
```

## 测试
![](https://raw.githubusercontent.com/erbiaoger/PicGo/main/20230404/202304101312847.gif)