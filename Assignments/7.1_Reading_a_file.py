
fname = input("Provide file name:")
fhandle = open(fname,'r')
fcontents = fhandle.read()
print((fcontents.upper()).strip())
