import random
def GCD(a,b):
    while(b!=0):
        temp=b
        b=a%b
        a=temp
    return(a)
a=random.randint(1,5000)
b=random.randint(1,5000)    
print(a,b)
print(GCD(a,b))