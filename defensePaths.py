import math, random, sys
from panda3d.core import *


def cloud(radius = 1):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    z = 2 * random.random() - 1

    unitVec = Vec3(x, y, z)
    unitVec.normalize()
    
    return unitVec * radius

def BaseballSeams(step, numSeams, B, F = 1):
    time = step / float(numSeams) * 2 * math.pi

    F4 = 0
    
    R = 1

    xxx = math.cos(time) - B * math.cos(3 * time)
    yyy = math.sin(time) + B  * math.sin(3 * time)
    zzz = F * math.cos(2 * time) + F4 * math.cos(4 * time)

    rrr = math.sqrt(xxx ** 2 + yyy  ** 2 + zzz ** 2)

    x = R * xxx / rrr
    y = R * yyy / rrr
    z = R * zzz / rrr

    return Vec3(x, y, z)


def CircleX():
    x = 0
    for i in range(100):
        theta = x
        self.placeholder2 = self.render.attachNewNode('Placeholder2')
        self.placeholder2.setPos(50.0 * math.cos(theta), 50.0 * math.sin(theta), 0.0 * math.tan(theta))
        red = 0.6 + random.random() * 0.4
        blue = 0.0 + random.random() * 0.0
        green = 0.0 + random.random() * 0.0
        self.placeholder2.setColorScale(red, blue, green, 1.0)
        self.parent.instanceTo(self.placeholder2)
        x = x + 0.06

def CircleY():
    y = 0
    for i in range(100):
        theta = y
        self.placeholder2 = self.render.attachNewNode('Placeholder2')
        self.placeholder2.setPos(50.0 * math.sin(theta), 0.0 * math.cos(theta), 50.0 * math.cos(theta))
        red = 0.0 + random.random() * 0.0
        blue = 0.6 + random.random() * 0.4
        green = 0.0 + random.random() * 0.0
        self.placeholder2.setColorScale(red, blue, green, 1.0)
        self.parent.instanceTo(self.placeholder2)
        y = y + 0.06

def CircleZ():
    z = 0
    for i in range(100):
        theta = z
        self.placeholder2 = self.render.attachNewNode('Placeholder2')
        self.placeholder2.setPos(0.0 * math.cos(theta), 50.0 * math.cos(theta), 50.0 * math.sin(theta))
        red = 0.0 + random.random() * 0.0
        blue = 0.0 + random.random() * 0.0
        green = 0.6 + random.random() * 0.4
        self.placeholder2.setColorScale(red, blue, green, 1.0)
        self.parent.instanceTo(self.placeholder2)
        z = z + 0.06
     

