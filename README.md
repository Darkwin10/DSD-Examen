# DSD-Examen

def validacion (ar):
    a = ar.split (",") #separa por comas y guarda en una lista
    r = len (a)  #espacios de la lista
    j=0
    i=0
    for i in range (r):
        if a[i].isdigit () == 0: #compara caracteres numericos
            j=1                  #bandera, cuando la cadena contiene un carater no numerico menosr que 0 la bandera es 1
    if j == 1:
        print("La entrada de caracteres debe ser numeros enteros positivos o 0")
        exit()
    print("arreglo validado:",a)
    serie = []
    i = 0
    for i in a:
        if i not in serie: #quita repeticiones de numeros
            serie.append(i)
    print("arreglo normal sin repeticiones: ",serie)
    i=0
    serie={}
    for i in range(r):
        serie[i] = int (a[i])    #casteo para pasar la lista a enteros
    print ("suma de los dos primeros para comprobar el casteo a entero:",serie[0]+serie[1])



ar = str(input("hola"))
validacion(ar)
