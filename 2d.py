class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
    def __str__(self):
        return "<{},{}>".format(self.x_cod,self.y_cod)
    def euclian_distance(self,other):
        return ((other.x_cod-self.x_cod)**2 + (other.y_cod-self.y_cod)**2)**0.5
    def distance_f_origin(self):
        return self.euclian_distance(Point(0,0))
        #return ((other.x_cod)**2 + (other.y_cod)**2)**0.5
p1=Point(3,4)
p2=Point(5,6)
print(p1)
print(p2.distance_f_origin())

class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
    def __str__(self):
        return "{}x +{}y +{} = 0".format(self.A,self.B,self.C)
    def point_on_line(self,point):
        if self.A*point.x_cod +self.B*point.y_cod+ self.C==0:
            return "lies"
        else:
            return "not"
    def shortest_dist(line,point):
        return  abs(line.A*point.x_cod+line.B*point.y_cod+line.C)/(line.A**2 + line.B**2)**0.5
l=Line(1,1,-2)
p1=Point(1,1)
print(l,p1)
print(l.point_on_line(p1))
print(l.shortest_dist(p1))