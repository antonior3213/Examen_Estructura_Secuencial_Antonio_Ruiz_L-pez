n = int(input("Ingrese un numero de tres cifras: "))
centenas = n // 100 % 10
decenas = n // 10 % 10
unidades = n % 10
suma = centenas + decenas + unidades
invertido = unidades * 100 + decenas * 10 + centenas * 1
print("numero de entrada: " , n)
print("Centenas: ", centenas)
print("Decenas: ", decenas)
print("Unidades: ", unidades)
print("Suma de las cifras: ", suma)
print("Numero invertido: ", invertido)



