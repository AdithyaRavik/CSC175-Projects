class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord
            
    """print out the attributes of this point """
    def __str__(self):
       return "Point: (" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def double(self):
        self.x=self.x*2
        self.y=self.y*2

    def getDistanceFromOrigin(self):
        return (self.x**2 + self.y**2)**.5

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

    def isAbove(self, Pointother):
        if self.y > Pointother.y:
            return True
        else:
            return False

    def reflect_x(self):
        self.y = -(self.y)
        return Point(self.x,self.y)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    #The order of subtration does matter.
    #If you do a-b and b-a you will get different answers.
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)


a = Point(4,4)
b = Point(3,6)

print(a.isAbove(b))
print(b.isAbove(a))
print(a-b)
print(b-a)
print(a.reflect_x())

a.move(1,2)
print(a) 



    

    
