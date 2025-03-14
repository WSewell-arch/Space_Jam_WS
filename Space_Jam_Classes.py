from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from CollideObjectBase import *
from direct.gui.OnscreenImage import OnscreenImage




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
     
     def Thrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyThrust,'forward-thrust')
        else:
            self.taskMgr.remove('forward-thrust')

     def ApplyThrust(self, task):
          rate = 5
          trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
          
          trajectory.normalize()
          self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
          
          return Task.cont
     
     def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.taskMgr.remove('left-turn')
         
     def ApplyLeftTurn(self, task):
         # Half a degree turn every time
          rate = 0.5
          
          self.modelNode.setH(self.modelNode.getH() + rate)
          return Task.cont
     
     def SetKeyBindings(self):
        self.accept("space", self.Thrust, [1])
        self.accept("space-up", self.Thrust, [0])

        self.accept("left", self.LeftTurn, [1])
        self.accept("left-up", self.LeftTurn, [0])


     def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        self.SetKeyBindings().modelNode
        
        
    

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
         
    
     #def ApplyThrust(self, Task):
          #rate = 5
          #trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
          
          #trajectory.normalize()
          #self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
          
          #return Task.cont
     
     #def LeftTurn(self, keyDown):
    #    if keyDown:
    #        self.taskManager.add(self.ApplyLeftTurn, "left-turn")
    #    else:
    #        self.taskManager.remove("left-turn")

     #def ApplyLeftTurn(self, Task):
         # Half a degree turn every time
          #rate = 0.5
          
         # self.modelNode.setH(self.modelNode.getH() + rate)
        #  return Task.cont
     
     def RightTurn(self, keyDown):
         if keyDown:
             self.taskManager.add(self.ApplyRightTurn, "right-turn")
         else:
             self.taskManager.remove('right-turn')

     def ApplyRightTurn(self, Task):
         rate = 0.5
         self.modelNode.setR(self.modelNode.getR() + rate)
         
         return Task.cont
     
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
    missleCount = {}
        
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec : Vec3, scaleVec: float = 1.0):
        super(Missle, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), 3.0)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)

        Missle.missleCount += 1
        Missle.firemodels[nodeName] = self.modelNode
        Missle.cNodes[nodeName] = self.collisionNode
        Missle.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
        Missle.cNodes[nodeName].show()

        print("Fire Torpedo #" + str(Missle.missleCount))
       


      


    

   