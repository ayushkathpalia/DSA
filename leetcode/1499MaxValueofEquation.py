import heapq
def findMaxValueOfEquation(points, k):
        res = float("-inf")
        max_heap = [] # store (-(yi - xi), xi)
        for xi, yi in points:
            print(f"max_heap before {xi, yi}: {max_heap}")
            while max_heap and xi - max_heap[0][1] > k:
                heapq.heappop(max_heap)
            if max_heap:
                res = max(res, -max_heap[0][0] + xi + yi)
            heapq.heappush(max_heap, (-(yi - xi), xi))
            print(f"max_heap after {xi, yi}: {max_heap}")
        print (res)
points =[[1,3],[2,0],[5,10],[6,-10]]
k=1      
findMaxValueOfEquation(points,k)

# import collections
# def findMaxValueOfEquation(self, points, k):
#         res = float("-inf")
#         deque = collections.deque()
#         for x, y in points:
#             while deque and deque[0][1] < x - k:
#                 deque.popleft()
#             if deque:
#                 res = max(res, x + y + deque[0][0])
#             while deque and deque[-1][0] < y - x:
#                 deque.pop()
#             deque.append((y - x, x))
#         return res