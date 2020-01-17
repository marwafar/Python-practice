def make_Array_Consecutive2(status):
  
  status.sort()
  count=0
  for index in range(len(status)-1):
    if status[index]!=status[index+1]-1:
      diff = status[index+1]-status[index]-1
      count+= diff
  return count 

status=[6, 2, 3, 8]
print(make_Array_Consecutive2(status))
