# module to get the parameters from the command line
import sys
# module to create the window
import glfw

# local modules
from utils.parsers import argument_parser as ap
from utils.timer.Timer import Timer
from window.Window import Window
from renderer.Renderer import Renderer
from controller.Controller import Controller

def main():
    # parse the arguments from the command line
    ap.parse_arguments(sys.argv)

    # window object
    window = Window()
    # renderer object
    renderer = Renderer()
    # controller object
    controller = Controller()

    # execution timer
    frametime = Timer()
    # timer to limit how often the timer should be printed
    print_timer = Timer()

    dt = 0
    
    # game loop
    while not glfw.window_should_close(window.window):
        controller.update(window, dt)

        renderer.render()
        
        # refresh the screen and handle events
        glfw.swap_buffers(window.window)
        glfw.poll_events()
        
        # print the execution time
        if print_timer.elapsed() > 2000:
            frametime.elapsed(True, True)
            print_timer.reset()


        dt = frametime.elapsed()
        frametime.reset()
        
    glfw.terminate()
            

if __name__ == "__main__":
    main()