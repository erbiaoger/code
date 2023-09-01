

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep


aa = []
fig, ax = plt.subplots()
for i in range(100):
    ax.cla()
    y = np.sin(i)
    aa.append(y)
    if len(aa) > 10:
        ax.plot(aa[-10:])
        #sleep(0.1)
        
        plt.pause(0.1)
    

# %%
import matplotlib.pyplot as plt

depth_end = 200.
freqs_end = 10.

X, y = next(iter(test_iter))
yyy = model(X)
j = 11

true_v = 100*y[j][0][0].detach().numpy()
syn_v = 100*yyy[j][0][0].detach().numpy()
depth = torch.linspace(0, depth_end, len(true_v))
freq = torch.linspace(0, freqs_end, len(true_v))


with plt.style.context('ggplot'):

    # 创建图形和坐标轴对象
    fig, ax = plt.subplots(figsize=(6, 8))

    ax.plot(true_v, depth, label='true', color='tab:red')
    ax.plot(syn_v, depth, label= 'syn', color='tab:green')


    # 设置 y 轴刻度方向
    ax.yaxis.tick_left()
    #ax.yaxis.set_label_position('top')
    ax.set_xlabel('depth [m]')
    ax.set_ylabel('true velocity [m/s]')
    # 设置坐标轴位置
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    ax.set_ylim([0, 200])
    ax.set_xlim([80, 920])
    ax.legend(loc='lower left')
    ax.set_title('Velocity Model')

    # 反转y轴
    ax.invert_yaxis()
    #plt.show()

    # model_sm = np.apply_along_axis(smooth,1,model,window_len=71, window='blackman')
    # model_smb = fil.gaussian_filter(model_sm,sigma=0.8)

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep


aa = []
x = np.linspace(0, 2 * np.pi, 120)
with plt.style.context('ggplot'):

    # 创建图形和坐标轴对象
    fig, ax = plt.subplots(figsize=(6, 8))

    for i in range(100):

        ax.cla()
        y = np.sin(x + i)
        aa.append(y)
        if len(aa) > 10:
            ax.imshow(aa[-10:])
            #sleep(0.1)
            
            plt.pause(0.1)
        
# %%
