# Creado por Anonymous
#MODULOS
import os

#CALCULADORA
print("---------CALCULADORA----------")
n1= int(input("INTRODUSCA UN NUMERO:"))
n2= int(input("INTRODUSCA OTRO:"))

#BORRANDO PANTALLA
os.system("clear")

#OPCIONES A SELECCIONAR
print("-----OPCIONES-----")
print("Q DESEA HACER ?")
print("#1 SUMAR")
print("#2 RESTAR")
print("#3 DIVIDIR")
print("#4 MULTIPLICAR")
opcion=int(input("SELECCIONE UN NUMERO:"))

if opcion == 1:
   print("SU RESULTADO ES:",n1+n2)

else:
   print("OPCION NO VALIDA EN ESTOS MOMENTOS")
