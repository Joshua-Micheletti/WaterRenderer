from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.GL import *

class Shader:
    def __init__(self, vert_path, frag_path):
        f = open(vert_path)
        vertex_src = f.read()

        f.close()

        f = open(frag_path)
        fragment_src = f.read()

        f.close()

        self.program = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

    def use(self):
        glUseProgram(self.program)
