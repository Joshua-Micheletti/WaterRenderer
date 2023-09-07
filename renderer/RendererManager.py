from OpenGL.GL import *

from utils.singleton.Singleton import Singleton
from renderer.model.Model import Model
from renderer.shader.Shader import Shader

class RendererManager(metaclass=Singleton):
    def __init__(self):
        self.models = dict()

        # self.models["plane"] = Model([-0.5, -0.5, 0.0,
        #                                0.5, -0.5, 0.0,
        #                               -0.5,  0.5, 0.0,
        #                                0.5,  0.5, 0.0,
        #                               -0.5,  0.5, 0.0,
        #                                0.5, -0.5, 0.0])
        
        self.models["box"] = Model("models/box.obj")
        self.models["box"].scale(0.5, 0.5, 0.5)
        self.models["box"].rotate(45.0, 45.0, 45.0)
    
        # self.models["plane"].place(0, 0.5, 0)
        # self.models["plane"].scale(1.1, 0.9, 1.2)
        # self.models["plane"].rotate(45.0, 45.0, 45.0)
        
        self.shaders = dict()
        self.shaders["default"] = Shader("./shaders/default/default.vert", "./shaders/default/default.frag")