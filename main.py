from gastos import registrar_gasto
from registros import buscar_gastos
from reportes import mostrar_gastos, calcular_total


def menu():

    while True:

        print("=== CONTROL DE GASTOS VEHÍCULOS ===")
        print("1. Registrar gasto")
        print("2. Mostrar gastos")
        print("3. Buscar gastos por vehículo")
        print("4. Ver total gastado")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gasto()

        elif opcion == "2":
            mostrar_gastos()

        elif opcion == "3":
            buscar_gastos()

        elif opcion == "4":
            calcular_total()

        elif opcion == "5":
            print("Programa finalizado")
            break

        else:
            print("Opción inválida")


menu()