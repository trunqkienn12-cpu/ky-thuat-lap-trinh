fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
total = 0.0
for line in fhand:
    line = line.strip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    colon_pos = line.find(':')
    value = line[colon_pos+1:]
    num = float(value)
    total += num
    count += 1
if count > 0:
    print('Average spam confidence:', total / count)
else:
    print('No spam confidence lines found.')
