import sys

list = [1,2,3,4,4,4,6,7,8,8,10,2,3,1,4,6,3,7,30]

x = list.size 

for i in range (x):
  for j in range(x):
    if i != j:
      if list[i] == list[j]:
        delete list[i]
        
        

      
