# Assaignment 7
# Chris Tan
# This is a program that will read in a filename of a .txt file
# from the user, and print out all the tied-for-longest words in
# the text, preferrably in alphabetical order.

def CleanUp( text ):
    '''This is a function that will help me clean uo some punctuations i dont want'''
    text = text.lower()
    text = text.replace('.' , ' ' )
    text = text.replace(',' , ' ' )
    text = text.replace('*' , ' ' )
    text = text.replace('?' , ' ' )
    text = text.replace('!' , ' ' )
    text = text.replace('(' , ' ' )
    text = text.replace(')' , ' ' )
    text = text.replace(';' , ' ')
    text = text.replace('--' , ' ' )
    text = text.replace('-' , '' )
    text = text.replace('\'', '' )

    return text
    

def main():
# I'm getting the text from the users
    file = input("Hey, please tell me which file are you looking for:" )
    text_ = open(file, 'r')
    text = text_.read()
    text_.close()

    text = CleanUp( text )

    w_lst = text.split( )
    wlen_lst = []
    num_wlen_lst = []
    for word in w_lst:
        pair = []
        wordlen = len( word )
        pair.append(wordlen)
        pair.append(word)
        wlen_lst.append(pair)
        num_wlen_lst.append(wordlen)

    wlen_lst.sort()
    num_wlen_lst.sort()
    wlen_lst.reverse()
    num_wlen_lst.reverse()

    cnt = num_wlen_lst.count( num_wlen_lst[0] )

# The following lines are checking that if I thould use
# Here ARE all the words of length....
# Or
# Here IS the word of length....
    if num_wlen_lst[ 0 ] == num_wlen_lst[ 1 ]:
        print('The longest words in the text have', num_wlen_lst[0], 'letters')
        print('Here are all the words of length', num_wlen_lst[0])
        print('-'*35)
        for pair in wlen_lst[:cnt]:
            print(pair[1])
    else:
        print('The longest words in the text have', num_wlen_lst[0], 'letters')
        print('Here is the words of length', num_wlen_lst[0])
        print('-'*35)
        for pair in wlen_lst[:cnt]:
            print(pair[1])
        


main()
    

    
        

    





    
