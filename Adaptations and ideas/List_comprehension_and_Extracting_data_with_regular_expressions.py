import re
#this is very complex at my current understanding, but I achieved it and it completes everything that the Extracting_data_with_regular_expression.py does.
#print sum of ['list comprehension']
          #convert iteration variable to int
                #for each sequential element of the return of re.findall (i.e. for every element of the list)
                              #extract and return as list for every match
                                        #match if a a numerical range of characters of any size
                                                    #get a string of the file
print(sum([int(i) for i in re.findall('[0-9]+',(open("regex_sum_1096068.txt")).read())]))
