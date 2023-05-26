"""
This is a sample script to plot figure.

Author: Zhang Zhiyu
Email: erbiaoger@gmail.com
Created: 2023/4/9 10:52
Version: 0.0.1

Description:
- Draw in svg format
- Bringing drawing functions together

Usage:
import mytools.plot as plot
def f(x): return 3 * x ** 2 - 4 * x
x =np.arange(0, 3, 0.1)
plot(x, [f(x), 2*x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])

Change Log:
- April 10, 2023, added a new data processing function
- April 11, 2023, fixed a bug
"""

from matplotlib_inline import backend_inline 
import matplotlib.pyplot as plt

def use_svg_display(): 
    """使用svg格式在Jupyter中显示绘图"""
    backend_inline.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)):
    """设置matplotlib的图表大小"""
    use_svg_display()
    plt.rcParams['figure.figsize'] = figsize

def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
    """设置matplotlib的轴"""
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend:
        axes.legend(legend)
    axes.grid()

def plot(X, Y=None, xlabel=None, ylabel=None, legend=None, xlim=None,
         ylim=None, xscale='linear', yscale='linear', 
         fmts=('-', 'm--', 'g-', 'r:'), figsize=(3.5, 2.5), axes=None):
    """绘制数据点
    
    Attributes
    ----------
    X, Y : ndarray
        Vector of frequencies corresponds to each column.
    xlabel, ylabel : ndarray
        Vector of frequencies corresponds to each column.
    legend : list
        List of strings for the legend.
    xlim, ylim : ndarray
        Vector of frequencies corresponds to each column.
    xscale, yscale : ndarray
        Vector of frequencies corresponds to each column.
    fmts : list
        List of strings for the legend.
    figsize : ndarray
        Vector of frequencies corresponds to each column.
    axes : ndarray
        Vector of frequencies corresponds to each column.
    
    """
    if legend is None:
        legend = []
    
    set_figsize(figsize)
    axes = axes if axes else plt.gca()

    # 如果X有一个轴，输出True
    def has_one_axes(X):
        return (hasattr(X, 'ndim') and X.ndim == 1 or isinstance(X, list)
                and not hasattr(X[0], '__len__'))
        
    if has_one_axes(X):
        X = [X]
    if Y is None:
        X, Y = [[]] * len(X), X
    elif has_one_axes(Y):
        Y = [Y]
    if len(X) != len(Y):
        X = X * len(Y)
    axes.cla()
    for x, y, fmt in zip(X, Y, fmts):
        if len(x):
            axes.plot(x, y, fmt)
        else:
            axes.plot(y, fmt)
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)


# Test
# def f(x): return 3 * x ** 2 - 4 * x
# x =np.arange(0, 3, 0.1)
# plot(x, [f(x), 2*x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])
