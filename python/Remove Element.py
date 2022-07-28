nums = [0,1,2,2,3,0,4,2]
val = 2

lengh, i = len(nums), 0
while i < lengh:
    if nums[i]==val:
        nums[i] = nums[lengh-1]
        lengh-=1
    else:
        i+=1
print(lengh)
