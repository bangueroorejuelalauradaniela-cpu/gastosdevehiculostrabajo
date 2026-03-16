from datos import gastos

def mostrar_gastos():

    if len(gastos) == 0:
        print("No hay gastos registrados")
        return

    for gasto in gastos:

        print("Vehículo:", gasto["vehiculo"])
        print("Tipo:", gasto["tipo"])
        print("Valor:", gasto["valor"])
        print("--------------------")


def calcular_total():

    total = 0

    for gasto in gastos:
        total = total + gasto["valor"]

    print("Total gastado:", total)