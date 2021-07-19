

import datetime
import calendar

nombresCompletos = [ ]
identificacion = [ ]
edad = [ ]
fechas = [ ]
indices = [ ]

totalPersonas = int(input("Indique la cantidad de personas a ingresar: "))

for i in range(totalPersonas):
    nombre = input("Ingrese Nombres y apellidos: ")
    dni = input("ingrsee DNI: ")
    fechaNac = datetime.datetime.strptime(input("ingrese fecha de nacimiento en formato AAAA/MM/DD: "),"%Y/%m/%d")
    nombresCompletos.append(nombre)
    identificacion.append(dni)
    fechas.append(calendar.timegm(fechaNac.timetuple()))

fechasOrdenadas = list(fechas)
fechasOrdenadas.sort(reverse=True)


for j in range(totalPersonas):
    indices.append(fechas.index(fechasOrdenadas[j]))


print("Personas ordenadas de menor a mayor edad")

for k in range(totalPersonas):
    print(nombresCompletos[indices[k]])
    