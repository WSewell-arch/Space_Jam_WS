from direct.showbase.ShowBase import ShowBase


class myApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        
        
        
        def SetupScene():
            self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
            
            self.Universe.reparentTo(self.render)
            self.Universe.setScale(15000)
            tex = self.loader.loadTexture("./Assets/Universe/Universe.jpg")

            self.Universe.setTexture(tex, 1)

            #Earth
            self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
            self.Planet1.reparentTo(self.render)
            self.Planet1.setPos(150, 5000, 67)
            self.Planet1.setScale(350)
            Earth_tex = self.loader.loadTexture("./Assets/Planets/Earth.png")
            self.Planet1.setTexture(Earth_tex, 1)

            #Mercury
            self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
            self.Planet2.reparentTo(self.render)
            self.Planet2.setPos(-1500, 10500, 550)
            self.Planet2.setScale(500)
            Mercury_tex = self.loader.loadTexture("./Assets/Planets/Mercury.jpg")
            self.Planet2.setTexture(Mercury_tex,1)

            #Venus
            self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
            self.Planet3.reparentTo(self.render)
            self.Planet3.setPos(1050, 9500, -1800)
            self.Planet3.setScale(750)
            Venus_tex = self.loader.loadTexture("./Assets/Planets/Venus.jpg")
            self.Planet3.setTexture(Venus_tex, 1)

            #Mars
            self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
            self.Planet4.reparentTo(self.render)
            self.Planet4.setPos(-1000, 10000, -10000)
            self.Planet4.setScale(300)
            Mars_tex = self.loader.loadTexture("./Assets/Planets/Mars.jpg")
            self.Planet4.setTexture(Mars_tex, 1)

            #Jupiter
            self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
            self.Planet5.reparentTo(self.render)
            self.Planet5.setPos(150, -8000, -15)
            self.Planet5.setScale(1000)
            Jup_tex = self.loader.loadTexture("./Assets/Planets/Jupiter.png")
            self.Planet5.setTexture(Jup_tex, 1)

            #Neptune
            self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
            self.Planet6.reparentTo(self.render)
            self.Planet6.setPos(-1950, -7000, 400)
            self.Planet6.setScale(550)
            Nep_tex = self.loader.loadTexture("./Assets/Planets/Neptune.jpg")
            self.Planet6.setTexture(Nep_tex, 1)

            #Spaceship
            self.Ship = self.loader.loadModel("./Assets/Spaceships/Dumbledore/Dumbledore.x")
            self.Ship.reparentTo(self.render)
            self.Ship.setPos(1,1,1)
            self.Ship.setScale(50)

            #Space Station
            self.station = self.loader.loadModel("./Assets/Space Station/spaceStation.x")
            self.station.reparentTo(self.render)
            self.station.setPos(50, -1000, -700)
            self.station.setScale(25)
            

        
            

        
        SetupScene()






app = myApp()
app.run()