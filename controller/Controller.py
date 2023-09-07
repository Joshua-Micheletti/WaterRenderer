import glfw

from utils.singleton.Singleton import Singleton
from renderer.RendererManager import RendererManager

# class to handle inputs from the user and update the program logic accordingly (singleton)
class Controller(metaclass=Singleton):
    # constructor method
    def __init__(self):
        # store all the states in a dictionary and update them depending on the user inputs
        # then use the states to update the program logic accordingly
        self.states = dict()

        self.states["up"] = False
        self.states["down"] = False
        self.states["forward"] = False
        self.states["backwards"] = False
        self.states["left"] = False
        self.states["right"] = False
        self.states["close"] = False

        # variables to track the mouse movement
        self.first_mouse = True
        self.last_x = 0
        self.last_y = 0

    # function called by the window when a key is pressed
    def handle_key_press(self, key, mods):
        if key == glfw.KEY_W:
            self.states["forward"] = True
        if key == glfw.KEY_S:
            self.states["backwards"] = True
        if key == glfw.KEY_A:
            self.states["left"] = True
        if key == glfw.KEY_D:
            self.states["right"] = True
        if key == glfw.KEY_SPACE:
            self.states["up"] = True
        if key == glfw.KEY_LEFT_CONTROL:
            self.states["down"] = True
            
        if key == glfw.KEY_ESCAPE:
            self.states["close"] = True

    # function called by the window when a key is released
    def handle_key_release(self, key, mods):
        if key == glfw.KEY_W:
            self.states["forward"] = False
        if key == glfw.KEY_S:
            self.states["backwards"] = False
        if key == glfw.KEY_A:
            self.states["left"] = False
        if key == glfw.KEY_D:
            self.states["right"] = False
        if key == glfw.KEY_SPACE:
            self.states["up"] = False
        if key == glfw.KEY_LEFT_CONTROL:
            self.states["down"] = False

    # function called by the window when the cursor is moved
    def handle_mouse_movement(self, window, xpos, ypos):
        # if it's the first time that the mouse moves
        if self.first_mouse:
            # setup the last position variables with the current variables
            self.last_x = xpos
            self.last_y = ypos
            # keep track that the initialization already happened
            self.first_mouse = False

        # calculate the movement offset of the cursor on the screen
        xoffset = xpos - self.last_x
        # y axis is flipped
        yoffset = self.last_y - ypos

        # store the current position for the next frame
        self.last_x = xpos
        self.last_y = ypos

        # set the mouse sensitivity
        sensitivity = 0.1

        # calculate the cursor offset
        xoffset *= sensitivity
        yoffset *= sensitivity

        # apply the changes to turn the camera accordingly
        RendererManager().camera.turn(xoffset, yoffset)

    # method called on every frame to update the entities depending on the states
    def update(self, window, dt):
        # get a reference to the camera
        camera = RendererManager().camera

        # camera controls
        if self.states["forward"] == True:
            camera.move(1 * dt)
        if self.states["backwards"] == True:
            camera.move(-1 * dt)
        if self.states["left"] == True:
            camera.strafe(1 * dt)
        if self.states["right"] == True:
            camera.strafe(-1 * dt)
        if self.states["up"] == True:
            camera.lift(1 * dt)
        if self.states["down"] == True:
            camera.lift(-1 * dt)

        # control to close the window
        if self.states["close"] == True:
            glfw.set_window_should_close(window.window, 1)
        
        