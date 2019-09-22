# Numeros
2+2 #Realiza la suma de dos dígitos, en este caso, 2 y 2.
50 - 5*6 #Separa las operaciones, primero realiza el producto y luego realiza la resta
(50 - 5*6) / 4 #Realiza primero la operación dentro del paréntesis (siguiendo el orden esstablecido en el comentario de arriba) y luego la división
8/5 #El resultado de una división siempre lo mostrará en decimales

17 / 3 #Realiza la división de 17 entre 3
17 // 3 #Elimina los decimales de la división
17 % 3 #Nos muestra el residuo de la división
5 * 3 + 2 #Separa las operaciones partiendo del signo de suma, primero realiza el producto y luego lo suma

5 ** 2 #Eleva el número a la potencia 2
2 ** 7 #Eleva el número a la potencia 7
9 ** 0.5 #Eleva el número a la potencia .5 (o realiza la raíz cuadrada)
2 ** 1/2 #Primero eleva el número a la potencia 1 y luego divide entre dos el resultado
2 ** (1/2) #Eleva el número a la potencia 1/2 o realiz ala raíz cuadrada

ancho = 20 #Guarda en la memoria el valor del "ancho"
alto = 5 * 9 #Guarda en la memora el valor del "alto"
ancho * alto #Realiza la operación de los valores guardados en el "ancho" y el "alto"

n

4 * 3.75 - 1 #Realiza primero el producto a la izquierda del signo de resta y luego lo resta.

iva = 16/100 #Guarda en la memoria el valor del iva
precio = 120.5 #Guarda en la memoria el valor del "precio"
precio * iva #Realiza el producto del "precio" y el iva, primero multiplica 120.5 * 16 y luego divide entre 100 (Realiza una regla de tres definida)
precio + _ #Realiza la suma del valor guardado como precio y luego lo suma al resultado obtenido en la operacion anterior
round(_, 2) #Redondea el valor asignado al número de decimales especificados

# Cadenas
'una cadena' #Imprime los simbolos asignados a la cadena
'La comilla simple \'' #Convierte comillas simples en dobles y nos permite imprimir comillas dentro de la cadena
'La comilla simple \''
"\"Si,\" afirmo" #El backslash nos permite imprimir las comillas

"\"Si,\" afirmo" 
print("\"Si,\" afirmo") #Imprime los símbolos dentro de las comillas

c = 'Primera linea.\nSegunda linea.' #Guarda en la memoria el valor asignado a c en este caso, una cadena
c #Nos muestra el valor asigando a c
print(c) #Imprime el valor de c, dentro de la cadena se usa \n que nos ayuda a dividir por líneas la cadena
len(c) #Nos muestra el número de carácteres en el valor "c"


print('Una ruta en windows C:\algun\nombre') #Imprime los símbolos dentro de la cadena, pero elimina \a y utiliza \n como el generador de otra línea.
print(r'Una ruta en windows C:\algun\nombre') #Nos permite imprimir los símbolos dentro de la cadena sin utilizar las funciones de "\"


print("""\
Uso: ssh [OPCIONES] <usuario>@<servidor>
     -v                 muestra informacion adiciona de la conexion
     -p puerto          Puerto para la conexion segura, 22 es el predeterminado
""") #Las triples comillas nos permiten generar distintas líneas dentro de la cadena

2 * 'goya ' + 'cachun' #Realiza el producto de las cadenas, muestra dos veces "goya" y le suma al resultado "cachún"

'Py' 'thon' #Junta las cadenas, no muestra espacios o alguna señal de que eran cadenas distintas

text = ('Escribe varias cadenas dentro del par´entesis '
        'para tenerlas unidas') #Guarda los valores de text en la memoria, en este caso, dos cadenas que para unirlas es necesario el paréntesis
text #Nos muestra el valor de "text" en este caso, ya nos muestra las cadenas unidas

prefijo = 'Py' #Guarda el valor de "Prefijo" en la memoria
prefijo 'thon' #Nos muestra un error en la sintaxis, lo señala en "thon'"
('un' * 3) 'ium' #Muestra el mismo error que arriba

prefijo + 'thon' #Muestra el resultado de sumar las cadenas, las une sin espacios

nombre = "Ada" #Guarda en la memoria el valor de "nombre"
apellido = "Lovelace" #Guarda en la memoria el valor de "apellido"

print(nombre.upper()) #Muestra en mayúsculas el valor asignado a "Nombre" que es una cadena 
print(nombre.lower()) #Muestra en minúsculas el valor de la cadena asiganda a "Nombre"
print(nombre.isalnum()) #Nos dice si los valores asignados a "nombre" son alfanuméricos o no
print(nombre.isalpha()) #Nos dice si los valores asignados a la cadena dentro de "Nombre" son letras del alfabeto
print(nombre.islower()) #Nos dice si los valores asignados a la cadena dentro de "Nombre" son minúsculas
print(nombre.isnumeric()) #"" son números
print(nombre.isspace()) #"" contiene espacios o no. 
print(nombre.istitle()) #"" inicia con una Mayúscula y los siguientes valores son minúsculas
asignatura = "Taller De Herramientas Computacionales" #Asigna a "asignatura" el valor de la cadena
print(asignatura.istitle()) #Nos muestra si las palabras dentro de la cadena incian con una mayúscula y las que le siguen son minúsculas
print(asignatura.isupper()) #Nos dice si todas las letras dentro del la cadena asignada al valor "asignatura" son mayúsculas o no 

numero = "1024" #Guarda en la memoria el valor de la cadena asignada a "numero"
vocales = "aeiou" #Guarda en la memoria el valor de la cadena asiganda a "Vocales"
print(numero.isnumeric()) #Nos dice si los valores dentro de la cadena son numeros o no
print(vocales.isnumeric()) #Nos dice si los valores dentro de la cadena son numeros o no (en este caso no)

pelicula = "2001: UNA MENTE BRILLANTE"
libro = "Cinco Ecuaciones Que CAmbiaron Al Mundo"
poema = "nadie en oro se convertirá:"

print(pelicula.islower()) #Nos dice que los simbolos dentro de película no son todos minúsculas
print(pelicula.isupper()) #Nos dice que los simbolos dentro de película son todos mayúsculas 

print(libro.istitle()) #Nos dice que las palabras dentro de la cadena asignada a libro inician con una Mayúscula y luego continúan minúsculas (Modifiqué el valor de libro ya que una de las apalabras iniciaba con una mayúscula y conyinuaba otra)
print(libro.isupper()) #Nos dice que las palabras dentro de la cadena asignada a libro no son todas mayúsculas

print(poema.istitle()) #Nos dice que las palabras dentro de poema no inician todas con mayúsculas y continúan con minúsculas
print(poema.islower()) #Nos dice qeu todas las letra dentro de poema son minúsculas

cadena = "Linux es un kernel." #Guarda en la memoria la cadena asignada como valor de "cadena"
" ".join(cadena) #Asigna un espacio extra a todos los carácteres dentro de "cadena"
print(cadena) #Imprime el valor de cadena
print(" ".join(cadena)) #Imprime el valor de cadena pero le asigna un espacio extra a todos los carácteres

print("".join(reversed(cadena))) #Imprime "al revés" la cadena asignada como valor de "cadena"

# https://docs.python.org/3/tutorial/introduction.html#strings
# https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3
