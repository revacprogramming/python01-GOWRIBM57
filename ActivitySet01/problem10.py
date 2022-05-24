fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  words=line.split()
  for test in words:
    if test not in lst:
      lst.append(test)
    else:
      continue
#print(line.strip())
lst.sort()
print(lst)
