def shape_area(n):
 if n==1:
  return 1
 else:
   p = 4*n
   a = n-1
   area=(p*a)/2+1
 return area

print(shape_area(2))
