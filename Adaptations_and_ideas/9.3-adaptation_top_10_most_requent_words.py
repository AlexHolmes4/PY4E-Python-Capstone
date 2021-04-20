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

print(sorted(counts.items(), key=lambda var: var[1], reverse=True)) #this uses lambda to present in correct variable element order 

#print(sorted([(val, key) for key, val in counts.items()], reverse=True)) #returns a sorted list in one line, but not presented with the value first then key.
