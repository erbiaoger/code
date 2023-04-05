# mytools made by erbiaoger

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
        return self.times[-1]
    
    def avg(self):
        return sum(self.times) / len(self.times)
    
    def sum(self):
        return sum(self.times)
    
    def cumsum(self):
        return np.array(self.times).cumsum().tolist()
    
    def print(self):
        print(f'Done! {timer.stop(): .2f} sec')
