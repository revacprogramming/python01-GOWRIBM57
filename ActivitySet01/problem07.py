largest = None
 while True: 
   try:
       num = input('Enter the number')
       if num == 'done':
           break ;
       n = int(num)
       largest = num if largest < num or largest == None
else largest
       smallest = num if smallest > num or smallest == None
else smallest
    except:
           print('Invalid')
print('Maximum number is',largest)
print('Minimum number is',smallest)