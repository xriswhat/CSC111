# Lab8: User walks through a maze.
# Maze code provided by JORourke
# Chris Tan (no partner because didn't go to lab)
# In this maze, the user will use keyboard to control the movement of trump
# and help him get out off the maze

from random import shuffle, randrange
from graphics import *

#================================================================
def MakeStringMaze(w = 12, h = 8):
    ''' https://rosettacode.org/wiki/Maze_generation#Python
        (Author unknown, but based on
        https://en.wikipedia.org/wiki/Maze_generation_algorithm.)
        Default w,h=12,8. Returns a string.
    '''
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))

    # Create a string representation of the maze:
    s = ''
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s

def DrawMaze( s, win, w ):
    '''Convert string-maze s to graphics-maze.
       Assumes default w,h=12,8, and win coords +/-100.
       Author: JORourke
    '''
    # Break up s into rows:
    slist = s.split( '\n' )

    dx,dy = 5,10 # Mimic char aspect ratio, about 1::2
    Lgobjs=[] # List of graphics objects
    # i : controls x coord
    # j : controls y coord
    for j in range( len( slist ) ):
        row = slist[j]
        y = -j * dy + w - 2*dy
        for i in range( len(row) ):
            x = i * dx - w + 2*dx
            c = row[i] # c: single character
            if c=='|':
                Lgobjs.append( Line(Point(x,y+dy),Point(x,y-dy)) )
            elif c=='-':
                Lgobjs.append( Line(Point(x-dx,y),Point(x+dx,y)) )

    # Now draw all the graphic objects                              
    for gobj in Lgobjs:
        gobj.setWidth( 2 )
        gobj.setFill( 'DarkBlue' )
        gobj.draw( win )

    # Begin & End circs
    def BeginEnd( x, y ):
        print( 'Corner:', x, y)
        p = Point( x, y )
        circ = Circle( p, dx )
        circ.setFill( 'Pink' )
        circ.draw( win )

    BeginEnd( x, y+2*dy )
    BeginEnd( -w + dy, w - 2*dy )
#================================================================

def CreateTrump( win ):
    '''I will import a trump.gif into the file'''
    trump = Image(Point(90,-80), 'trump.gif')
    trump.draw(win)

    return trump


def TrumpMove( trump, win ):
    '''This function will let the users control the movement of Trump, for each
        move Trump makes, there will be a line drawn as the track line,
        If Trump reaches to the destination, the function will return False
    '''
    while True:
        k = win.checkKey()
        cent = trump.getAnchor()
        cx, cy = cent.getX(), cent.getY()
        
        if (k == 'Right'):
            trump.move(5,0)
        elif (k == 'Left'):
            trump.move(-5,0)
        elif (k == 'Up'):
            trump.move(0,5)
        elif (k == 'Down'):
            trump.move(0,-5)


        newcent = trump.getAnchor()
        ccx, ccy = newcent.getX(), newcent.getY()
        line = Line(Point(cx,cy), Point(ccx, ccy))
        line.draw(win)
        
        if ( -95 <= ccx <= -85 ) and ( 75 <= ccy <= 85 ):
            return False

        
def TrumpInDes( trump,win ):
    '''This is a function that will congradulate the user for getting to the
        destination
    '''
        text = Text(Point(0,-85), "GOOD JOB! TRUMP MADE IT!")
        text.setStyle('bold')
        text.setSize(18)
        text.setTextColor('red')
        text.draw(win)

        text2 = Text(Point(0,-95), "Click anywhere to close")
        text2.draw(win)

def main( ):
    win = GraphWin( 'Maze', 500, 500 )
    win.setBackground( 'cornflowerblue' )
    w = 100
    win.setCoords( -w, -w, w, w)

    # Create a maze as a string:
    s = MakeStringMaze( )
    print( s )
    # Convert string maze to graphics maze:
    DrawMaze( s, win, w )


    #-----------------------------------------

    
    trump = CreateTrump( win )
    TrumpMove( trump, win )
    TrumpInDes( trump,win )
    
    #-----------------------------------------

    print( 'Click in window to close' )
    win.getMouse( )
    win.close( )

main( )

