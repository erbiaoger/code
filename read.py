import struct
import numpy as np
import matplotlib.pyplot as plt

nx = 2250
nz = 750
filename = "pp1.dat"

numpy_data = np.empty([nx,nz], dtype = float)

with open(filename, 'rb') as f:
    for i in range(nx):
        for j in range(nz):
            data = f.read(4)
            data_float = struct.unpack("f", data)[0]
            numpy_data[i][j] = data_float

np.savetxt("pp.txt", numpy_data)

#pic[nx][nz] = 0
#with open("2.dat", 'wb') as f:
#    for i in range(nx):
#        for j in range(nz):
#            f.write(str(pic[i][j]))


#def xshow(filename, nx, nz):
#    f = open(filename, "rb")
#    pic = np.zeros((nx, nz))
#    for i in range(nx):
#        for j in range(nz):
#            data = f.read(4)
#            elem = struct.unpack("f", data)[0]
#            pic[i][j] = elem
#    f.close()
#    return pic

#xshow(filename, nx, nz)
#im = w.image_binary(pic)
#plt.imsave('output.tiff', im, format='tiff', cmap=plt.cm.gray)
