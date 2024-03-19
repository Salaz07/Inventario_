# Codigo realizado por:
# Santiago Salazar Avendaño
# Santiago Mejia
# Fernando Garcia Guiral

import os
import random


inventario = {
    "zanahorias": [100, 70],  #Lista: [cantidad actual, umbral mínimo]
    "platanos": [120, 50],   #Lista: [cantidad actual, umbral mínimo]
    "papitas": [80, 30],    #Lista: [cantidad actual, umbral mínimo]
}

def imprimir_menu():   
    print("Menú Principal:")
    print("1. Agregar producto")
    print("2. Simular consumo")
    print("3. Mostrar reporte del inventario")
    print("4. Calcular inventario total")
    print("5. Verificar alertas de reorden")
    print("6. Reabastecer producto")
    print("7. Salir del programa")

def digitar_opcion():   #Funcion para ingresar la opcion del menu
    while True:
        opcion = input("Por favor, digite la opción del menú que deseas realizar: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion in range(1, 8):  
                return opcion
        print("Opción no válida. Por favor, digite un número de opción válida del menú.")

def agregar_producto(): #Opción 1 usada para agregar un producto a la lista
    while True:
        producto_nuevo = input("Ingrese el nombre del nuevo producto: ")
        cantidad_actual = input("Ingrese la cantidad actual del producto: ")
        umbral_minimo = input("Ingrese el umbral mínimo del producto: ")

        
        if cantidad_actual.isdigit() and umbral_minimo.isdigit():
            cantidad_actual = int(cantidad_actual)
            umbral_minimo = int(umbral_minimo)
            if cantidad_actual >= 0 and umbral_minimo >= 0:
            
                inventario[producto_nuevo] = [cantidad_actual, umbral_minimo]
                print(f"El producto '{producto_nuevo}' ha sido agregado al inventario.")
                break
            else:
                print("Las cantidades deben ser números enteros positivos. Inténtelo de nuevo.")

def simular_consumo(): #Opción 2 usada para simular el consumo de manera aleatoria
    print("Simulando consumo de productos...\n")
    for producto, datos in inventario.items():
        cantidad_actual = datos[0]
        if cantidad_actual == 0:
            print(f"No hay suficiente cantidad de '{producto}' para la venta.")
            continue
        
        cantidad_consumida = random.randint(1, cantidad_actual)
        print(f"Se han consumido {cantidad_consumida} unidades de '{producto}'.")
        inventario[producto][0] -= cantidad_consumida

def mostrar_reporte(): #Opción 3 para mostrar los productos y el inventario en una tabla
    print("Reporte del inventario:\n")
    print(f'Producto\t   ║\t\t    Cantidad Actual\t\t║    Umbral Mínimo\n---------------------------------------------------------------------------------------------')
    for producto, datos in inventario.items():
        if datos[0] <= (datos[1]):
            print(f"{producto:15}    ║    \t\t\033[91m{datos[0]:10}\033[0m\t\t║{datos[1]:10}") #En esta linea se le agrega el color rojo cuando la cantidad de productos es menor a la del umbral
        else:
            print(f"{producto:15}    ║    \t\t{datos[0]:10}\t\t║{datos[1]:10}")

def calcular_inventario(): #Opción 4 usada para calcular la cantidad total de inventario 
    total = sum(cantidad for cantidad, _ in inventario.values())
    print(f"El inventario total es: {total}")

def verificar_alertas_reorden(): #Opción 5 usada para saber que producto necesita de un reabastecimiento
    print("Verificando alertas de reorden...\n")
    for producto, datos in inventario.items():
        cantidad_actual = datos[0]
        umbral_minimo = datos[1]
        if cantidad_actual < umbral_minimo:
            print(f"Alerta: La cantidad actual de '{producto}' ({cantidad_actual}) está por debajo del umbral mínimo ({umbral_minimo}).")
        elif cantidad_actual >= umbral_minimo:
            print(f"No hay alertas de reorden para '{producto:15}'\n")

def reabastecer_producto(): #Opción 6 usada para reabastecer cualquiera de los productos existentes en el inventario
    nombre_producto = input("Ingrese el nombre del producto que desea reabastecer: ")
    if nombre_producto in inventario:
        while True:
            cantidad_reabastecimiento = input(f"Ingrese la cantidad de '{nombre_producto}' que desea reabastecer: ")
            if cantidad_reabastecimiento.isdigit() and int(cantidad_reabastecimiento) >= 0:
                cantidad_reabastecimiento = int(cantidad_reabastecimiento)
                inventario[nombre_producto][0] += cantidad_reabastecimiento
                print(f"Se han reabastecido {cantidad_reabastecimiento} unidades de '{nombre_producto}'.")
                break
            else:
                print("La cantidad de reabastecimiento debe ser un número entero positivo. Inténtelo de nuevo.")
    else:
        print(f"El producto '{nombre_producto}' no existe en el inventario. No se puede reabastecer.")

def limpiar_pantalla(): #Funcion usada para limpiar el terminal y generar una imagen mas limpia
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    imprimir_menu()
    opcion = digitar_opcion()

    if opcion == 1:
        agregar_producto()
        input("Presione Enter para continuar...")
        limpiar_pantalla()
    elif opcion == 2:
        simular_consumo()
        input("Presione Enter para continuar...")
        limpiar_pantalla()
    elif opcion == 3:
        mostrar_reporte()
        input("Presione Enter para continuar...")
        limpiar_pantalla()
    elif opcion == 4:
        calcular_inventario()
        input("Presione Enter para continuar...")
        limpiar_pantalla()
    elif opcion == 5:
        verificar_alertas_reorden()
        input("Presione Enter para continuar...")
        limpiar_pantalla()
    elif opcion == 6:
        reabastecer_producto()
        input("Presione Enter para continuar...")
        limpiar_pantalla()
    elif opcion == 7:
        print("¡Hasta luego!")
        break