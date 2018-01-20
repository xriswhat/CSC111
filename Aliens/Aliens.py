# Assignment 4
# Chris Tan
# In this program I will draw lots of aliens

from graphics import *
from random import *

########################################
### HEY! My Aliens are teletubbies!!!###
########################################

    

# I want to draw heads for the aliens
def Eye( x, y, scale, win ):
    '''This function will draw one of the three eyes for my little alien
    '''
    # scale = radius
    peye = Point( x, y )
    eye = Circle( peye, scale )
    eye.setFill( 'white' )
    eye.draw( win )
    # Now I want to draw pupils
    pupil = Circle( Point( x, y-scale+scale*0.7 ), scale*0.7)
    pupil.setFill( 'saddle brown' )
    pupil.draw(win)


# I will now draw mouth
def Mouth( x, y, scale, win ):
    '''This function will draw the mouth of my alien, which contains
       a rectangle and a oval
    '''
    # x is the central points of mouth while y is on the bottom line of mouth
    # mouth scale is the half of the width of the mouth
    oval_mth = Oval( Point( x-scale/2,y-scale/4 ), Point( x+scale/2, y+scale/4 ))
    oval_mth.setOutline( 'red4' )
    oval_mth.setFill( 'red4' )
    oval_mth.draw(win)
    mth_p1 = Point( x-scale/2,y )
    mth_p2 = Point( x+scale/2, y+scale/4 )
    mouth = Rectangle( mth_p1, mth_p2 )
    mouth.setFill( 'burlywood1' )
    mouth.setOutline( 'burlywood1' )
    mouth.draw( win )

# I will now draw Antenna
def Antenna( x, y, scale, win ):
    '''This function will draw the antenna for my alien
       which contains two circles and a rectangle
    '''
    # the Antenna contains two circles and a ractangle
    # scale in the circle is the radius

    # attributions of the bar:
    height = 1.2 * scale
    width = 0.3 * scale
    
    circle_out = Circle( Point( x, y+height ), scale )
    circle_in = Circle( Point( x, y+height ), scale/1.5 )
    circle_out.setFill('firebrick')
    circle_out.draw( win )
    circle_in.setFill('white') 
    circle_in.draw( win )

    rec = Rectangle( Point( x-width/2,y-height*0.8 ), Point( x+width/2,y+height/2.5 ))
    rec.setOutline('firebrick')
    rec.setFill('firebrick')
    rec.draw( win )

# Also my aliens have ears
def Ears( x, y, face_radius, win ):
    '''This Function will draw the ears for my alien
       which contains two ovals
    ''' 
    # the x and y are the central point of the face, so the points of the ears are x -/+ radius_of_face
    # the scale is the radius of head, the scale of the ear is 1/4 of the face 
    P_ear_l = Point(x-face_radius,y)
    P_ear_r = Point(x+face_radius,y)
    scale = face_radius / 2
    ear_l = Circle( P_ear_l,scale )
    ear_r = Circle( P_ear_r,scale )
    ear_l.setOutline('firebrick')
    ear_r.setOutline('firebrick')
    ear_l.setFill('firebrick')
    ear_r.setFill('firebrick')
    ear_l.draw(win)
    ear_r.draw(win)
    

def Face( x, y, scale, win ):
    '''This function draws a face for my alien
       And the eyes, mouth, antenna functions are invoked here
    '''
    center = Point ( x, y )
    face = Circle( center, scale ) # radius = scale
    face.setFill( 'burlywood1' )
    face.draw( win )

    
    eye_scale = scale * 0.2
    ex = x
    ey = y + eye_scale
    Eye( ex, ey + eye_scale/2, eye_scale, win )
    Eye( ex - 2.5 * eye_scale, ey - eye_scale, eye_scale, win )
    Eye( ex + 2.5 * eye_scale, ey - eye_scale, eye_scale, win )

    mouth_scale = scale * 0.8
    mx = x
    my = y - mouth_scale * 0.6
    Mouth( mx, my, mouth_scale, win )


    antenna_scale = scale/2
    Ax = x
    Ay = y + scale + antenna_scale
    Antenna( Ax, Ay, antenna_scale, win )
    

def AlienHead( x, y, head_scale, win ):
    '''This is a function drawing the head of the alien,
       And invokes the Ear and Face functions
    '''
    P_head_center = Point ( x,y )
    head = Circle( P_head_center, head_scale )
    head.setFill('firebrick')
    head.draw( win )

    face_scale = head_scale * 0.8
    # Because I dont want the ear obscured the face so I'm putting the ear codes here
    Ears( x, y, face_scale, win )
    Face( x, y , face_scale, win )



def main():
    '''This is the main function'''
    win = GraphWin('My Alien', 500, 500)
    win.setCoords(-100,-100,100,100)
    # The background is the picture of teletubbies' playground
    playground = Image(Point( 0, 0 ), 'playground.gif')
    playground.draw(win)

    for i in range (10):
        x = randint( -100, -10 )
        y = randint( 20, 50 )
        head_scale = randint( 0,8 )
        AlienHead( x, y, head_scale, win )

    for n in range (7):
        x = randint( -100, 100 )
        y = randint( 0,20 )
        head_scale = randint( 8,15 )
        AlienHead( x, y, head_scale, win )

    for p in range (5):
        x = randint( -100,100 )
        y = randint( -50,0 )
        head_scale = randint( 15,25 )
        AlienHead( x, y, head_scale, win )

    for q in range (5):
        x = randint( -100,100 )
        y = randint( -100,-50 )
        head_scale = randint( 25,32 )
        AlienHead( x, y, head_scale, win )

    # In the last step I want to add logo for my projrct
    logo = Image( Point( -50,75 ), 'Logo.gif')
    logo.draw(win)
        



    win.getMouse()
    win.close()

main()

    
