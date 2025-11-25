largest=None
smallest=None
while True:
    number=input("Enter a munber:")
    if number=="done":
        break
    try:
        num=float(number)
    except:
        print("Invalid input")
        continue
    if largest is None or num>largest:
        largest=num
    if smallest is None or num<smallest:
        smallest=num
print("Maximun is:", int(largest))
print("Minimum is:", int(smallest))

