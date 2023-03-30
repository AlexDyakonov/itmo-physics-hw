import math
from copy import deepcopy

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2) # ~ distance(Coordinates(0, 0))

    def distance(self, cord):
        return math.sqrt((self.x - cord.x)**2 + (self.y - cord.y)**2)
    
    def __add__(self, coordinates):
        return Coordinates(self.x + coordinates.x, self.y + coordinates.y)
    def __sub__(self, coordinates):
        return Coordinates(self.x - coordinates.x, self.y - coordinates.y)
    def __mul__(self, const):
        return Coordinates(const*self.x, const*self.y)
    def __rmul__(self, const):
        return Coordinates(const*self.x, const*self.y)
    def __truediv__(self, const):
        return Coordinates(self.x / const, self.y / const)
    def __lt__(self, coordinates):
        return self.x < coordinates.x or self.y < coordinates.y

class Ball:
    def __init__(self, coordinates : Coordinates, speed : Coordinates, acceleration : Coordinates, m, r):
        self.coordinates = coordinates
        self.setSpeed(speed)
        self.setAcceleration(acceleration)
        self.m = m
        self.r = r
    def setSpeed(self, speed):
        self.speed = deepcopy(speed)
    def getSpeed(self):
        return self.speed
    def setAcceleration(self, acceleration : Coordinates):
        self.acceleration = deepcopy(acceleration)
    def getAcceleration(self):
        return self.acceleration
    
    def iteration(self, dt):
        dv = dt*self.acceleration
        if abs(self.speed.x) < abs(dv.x):
            dv.x = -self.speed.x
        if abs(self.speed.y) < abs(dv.y):
            dv.y = -self.speed.y
        self.coordinates = self.coordinates + dt*self.speed
        self.speed = self.speed + dv

    def isCollision(self, ball):
        return self.coordinates.distance(ball.coordinates) <= self.r + ball.r
    
    def isCollisionWall(self, Lx, Ly):
        def is_collision_side(Lx):
            if self.coordinates.x + self.r >= Lx or self.coordinates.x - self.r <= 0:
                return -1
            else:
                return 1
        def is_collision_end(Ly):
            if self.coordinates.y + self.r >= Ly or self.coordinates.y - self.r <= 0:
                return -1
            else:
                return 1
        self.speed.x = self.speed.x * is_collision_side(Lx)
        self.speed.y = self.speed.y * is_collision_end(Ly)
        self.acceleration.x = self.acceleration.x * is_collision_side(Lx)
        self.acceleration.y = self.acceleration.y * is_collision_end(Ly)
