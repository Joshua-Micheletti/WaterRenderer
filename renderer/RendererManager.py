from OpenGL.GL import *

from utils.singleton.Singleton import Singleton
from renderer.model.Model import Model
from renderer.shader.Shader import Shader

class RendererManager(metaclass=Singleton):
    def __init__(self):
        self.models = dict()

        # self.models["plane"] = Model([-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
        #                                0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
        #                               -0.5,  0.5, 0.0, 0.0, 0.0, 1.0,
        #                                0.5,  0.5, 0.0, 1.0, 1.0, 1.0])
        
        self.shaders = dict()
        self.shaders["default"] = Shader("./shaders/default/default.vert", "./shaders/default/default.frag")