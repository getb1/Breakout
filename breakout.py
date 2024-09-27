from pygame_functions import *
import random

setAutoUpdate(False)
WIDTH=1000
HEIGHT=700
GRAVITY=0
screenSize(WIDTH,HEIGHT)

class BALL:

    def __init__(self,xpos,ypos,colour,yspeed,xspeed,size):
        #atributes
        self.xpos=xpos
        self.ypos=ypos
        self.xspeed=yspeed
        self.yspeed=xspeed
        self.diameter=size
        self.radius = size//2
        self.colour = colour
        

    def move(self):
        self.yspeed+=GRAVITY
        self.ypos+=self.yspeed
        self.xpos+=self.xspeed
        if self.ypos>=HEIGHT:
            self.yspeed=-self.yspeed
            self.ypos=HEIGHT-self.radius
        if self.ypos<=0:
            self.yspeed=-self.yspeed
            self.ypos=0+self.radius
        if self.xpos>=WIDTH:
            self.xspeed=-self.xspeed
            self.xpos=WIDTH-self.radius
        if self.xpos<=0:
            self.xspeed=-self.xspeed
            self.xpos=self.radius
        drawEllipse(self.xpos,self.ypos,self.diameter,self.diameter,self.colour)

    def collide(self):
            self.xspeed=-self.xspeed
            self.yspeed=-self.yspeed

#W 75
#H 50
class BRICK:

    def __init__(self,xpos,ypos,length,width,health,colour):
        self.xpos=xpos
        self.ypos=ypos
        self.length=length
        self.width=width
        self.health=health
        self.colour=colour

    def draw(self):
        drawRect(self.xpos, self.ypos, self.width, self.length, self.colour)

    def detectHit(self,ball:BALL):
        
        max_x=self.xpos+(self.width//2)
        min_x=self.xpos-(self.width//2)

        max_y=self.ypos+(self.length//2)
        min_y=self.ypos-(self.width//2)

        ball_y_max=ball.ypos+ballradius
        ball_y_min=ball.ypos-ballradius

        ball_x_max=ball.xpos+ballradius
        ball_x_min=ball.xpos-ballradius
        print(max_y,min_y)
        if min_x<=ball_x_min<=max_x or min_x<=ball_x_max<=max_x:
            #print("HELLO")
            if min_y<=ball_y_min<=max_y or min_y<=ball_y_max<=max_y:
                ball.collide()
                self.colour("black")
                

        





#setBackgroundColour("darkgreen")
balldiameter=50
ballradius = balldiameter//2

balls = []
colours = ["red","orange","blue","green","red","orange","blue","green"]
balls.append(BALL(950,650,"red",8,10,20))
bricks = [BRICK(x,y,45, 75, 1, col) for x in range(0,WIDTH,77) for col,y in zip(colours,range(100,1000, 47))]
while True:
    clearShapes()
    for b in balls:
        b.move()
    
    for b in bricks:
        b.draw()
        b.detectHit(balls[0])
    
    
    tick(1)
    updateDisplay()
    

    


    

    

endWait()