# COMENTARIO DE LINEA

'''
COMENTARIO DE BLOQUE
'''


# SALIDA POR CONSOLA
#print("Hola mundo desde Python, ome")

# VARIABLES O ENTRADAS
#nombre = 'Mateo'
#edad:int = 23
#estatura:float = 1.71
#gamer:bool = True
# Salida
'''print(nombre)
print('Buenos días',nombre,' tu edad es',edad, 'tu estatura es ', estatura)
print(f'Buenos días {nombre}, tu edad es {edad}, tu estatura es {estatura} y eres gamer {gamer}')'''

# VARIABLES DESDE LA CONSOLA
#numero1 = int(input('Digita un número entero: '))
#numero2 = int(input('Digita un número entero: '))
#print(f'Usted digitó los números {numero1} y {numero2}')

#suma=numero1+numero2
#resta=numero1-numero2
#multi=numero1*numero2
#divi=numero1/numero2
#print(f'{numero1} + {numero2} = {suma}')
#print(f'{numero1} - {numero2} = {resta}')
#print(f'{numero1} * {numero2} = {multi}')
#print(f'{numero1} / {numero2} = {divi}')


# TOMANDO DECISIONES
#numero = int(input('Digite un número: '))
#print(f'El número digitado fue: {numero}')

'''if(numero>=0):
    print(f'El número es positivo')
else:
    print(f'El número es negativo')
    print("Bobito ome")'''

#Ejemplo 2
'''nivelAgua = int(input('Digite un numero: '))
if(nivelAgua<200):
    print(f'Hay muy poca agua en la represa')
elif(nivelAgua>=200 and nivelAgua<450):
    print(f'El nivel del agua está estable')
else:
    print(f'Riesgo de desborde de agua')'''

#Ejercicio practica
'''mes = input('Digite un mes: ')
if(mes=="enero" or mes=="febrero" or mes=="marzo"):
    print(f'En el mes de {mes} estamos en invierno')
elif(mes=="abril" or mes=="mayo" or mes=="junio"):
    print(f'En el mes de {mes} estamos en verano')
elif(mes=="julio" or mes=="agosto" or mes=="septiembre"):
    print(f'En el mes de {mes} estamos en otoño')
else:
    print(f'En el mes de {mes} estamos en primavera')'''

#Ejercicio practica 2
'''edad = int(input('Digite la edad: '))
if(edad<=14):
    print(f'Eres un niño')
elif(edad>14 and edad<=28):
    print(f'Eres un joven')
elif(edad>28 and edad<=60):
    print(f'Eres un adulto')
else:
    print(f'Eres un adulto mayor')'''

# Bucles o loops
contador = 0

'''while(contador<10):
    contador+=1 # Dos formas de escribir un contador ya que no existen el i++, se usa +=1 o variable=variable+1
    print(contador)
else:
    print("Terminó el ciclo") # Se puede usar el else en el while para saber cuando termina un ciclo'''