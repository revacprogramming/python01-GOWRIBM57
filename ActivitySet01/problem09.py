# Files

fname = input("Enter file name: ")
fh = open(fname)
avg=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    test=line.find(':')
    toadd=line[test+1 : ]
    fcopy=float(toadd)
    avg=avg+fcopy
    count=count+1
    
result=avg/count
print("Average spam confidence:",result)

