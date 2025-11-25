try:
    hours=float(input("Enter Hours:"))
    rate=float(input("Enter Rate:"))
    if hours>40:
        pay=hours*40+(((hours*rate)-40)*rate*1.5)
    else:
        pay=hours*rate
    print("Enter Hours:", )
    print("Enter Rate:", )
    print("Pay:",)
except:
    print("Error, please enter numeric input:")
