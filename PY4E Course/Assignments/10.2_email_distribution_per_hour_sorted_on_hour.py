name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#build histogram of hours and counts of messages sent in those hours
counts = dict()
for line in handle :
    if not line.startswith('From '):
        continue
    else :
        words = line.split()
        time = words[5]
        hour = time[:2]
        counts[hour] = counts.get(hour, 0) + 1
#takes the histogram, turns it into a sorted list of tuples
sortedlist = sorted([(k,v) for k, v in counts.items()])

#prints out the two iteration variables representing the tuple item's elements (sequentially)
for k,v in sortedlist:
    print(k, v)
