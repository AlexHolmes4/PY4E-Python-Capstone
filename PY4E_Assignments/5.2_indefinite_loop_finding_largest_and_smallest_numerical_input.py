x = True
largestnum = None
smallestnum = None

while x is True :
    userprovidednum = input("provide a number:")
    if userprovidednum == 'done':
        print("Maximum is", largestnum)
        print("Minimum is",smallestnum)
        break
    else :
            try:
                iuserprovidednum = int(userprovidednum)
            except:
                print("Invalid input")
                continue

    if largestnum is None :
        largestnum = iuserprovidednum
        smallestnum = iuserprovidednum
    elif iuserprovidednum > largestnum :
        largestnum = iuserprovidednum
    elif iuserprovidednum < smallestnum :
        smallestnum = iuserprovidednum
