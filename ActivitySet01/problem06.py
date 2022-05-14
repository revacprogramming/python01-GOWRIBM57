def computepay(h,r):
  if h < 40:
    pay = (h*r)
  else:
    pay = (40-h) * 1.5 * r + (40*r)
  return pay 

hrs=input("Enter hrs : ")
h=float(hrs)
rate=input("Enter rate :")
r=float(rate)

pay = computepay(h,r)
print(pay)    
