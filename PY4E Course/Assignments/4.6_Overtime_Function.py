hours = input("provide hours:")
rate = input("provide rate:")
fhours = float(hours)
frate = float(rate)

#defines the function but does not invoke it
def computepay(hrs,rt):
    if hrs <= 40 :
        grosspay = hrs * rt
        return grosspay
    else :
        othours = hrs - 40
        grosspay = (othours * (rt * 1.5)) + (40 * rt)
        return grosspay
#invokes the function and passes two arguments to the paramaters 
print("Pay",computepay(fhours,frate))
