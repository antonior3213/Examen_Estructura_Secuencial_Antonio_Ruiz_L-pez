#Haremos un programa el cual incluyendo el precio sin iva de un producto, calcule el precio final con iva
PrecioSinIva = float(input("Ingrese el precio de sin iva: "))
IvaCalculo = PrecioSinIva * 0.21
IvaIncluido = IvaCalculo + PrecioSinIva
print(IvaIncluido)
