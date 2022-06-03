#conditional execution

hrs=input('Enter the hours:')
h=float(hrs)
rate=input('Enter the rate:')
rt=float(rate)
if h>40:
   
    gpay=(40* rt + (h-40)*1.5*rt)
else:
   
    gpay=h*rt
print(gpay)