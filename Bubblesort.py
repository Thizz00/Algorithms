import random
def Bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return(arr)
arr=[]
for i in range(0,20):
    arr.append(random.randint(1,99))
print(f"Przed sortowaniem: {arr}")
print(f"Po sortowaniu :{Bubblesort(arr)}")
