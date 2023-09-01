# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax=fig.add_subplot()
def f(x, y):
    return np.sin(x+y)
x = np.linspace(0, 2 * np.pi, 120)
ims = []
for i in np.linspace(0,2,100):
    im,=ax.plot(x,f(x,i),'r')
    title= ax.text(0.5,1.05,"time = {:.2f}s".format(i), 
                    size=plt.rcParams["axes.titlesize"],
                    ha="center", transform=ax.transAxes, )
    ims.append([im,title])
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=False)
#ani.save("sin.gif",writer='pillow')
plt.show()

# %%
