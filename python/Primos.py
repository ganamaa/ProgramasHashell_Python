
def divisible(a,b):
    if(a%b==0):
        return True
    else:
        return False    

def divisibles(a):
    c=0
    lista=[]
    for i in range(1,a+1):
        if(divisible(a,i)==True):
            c+=1
            lista.insert(c,i) 
    return len(lista)

def esPrimo(x):
    if(divisibles(x)<=2):
        return True
    else:
        return False

def primos(n):
    b=0
    lista=[]
    for j in range(1,n):
        if(esPrimo(j)==True):
            b+=1
            lista.insert(b,j)
   
    #for i in range(0,len(lista)):
    return  lista
        
print(primos(100))
