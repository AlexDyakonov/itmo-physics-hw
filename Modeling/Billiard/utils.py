import math as m

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, cord):
        return m.sqrt(m.pow((cord.x - self.x ), 2) + m.pow((cord.y - self.y ), 2))

class Ball:
    def __init__(self, coordinates : Coordinates, m, r):
        self.coordinates = coordinates
        self.m = m
        self.r = r
    
    def isInsideOtherBall(self, ball):
        if((self.coordinates.distance(ball.coordinates)) > self.r):
            return True
        else:
            return False

