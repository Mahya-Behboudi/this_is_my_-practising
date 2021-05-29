from testing12 import test
# from class import point/
class point:
    """ Create a new Point, at coordinates x, y"""
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y   
class Rectangle:
    def __init__(self,pos,w,h):
        self.corner = pos
        self.width = w
        self.height = h
    def __str__(self):
        return "({0},{1},{2})".format(self.corner,self.width,self.height)
    def bound(self , target):
        uppen_x = self.corner.x + self.width
        uppen_y = self.corner.y + self.height
        if self.corner.x <= target.x <= uppen_x and self.corner.y <= target.y <= uppen_y:
            return True
        else:
            return False
r = Rectangle(point(0, 0), 10, 5)
test(r.bound(point(0, 0)))
test(r.bound(point(3, 3)))
test(not r.bound(point(3, 7)))
test(not r.bound(point(3, 5)))
test(r.bound(point(3, 4.99999)))
test(not r.bound(point(-3, -3)))

