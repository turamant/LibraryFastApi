from math import cos, sin



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x,y):
        return Point(x,y)

    @staticmethod
    def new_polar_point(rho, pheta):
        return Point(rho * sin(pheta), rho*cos(pheta))


    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

if __name__=='__main__':
    p = Point(2,3)
    print(p)
    p2 = Point.new_cartesian_point(2,3)
    print(p2)
    p3 = Point.new_polar_point(1,2)
    print(p3)
