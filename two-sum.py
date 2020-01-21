def two_Sum(nums,target):
   for index1 in range(len(nums)-1):
      index2=index1+1
      for k in range(index2,len(nums)):
         if nums[index1]+nums[k] == target:
            return [index1,k]

nums=[2,7,3,1]
print (two_Sum(nums,9))
