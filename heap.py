#1: The heap is supported through a library. 
import heapq 

#2: heappush:
data1 = [3,1,4,1,5,9,2,6,5,3,5]
data2 = [8,9,7,9,3,2,3,8,4,6]
heap = [] #note that's a list syntax!
for item in data1:
  #similar to cpp, heappush gets a list and
  #manipulates it. Note that a binary tree can
  #be decoded in a list as long as its inner node
  #contains 2^i node for layer i (starting from 0).
  heappush(heap, item) 

#3: heapop
#in python the heap is a min-heap
ordered = []
while heap:
  ordered.append(heappop(heap))
print(ordered) #prints [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
data1.sort()
print(ordered == data1) #prints True.
#Note: for a max heap of numbers - insert their negative
#      value and when popped, return an absolute value.

