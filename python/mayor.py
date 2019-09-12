def mayor(lista):

    mayor = 0
    maximo = len(lista) #Cantidad de numeros, puede variar
    for i in lista:
        num = i
        if num > mayor:
            mayor = num
    return mayor
print(mayor([78,24,56,93,21,237,46,74,125]))
