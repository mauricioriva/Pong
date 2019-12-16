import turtle

class Shape:
    """Class Shape generate all the entities with a certain behaviour
    so its the same as in the classic Pong game
    """
    def __init__(self, posx, posy, width=5, length=1, 
                shape="square", color="white", dx=0.1, dy=0.1):
        """Creates a Form, such as a paddle, a ball, or text

        Arguments:
            posx {float} -- The x coordinate
            posy {float} -- The y coordinate
        
        Keyword Arguments:
            width {int} -- The width of the shape (default: {5})
            length {int} -- The length of the shape (default: {1})
            shape {str} -- The shape for the object (default: {"square"})
            color {str} -- The color of the shape (default: {"white"})
            dx {float} -- The speed of the ball (default: {0.1})
            dy {float} -- The speed of the ball (default: {0.1})
        """
        self.action = turtle.Turtle()
        self.action.speed(0)
        self.action.shape(shape)
        self.action.color("white")
        self.action.shapesize(stretch_wid=width, stretch_len=length)
        self.action.penup()
        self.action.goto(posx,posy)
        self.ball_dx = dx
        self.ball_dy = dy

    def paddle_up(self) -> None:
        """Move the paddle 20 pixels up
        """
        if self.action.ycor() > 240:
            pass
        else:
            y = self.action.ycor()
            y += 20
            self.action.sety(y)

    def paddle_down(self) -> None:
        """Move the paddle 20 pixels down
        """
        if self.action.ycor() < -240:
            pass
        else:
            y = self.action.ycor()
            y -= 20
            self.action.sety(y)

    def xcor(self):
        """Getter for the x coordinate of the shape
        
        Returns:
            float -- The x coordinate of the shape
        """
        return self.action.xcor()

    def ycor(self):
        """Getter for the y coordinate of the shape
        
        Returns:
            float -- The y coordinate of the shape
        """
        return self.action.ycor()

    def setx(self, x):
        """Setter for the x coordinate of the shape
        
        Arguments:
            x {float} -- The new x coordinate of the shape
        """
        self.action.setx(x)

    def sety(self, y):
        """Setter for the y coordinate of the shape
        
        Arguments:
            y {float} -- The new y coordinate of the shape
        """
        self.action.sety(y)

    def increase_dx(self):
        """Increase the dx of the ball
        """
        self.ball_dx += 0.02

    def increase_dy(self):
        """Increase the dy of the ball
        """
        self.ball_dy += 0.02

    def decrease_dx(self):
        """Decrease the dx of the ball
        """
        self.ball_dx -= 0.02

    def decrease_dy(self):
        """Decrease the dy of the ball
        """
        self.ball_dy -= 0.02