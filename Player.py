from CollideObjectBase import SphereCoilliableObject
from panda3d.core import Loader, NodePath, Vec3
from direct.task.Task import TaskManager
from typing import Callable
from direct.task import Task
import Space_Jam_Classes as space_jam_classes
from direct.gui.OnscreenImage import OnscreenImage



class Spaceship(SphereCoilliableObject):
    def __init__(self, loader: Loader, taskMGR: TaskManager, accept: Callable[[str, Callable], None], modelPath: str, parentNode: NodePath, nodeName: str, texPath: str ,posVec: Vec3, scaleVec: float):
        super(Spaceship, self).__init__(loader, modelPath, parentNode, nodeName, 0,0,1, 1)

        self.TaskMGR = taskMGR
        self.accept = accept
        self.render = parentNode
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        

        self.SetKeyBindings()

        self.reloadTime = .25
        self.missleDistance = 4000 #Until missle explodes
        self.missleBay = 1

        #self.TaskMGR.add(self.checkIntervals, 'checkMissles', 34)

    def CheckIntervals(self, task):
        for i in space_jam_classes.Missle.Intervals:
            if not space_jam_classes.Missle.Intervals[i].isplaying():
                space_jam_classes.Missle.cNodes[i].detachNode()
                space_jam_classes.Missle.firemodels[i].detachNode()
                
                del space_jam_classes.Missle.Intervals[i]
                del space_jam_classes.Missle.firemodels[i]
                del space_jam_classes.Missle.cNodes[i]
                del space_jam_classes.Missle.collisionSolids[i]
                print(i + "Has reached the end on its firiing position")

                break
            return Task.cont 
         
    def EnableHUD(self):
        self.HUD = OnscreenImage(image= "./Assets/Hud/Reticle3b.png", pos = Vec3(0, 0, 0), scale = 0.1)
        self.HUD.setTransparency(TransparencyAttrib.MAlpha)
    
    def SetKeyBindings(self):
        self.accept('space', self.Thrust, [1])
        self.accept('space_up', self.Thrust, [0])

        self.accept('shift', self.Boost, [1])
        self.accept('shift-up', self.Boost, [0])

        self.accept('arrow_left', self.LeftTurn, [1])
        self.accept('arrow_left-up', self.LeftTurn, [0])

        self.accept('arrow_right', self.RightTurn, [1])
        self.accept('arrow_right-up', self.RightTurn, [0])

        self.accept('arrow_up', self.LookUp, [1])
        self.accept('arrow_up-up', self.LookUp, [0])

        self.accept('arrow_down', self.LookDown, [1])
        self.accept('arrow_down-up', self.LookDown, [0])

        self.accept('w', self.LeftRoll, [1])
        self.accept('w-up', self.LeftRoll, [0])

        self.accept('e', self.RightRoll, [1])
        self.accept('e-up', self.RightRoll, [0])

        #self.accept('f', self.fire)
    
    def Thrust(self, keyDown):
        if keyDown:
            self.TaskMGR.add(self.ApplyThrust, 'forward-thrust')
        else:
            self.TaskMGR.remove('forward-thrust')

    def ApplyThrust(self, task):
        rate = 5
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()

        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont
    
    def Boost(self, KeyDown):
        if KeyDown:
            self.TaskMGR.add(self.ApplyBoost, "boost")
        else:
            self.TaskMGR.remove('boost')
    
    def ApplyBoost(self, task):
        rate = 15
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()

        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont

    def LeftTurn(self, KeyDown):
        if KeyDown:
            self.TaskMGR.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.TaskMGR.remove('left-turn')

    def ApplyLeftTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont

    def RightTurn(self, KeyDown):
        if KeyDown:
            self.TaskMGR.add(self.ApplyRightTurn, 'right-turn')
        else:
            self.TaskMGR.remove('right-turn')

    def ApplyRightTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() - rate)

        return Task.cont
    
    def LookUp(self, KeyDown):
        if KeyDown:
            self.TaskMGR.add(self.ApplyUp, 'turn-up')
        else:
            self.TaskMGR.remove('turn-up')
    
    def ApplyUp(self, task):
        rate = .5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont
    
    def LookDown(self, KeyDown):
        if KeyDown:
            self.TaskMGR.add(self.ApplyDown, 'turn-down')
        else:
            self.TaskMGR.remove('turn-down')

    def ApplyDown(self, task):
        rate = .5
        self.modelNode.setP(self.modelNode.getP() - rate)
        return Task.cont
    
    def LeftRoll(self, KeyDown):
        if KeyDown:
            self.TaskMGR.add(self.ApplyLRoll, 'Left-Roll')
        else:
            self.TaskMGR.remove('Left-Roll')
    
    def ApplyLRoll(self, task):
        rate = 1
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont
    
    def RightRoll(self, KeyDown):
        if KeyDown:
            self.TaskMGR.add(self.ApplyRRoll, 'Right-Roll')
        else:
            self.TaskMGR.remove('Right-Roll')
    
    def ApplyRRoll(self, task):
        rate = 1
        self.modelNode.setR(self.modelNode.getR() - rate)
        return Task.cont
    
    def fire(self):
        if self.missleBay:
            travRate = self.missleDistance
            aim = self.render.getRelativeVector(self.modelNode, Vec3.forward())
            aim.normalize()
            fireSolution = aim * travRate
            inFront = aim * 150

            travVec = fireSolution + self.modelNode.getPos()
            self.missleBay -= 1
            tag = "Missle" + str(space_jam_classes.Missle.missleCount)

            posVec = self.modelNode.getPos() + inFront #Spawns the missles in front of ship
            #Create Missle
            currentMissle = space_jam_classes.Missle(self.loader, './Assets/Phaser/phaser.x', self.render, tag, posVec, 4.0)     
            space_jam_classes.Missle.intervals[tag] = currentMissle.modelNode.posInterval(2.0, travVec, startPos = posVec, fluid = 1)
            space_jam_classes.Missle.Intervals[tag].start()

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

       