name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#make a histogram for email and count
counts = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

#order a list of tuples by highest frequency email occurance use
templist = list()
for key,value in counts.items():
    templist.append((value,key))
templist = sorted(templist, reverse=True)
print(templist)

print("\n Seperate lists \n")
#just show the highest freq emailers in order, no values associated.
orderedemails = list()
for a,b in templist:
    orderedemails.append(b)
print(orderedemails)
