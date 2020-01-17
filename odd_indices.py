def odd_indices(lst):
  new_lst = []
  new_lst = [lst[index] for index in range(len(lst)) if index%2 !=0 ]
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))
