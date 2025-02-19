from direct.showbase.ShowBase import ShowBase
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.init__(self)
        self.fighter = self.loader.loadModel("./Assets/sphere")
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0, 0.0, 0.0, 1.0)