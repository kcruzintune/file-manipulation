# -*- coding: utf-8 -*-

###############################################################################
def prod (start, stop):   
   '''
   This function returns the product of the integers start through stop 
   inclusive
   ''' 
   mult = 1
   #mult is 1 so the first number that is multiplied by start value will be
   #that number, which will also update as the loop continues.
   for i in range (start, stop + 1):
       #This lists the range of numbers based on the input given for start and 
       #stop
        mult *= i
        #initially mult is 1 so the first value of mult should be the number
        #for the start parameter. i represents the numbers from start and stop.
        #mult changes as the value i goes through the numbers within the range
   return mult
   #This returns the product of the integers start through stop 
   #inclusive
###############################################################################

def word_count(st):
    '''
    This function returns the number of words in string st, where a "word" is 
    any sequence of non-whitespace characters
    '''
    count = 0
    
    if st.isspace() == True:
        return 0
    else:
        count += 1
    for i in range(len(st) - 1):
        char = st[i]
        # print(char)
        nxt = st[i + 1] 
        # print(char)
        if char.isspace() == True:
            # print('whitespace')
            if nxt.isspace() == False:
                # print('not space')
                count += 1
    return count

#########################################################################    

def wc(filename):
    '''
    wc takes one string as input, which should be the name of a text 
    # file. wc prints on one line, the number of lines, the number of words, 
    and # the number of characters in the file (three numbers separated by 
    tabs).
    '''
    number = 0
    
    start = 0
     ##################################################
     #This part is for counting number of lines
     #################################################
    with open (filename, 'r') as f:
        
        read = f.readlines()
        count_lines = (len(read))
    
        
    ##################################################
    #This part is for counting number of words
    #################################################
    with open (filename, 'r') as f:
                
        read = f.read()
        
        if read.isspace == True:
            return 0
        else:
            start += 1
        for i in range(len(read) - 1):
            char = read[i]
            nxt = read[i + 1]
            if char.isspace() == True:
                if nxt.isspace() == False:
                    start += 1
        # print(str(start.strip("\n"))
    # print(count_lines , '\t' , number , '\t' , start)
     ##################################################
     #This part is for counting number of characters
     ################################################# 
    with open (filename, 'r') as f:
    
        for line in f:
            count = len(line)
            number += count
        # print(str(number))
    print(count_lines , '\t' , start , '\t' , number)
    
    
    
    