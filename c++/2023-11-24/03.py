class Circle():
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return 3.14 * self.r * self.r
    
    
if __name__ == "__main__":
    c = Circle(5)
    print(c.r)
    print(c.area())