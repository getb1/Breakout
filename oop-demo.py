from pygame_functions import *
import random

setAutoUpdate(False)
HEIGHT=1000
WIDTH=700
GRAVITY=1
screenSize(HEIGHT,WIDTH)

class BALL:

    def __init__(self,xpos,ypos,colour):
        #atributes
        self.xpos=xpos
        self.ypos=ypos
        self.xspeed=random.randint(-10,10)
        self.yspeed=random.uniform(0,10)
        self.colour = colour
        

    def move(self):
        self.yspeed+=GRAVITY
        self.ypos+=self.yspeed
        self.xpos+=self.xspeed
        if self.ypos>=WIDTH:
            self.yspeed=-self.yspeed
            self.ypos=WIDTH-ballradius

        if self.xpos>=HEIGHT:
            self.xspeed=-self.xspeed
            self.xpos=HEIGHT-ballradius
        if self.xpos<=0:
            self.xspeed=-self.xspeed
            self.xpos=ballradius
        drawEllipse(self.xpos,self.ypos,balldiameter,balldiameter,self.colour)

    def collide(self):
            self.xspeed=-self.xspeed
            self.yspeed=-self.yspeed


def check_bounce(balls):
    poses = [(b.xpos,b.ypos) for b in balls]


#setBackgroundColour("darkgreen")
balldiameter=50
ballradius = balldiameter//2

balls = [BALL(random.randint(50,WIDTH-50), random.randint(0,HEIGHT//2), (random.randint(0,255),random.randint(0,255),random.randint(0,255))) for i in range(1000)]

while True:
    clearShapes()
    for b in balls:
        b.move()
    
    
    tick(60)
    updateDisplay()
    

    


    

    

endWait()