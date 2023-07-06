import struct
import numpy as np
import os

def read2A(filename=None):
    ScanNum = 1063
    RecLen = 8283
    SampleNum = 2048
    RecOffset = 90
    LabNum = 0
    DatclonNum = ScanNum - 1  # LabNum + DatclonNum = ScanNum

    fin = open(filename, 'rb')
    datalist = []
    for i in range(1, ScanNum - LabNum + 1):
        fin.seek(RecOffset + RecLen * (i + LabNum - 1))
        A = struct.unpack('f'*SampleNum, fin.read(4*SampleNum))
        datalist.append(A)       
    
    fin.close()
    return np.asmatrix(np.array(datalist).T)

