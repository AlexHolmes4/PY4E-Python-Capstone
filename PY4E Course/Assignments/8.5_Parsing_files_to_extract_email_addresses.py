fname = input("Enter the file name: ")
fhandle = open(fname)
count = 0
for line in fhandle:
    if not line.startswith("From "):
        continue
    else:
        count = count + 1
        words = line.split()
        print(words[1])
print("There were", count, "lines in the file with From as the first word")
