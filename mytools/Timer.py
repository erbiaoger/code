"""
This is a sample script to calculating time.

Author: Zhang Zhiyu
Email: erbiaoger@gmail.com
Created: 2023/4/9 10:50
Version: 0.0.1

Description:
- Calculate the time taken by the code

Usage:
import mytools.Timer as Timer

timer = Timer()
for i in range(1000):
    print(i**2)
timer.stop()

Change Log:
- April 10, 2023, added a new data processing function

"""

import time 
class Timer: 
    """
    Calculate time spent
    """
    def __init__(self):
        self.times = []
        self.start()
        
    def start(self):
        self.tik = time.time()
        
    def stop(self):
        self.times.append(time.time() - self.tik)
        self.print()
        #return self.times[-1]
    
    def avg(self):
        return sum(self.times) / len(self.times)
    
    def sum(self):
        return sum(self.times)
    
    def cumsum(self):
        return np.array(self.times).cumsum().tolist()
    
    def print(self):
        print(f'Done! {self.times[-1]: .2f} sec')