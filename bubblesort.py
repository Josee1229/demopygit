def bubbleSort(list):
  n = len(list)
  for i in range(n-1,0,-1):
    for j in range(i):
      if list[j]>list[j+1]:
        list[j],list[j+1] = list[j+1],list[j]

list = [5,2,3,5,2,45,23,4,12,41,12]
print(list)
bubbleSort(list)
print(list)
