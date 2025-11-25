fname = input("Enter file name: ")
fh = open(fname)
lst = []  
for line in fh:
    words = line.split()
    for w in words:
        if w not in lst:
            lst.append(w)
lst.sort()
print(lst)
