import glfw

from utils.singleton.Singleton import Singleton

class Controller(metaclass=Singleton):
    def __init__(self):
        self.states = dict()

        self.states["up"] = False
        self.states["down"] = False
        self.states["left"] = False
        self.states["right"] = False
        self.states["close"] = False

    def handle_key_press(self, key, mods):
        if key == glfw.KEY_UP:
            self.states["up"] = True
        if key == glfw.KEY_DOWN:
            self.states["down"] = True
        if key == glfw.KEY_LEFT:
            self.states["left"] = True
        if key == glfw.KEY_RIGHT:
            self.states["right"] = True

        if key == glfw.KEY_ESCAPE:
            self.states["close"] = True

    def handle_key_release(self, key, mods):
        if key == glfw.KEY_UP:
            self.states["up"] = False
        if key == glfw.KEY_DOWN:
            self.states["down"] = False
        if key == glfw.KEY_LEFT:
            self.states["left"] = False
        if key == glfw.KEY_RIGHT:
            self.states["right"] = False

    def update(self, window, dt):
        if self.states["up"] == True:
            print("up")
        if self.states["down"] == True:
            print("down")
        if self.states["left"] == True:
            print("left")
        if self.states["right"] == True:
            print("right")

        if self.states["close"] == True:
            glfw.set_window_should_close(window.window, 1)
        
        