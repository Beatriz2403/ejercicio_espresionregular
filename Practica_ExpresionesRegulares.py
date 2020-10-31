import re

opcion = 0
while opcion != 11:
    print('COMENZAMOS')
    print('\nSelecciona una Opción')
    print('1.- Todas las palabras que tengan una longitud de 7 o más letras')
    print('2.- Expresiones que NO finalicen con una vocal')
    print('3.- Las palabras que inicien con “M” donde la segunda letra no sea vocal')
    print('4.- Expresiones encerradas entre comillas')
    print('5.- Busqueda de Ip’s')
    print('6.- Horas')
    print('7.- Telefonos')
    print('8.- Correos electronicos')
    print('9.- Url´s')
    print('10.- Codigo Postal')
    print('11.- Salir')
    
    
    opcion = int(input("Opción que desea realizar: "))

    if opcion == 1:
        print('Todas las palabras que tengan una longitud de 7 o más letras')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "[a-zA-z]{7,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 2:
        print('Expresiones que NO finalicen con una vocal')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            regex = "[A-Za-z]+[^aeiou]$"
            for elemento in lista:
                if re.search(regex,elemento):
                   print(elemento)
        textfile.close()   
    elif opcion == 3:
        print('Las palabras que inicien con “M” donde la segunda letra no sea vocal')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "([M][^aeiou][a-zA-z]+)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 4:
        print('Expresiones encerradas entre comillas')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "(\".*\")"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 5:
        print('Busqueda de Ip´s')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "([0-9]{0,3}[\.]+[0-9]{0,3}[\.]+[0-9]{0,3}[\.]+[0-9]{0,3})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 6:
        print('Busqueda de Horas')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "([0-9]{0,2}\:[0-9]{2})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 7:
        print('Busqueda de Telefonos')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "(\+[0-9]{2}\ [0-9]{10})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 8:
        print('Correos electrónicos')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "([a-zA-z]{0,}\@[a-zA-z]{0,}\.[a-zA-z]{0,})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 9:
        print('Busqueda de Url’s')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "([a-zA-Z]{0,}\:[\/][\/]+[a-zA-Z0-9].*\.[a-zA-Z0-9].*\.[a-zA-Z].*\/[a-zA-Z].*\/[a-zA-Z0-9].*\?[a-zA-Z].*\=[a-zA-Z]{0,})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 10:
        print('Codigos postales')
        filename = "Textoprueba.txt"
        textfile = open(filename, "r")
        regex = "[0-9]{5}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()  
    else:
        print('Ingresa valores dentro de las opciones')
    
