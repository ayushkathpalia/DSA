def reverseWords(s) -> str:        
    res=""
    start = 0
    for index in range(len(s)):
        if s[index] == ' ' or index == len(s)-1:
            end = index
            print(start,end)
            print(s[start:end+1])
            res = " "+s[start:end+1]+res
            start = end
    return res.strip()

s = "the sky is blue"
ans = reverseWords(s)
print(ans)