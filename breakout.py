from pygame_functions import *
import random

setAutoUpdate(False)
WIDTH=1000
HEIGHT=700
GRAVITY=0.001
screenSize(WIDTH,HEIGHT)

LIVES = 3

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
        

    def move(self,LIVES):
        
        self.yspeed+=GRAVITY
        self.ypos+=self.yspeed
        self.xpos+=self.xspeed
        if self.ypos>=HEIGHT:
            self.yspeed=-self.yspeed
            self.ypos=HEIGHT-self.radius
            if self.colour=="red":
                LIVES-=1
                self.xpos=500
                self.ypos=400
            
        

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
        return LIVES
    def collide(self):
            self.xspeed=-self.xspeed
            self.yspeed=-self.yspeed

#W 75
#H 50
class BRICK:

    def __init__(self,xpos,ypos,length,width,health,colour):
        self.xpos=xpos
        self.ypos=ypos
        self.height=length
        self.width=width
        self.health=health
        self.colour=colour
        self.active = True

    def draw(self):
        if self.active:
            drawRect(self.xpos, self.ypos, self.width, self.height, self.colour)

    def detectHit(self,balls):
        for ball in balls:
            '''
            max_x=self.xpos+(self.width//2)
            min_x=self.xpos-(self.width//2)

            max_y=self.ypos+(self.length//2)
            min_y=self.ypos-(self.width//2)

            ball_y_max=ball.ypos+ballradius
            ball_y_min=ball.ypos-ballradius

            ball_x_max=ball.xpos+ballradius
            ball_x_min=ball.xpos-ballradius
            
            if min_x<=ball_x_min<=max_x or min_x<=ball_x_max<=max_x:
                
                if  min_y<=ball_y_min<=max_y or min_y<=ball_y_max<=max_y:
            '''

            if self.xpos<=ball.xpos <=self.xpos + self.width and self.active:
                if self.ypos<= ball.ypos<=self.ypos+self.height:
                    ball.yspeed*=-1
                    #ball.ypos = ball.ypos+ball.radius
                    
                    

                    return True   
        return False 

                    

    def update(self, ball):
        self.draw()
        
        if self.detectHit(ball) and self.health<=0:
            self.active=False
        else:
            self.health=self.health-1
        
                

        
class BAT(BRICK): # inherits brck class
    
    def __init__(self, xpos,ypos,length,width,health,colour):
        super().__init__(xpos,ypos,length,width,health,colour)
        self.width=10000
        del self.health
        self.height=25
        self.active = True
    
    def update(self, balls):
        self.active = True
        self.draw()
        self.detectHit(balls)
            

        #if keyPressed("D"):
        #    self.xpos+=10
        #elif keyPressed("A"):
        #    self.xpos-=10
        self.xpos=mouseX()-self.width//2


class MULTIBRICK(BRICK):

    def update(self, balls):
        self.draw()
        if self.detectHit(balls) and self.health<=0:
            self.active=False
            balls.append(BALL(self.xpos, self.ypos, "yellow",4,5,20))
        else:
            self.health=self.health-1


#setBackgroundColour("darkgreen")
balldiameter=50
ballradius = balldiameter//2

balls = []
colours = ["red","orange","blue","green","red","orange","blue","green"]
balls.append(BALL(550,650,"red",4,-5,20))
bricks = [MULTIBRICK(x,y,45, 75, 1, col) for x in range(0,WIDTH,77) for col,y in zip(colours,range(100,200, 47))]
'''
for i in range(5):
    randompos = random.randint(0,len(bricks))
    removed = bricks.pop(randompos)
    bricks.append()
    '''
bat = BAT(HEIGHT-100, (WIDTH//2)+50, 600,100 ,0,"red")

livesLabel = makeLabel(f"Lives: {LIVES}",23,10,10,"white")
deathLabel = makeLabel("GAME OVER", 50, 350, 450, "white")
showLabel(livesLabel)
running = True
while running:
    clearShapes()
    changeLabel(livesLabel, f"Lives: {LIVES}")
    if LIVES<=0:
        showLabel(deathLabel)
        running = False
    for b in bricks:
        b.update(balls)
    print(LIVES)
    for b in balls:
        if b == balls[0]:
            LIVES=b.move(LIVES)
        else:
            b.move(LIVES)
    
    bat.update(balls)
    #print(balls)
    tick(60)
    updateDisplay()
    
endWait()
