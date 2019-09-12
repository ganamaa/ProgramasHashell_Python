def contarPares(lista):
    cont =0
    for i in lista:
        if(i%2==0):
            cont +=1
    return cont

print(contarPares([5,4,7,8]))
