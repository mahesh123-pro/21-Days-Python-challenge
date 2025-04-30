import math
def ball_collide(x1,y1,r1,x2,y2,r2):
    
    dist=math.sqrt((x1-x2)**2+(y1-y2)**2)
    print("distance b/w two balls:",dist)
    center=dist/2;
    
    print("collision point:",center);
    r=r1+r2;
    
    print("sum of radius:",r);
    if center<=r:
        print("collision occurs")
        return True
    else:
        print("collision does not occur")
        return False
        
#------------Main program------------------
x1=float(input("Enter x1: "))
y1=float(input("Enter y1: "))
r1=float(input("Enter r1: "))
x2=float(input("Enter x2: "))
y2=float(input("Enter y2: "))
r2=float(input("Enter r2: "))
collision = ball_collide(x1, y1, r1, x2, y2, r2)
print("Collision result (True/False):", collision)
#------------------End of program----------------ṇ