
import turtle
from shape import Shape

class Window:
    """Class Window, here defines the window and the impact 
    on it when certain keys are pressed
    """
    def __init__(self, title, color, width, height):
        """Create a new window, a graphic interface
        
        Arguments:
            title {String} -- The title of the window
            color {String} -- The background color of the window
            width {int} -- The width in pixels of the window
            height {int} -- The height in pixels of the window
        """
        self.wn = turtle.Screen()
        self.wn.title(title)
        self.wn.bgcolor(color)
        self.wn.setup(width=width, height=height)
        self.wn.tracer(0)

    def actions(self, paddle_a, paddle_b):
        """The movement of the paddles
        
        Arguments:
            paddle_a {Shape} -- The paddle of the player A
            paddle_b {Shape} -- The paddle of the player B
        """
        self.wn.listen()
        self.wn.onkeypress(paddle_a.paddle_up, "w")
        self.wn.onkeypress(paddle_a.paddle_down, "s")
        self.wn.onkeypress(paddle_b.paddle_up, "Up")
        self.wn.onkeypress(paddle_b.paddle_down, "Down")

    def update(self):
        """Update the changes in the window, so they can be seen
        """
        self.wn.update()