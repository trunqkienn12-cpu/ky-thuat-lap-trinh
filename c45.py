def computepay(hours, rate):
    if hours>40:
        pay=(hours-40)*rate*1.5+40*rate
    else:
        pay=hours*rate
    return pay
try:
    hours=float(input("Enter hours:"))
    rate=float(input("Enter rate:"))
    pay=computepay(hours,rate)
    print("Pay:", pay)
except:
    print("Invalid input")