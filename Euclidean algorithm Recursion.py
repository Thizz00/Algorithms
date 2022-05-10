import random
def GCD(a,b):
    if b>0:
        return GCD(b,a%b)
    return(a)
a=random.randint(1,5000)
b=random.randint(1,5000)    
print(a,b)
print(GCD(15,3))