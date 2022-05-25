# Tuples

filename = "dataset/mbox-short.txt"


fname = input("Enter file name: ")
fh = open(fname)
count = dict()
for line in fh:
    if line.startswith("From"):
        words=line.split()
        test=words[1]
        for test in words:
            if test in count:
                count[test] = count[test] + 1
            else:
                count[test] = 1
        
#print(line.strip())
for k,v in count.items():
    print(k,'-',v)
#print(count.keys())
#print(count.values())