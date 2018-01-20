# FishClass.py
# Assaignment 9
# Chris Tan
# This program will create some fishes swimming in SpongeBob Squarepant's hometown
# with bubbles drifting up and down

from graphics import *
from random import randint, uniform

class Fish:

    def __init__(self, L, w, win):
        '''This function will generate a fish with tail, body and eye'''
    

        x,y = randint(-w,w), randint(-w,w)
        print('Init coords:', x, y)


        self.xspeed = uniform(-2,2)
        self.yspeed = 0

        if self.xspeed < 0:
        # when fish has negative speed, its will have eyes at left and tail at right           
            fishtail = Oval(Point(x+L/4, y-L/2), Point(x+L/2, y+L/2))
            r1 = randint(0,225)
            g1 = randint(0,225)
            b1 = randint(0,225)
            fishtail.setFill(color_rgb(r1,g1,b1))
            fishtail.draw(win)
            
            fishbody = Oval(Point(x-L/2,y-L/4), Point(x+L/2,y+L/4))
            r2 = randint(0,225)
            g2 = randint(0,225)
            b2 = randint(0,225)
            fishbody.setFill(color_rgb(r2,g2,b2))
            fishbody.draw(win)

            fisheye = Circle(Point(x-L/3, y), L/10)       
            fisheye.setFill('white')
            fisheye.draw(win)

        elif self.xspeed > 0:
        # when fish has negative speed, its will have eyes at right and tail at left           
            fishtail = Oval(Point(x-L/4, y-L/2), Point(x-L/2, y+L/2))
            r1 = randint(0,225)
            g1 = randint(0,225)
            b1 = randint(0,225)
            fishtail.setFill(color_rgb(r1,g1,b1))
            fishtail.draw(win)
            
            fishbody = Oval(Point(x-L/2,y-L/4), Point(x+L/2,y+L/4))
            r2 = randint(0,225)
            g2 = randint(0,225)
            b2 = randint(0,225)
            fishbody.setFill(color_rgb(r2,g2,b2))
            fishbody.draw(win)
            self.bodypoint = fishbody.getCenter()

            fisheye = Circle(Point(x+L/3, y), L/10)       
            fisheye.setFill('white')
            fisheye.draw(win)


        self.parts = [fishtail, fishbody, fisheye]
        

  
    def moveFish(self):
        '''This function wll make my fish swim at a random speed'''
        for parts in self.parts:
            parts.move(self.xspeed, self.yspeed)
                  
            
    def jumpFishup(self):
        '''This function will make my fish jump up'''
        for parts in self.parts:
            parts.move(0,1)
            

    def jumpFishdown(self):
        '''This function will make my fish jump down'''
        for parts in self.parts:
            parts.move(0,-1)


    def wrapFish( self, w ):
        '''This function will wrap my fish if it exceed the window'''
        for parts in self.parts:
            pcent = parts.getCenter()
            xc,yc = pcent.getX(), pcent.getY()
            xnew, ynew = xc, yc

            if xc > w:
                xnew = xc - 2*w
            elif xc < -w:
                xnew = xc + 2*w

            if (xnew != xc):
                parts.move(xnew - xc, 0)
            
class Bubble:

    def __init__(self, win, w):
        '''Generate a bubble'''
        x, y = randint(-w,w), randint(-w,w)

        self.bubble = Circle(Point(x,y),3)
        self.bubble.setFill('white')
        self.bubble.setOutline('black')
        self.bubble.draw(win)

        self.speedy = uniform(0.5,2)

    def bubbleMove(self):
        '''This function controls the move of the bubble'''
        self.bubble.move(0,self.speedy)


    def bubbleLeft(self):
        '''This function and the next function will make my bubble tremble'''
        self.bubble.move(-0.3,0)

    def bubbleRight(self):
        self.bubble.move(0.3,0)

    def bubbleWrap(self, w):
        '''This function will wrap my bubble if it run out of the window'''
        self.center = self.bubble.getCenter()
        self.centerx, self.centery = self.center.getX(), self.center.getY()
        
        if self.centery > w:
            self.bubble.move(0, -w-w)


class Sbsp:

    def __init__(self, win, w, name):
        '''Import characters from spoungebob squarepants and draw them in the window'''
        self.chx, self.chy = randint(-w, w), randint(-w, w)

        self.image = Image(Point(self.chx, self.chy), name)
        self.image.draw(win)

        self.speedx, self.speedy = uniform(-2,2),0
        
    def chrMove(self):
    
        self.image.move(self.speedx, self.speedy)
        

    def chrWrap(self, w):
        self.cent = self.image.getAnchor()
        self.centx = self.cent.getX()
        if self.centx > w:
            self.image.move( -w-w,0 )
        if self.centx < -w:
            self.image.move( 2*w,0 )
        
        
def main():
    win = GraphWin('FishSwimming', 500, 500, autoflush=False)
    background = Image(Point(0,0), 'background.gif')
    background.draw(win)
    w = 100
    win.setCoords(-w, -w, w, w)

    # draw nine fishes
    nfish = 9
    Lfishes = []
    for i in range(nfish):
        L = randint(10, 30)
        fish = Fish(L, w, win)
        Lfishes.append( fish )

    # import characters
    bob = Sbsp(win, w, 'sbsp.gif')
    plankton = Sbsp(win, w, 'plankton.gif')
    patrick = Sbsp(win, w, 'patrick.gif')
    sqward = Sbsp(win, w, 'sqward.gif')
    chrct = [] # creat a list and store my characters
    chrct.append(bob)
    chrct.append(plankton)
    chrct.append(patrick)
    chrct.append(sqward)

    # creat 30 bubbles
    Lbubbles = []
    for i in range(30):
        bubble = Bubble(win, w)
        Lbubbles.append( bubble )

    
    # animation loop
    count = 0
    while True:
        for fish in Lfishes:
            fish.moveFish()
            count = count + 1
            if count % 10 == 0:
                fish.jumpFishup()
            if count % 10 == 5:
                fish.jumpFishdown()
            fish.wrapFish(w)
 
                
        for bubbles in Lbubbles:
            bubbles.bubbleMove()
            count += 1
            if count % 2 == 0:
                bubbles.bubbleLeft()
            if count % 2 == 1:
                bubbles.bubbleRight()
            bubbles.bubbleWrap(w)
            
        for obj in chrct:
            obj.chrMove()
            obj.chrWrap(w)
            
        update()


main()
