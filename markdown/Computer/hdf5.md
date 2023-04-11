```python
import h5py
import numpy as np

def main():
  with h5py.File("h5py_example.hdf5", 'w') as f:
    
    # create two groups under root '/'
    g1 = f.create_group('bar1')
    g2 = f.create_group('bar2')
    
    # create a dataset under root '/'
    d = f.create_dataset('dset', data=np.arange(16).reshape(4, 4))
    
    # add two attributes to dataset 'dset'
    d.attrs['myAttr1'] = [100, 200]
    d.attrs['myAttr2'] = "Hello World!"
    
    # create a group and a dataset under group 'bar1'
    c1 = g1.create_group('car1')
    d1 = g1.create_dataset('dset1', data=np.arange(10))
    
    
    
  with h5py.File('h5py_example.hdf5', 'r') as f:
    
    print(f.filename, ':')
    print([key for key in f.keys()], '\n')
    
    # read dataset 'dset' under '\'
    d = f['dset']
    
    # print the data of 'dset'
    print(d.name, ':')
    print(d[:])
    
    # print the attributes of dataset 'dset'
    for key in d.attrs.keys():
      print(key, ':', d.attrs[key])
      
    print()
  
  
  
if __name__ == "__main__":
  main()
```





# 安装 h5dump

```shell
sudo apt install hdf5-tools
```



## 使用 h5dump

```shell
h5dump -H 
```



```shell
❯ h5dump -H SectionA_traces200m_171025_180305.h5
```

