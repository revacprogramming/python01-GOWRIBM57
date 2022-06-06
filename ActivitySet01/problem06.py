#functions


def computepay(hrs,rt):
    hrs=input("Enter the hours:")
hrs=float(hrs)
rt=input("Enter the rate:")
rt=float(rt)
if hrs>40:
    pay=((40*rt)+((hrs-40)*(1.5*rt)))
else:
    pay=hrs*rt
pay=computepay(hrs,rt)
print('pay' ,pay)
