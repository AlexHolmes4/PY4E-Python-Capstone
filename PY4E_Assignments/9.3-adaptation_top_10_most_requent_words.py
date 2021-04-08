name = input('Enter file: ')
handle = open(name)

#creates a histgram
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        #iterate through the list and check the dict
        #word already added returns the value, if not return 0. Add 1
        #and assign to the dictionary.
        counts[word] = counts.get(word, 0)+ 1

tuplelist = list()
for key, val in counts.items():
    #constructs a list that switches the element order per item so that val is ipos[0]
    tuplelist.append((val, key)) #could have assigned (val, key) to a variable and then passed as argument to append method.
tuplelist = sorted(tuplelist, reverse=True)

#iterates over the tuplelist and returns ipos 0 - up to but not including ipos10
for val, key in tuplelist[:10]:
    print(key, val) #flipped the order of iteration variables.
