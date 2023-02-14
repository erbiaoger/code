# coding: utf-8

def cartesian():

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
