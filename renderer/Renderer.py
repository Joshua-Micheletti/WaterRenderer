from utils.singleton.Singleton import Singleton
from OpenGL.GL import *
import numpy as np

from renderer.RendererManager import RendererManager

class Renderer(metaclass=Singleton):
    def __init__(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_DEPTH_TEST)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        shader = RendererManager().shaders["default"]
        shader.use()

        for name, model in RendererManager().models.items():
            glUniformMatrix4fv(shader.uniforms["model"], 1, GL_FALSE, model.get_ogl_matrix())

            glBindBuffer(GL_ARRAY_BUFFER, model.vbo)

            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

            glDrawArrays(GL_TRIANGLES, 0, int(model.vertices_count))

        