def binary_search(nums, target):
    left=0
    right= len(nums)-1

    while left <= right:
         
         mid = (left + right)//2

         if nums[mid]<target:
              left = mid + 1
         elif nums[mid]>target:
              right = mid -1
         else: 
              return mid
    return -1 


nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
target=-1

binary_search(nums,target)