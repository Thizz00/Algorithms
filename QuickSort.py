import random
def partition(arr,left,right):
    pivot=arr[right]
    i=left-1
    for j in range(left,right):
        if arr[j]<=pivot:
             i=i+1
             arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]
    return(i+1)
def quicksort(arr,left,right):
    if left<right:
        p=partition(arr,left,right)
        quicksort(arr,left,p-1)
        quicksort(arr,p+1,right)
    return(arr)

arr=[]
for i in range(0,20):
    arr.append(random.randint(1,99))
print(f"Przed sortowaniem: {arr}")
print(f"Po sortowaniu : {quicksort(arr,0,len(arr)-1)}")