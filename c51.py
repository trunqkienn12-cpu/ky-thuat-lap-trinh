total = 0
count = 0
while True:
    a = input("Enter a number:")
    if a == "done":
        break
    try:
        number = float(a)
        total += number
        count += 1
    except:
        print("Invalid input")

if count > 0:
    average = total / count
    print(total, count, average)
else:
    print("No valid numbers were entered.")
