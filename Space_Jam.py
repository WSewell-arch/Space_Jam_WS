from direct.showbase.ShowBase import ShowBase
from direct.interval.LerpInterval import LerpFunc
from direct.particles.ParticleEffect import ParticleEffect
#Regex module for string editing
import re
from panda3d.core import *
from panda3d.core import CollisionTraverser, CollisionHandlerPusher
from panda3d.core import CollisionHandlerEvent
import Space_Jam_Classes as space_jam_classes
import defensePaths as Defensepaths
import Player as playerclass
import math, sys, random



class myApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
   

        #base.disableMouse()
        

        
        
        
        def SetupScene():
        

            self.Universe = space_jam_classes.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, "Universe", "./Assets/Universe/Universe.jpg", (0,0,0), 15000)

            #Earth
            self.Planet1 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet1", "./Assets/Planets/New Earth.png", (150, 5000, 67), 350)
            #Mercury
            self.Planet2 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet2", "./Assets/Planets/Mercury.jpg", (-500, 10500, 1000),600)
            #Venus
            self.Planet3 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet3", "./Assets/Planets/Venus.jpg", (5000, -800, 3000), 750)
            #Mars
            self.Planet4 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x",  self.render, "Planet4", "./Assets/Planets/Mars.jpg", (-4000, 1000, -7500), 300)
            #Jupiter
            self.Planet5 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet5", "./Assets/Planets/Jupiter.png", (150, -8000, -15),1000)
            #Neptune
            self.Planet6 = space_jam_classes.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet6", "./Assets/Planets/Neptune.jpg", (-1950, -7000, 400),550)
            #SpaceStation
            self.SpaceStation1 = space_jam_classes.SpaceStation(self.loader, "./Assets/Space Station/spaceStation.x", self.render, "Space Station",  (-1500, 1000, 800), 50)
            #Ship
            self.Ship = playerclass.Spaceship(self.loader, self.task_mgr, self.accept, "./Assets/Spaceships/Dumbledore/Dumbledore.x", self.render, "Spaceship","./Assets/Spaceships/Dumbledore/spacejet_C.png" ,(-1000, 1000, 800), 50, self.cTrav)
            #Wanderer
            #self.Wanderer = space_jam_classes.Wanderer(self.loader, "./Assets/Drone Defender/DroneDefender.x", self.render, "Drone", 6.0, "./Assets/Drone Defender/octotoad1_auv.png", self.Ship)


            self.cTrav = CollisionTraverser()
            #self.cTrav.traverser(self.render)
            self.pusher = CollisionHandlerPusher()
            #self.pusher.addCollider(self.Ship, self.Ship.modelNode)
            #self.cTrav.addCollider(self.Ship, self.pusher)

            self.cTrav.showCollisions(self.render)

            
            self.Sentinal1 = space_jam_classes.Orbiter(self.loader, self.taskMgr, "./Assets/Drone Defender/DroneDefender.x", self.render,
            "Drone", 6.0,  "./Assets/Drone Defender/Drones.jpg", self.Planet5, 900 ,"MLB", self.Ship)
            self.Sentinal2 = space_jam_classes.Orbiter(self.loader, self.taskMgr, "./Assets/Drone Defender/DroneDefender.x", self.render,
            "Drone", 6.0,  "./Assets/Drone Defender/Drones.jpg", self.Planet2, 500 ,"Cloud", self.Ship)
            



            self.parent = self.loader.loadModel("./C_Assets/cube")
        

            fullCycle = 60
            halfCycle = 130
            cycle_3 = 200
            cycle_4 = 70
            cycle_5 = 111
            cycle_6 = 1000

            for j in range(fullCycle):
                space_jam_classes.Drone.droneCount += 1
                nickName = "Drone" + str(space_jam_classes.Drone.droneCount)

                self.DrawCloudDefense(self.Planet1, nickName)
                self.DrawBaseballSeams(self.SpaceStation1, nickName, j, fullCycle, 2)
            
            for j in range(halfCycle):
                space_jam_classes.Drone.droneCount += 1
                nickName = "Drone" + str(space_jam_classes.Drone.droneCount)

                self.DrawCloudDefense(self.Planet2, nickName)
                self.DrawBaseballSeams(self.Planet3, nickName, j, halfCycle, 5)

            for j in range(cycle_3):
                space_jam_classes.Drone.droneCount += 1
                nickName = "Drone" + str(space_jam_classes.Drone.droneCount)

                self.DrawCloudDefense(self.Planet3, nickName)
                self.DrawBaseballSeams(self.Planet3, nickName, j, cycle_3, 5)
            
            for j in range(cycle_4):
                space_jam_classes.Drone.droneCount += 1
                nickName = "Drone" + str(space_jam_classes.Drone.droneCount)

                self.DrawCloudDefense(self.Planet4, nickName)
                self.DrawBaseballSeams(self.Planet4, nickName, j, cycle_4, 1)
            
            for j in range(cycle_5):
                space_jam_classes.Drone.droneCount += 1
                nickName = "Drone" + str(space_jam_classes.Drone.droneCount)

                self.DrawCloudDefense(self.Planet5, nickName)
                self.DrawBaseballSeams(self.Planet5, nickName, j, cycle_5, 1)
            
            for j in range(cycle_6):
                space_jam_classes.Drone.droneCount += 1
                nickName = "Drone" + str(space_jam_classes.Drone.droneCount)

                self.DrawCloudDefense(self.Planet6, nickName)
                self.DrawBaseballSeams(self.Planet5, nickName, j, cycle_6, 5)




            
            self.SetCamera()
            self.CircleX()
            self.CircleY()
            self.CircleZ()
            
        

        SetupScene()
      



    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = Defensepaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        space_jam_classes.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png" ,position, 5)
    
    def DrawCloudDefense(self, CentralObject, droneName):
        unitVec = Defensepaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + CentralObject.modelNode.getPos()
        space_jam_classes.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png", position, 10)
    
    def SetCamera(self):
        self.disableMouse()
        self.camera.reparentTo(self.Ship.modelNode)
        self.camera.setFluidPos(0,1,0)
    
    def CircleX(self):
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

    def CircleY(self):
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
        
    def CircleZ(self):
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
         



app = myApp()
app.run()