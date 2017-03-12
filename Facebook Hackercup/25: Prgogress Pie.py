import math
def hackercup():
    T = int(input())
    for i in range(T):
        P, X, Y = input().split(" ")
        P = int(P)
        X = int(X)
        Y = int(Y)
        if isInsideRadius(X, Y, 50) and isInsideAngle(X, Y, P):
            print("Case #" + str(i+1) + ": black")
        else:
            print("Case #" + str(i+1) + ": white")

def isInsideRadius(x, y, totalRaidus):
    x = x-50
    y = y-50
    radius = math.sqrt(x*x + y*y)
    if radius <= totalRaidus:
        return True
    return False

def isInsideAngle(x, y, p):
    totalAngle = p*3.6
    point_angle = 0
    if x == 50 and y>= 50:
        point_angle = 0
    elif x == 50 and y < 50:
        point_angle = 180
    elif y == 50 and x >= 50:
        point_angle = 90
    elif y == 50 and x < 50:
        point_angle = 270
    #firstQuadrant
    if 50 < x < 100 and 50 < y < 100:
        x = x- 50
        y = y- 50
        point_angle = 90 - math.degrees(math.atan(y/x))
    #second Quad
    elif 50 < x < 100 and 0 < y < 50:
        x = x- 50
        y = 50 - y
        point_angle = 90 + math.degrees(math.atan(y/x))
    #third Quad
    elif 0 < x < 50 and 0 < y < 50:
        x = 50 - x
        y = 50 - y
        point_angle = 270 - math.degrees(math.atan(y/x))
    #fourth
    elif 0 < x < 50 and 50 < y < 100 :
        x = 50 - x
        y = y - 50
        point_angle = 270 + math.degrees(math.atan(y/x))
    #print(str(point_angle) + " " + str(totalAngle))
    if totalAngle!=0 and point_angle <= totalAngle:
        return True
    return False
if __name__ == '__main__':
    hackercup()