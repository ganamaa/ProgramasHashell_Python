def ordenada(lista):
    i=0
    condicion =True
    while(i<len(lista)):
        
        for  j  in range(i+1,len(lista)):
            if(ord(lista[i])>ord(lista[j])):
                condicion=False        
        i+=1          
    return condicion

print(ordenada(['a','b','c','d']))
