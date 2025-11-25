def  computegrade(Score):
    if Score<0.0 or Score>1.0:
        return("Bad score:")
    elif Score>=0.9:
        return"A"
    elif Score>=0.8:
        return("B")
    elif Score>=0.7:
        return("C")
    elif Score>=0.6:
        return("D")
    else:
        return("F")
try:
    Score=(input("Enter score:"))
    S=float(Score)
    print(computegrade(S))
except:
    print("Bad core:")
