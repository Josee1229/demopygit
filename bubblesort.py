def bubbleSort(list):
  n = len(list)
  for i in range(n-1,0,-1):
    for j in range(i):
      if list[j]>list[j+1]:
        list[j],list[j+1] = list[j+1],list[j]

list = [12,29,41,3,2,5234,34,153,53]
print(list)
bubbleSort(list)
print(list)
