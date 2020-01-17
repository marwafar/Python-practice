def delete_starting_evens(lst):
  if len(lst) == 0:
    return "list is empty"
  elif len(lst) == 1:
    if lst[0]%2 != 0:
      return lst
    else:
      lst = []
      return lst
  else:
    count=0
    for index in range(len(lst)):
      if lst[index]%2 == 0:
        count+=1
      elif lst[index]%2 != 0:
        break
    if count < len(lst):      
      return lst[count:]
    else:
      lst = []
      return lst


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

