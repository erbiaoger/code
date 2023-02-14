# coding: utf-8
import os

import math
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist #导入坐标轴加工模块
def cartesian():
    """
    笛卡尔坐标系
    """
    fig=plt.figure(figsize=(8, 6)) #新建画布
    ax=axisartist.Subplot(fig,111) #使用axisartist.Subplot方法创建一个绘图区对象ax
    fig.add_axes(ax) #将绘图区对象添加到画布中

    #fig.title("$tanh\ x = \frac{e^x - e^{-x}}{e^x + e^{-x}}$")
    ax.axis[:].set_visible(False) #隐藏原来的实线矩形

    ax.axis["x"]=ax.new_floating_axis(0,0,axis_direction="bottom") #添加x轴
    ax.axis["y"]=ax.new_floating_axis(1,0,axis_direction="bottom") #添加y轴
    ax.axis["x"].set_axisline_style("->",size=1.0) #给x坐标轴加箭头
    ax.axis["y"].set_axisline_style("->",size=1.0) #给y坐标轴加箭头

    ax.annotate(text='x' ,xy=(10, 0) ,xytext=(10.5, -0.07)) #标注x轴
    ax.annotate(text='y' ,xy=(0, 1.0) ,xytext=(-0.5, 1.0)) #标注y轴
    ax.set_xticks([-10, -5, 0, 5, 10]) #设置x轴刻度
    ax.set_yticks([-1, -0.5, 0.5, 1]) #设置y轴刻度
## Plot tanh x
tanh = lambda y: (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

x = np.linspace(-10, 10, 1000)
y = tanh(x)

cartesian()

plt.title(r"$tanh\ x = \frac{e^x - e^{-x}}{e^x + e^{-x}}$")
plt.plot(x, y, color='red', label='tanh x')
plt.legend()
plt.savefig("tanhx.png")
## Plot simgmoid(x)
sigmoid = lambda y: 1 / (1 + np.exp(-x))

x = np.linspace(-10, 10, 1000)
y = sigmoid(x)

cartesian()

plt.title(r"$sigmoid(x) = \frac{1}{1 + e^{-x}}$")
plt.plot(x, y, color='red', label='sigmoid(x)')
plt.legend()
plt.savefig("sigmoid(x).png")
## Plot ReLU
x = np.linspace(-10, 10, 1000)
y = np.maximum(0, x)

fig=plt.figure(figsize=(8, 6)) #新建画布
ax=axisartist.Subplot(fig,111) #使用axisartist.Subplot方法创建一个绘图区对象ax
fig.add_axes(ax) #将绘图区对象添加到画布中

ax.axis[:].set_visible(False) #隐藏原来的实线矩形

ax.axis["x"]=ax.new_floating_axis(0,0,axis_direction="bottom") #添加x轴
ax.axis["y"]=ax.new_floating_axis(1,0,axis_direction="bottom") #添加y轴
ax.axis["x"].set_axisline_style("->",size=1.0) #给x坐标轴加箭头
ax.axis["y"].set_axisline_style("->",size=1.0) #给y坐标轴加箭头

ax.annotate(text='x' ,xy=(10, 0) ,xytext=(10.5, -0.07)) #标注x轴
ax.annotate(text='y' ,xy=(0, 10.0) ,xytext=(-0.5, 10.0)) #标注y轴
ax.set_xticks([-10, -5, 0, 5, 10]) #设置x轴刻度
ax.set_yticks([-1, -0.5, 5, 10]) #设置y轴刻度

plt.title("relu(x)")
plt.plot(x, y, color='red', label='relu(x)')
plt.legend()
plt.savefig("relu.png")
