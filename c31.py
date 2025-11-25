Hours=float(input("Enter Hours:"))
Rate=float(input("Enter Rate:"))
print("Enter Hours:", Hours)
print("Enter Rate:", Rate)
if Hours>40:
    Time_More= Hours-40
    Rate_More= Rate*1.5
    Pay_More= Time_More*Rate_More
    Normal_Pay= 40*Rate
    Pay=Pay_More+Normal_Pay
else:
    Pay=Hours*Rate
print("Pay:", Pay)


