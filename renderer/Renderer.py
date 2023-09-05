from utils.singleton.Singleton import Singleton
from OpenGL.GL import *
import numpy as np

from renderer.RendererManager import RendererManager

class Renderer(metaclass=Singleton):
    def __init__(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.vbo = 0
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        print(self.vbo)

        vertices = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                     0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                    -0.5,  0.5, 0.0, 0.0, 0.0, 1.0,
                     0.5,  0.5, 0.0, 1.0, 1.0, 1.0]

        vertices = np.array(vertices, dtype=np.float32)

        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT)

        RendererManager().shaders["default"].use()
        # glBindBuffer(GL_ARRAY_BUFFER, RendererManager().models["plane"].vbo)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        