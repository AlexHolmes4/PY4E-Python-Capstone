# Used a flat text file in format of mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname,'r')
count = None
totalfloat = None
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    if totalfloat is None :
        count = 1
        ipos = line.find(':') #i know this is fixed but hay ho
        floatvalue = float(line[ipos+1:]) #converting to float auto removes the whitespace
        totalfloat = floatvalue
    else:
        count = count + 1
        ipos = line.find(':') #i know this is fixed but hay ho
        floatvalue = float(line[ipos+1:]) #converting to float auto removes the whitespace
        totalfloat = totalfloat + floatvalue

print("Average spam confidence:",totalfloat/count)
