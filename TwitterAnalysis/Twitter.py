# Assaignment 6
# Chris Xiaoyue Tan
# This program will will search through a Twitter-stream file of
# about 9000 tweets that Joe gathered on October 20,23,24.

def task_1( content ):
    '''This is a function that meets the requirement for the first task
    which is to count the frequency of 'trump','clinton' and 'halloween' '''
    trump_count = 0
    clinton_count = 0
    halloween_count = 0
    college_count = 0
    for line in content.readlines():
         if line [ :4 ] == 'text':
            line = line[ 5: ]
            line = line.lower()
##    In order to have the strings in any combination of upper or lowercase,
##    I want to convert them all into lowercases and so that my words and them
##    will all be lowercased
            trump_count = trump_count + line.count( 'trump' )
            clinton_count = clinton_count + line.count('clinton')
            halloween_count = halloween_count + line.count('halloween')
            college_count = college_count + line.count('smithcollege')
            if 'trump' in line:
                print (line)
        
        
    print ('\n')
    print ('trump: occurs', trump_count, 'times in tweets text' )
    print ('clinton: occurs', clinton_count, 'times in tweets text' )
    print ('halloween: occurs', halloween_count, 'times in tweets text')
    print (college_count)
        


def task_2( content ):
    '''This is a funtion that meets the requirement for task 2, which is to count
    the number of unique hashtags, and print out the last ten hashtags according
    alphabetically.'''
    unq_hashtag = [ ]
    for line in content.readlines():
        line = line.lower()
        if line[ :8 ] == 'hashtags' :
            line_ls = eval ( line[ 10: ] )
            for obj in line_ls:
                if obj not in unq_hashtag:
                    unq_hashtag.append( obj )

    unq_hashtag.sort()
    num_of_content = len(unq_hashtag)
    print (num_of_content, 'unique hashtags')
    print ('Last 10 alphabetically:')
    print ('-'*30)
    for word in unq_hashtag [ -10: ]:
        print (word)


def extra( content ):
    '''This is the extra task which will count out the 10 most commonly occurring
    hashtags'''

    print('10 most commonly occurring hashtags:')
    print('-' * 30)

    list = [ ]
    for line in content.readlines():
        line = line.lower()
        if line[ : 8 ] == 'hashtags':
            line_ls = eval( line[ 10: ] )
            if len(line_ls) > 0:
                for word in line_ls:
                    list.append( word )


    final_list = []
    for words in list:
        pair = []
        frqc = list.count( words )
        pair.append( frqc )
        pair.append( words )
        if pair not in final_list:
            final_list.append( pair )
    final_list.sort()
    final_list.reverse()
    for obj in final_list[ :10 ]:
        print( obj[0], obj[1] )
        


def main():
    '''In main function, in order to call all three tasks, I will open the file
    three times and read them and close them'''
    filename = input('filename:')
    content = open( filename, 'r')
    task_1( content )
    content.close

    print('\n')

    content = open( filename, 'r')
    task_2( content )
    content.close()

    print('\n')
    
    content = open( filename, 'r')
    extra( content )
    content.close()           
            

    

main()
    
