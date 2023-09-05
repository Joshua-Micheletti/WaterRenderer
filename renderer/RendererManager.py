from utils.singleton.Singleton import Singleton
from OpenGL.GL import *

class RendererManager(metaclass=Singleton):
    def __init__(self):
        self.models = dict()