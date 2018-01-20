# Assaignment 8
# Chris Tan
# This is a crude version of Breakout, a ball is bouncing around in the window
# a paddle is at the bottom and some bricks on the top. Each time when the user
# catch the ball, the score will be added 1, if the ball fall off the window
# five times, the user will lose the game



from graphics import *
from random import randint, uniform


def BuildBricks( xr,yr,win,bricklist ):
    '''This function will help me build up bricks on the top'''
    for i in range(8):
        brick = Rectangle(Point(xr+20*i,yr),Point(xr+20+20*i,yr+10))
        brick.setFill('steelblue4')
        brick.setOutline('black')
        brick.draw(win)

        # I make a list store the bricks
        bricklist.append(brick)

    
def MovePaddle( paddle, win ):
    '''This is a function that control the move of keys'''
    while True:
        p1, p2 = paddle.getP1(), paddle.getP2()
        p1x,p1y = p1.getX(), p1.getY()
        p2x,p2y = p2.getX(), p2.getY()
        k = win.checkKey()

        if k == 'Right' and (p1x<=85) and (p2x<=85):
            paddle.move(5,0)
        elif k == 'Left' and (p1x>=-85) and (p2x>=-85):
            paddle.move(-5,0)

        return paddle

    
def BallOnPaddle( ball, paddle ):
    '''This function will test whether the paddle catches the ball or not'''
    paddletop = paddle.getP2()
    p1,p2 = paddletop.getX()-20, paddletop.getX()

    ballcenter = ball.getCenter()
    cx,cy = ballcenter.getX(), ballcenter.getY()-5

    # If the ball in the range of the paddle, return True
    if ( cy <= -85 ) and ( p1 <= cx <= p2 ):
        return True
    

def BallTouchColum( ball ):
    '''This function will test if the ball hits the wall or not'''
    ballcenter = ball.getCenter()
    cx,cy = ballcenter.getX(), ballcenter.getY()

    if ( cx >= 85 ) or ( cx <= -85 ) or ( cy >= 75 ):
        return True

def BallFallOff( ball ):
    '''This function will test if the ball fall off the window'''
    ballcenter = ball.getCenter()
    cx,cy = ballcenter.getX(), ballcenter.getY()

    if cy <= -99 :
        return True

def ReflectBall1( paddle, ball, sx, sy ):
    '''This is a reflection function that make the ball reflect from the paddle'''
    ballcenter = ball.getCenter()
    cx,cy = ballcenter.getX(), ballcenter.getY()

    paddletop = paddle.getCenter()
    p1,p2 = paddletop.getX(), paddletop.getY()+7.5

    
    ball.move(p1-cx, p2-cy)
    sx = sx+0.1
    sy = -sy+0.1   

    # Update the shift speed
    return sx,sy


def ReflectBall2( ball, sx, sy ):
    '''This is a reflection function that make the ball reflect from the three
        colums( the celling, the left and the right)
    '''
    ballcenter = ball.getCenter()
    cx,cy = ballcenter.getX(), ballcenter.getY()

    if cx >= 85:
        ccx = 85
        ccy = cy
        sx = -sx
        sy = sy
    if cy >= 75:
        ccx = cx
        ccy = 75
        sx = sx
        sy = -sy
    if cx <= -85:
        ccx = -85
        ccy = cy
        sx = -sx
        sy = sy

    ball.move(ccx-cx, ccy-cy)

    # Update the shift speed
    return sx,sy


def BallTouchBricks( ball, bricklist, sx, sy ):
    '''This is a function that test if ball hits the brick'''
    for bricks in bricklist:
        p1,p2 = bricks.getP1(), bricks.getP2()
                
        ballcenter = ball.getCenter()
        cx,cy = ballcenter.getX(), ballcenter.getY()

        p1x,p1y = p1.getX(), p1.getY()
        p2x,p2y = p2.getX(), p2.getY()

        # if the ball hits the bricks, return true
        if ( p1x < cx < p2x ) and ( p1y-5 <= cy <= p1y-4):
        
            return True


