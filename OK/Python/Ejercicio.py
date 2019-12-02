# Numeros
2+2 #Realiza la suma de dos dígitos.
50 - 5*6 #Sirve para separar las operaciones
(50 - 5*6) / 4 #la operación dentro del paréntesis es la que realiza primero (siguiendo el orden esstablecido en el comentario de arriba) y luego la división
8/5 #El resultado de la división se muestra en decimales

17 / 3 #Realiza la división de 17 entre 3
17 // 3 #Quita los decimales al resultado de la división
17 % 3 #Miuestra el residuo de la división
5 * 3 + 2 #Separa las operaciones partiendo del signo de suma, primero realiza el producto y luego lo suma

5 ** 2 #Eleva el número al cuadrado
2 ** 7 #Eleva el número a la potencia 7
9 ** 0.5 #Eleva el número a la potencia 
2 ** 1/2 #Primero eleva el número a la potencia 1 y luego divide entre dos el resultado
2 ** (1/2) # obtiene la raíz cuadrada

ancho = 20 #Registra en la memoria el valor del "ancho"
alto = 5 * 9 #Registra en la memora el valor del "alto"
ancho * alto #Realiza la operación de los valores que registró como el "ancho" y el "alto"

n

4 * 3.75 - 1 #Realiza primero el producto y luego lo resta.

iva = 16/100 #Registra en la memoria el valor del iva
precio = 120.5 #Registra en la memoria el valor del "precio"
precio * iva #Realiza una regla de tres definida
precio + _ #Realiza la suma del valor registrado como precio y luego lo suma al resultado obtenido en la operacion anterior
round(_, 2) #Redondea el valor asignado 

# Cadenas
'una cadena' #muestra los simbolos asignados a la cadena
'La comilla simple \'' #Convierte comillas simples en dobles y nos permite imprimir comillas dentro de la cadena
'La comilla simple \''
"\"Si,\" afirmo" #El backslash nos permite imprimir las comillas

"\"Si,\" afirmo" 
print("\"Si,\" afirmo") #Muestra los símbolos dentro de las comillas

c = 'Primera linea.\nSegunda linea.' #Registra en la memoria el valor asignado a c en este caso, una cadena
c #Nos muestra el valor asigando a c
print(c) #Imprime el valor de c, dentro de la cadena se usa \n que nos ayuda a dividir por líneas la cadena
len(c) #Nos muestra el número de carácteres que tiene "c"


print('Una ruta en windows C:\algun\nombre') #Imprime los símbolos dentro de la cadena, pero elimina \a y utiliza \n como el generador de otra línea.
print(r'Una ruta en windows C:\algun\nombre') #Nos permite imprimir los símbolos dentro de la cadena sin utilizar las funciones de "\"


print("""\
Uso: ssh [OPCIONES] <usuario>@<servidor>
     -v                 muestra informacion adiciona de la conexion
     -p puerto          Puerto para la conexion segura, 22 es el predeterminado
""") #Las triples comillas nos permiten dividir la cadena en varias líneas 

2 * 'goya ' + 'cachun' #Realiza el producto de las cadenas, muestra dos veces "goya" y a lo que resulte le suma "cachún"

'Py' 'thon' #Une dos cadenas

text = ('Escribe varias cadenas dentro del par´entesis '
        'para tenerlas unidas') #Guarda los valores de text en la memoria, en este caso, dos cadenas que se unen mediante el paréntesis
text #Nos muestra el valor de "text" en este caso, ya nos muestra las cadenas unidas

prefijo = 'Py' #Guarda el valor de "Prefijo" en la memoria
prefijo 'thon' #Nos muestra un error en la sintaxis
('un' * 3) 'ium' #Muestra el mismo error que el anterior

prefijo + 'thon' #Muestra el resultado de sumar las cadenas, las une sin espacios

nombre = "Ada" #Registra en la memoria el valor de "nombre"
apellido = "Lovelace" #Registra en la memoria el valor de "apellido"

print(nombre.upper()) #Muestra en mayúsculas el valor asignado a "Nombre" que es una cadena 
print(nombre.lower()) #Muestra en minúsculas el valor de la cadena asiganda a "Nombre"
print(nombre.isalnum()) #Nos dice si "nombre" tiene valores alfanuméricos o no
print(nombre.isalpha()) #Nos dice si "Nombre" tiene valores que son letras del alfabeto
print(nombre.islower()) #Nos dice si la cadena dentro de "Nombre" tiene valores que son minúsculas
print(nombre.isnumeric()) #"" son números
print(nombre.isspace()) #"" contiene espacios o no. 
print(nombre.istitle()) #"" inicia con una Mayúscula y los siguientes valores son minúsculas
asignatura = "Taller De Herramientas Computacionales" #Asigna a "asignatura" el valor de la cadena
print(asignatura.istitle()) #Nos muestra si las palabras dentro de la cadena incian con una mayúscula y las que le siguen son minúsculas
print(asignatura.isupper()) #Nos dice si todas las letras dentro del la cadena asignada al valor "asignatura" son mayúsculas o no 

numero = "1024" #Registra en la memoria el valor de la cadena asignada a "numero"
vocales = "aeiou" #Registra en la memoria el valor de la cadena asiganda a "Vocales"
print(numero.isnumeric()) #Nos dice si los valores dentro de la cadena son numeros o no
print(vocales.isnumeric()) #Nos dice si los valores dentro de la cadena son numeros o no 

pelicula = "2001: UNA MENTE BRILLANTE"
libro = "Cinco Ecuaciones Que CAmbiaron Al Mundo"
poema = "nadie en oro se convertirá:"

print(pelicula.islower()) #Nos dice que los valores de película no son todos minúsculas
print(pelicula.isupper()) #Nos dice que los valores de película son todos mayúsculas 

print(libro.istitle()) #Muestra si las palabras dentro de la cadena asignada a libro inician con una Mayúscula y luego continúan minúsculas
print(libro.isupper()) #Muestra si las palabras dentro de la cadena asignada a libro no son todas mayúsculas
print(poema.istitle()) #NMuestra si las palabras dentro de poema no inician todas con mayúsculas y continúan con minúsculas
print(poema.islower()) #Muestra si todas las letra dentro de poema son minúsculas

cadena = "Linux es un kernel." #Guarda en la memoria la cadena asignada como valor de "cadena"
" ".join(cadena) #Asigna un espacio extra a los carácteres dentro de "cadena"
print(cadena) #Muestra el valor de cadena
print(" ".join(cadena)) #Muestra el valor de cadena pero le asigna un espacio extra a todos los carácteres

print("".join(reversed(cadena))) #Muestra "al revés" la cadena asignada como valor de "cadena"

# https://docs.python.org/3/tutorial/introduction.html#strings
# https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3
