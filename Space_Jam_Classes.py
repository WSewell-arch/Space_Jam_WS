from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from CollideObjectBase import *




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
        tex = loader.loadTexture(texPath)
        self.modelNode(tex, 0)

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


    # def SetKeyBindings(self):
    #  #All keybindings for the spaceships movement
    #  self.accept("space", self.Thrust, [1])
    #  self.accept("space-up", self.Thrust, [0])
      
    #  self.accept("left", self.LeftTurn, [1])
    #  self.accept("left-up", self.LeftTurn, [0])
    
     def Thrust(self, keyDown):
          if keyDown:
               self.taskManager.add(self.ApplyThrust, "forward-thrust")
          else:
               self.taskManager.remove("forward-thrust")
    
     def ApplyThrust(self, Task):
          rate = 5
          trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
          
          trajectory.normalize()
          self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
          
          return Task.cont
     
     def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, "left-turn")
        else:
            self.taskManager.remove("left-turn")

     def ApplyLeftTurn(self, Task):
         # Half a degree turn every time
          rate = 0.5
          
          self.modelNode.setH(self.modelNode.getH() + rate)
          return Task.cont
     
     def RightTurn(self, keyDown):
         if keyDown:
             self.taskManager.add(self.ApplyRightTurn, "right-turn")
         else:
             self.taskManager.remove('right-turn')

     def ApplyRightTurn(self, Task):
         rate = 0.5
         self.modelNode.setR(self.modelNode.getR() + rate)
         
         return Task.cont
    
class Spaceship(SphereCoilliableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float):
        super(Spaceship, self).__init__(loader, modelPath, parentNode, nodeName, 0,0,1, 1)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)

      


    

   