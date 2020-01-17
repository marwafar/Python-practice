def adjacent_elemnet_product(array):
 list_product=[]
 for i in range(len(array)-1):
   product=array[i]*array[i+1]
   list_product.append(product)
 return max(list_product)

list = [3,6,-2,-5,7,3]
print (adjacent_elemnet_product(list))
