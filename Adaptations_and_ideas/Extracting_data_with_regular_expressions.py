import re
intlist = list()

fname = input("Enter File Name: ")
#test file : if len(fname) < 1 : fname = "regex_sum_42.txt"
if len(fname) < 1 : fname = "regex_sum_1096068.txt"
fhandle = open(fname)

for line in fhandle:
    #Extract string that matches regular expression; numerical value 0 - 9, repeated once or more
    if re.search('[0-9]+', line):
        list = re.findall('[0-9]+', line)
        for item in list:
            intlist.append(int(item))
print(sum(intlist))
