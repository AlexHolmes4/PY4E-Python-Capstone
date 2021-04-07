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

bigcount = None
bigword = None
#word is the key, count is the value; iteration through the dict()
#loops through the dictionary thats been made into tuples,and runs a condition.
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
