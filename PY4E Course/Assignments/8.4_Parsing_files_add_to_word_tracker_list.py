fname = input("Enter the file name:")
fhandle = open(fname, 'r')
listofwords = list()
for line in fhandle:
    words = ((line.rstrip()).split()) #no need to strip the whitespace here as split delimits on white space, it considers any number whitespace a single split.
    for word in words:
        if word in listofwords:
            continue
        else:
            listofwords.append(word)
print(sorted(listofwords))
