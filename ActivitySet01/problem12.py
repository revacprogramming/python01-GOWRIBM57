import re

file=input('enter the file name:')
fhand=open(file)
number=list()
for line in fhand:
    line=line.rstrip()
    nums = re.findall('[0-9]+',line)
    
    for i in nums:
        num=int(i)
        number.append(num)
    
print(sum(number))


