



# %%
import numpy as np
import matplotlib.pyplot as plt

nt = 250
nx = 100
aa = np.zeros((nt, nx))
for i in range(nt):
    aa[i] = 1000

aa[100] += 10000
aa[150, 50:70] = 0
aa[200] += 10000
np.save('aa.npy',aa)
    

# %%
import h5py
import numpy as np
with h5py.File('aa.h5', 'w') as f:
    aa = np.load('aa.npy')
    f['aa'] = aa

with h5py.File('aa.h5', 'r') as f:
    print(f.keys())
    aa = f['aa'][:]
    print(aa.shape)
# %%

import numpy as np
import matplotlib.pyplot as plt

#aa = np.load('aa.npy')
dt = 1e-2
dx = 10
disp_nt = 100
disp_dt = 0.1

speed = 0.25 # 1x 2x 3x 0.5x 0.25x

nt = np.arange(disp_nt, len(aa), disp_dt/dt * speed)

# with plt.style.context('ggplot'):
fig, ax = plt.subplots(figsize=(6, 8))
for i in nt:
    ax.cla()

    ax.imshow(aa[int(i-disp_nt): int(i)], aspect='auto', cmap='rainbow', \
            origin='lower', extent=[0, nx*dx, 0, disp_nt*dt])
    ax.set_xlabel('distance [m]')
    ax.set_ylabel('time [s]')
    ax.set_title('time = {:.2f}s'.format(i*dt))
    plt.pause(disp_dt)
