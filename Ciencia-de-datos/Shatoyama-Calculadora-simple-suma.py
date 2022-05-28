#Creado por Shatoyama
#importando modulo
import os

#limpiando pantalla
os.system("clear")

#presentando
while True:
    print (">>>>>>Calculadora<<<<<<")
    print ('''
×Para usar alguna función×
Funciones:
1.- Sumar (+)
2.- Restar (-)
3.- Multiplicar (×)
4.- División (÷)
5.- Residuo de divisón
6.- Potencia ''')

#pidiendo datos al usuario
    func_selec = int(input("Selecciona tu funcion a usar : "))
    num_un = int(input("Ingresa tu primer numero : "))
    num_do = int(input("Ingresa tu segundo numero : "))
#dando resultado
    print ('''Resultados:
        
        ''')
    if func_selec == 1:
        print("La suma de", num_un, "y", num_do, "es", num_un + num_do)
    if func_selec == 2:
        print("La resta de", num_un, "y", num_do, "es", num_un - num_do)
    if func_selec == 3:
        print("La Multiplicación de", num_un, "y", num_do, "es", num_un * num_do)
    if func_selec == 4:
        print("La división de", num_un, "y", num_do, "es", num_un / num_do)
    if func_selec == 5:
        print("El residuo de", num_un, "y", num_do, "es", num_un % num_do)
    if func_selec == 6:
        print(num_un,"elevado a", num_do,"es", num_un ** num_do )
    
    sa = int(input('''
    Desea salir: 
    1.- Sí
    2. No
     '''))
    if sa == 1:
         print ("Adios.")
         break
    else:
       os.system('clear')
       pass
