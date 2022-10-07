def canConstruct(ransomNote: str, magazine: str) -> bool:
    # map={}
    # for char in magazine:
    #     if char in map:
    #         map[char]+=1
    #     else:
    #         map[char] =1
    # for char in ransomNote:
    #     if char in map:
    #         map[char]-=1
    #         if map[char] < 0:
    #             return False
    #     else:
    #         return False
    # return True
    
    
    import collections
    rm = collections.Counter(ransomNote) #->Counter({'a': 2}) 
    mg = collections.Counter(magazine) #->Counter({'a': 1, 'b': 1})

    for k, v in rm.items():
        if k not in mg or mg[k] < v:
            return False

    return True

ans = canConstruct("aa","ab")
print(ans)