from datos import gastos

def registrar_gasto():

    vehiculo = input("Ingrese la placa del vehículo: ")
    tipo = input("Ingrese el tipo de gasto: ")

    while True:
        valor = input("Ingrese el valor del gasto: ")

        if valor.isdigit():
            valor = float(valor)
            break
        else:
            print("Ingrese un número válido")

    gasto = {
        "vehiculo": vehiculo,
        "tipo": tipo,
        "valor": valor
    }

    gastos.append(gasto)

    print("Gasto registrado correctamente")