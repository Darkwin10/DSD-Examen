import math
import cmath


def nbits(ng):
	nbitn = math.ceil(math.log2(ng + 1))  # Obtiene el minimo valor entero que sea >= al logaritmo base dos de ng + 1
	return nbitn


def toBin(intList):
	strBinList = []
	for i in intList:  # Pasamos la lista de enteros a lista de binarios
		strBinList.append(bin(i))
	# print("Lista de binarios:", strBinList)

	ng = nbits(max(intList))
	print(ng)
	binList = []
	k = 0
	for i in strBinList:
		binList.append([])
		for j in range(ng - len(i[2:])):
			binList[k].append(0)
		for j in i[2:]:
			binList[k].append(int(j))
		k += 1

	print(binList)
	return binList


def val(strList):
	# Verifica que todos los caracteres sean numéricos
	onlyNum = 1
	for i in range(len(strList)):
		if strList[i].isdigit() == 0:  # compara caracteres numericos
			onlyNum = 0  # bandera, cuando la cadena contiene un carater no numerico menosr que 0 la bandera es 0
	if onlyNum == 0:
		print("La entrada de caracteres debe ser numeros enteros positivos o 0")
		exit()
	print("Arreglo validado:", strList)


cad = str(input("Introduce la serie(Números separados únicamente por comas):\n"))
strList = cad.split(",")  # separa por comas y guarda en una lista
val(strList)

# Eliminar repeticiones y convertir a enteros
intList = []
for i in strList:
	if i not in intList:  # quita repeticiones de numeros
		intList.append(int(i))
print("Arreglo entero sin repeticiones: ", intList)
print("Suma de los dos primeros para comprobar el casteo a entero:", intList[0] + intList[1])

# Número más grande de la serie
ng = max(intList)
print("Número mas grande en la lista", ng)

# Convierte la serie a binarios
binList = toBin(intList)

# Obtenemos el número de bits necesarios para la serie
print("Número de bits necesarios:", nbits(ng))  # Bits que se van a ocupar

# Inicializar tabla de verdad
tablaV = []
for i in range(2 ** nbits(ng)):
	tablaV.append([])
	for j in range(nbits(ng)):
		tablaV[i].append("x")
print(tablaV)

# Rellenar tabla de verdad
j = 0
for i in intList[:-1]:
	tablaV[i] = binList[j + 1][:]
	j += 1
tablaV[intList[len(intList) - 1]] = binList[0][:]
print(tablaV)

# Tabla de verdad numerada
for i in range(len(tablaV)):
	print(i, ": ", tablaV[i])

# Minitérminos
q = []
for j in range(nbits(ng)):
	q.append([])

for i in range(len(tablaV)):
	for j in range(nbits(ng)):
		if tablaV[i][j] == 1:
			q[j].append(i)

for i in range(len(q)):
	print("Minitérminos Q", i, ":", q[i])

# Expresión canónica
# Primero convertir de decimal a lista de dígitos binarios
# Cada binario en uno es la entra positiva, cada binario en cero es la entrada negada
qStrBin = []
for i in range(len(q)):
	qStrBin.append([])
	for j in q[i]:
		qStrBin[i].append(bin(j))
for i in range(len(qStrBin)):
	print("Canónica de sumas(Lista de strings binarios) Q", i, ":", qStrBin[i])

ng = nbits(max(intList))
qBin = []
l = 0
for i in qStrBin:  # por cada q
	qBin.append([])
	m = 0
	for j in i:  # por cada minitermino de q[i]
		qBin[l].append([])
		for k in range(ng - len(j[2:])):
			qBin[l][m].append(0)
		for k in j[2:]:
			qBin[l][m].append(int(k))
		m += 1
	l += 1
for i in range(len(qBin)):
	print("Canónica de sumas(Lista de dígitos binarioss) Q", i, ":", qBin[i])

# ng = nbits(max(intList))
# print(ng)
# binList = []
# k = 0
# for i in strBinList:
# 	binList.append([])
# 	for j in range(ng - len(i[2:])):
# 		binList[k].append(0)
# 	for j in i[2:]:
# 		binList[k].append(int(j))
# 	k += 1
#
# print(binList)
# return binList


#
# #print("Canónica Q", i, ":", q[i])
