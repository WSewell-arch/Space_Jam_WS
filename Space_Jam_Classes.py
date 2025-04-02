from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from direct.task.Task import TaskManager
from CollideObjectBase import *
from direct.gui.OnscreenImage import OnscreenImage
import defensePaths as Defensepaths




class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Planet(SphereCoilliableObject):
    
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, 0, 0, 0, 1.5)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        #tex = loader.loadTexture(texPath)
        #self.modelNode(tex, 0)

class Drone(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):

         self.modelNode = loader.loadModel(modelPath)
         self.modelNode.reparentTo(parentNode)
         self.modelNode.setPos(posVec)
         self.modelNode.setScale(scaleVec)

         self.modelNode.setName(nodeName)
         #tex = loader.loadTexture(texPath)
         #self.modelNode.setTexture(tex, 1)

class Drone(SphereCoilliableObject):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Drone, self).__init__(loader, modelPath, parentNode, nodeName, 0,0,0, 0)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Universe(InverseSphereColliadeObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), 0.9)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)


class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)

class SpaceStation(CapsuleColliableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float):
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 5, 1, -1, -5, 10)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)

class Spaceship(ShowBase):

     
    
     def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float, manager = Task):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        self.taskManager = manager



        

        #self.reloadTime = .25
        #self.missleDistance = 4000 #until Missiles Explode
        #self.missleBay = 1 #only One missile in the bay to be fired
        #self.taskMgr.add(self.CheckIntervals,"CheckMissles", 34)


     def CheckIntervals(self, task):
         for i in Missle.Intervals:
             if not Missle.Intervals[i].isplaying():
                 Missle.cNodes[i].detachNode()
                 Missle.firemodels[i].detachNode()

                 del Missle.Intervals[i]
                 del Missle.firemodels[i]
                 del Missle.cNodes[i]
                 del Missle.collisionSolids[i]
                 print(i + "Has reached the end on its firiing position")

                 break
             return Task.cont 
         
     def EnableHUD(self):
         self.HUD = OnscreenImage(image= "./Assets/Hud/Reticle3b.png", pos = Vec3(0, 0, 0), scale = 0.1)
         self.HUD.setTransparency(TransparencyAttrib.MAlpha)
         
     
     def fire(self):
         if self.missleBay:
             travRate = self.missleDistance
             aim = self.render.getRelativeVector(self.modelNode, Vec3.forward()) #The Direction the spaceship is moving
             aim.normalize()
             firesolution = aim * travRate
             inFront = aim * 150
             travRec = firesolution + self.modelNode.getPos()
             self.missleBay -= 1
             tag = "missle" + str(Missle.missleCount)

             posVec = self.modelNode.getPos() + inFront #Spawn the missle in front of the ship
             #Create our missle
             currentMissle = Missle(self.loader, "./Assets/Phaser/phaser.egg", self.render, tag, posVec, 4.0)
             Missle.intervals[tag] = currentMissle.modelNode.posInterval(2.0, travRec, startPos = posVec, fluid = 1)
             Missle.Intervals[tag].start()

             self.traverser.addCollider(currentMissle.collisionNode, self.handler)

         else:
             # If we aren't reloading, we want to start reloading
             if not self.taskMgr.hasTaskNamed('reload'):
                 print('initialzing reload...')
                 # Call the reload method without delay
                 self.taskMgr.doMethodLater(0, self.reload, "reload")
                 return Task.cont
     
     def reload(self, task):
         if task.time > self.reloadTime:
             self.missleBay -= 1
             print("Reload Complete")

         if self.missleBay > 1:
             self.missleBay = 1
             return Task.done
         
         elif task.time <= self.reloadTime:
             print("reload Proceeding")
             return Task.cont
#def SetKeyBindings(self):
    #self.accept('space', self.Thrust, [1])
    #self.accept('space-up', self.Thrust,[0])
#SetKeyBindings(Spaceship)

    
class Spaceship(SphereCoilliableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float):
        super(Spaceship, self).__init__(loader, modelPath, parentNode, nodeName, 0,0,1, 1)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)

class Missle(SphereCoilliableObject):
    
    firemodels = {}
    cNodes = {}
    collisionSolids = {}
    Intervals = {}
    missleCount = 0



    
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec : Vec3, scaleVec: float = 1.0):
        super(Missle, self).__init__(loader, modelPath, parentNode, nodeName, 0,0,0, 3.0)


        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)

        Missle.missleCount += 1
        Missle.firemodels[nodeName] = self.modelNode
        Missle.cNodes[nodeName] = self.collisionNode
        Missle.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
        Missle.cNodes[nodeName].show()

        print("Fire Torpedo #" + str(Missle.missleCount))


class Orbiter(SphereCoilliableObject):
    numOrbits = 0
    velocity = 0.005
    cloudTimer = 240

    def __init__(self, loader: Loader, taskMGR: TaskManager ,modelPath: str, parentNode: NodePath, nodeName: str, scaleVec: Vec3, texpath : str,
                 centralObject: PlacedObject, orbitRadius: float, orbitType: str, staringAt: Vec3):
        super(Orbiter, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), 3.2)
       
        self.taskMgr = taskMGR
        self.orbitType = orbitType
        self.modelNode.setScale(scaleVec)
        tex = loader.loadTexture(texpath)
        self.modelNode.setTexture(tex, 1)
        self.orbitObject = centralObject
        self.orbitRadius = orbitRadius
        self.startingat = staringAt
        Orbiter.numOrbits += 1

        self.cloudClock = 0

        self.taskFlag = "Traveler-" + str(Orbiter.numOrbits)
        taskMGR.add(self.Orbit, self.taskFlag)

    def orbit(self, task):
        if self.orbitType == "MLB":
            positionVec = Defensepaths.BaseballSeams(task.time * Orbiter.velocity, self.numOrbits, 2.0)
            self.modelNode.setPos(positionVec * self.orbitRadius + self.orbitObject.modelNode.getPos())

        elif self.orbitType == "cloud":
            if self.cloudClock < Orbiter.cloudTimer:
                self.cloudClock += 1

            else:
                self.cloudClock = 0
                positionVec = Defensepaths.Cloud()
                self.modelNode.setPos(positionVec * self.orbitRadius + self.orbitObject.modelNode.getPos())

        self.modelNode.lookAt(self.startingat.modelNode)
        return Task.cont


      


    

   