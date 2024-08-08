class shape:
    def __init__(self,length,width,radius,side):
        self.length=length
        self.width=width
        self.radius=radius
        self.side=side
    def circle(self):
        return 2*3.14*self.radius
    def rectangle(self):
        return 2*(self.length+self.width)
    def square(self):
        return 4*self.side

shapes=shape(5,4,8,4)
print(shapes.circle())
print(shapes.rectangle())
print(shapes.square())
