from datos import gastos

def buscar_gastos():

    placa = input("Ingrese la placa del vehículo: ")
    encontrado = False

    for gasto in gastos:

        if gasto["vehiculo"] == placa:

            print("Vehículo:", gasto["vehiculo"])
            print("Tipo:", gasto["tipo"])
            print("Valor:", gasto["valor"])
            print("--------------------")

            encontrado = True

    if not encontrado:
        print("No se encontraron gastos")