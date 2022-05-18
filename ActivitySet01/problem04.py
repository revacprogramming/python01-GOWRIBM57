hours=input('Enter the hours:')
rate=input('Enter the rate:')
hrs=float(hours)
rt=float(rate)
if hrs > 40:
    print('overtime')
    pay=hrs*rt*1.5
else:
    print('regular')
pay=(hrs)*(rt)
print(pay)
     