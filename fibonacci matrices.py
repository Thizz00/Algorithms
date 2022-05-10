def multiply(A,B):
    a00=(A[0][0]*B[0][0]+A[0][1]*B[1][0])
    a01=(A[0][0]*B[0][1]+A[0][1]*B[1][1])
    a10=(A[1][0]*B[0][0]+A[1][1]*B[1][0])
    a11=(A[1][0]*B[0][1]+A[1][1]*B[1][1])
    A[0][0]=a00
    A[0][1]=a01
    A[1][0]=a10
    A[1][1]=a11
    return([[a00,a01],[a10,a11]])

def power(A,n):
    M=[[1,1],[1,0]]
    for i in range(2,n+1):
        multiply(A,M)
def fib(n):
    F=[[1,1],[1,0]]
    if n==0:
        return 0
    power(F,n-1)
    return(F[0][0])

arr=[]
def array(n):
    for i in range(0,n):
        arr.append(fib(i))
    return(arr)
print(array(10))