def BriskRemove( ball, bricklist, sx, sy ):
    '''If the ball hits the brick, remove the brick from the list'''
    for bricks in bricklist:
        p1,p2 = bricks.getP1(), bricks.getP2()
                
        ballcenter = ball.getCenter()
        cx,cy = ballcenter.getX(), ballcenter.getY()

        p1x,p1y = p1.getX(), p1.getY()
        p2x,p2y = p2.getX(), p2.getY()

        if ( p1x < cx < p2x ) and ( p1y-5 <= cy <= p1y-2):
            bricks.undraw()
            bricklist.remove( bricks )
            ball.move(p1x+10-cx,p1y-6-cy)
            sx = sx
            sy = -sy
            
            # return a new shift speed
            return sx, sy
    
        
    
    
def main():
    win = GraphWin('BreakOut', 500, 500)
    win.setBackground('skyblue2')
    w = 100
    win.setCoords( -w,-w,w,w )


    
    # Set up background
    Colum1 = Rectangle(Point(-100,-100), Point(-90, 90))
    Colum2 = Rectangle(Point(90,-100), Point(100,90))
    Colum3 = Rectangle(Point(-100,80), Point(100,90))
    Colum1.setFill('skyblue4')
    Colum2.setFill('skyblue4')
    Colum3.setFill('skyblue4')
    Colum1.draw(win)
    Colum2.draw(win)
    Colum3.draw(win)
    
    # Set up score board
    num = 0
    score = Text(Point(-70, 95), 'Score:' )
    score.setSize(18)
    score.draw(win)
    scorenum = Text(Point(-50,95), num)
    scorenum.setSize(18)
    scorenum.draw(win)
    
    # Set up life count board
    num2 = 5
    life = Text(Point(40,95),'Life:')
    life.setSize(18)
    life.draw(win)
    lifenum = Text(Point(60,95), num2)
    lifenum.setSize(18)
    lifenum.draw(win)

    #Set up bricks
    bricklist = []
    BuildBricks( -80, 20, win, bricklist )
    BuildBricks( -80, 30, win, bricklist )
    BuildBricks( -80, 40, win, bricklist )
    BuildBricks( -80, 50, win, bricklist )
    BuildBricks( -80, 60, win, bricklist )

    
    #Set up paddle
    paddle = Rectangle(Point(-10,-90), Point(10,-85))
    paddle.setFill('white')
    paddle.draw(win)


    #Set up ball
    ball = Circle(Point(0,-80), 5)
    ball.setFill('royalblue4')
    ball.draw(win)

    #Set up Instruction
    instruction = Rectangle(Point(-70,-40),Point(70,40))
    instruction.setFill('cornsilk2')
    instruction.draw(win)
    literal1 = Text(Point(0,0), 'Use Left and Right to control the movement of the ball')
    literal2 = Text(Point(0,-20), 'Press . to quit game(give up)')
    literal1.draw(win)
    literal2.draw(win)
    
    p = win.getMouse()
    if p:
        instruction.undraw()
        literal1.undraw()
        literal2.undraw()        
        sx,sy = uniform(-0.5,0.5), uniform(0,0.5)
        while True:
            k = win.checkKey()
            if k == 'period':
                break
            else:
                ball.move(sx,sy)
                MovePaddle( paddle, win )
                if BallOnPaddle( ball, paddle ):
                   sx,sy = ReflectBall1( paddle, ball, sx, sy )
                   scorenum.undraw()
                   num = num +1
                   scorenum = Text(Point(-50,95), num)
                   scorenum.setSize(18)
                   scorenum.draw(win)
                if BallTouchColum( ball ):
                   sx,sy = ReflectBall2( ball, sx, sy )
                if BallTouchBricks( ball, bricklist, sx, sy ):
                   sx, sy = BriskRemove( ball, bricklist, sx, sy )
                if BallFallOff( ball ):
                   ball.undraw()
                   print('x')
                   lifenum.undraw()
                   pcnt = paddle.getCenter()
                   pcntx, pcnty = pcnt.getX(), pcnt.getY()
                   ball = Circle(Point(pcntx,pcnty+100),5)
                   ball.setFill('royalblue4')
                   ball.draw(win)

                   num2 = num2 - 1
                   lifenum = Text(Point(60,95), num2)
                   lifenum.setSize(18)
                   lifenum.draw(win)
                if num2 == 0:
                    print('loser!')
                    break
              


        loser = Image(Point(0,0),'loser.gif')
        loser.draw(win)
        click = Text(Point(0,-50),'Click')
                
                
            
    win.getMouse()
    win.close()

main()
            
            
            
        
            
        



    
