from panda3d.core import PandaNode, Loader, NodePath, CollisionNode, CollisionSphere, CollisionInvSphere, CollisionCapsule, Vec3

class PlacedObject(PandaNode):
    #Just a Generic Object
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        self.modelNode : NodePath = loader.loadModel(modelPath)

        #Check if right type is passed, else show an error
        if not isinstance(self.modelNode, NodePath):
            raise AssertionError("PlacedObject loader: loadmodel("+ modelPath +") did not return a proper PandaNode!")
        
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setName(nodeName)

class ColliableObject(PlacedObject):
    # Now we relate our placedObject to Collisions by using it as a helper class
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        super(ColliableObject, self).__init__(loader, modelPath, parentNode, nodeName)
        #Every single object will get the cNode tag
        self.collisionNode = self.modelNode.attachNewNode(CollisionNode(nodeName + "_cnode"))
        #self.collisionNode.show()

class InverseSphereColliadeObject(ColliableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, colRadius: float ):
        super(InverseSphereColliadeObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionInvSphere(colPositionVec, colRadius))
        #self.collisionNode.show()

class CapsuleColliableObject(ColliableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, ax: float, ay: float, az: float, bx: float, by: float, bz: float, r: float):
        super(CapsuleColliableObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionCapsule(ax, ay, az, bx, by, bz, r))
        self.collisionNode.show()

class SphereCoilliableObject(ColliableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, ax: float, ay: float, az: float, r: float):
        super(SphereCoilliableObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionSphere(ax, ay, az, r))
        self.collisionNode.show()