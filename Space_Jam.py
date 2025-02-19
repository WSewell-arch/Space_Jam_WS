from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import Space_Jam_Classes as space_jam_classes
import defensePaths as Defensepaths
import math, sys, random


class myApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        
        
        
        def SetupScene():
            

            self.Universe = space_jam_classes.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, "Universe", "./Assets/Universe/Universe.jpg", (0,0,0), 15000)
            self.Planet1 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet1", "./Assets/Planets/Earth.png", (150, 5000, 67), 350)
            self.Planet2 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet2", "./Assets/Planets/Mercury.jpg", (-1500, 10500, 550),500)
            self.Planet3 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet3", "./Assets/Planets/Venus.jpg", (1050, 9500, -1800), 750)
            self.Planet4 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x",  self.render, "Planet4", "./Assets/Planets/Mars.jpg", (-1000, 10000, -10000), 300)
            self.Planet5 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet5", "./Assets/Planets/Jupiter.png", (150, -8000, -15),1000)
            self.Planet6 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet6", "./Assets/Planets/Neptune.jpg", (-1950, -7000, 400),550)
            self.SpaceSpaceStation1 = space_jam_classes.SpaceStation(self.loader, "./Assets/Space Station/spaceStation.x", self.render, "Space Station",  (50, -1000, -700), 25)
            self.Ship = space_jam_classes.Spaceship(self.loader, "./Assets/Spaceships/Dumbledore/Dumbledore.x", self.render, "Spaceship", (30, -800, -900), 50)

            self.parent = self.loader.loadModel("./C_Assets/cube")      
         
        
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
          




        
        def DrawBaseballSeams (self, centralObject, droneName, step, numSeams, radius = 1):
            unitVec = Defensepaths.BaseballSeams(step, numSeams, B = 0.4)
            unitVec.normalize()
            position = unitVec * radius * 250 + centralObject.modelNode.getPos()
            space_jam_classes.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png" ,position, 5)

        
        def DrawCloudDefense (self, CentralObject, droneName):
            unitVec = Defensepaths.Cloud()
            unitVec.normalize()
            position = unitVec * 500 + CentralObject.modelName.getPos()
            space_jam_classes.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png", position, 10)
        
        fullCycle = 60

        for j in range(fullCycle):
                space_jam_classes.Drone.droneCount += 1
                nickName = "Drone" + str(space_jam_classes.Drone.droneCount)

                #self.DrawCloudDefense(self.Planet1, nickName)
                #5self.DrawBaseballSeams(self.spaceStation1, nickName, j, fullCycle, 2)
            

        
            

        
        SetupScene()
            







app = myApp()
app.run()