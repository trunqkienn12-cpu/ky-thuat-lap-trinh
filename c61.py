str='X-DSPAM-Confidence:0.8475'
a=str.find(':')
print(a)
host=float(str[a+1:])
print(host)