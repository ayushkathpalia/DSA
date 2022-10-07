
from ctypes import addressof


def isPalindrome(s):
    def helper(l,r):
        #base case
        if l == r:
            return True
        if l < r:
            if not alphanum(s[l]):
                l+=1
            if not alphanum(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            helper(l+1,r-1)
        
    if len(s) == 0:
            return True
        
    l,r = 0,len(s)-1
    return helper(l,r)    
    
def alphanum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))


s = 2
#ans = isPalindrome(s)
#print(ans)
# def subsets(nums):
#     res = []
#     subset = []
    
#     def dfs(i):
#         if i >= len(nums):
#             res.append(subset.copy())
#             return
        
#         subset.append(nums[i])
#         dfs(i+1)
        
#         subset.pop()
#         dfs(i+1)
        
#     dfs(0)
#     print(res)
# subsets(['a','b','c'])


from ctypes import c_int, addressof,cast,py_object
print(id(s))
print(addressof(c_int(s)))
print(hex(id(s)))

s = s+1
print(id(s))
print(addressof(c_int(s)))
print(hex(id(s)))
