from utils.singleton.Singleton import Singleton
from OpenGL.GL import *
import numpy as np

from renderer.RendererManager import RendererManager

class Renderer(metaclass=Singleton):
    def __init__(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT)

        RendererManager().shaders["default"].use()
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
        