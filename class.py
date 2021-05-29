from os import pipe
from testing12 import test
class point:
    """ Create a new Point, at coordinates x, y"""
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y     
    def reflect_x(self):
        return point(self.x , -self.y)
    def slope_from_origin(self):
        return(self.y)/(self.x)
# a method
    # def get_line_to(self,point):
    #     """ y =ax+b"""
    #     a = (point.y-self.y)/(point.x-self.x)
    #     b =((self.y)- (a*self.x))
    #     return point(a,b)
# -------- the same method ------------------------------------------------------------
    def get_slope(self,target=0):
        if target is None: target = point(0,0)
        return ((self.y - target.y ) / (self.x - target.x))
    def get_line_to(self , point):
        slope = self.get_slope(point)
        p = point.y-slope*point.x
        print("y ={0}x+{1}".format(slope,p))
        return (slope , p)
    def mid_point(self ,a =0, b= 0, c=0):
        d = 2*(a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y))

        rx = ((a.x**2 + a.y**2)*(b.y - c.y) + (b.x**2 + b.y**2)*(c.y - a.y) +
            (c.x**2 + c.y**2)*(a.y -b.y))/d

        ry = ((a.x**2 + a.y**2)*(c.x - b.x) + (b.x**2 + b.y**2)*(a.x - c.x) +
            (c.x**2 + c.y**2)*(b.x -a.x))/d
        return point(rx, ry)
#--------------------------------------------------

k = point(5,5).reflect_x()
print(k)
m = point(4,10).slope_from_origin()
print(m)
l =point(4,11).get_line_to(point(6,15))
print(l)
# ===========================================================
kl = point().mid_point(point(1,4),point(1,5),point(7,8))
print(kl.y)