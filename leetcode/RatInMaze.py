def searchMaze(arr, n):
    res = ''
    path = ''
    visited = []
    def backtrack(r,c,path):
        if r < 0 or c < 0 or r >= n or c >= n or arr[r][c] == 0 or (r,c) in visited:
            return
        if r == n-1 and c == n-1:
            #res.append(path.copy())
            res=''.join(path[:])
            return res
            
        visited.append((r,c))
        
        #path.append('D')
        path=path.join('D')
        backtrack(r+1,c,path)
        #path.pop()
        path=path[:-1]
        #path.append('L')
        path=path.join('L')
        backtrack(r,c-1,path)
        #path.pop()
        path=path[:-1]
        #path.append('R')
        path=path.join('R')
        backtrack(r,c+1,path)
        #path.pop()
        path=path[:-1]
        #path.append('U')
        path=path.join('U')
        backtrack(r-1,c,path)
        #path.pop()
        path=path[:-1]
    backtrack(0,0,path)
    return res

arr =[[1,0],[1,1]]
n=2
ans = searchMaze(arr,n)
print(ans)