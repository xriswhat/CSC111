# Assaignment 10 For Extra Credits
# Chris Xiaoyue Tan
# This home work uses recursion to generate more complex sentences


from random import randint


def ReadInDict( ):
    '''Reads in a list of words, one category per line
       The 0-th element of the list is the category name.
       The filename is hardwired to dict.txt.
    '''
    # Always open the same file:
    f = open( 'dictextended.txt', 'r' )

    # The lists will all be global variables,
    # so can be accessed w/o passing as parameter:
    global nouns
    global propernouns
    global transverbs
    global intransverbs
    global dets
    global adjs
    global preps
    global advs
    global passverbs


    # Assumes one list per line
    for line in f:
        # Turn line into a list of words:
        L = line.split( )
##        print(L)
        # Use 0th element to set appropriate variable:
        if L[0]=='nouns':
            nouns = L[1:]
        elif L[0] == 'transverbs':
            transverbs = L[1:]
        elif L[0] == 'propernouns':
            propernouns = L[1:]
        elif L[0] == 'intransverbs':
            intransverbs = L[1:]
        elif L[0] == 'dets':
            dets = L[1:]
        elif L[0] == 'adjs':
            adjs = L[1:]
        elif L[0] == 'preps':
            preps = L[1:]
        elif L[0] == 'advs':
            advs = L[1:]
        elif L[0] == 'passverbs':
            passverbs = L[1:]
        else:
            print( 'ReadInDict: Error' )
            
    f.close( )

    # Print out lists:
    print( 'ReadInDict finished:' )
    print( 30*'-' )
    print( 'nouns:', nouns )
    print( 'propernouns:', propernouns )
    print( 'transverbs:', transverbs )
    print( 'intransverbs:', intransverbs)
    print( 'dets:', dets )
    print( 'adjs:', adjs )
    print( 'preps:', preps )
    print( 'advs:', advs )
    print( 30*'-' )

def NP( depth ):
    '''Generate a list of categories contituting a noun phrase'''
    
    print ( depth * ' ', 'np, depth=', depth )
    if depth > dmax:
        return []

    x = randint( 1,2 )

    if (x == 1) or (depth + 1 >= dmax):
        return XN( depth+1 )

    else:
        return XN( depth+1 ) + PP( depth+1 )

def VP( depth ):
    '''Generate a list of categories contituting a verb phrase'''
    
    print ( depth * ' ', 'vp, depth=', depth)
    if depth > dmax:
        return []

    x = randint( 1, 2 )

    if (x == 1) or (depth + 1 >= dmax):
        return XV( depth+1 )

    else:
        return advs[randint(0,(len(advs)-1))]+' ' + XV( depth+1 )

def XN( depth ):
    '''Generate a list of categories contituting a (special) noun'''
    
    print ( depth*' ', 'xn, depth=', depth )
    if depth > dmax:
        return []

    x = randint( 1, 4 )

    if (x == 1) or (depth + 1 >= dmax):
        return dets[randint(0,(len(dets)-1))]+' ' + nouns[randint(0,(len(nouns)-1))]+' '
    elif ( x == 2 ):
        return dets[randint(0,(len(dets)-1))]+' ' + adjs[randint(0,(len(adjs)-1))]+' ' + nouns[randint(0,(len(nouns)-1))]+' '
    if (x == 3):
        return propernouns[randint(0,(len(propernouns)-1))]+' '
    else:
        return adjs[randint(0,(len(adjs)-1))]+' ' + propernouns[randint(0,(len(propernouns)-1))]+' '
    
def PP( depth ):
    '''Generate a list of categories contituting a prep phrase'''

    print ( depth*' ', 'pp, depth=', depth)
    if depth > dmax:
        return []

    return preps[randint(0,(len(preps)-1))]+' ' + XN( depth+1 )

def XV( depth ):
    '''Generate a list of categories contituting a special verb'''

    print ( depth*' ', 'xv, depth=', depth)
    if depth > dmax:
        return []

    x = randint( 1, 2 )
    if (x == 1) or (depth+1 >= dmax):
        return intransverbs[randint(0,(len(intransverbs)-1))]+' '
    else:
        return transverbs[randint(0,(len(transverbs)-1))]+' ' + NP( depth+1 )

def S( depth ):
    '''Generate a list of categories constituting a sentence'''
    
    print( depth*' ', 's, depth=', depth )
    if depth < dmax:

        x = randint(1,3)
        if (x == 1):
            return NP( depth+1 ) + VP( depth+1 )
        elif (x == 2):
            return passverbs[randint(0,(len(passverbs)-1))]+' ' + NP( depth +1 )+ VP( depth+1 ) +'?'
        else:
            return preps[randint(0,(len(preps)-1))]+' ' + NP( depth+1 ) + ',' + NP( depth+1 )+ VP( depth+1)

     
def main( ):
    '''Generate random sentences recursively'''

    # Read in the dictionary of words by category
    # NB: nouns etc. are global lists
    ReadInDict( )

    global dmax
    nsents,dmax = eval(input('nsents,dmax= '))
    

    for times in range(nsents):
        Lcats = S(1)
        print('Sentence: ',Lcats, '\n', 30*'-')

main( )
