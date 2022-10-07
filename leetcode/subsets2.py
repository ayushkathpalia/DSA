
def subsetsWithDup():
    nums = [1,2,2]
    res = []
    nums.sort()
    
    def backtrack(i,subset):
        if i == len(nums):
            res.append(subset.copy())
            return  
        
        subset.append(nums[i])
        backtrack(i+1,subset)
        subset.pop()
        
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i+=1
        backtrack(i+1,subset)
    
    backtrack(0,[])
    
    print(res)



subsetsWithDup()

