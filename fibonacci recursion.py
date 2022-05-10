def fib(n):
    if n==0:
        return(0) 
    if n==1:
        return(1)
    else:
        return(fib(n-2)+fib(n-1))
arr=[]
def array(n):
    for i in range(0,n):
        arr.append(fib(i))
    return(arr)
print(array(10))

