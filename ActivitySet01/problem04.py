#conditional statement



hrs=input('Enter the hours:')
h=float(hrs)
rate=input('Enter the rate:')
rt=float(rate)
if h>40:
    print('Overtime')
    gpay=(40* rt + (h-40)*1.5*rt)
else:
    print('Regular')
    gpay=h*rt
print(gpay)