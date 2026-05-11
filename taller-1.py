#1
nombres = ["daniela", "camila", "maria", "sofia", "valentina"]

for nombre in nombres:
    print(f"nombres: {nombre}")


#2
notas = []

for i in range(1, 8):
    nota = input(f"Ingrese la nota {i}: ")
    notas.append(nota)

notas = [float(n) for n in notas]
mayor = max(notas)
menor = min(notas)
print(f"La nota mayor es: {mayor}")
print(f"La nota menor es: {menor}")

promedio = sum(notas) / len(notas)
print("El promedio es:", round(promedio))



#3

vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

vector[4] = 99

print("Vector actualizado:", vector)


#4

edades = []

for i in range(1, 6):
    edad = int(input(f"Ingrese la edad {i}: "))
    
    edades.append(edad)
    
print("las edades mayores o iguales a 18 son:", [edad for edad in edades if edad >= 18])


#5
nombres.remove("maria")

print("nombres actualizados:", nombres)




