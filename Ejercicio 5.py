import cambio

importe = float(input("Ingrese el valor del importe de la compra: "))
DineroEntregado = float(input("Ingrese el valor del dinero que usted ingresó: "))
if importe > DineroEntregado:
    cambio =  importe - DineroEntregado
elif DineroEntregado > importe:
    cambio = DineroEntregado - importe
elif  DineroEntregado==importe:
    print("Usted entregó el dinero exacto")
else:
    print("Su cambio es de ", cambio)
