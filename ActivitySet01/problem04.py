#conditional execution

hrs=input('Enter the hours:')
h=float(hrs)
rate=input('Enter the rate:')
rt=float(rate)
if h>40:
  print("Overtime")
  grosspay=1.5*h*rt
else:
  print("Regular")
  grosspay=h*rt
print(grosspay)  
  