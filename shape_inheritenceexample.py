class Shape:
    def __init__(self):
        pass    
    def area(self):
        pass   

class Circle(Shape):
    def __init__(self,r):
        self.radius = r 
    def area(self):
        return self.radius**2*22.8/7.0
    def __repr__(self):
        return self.radius**2*3.141592      

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def __repr__(self):
        return self.length*self.width

class Square(Rectangle):
    def __init__(self, length):
        super.__init__(length, length)
    def __repr__(s):
        return f" Squr: side={s.length}"    

                    
                
