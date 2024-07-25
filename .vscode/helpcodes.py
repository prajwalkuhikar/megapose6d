#HOME ERROR
# $env:HOME = $env:USERPROFILE

from direct.showbase.ShowBase import ShowBase

from panda3d.core import loadPrcFileData, DirectionalLight

# Configuration settings before creating ShowBase
loadPrcFileData("", """
    win-size 800 600
    window-title My Panda3D Window
""")

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()

        # Load the model
        self.model = self.loader.loadModel("/c/Users/DEBIEKPR/Desktop/megapose6d/local_data/examples/barbecue-sauce/meshes/barbecue-sauce/hope_000002.ply")

        # Reparent the model to render so it is rendered
        self.model.reparentTo(self.render)

        # Optional: Set the model's position and scale
        self.model.setPos(0, 50, 0)
        self.model.setScale(0.5, 0.5, 0.5)

        # Optional: Set up camera and lighting
        self.camera.setPos(0, -100, 0)
        self.camera.lookAt(self.model)
        self.setupLight()

    def setupLight(self):
        # Simple directional light
        directionalLight = self.render.attachNewNode(DirectionalLight('directionalLight'))
        directionalLight.node().setColor((0.8, 0.8, 0.8, 1))
        self.render.setLight(directionalLight)

app = MyApp()
app.run()