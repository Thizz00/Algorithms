import random
def InsertionSort(arr):
    for i in range(1,len(arr)):
        value=arr[i]
        j=i-1
        while j>=0 and arr[j]>value:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=value
    return(arr)
arr=[]
for i in range(0,20):
    arr.append(random.randint(1,99))
print(f"Przed sortowaniem: {arr}")
print(f"Po sortowaniu : {InsertionSort(arr)}")