# COMENTARIO DE LINEA

'''
COMENTARIO DE BLOQUE
'''


# SALIDA POR CONSOLA
print("Hola mundo desde Python, ome")

# VARIABLES O ENTRADAS
nombre = 'Mateo'
edad:int = 23
estatura:float = 1.71
gamer:bool = True
# Salida
'''print(nombre)
print('Buenos días',nombre,' tu edad es',edad, 'tu estatura es ', estatura)
print(f'Buenos días {nombre}, tu edad es {edad}, tu estatura es {estatura} y eres gamer {gamer}')'''

# VARIABLES DESDE LA CONSOLA
numero1 = int(input('Digita un número entero: '))
numero2 = int(input('Digita un número entero: '))
print(f'Usted digitó los números {numero1} y {numero2}')

suma=numero1+numero2
resta=numero1-numero2
multi=numero1*numero2
divi=numero1/numero2
print(f'{numero1} + {numero2} = {suma}')
print(f'{numero1} - {numero2} = {resta}')
print(f'{numero1} * {numero2} = {multi}')
print(f'{numero1} / {numero2} = {divi}')
