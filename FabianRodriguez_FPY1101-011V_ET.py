import csv
import os
import random

rango = (300000,2500000)

def menu_de_cosas(menu):
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
def salida_programa(salida):
        print("Finalizando programa…")
        print("Desarrollado por Fabian Rodríguez")
        print("RUT  26.560.521-4")

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos =[1,2,3]
rango_sueldos = {1:1, 2:2, 3:3}

def reporte_sueldos(datos):
        print("Test")

while True:
        menu_de_cosas(print)
        try:
                print("")
                op = (int(input("Ingrese el número de la opción deseada: ")))
        except:
                ValueError
                print("")
                print("Seleccione un número.")
                print("")
        if op == 1:
                print("")
                print("Agregando sueldos aleatorios...")
                print("")
        elif op == 2:
                print("")
                print(sueldos)
                print("")
        elif op == 3:
                print("")
                print(rango)
                print("")
        elif op == 4:
                print("")
                reporte_sueldos(print)
                print("")
        elif op == 5:
                print("")
                salida_programa(print)
                break
        else:
                print("")
                print("Por favor seleccione un número del 1 al 5.")
                print("")
                continue