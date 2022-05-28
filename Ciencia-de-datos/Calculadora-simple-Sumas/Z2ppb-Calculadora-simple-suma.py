# Creado por Z2ppbWVuZXpkZXph
# Este programa fue creado para poder solicitar al usuario 2 dígitos, y a base de los datos ingresados, se imprimirá el resultado en pantalla.
# Importando módulos
import os

# Bienvenida al usuario
os.system("clear")
print ("  Bienvenido a esta calculadora básica")
print ("Para comenzar, dame tus primeros 2 dígitos")
# Conteo para el bucle
conteo = 0
# Lista para almacenar respuestas
lst = []
# Bucle, si el conteo de las respuestas es menor a 1, se solicitará los datos nuevamente
while conteo <= 1:
  var1 = int(input("Pon el primer dígito: "))
  lst.append(var1)
  conteo += 1
# Caso contrario, se imprimirá el resultado
else:
  print ("El resultado es", sum(lst))
