" Sympy"
" Aprovechamiento del potencial de Python para el uso de álgebra simbólica"
"2007 Año de lanzamiento y desde entonces ha crecido ya que es un open source"
from sympy import *
from sympy import init_session
init_session(use_latex=True) " Importa todo y activa la impresión de expresiones en LaTeX"
" Podemos manejar variables diferente a solo las numéricas"
a=symbols("a") " Definimos símbolos"
a
a+b
b=1
a+b
b=pi
c=a*b
type(c) " Tipo multiplicación, podemos sobreescribir ya que estamos trabajando sobre Python"
alpha, beta= symbols("alpha beta")
(alpha + beta)
alpha.assumptions0 " Por defecto trabajará en los complejos (.assumptions0 brindará las propiedades)"
x, y, z, t = symbols('x y z t')
x.assumptions0
x=symbols("x", real=True, positive=True) "Para especificar un campo, tendrá que ser desde la hipótesis"
x.assumptions0
cos(z)**2+sin(z)**2
simplify(_) " Simplifica la expresión, en este caso, usando identidades trigonométricas"
sqrt(z**2)
simplify(_) " Como z por defecto es un complejo, no podrá hacer nada simplify"
y=symbols("y",real=True)
sqrt(y**2)
simplify(_) " Nos dará el valor absoluto ya que no sabemos si y es negativo o postivo"
.subs( , ) " Por cada aparación del primer argumento lo sustuirá por el segundo argumento"
(cos(z)**2+sin(z)**2)
(cos(z)**2+sin(z)**2).subs(z , x**2+1)
(cos(x)**2+sin(y)**2)
(cos(x)**2+sin(y)**2).subs({x:z-1,y:z+1}) " En expresiones con más de un símbolo usamos un diccionario"
.replace( , ) " Trabaja de forma similar que .subs solo que remplaza símbolos o funciones"
(cos(x)**2+sin(y)**2).replace(sin, exp)
sin(x)+3*x
(sin(x)+3*x).replace(x,pi) " Reemplaza y evalua"
(3*pi).evalf()
N(3*pi) " Un método y una función con la misma función evaluar la expresión""

"Refinar expresiones"

x, y, z, t=symbols("x y z t")
(x**2+y**2)**2
expand(_) " Resuelve la expresión"
(3+x**2-2*x+1)/(x-1)**2
apart(_) " Lleva la expresión a fracciones más simples"
(x**3+9*x**2+27*x+27)
factor(_) " Factoriza la expresión"
sin(x+2*y)
expand(_,trig=True) " En algunos casos tenemos que especificar que tipo expresión estamos trabajando"

"Derivadas"

expresion=cos(x)
expresion.diff(x) " En el argumento especificamos respecto a que estamos derivando"
Derivative() " Para dejar la derivada indicada"
diff(expresion,x) " En Sympy encontraremos métodos y funciones con el mismo propósito"
" Tiene mucho potencial ya que podemos usar expresiones arbitrariamente complejas"
expr=y*exp(2*x)+x/(x**2+y**3)
expr
expr.diff(x, 2, y, 3)
"Regla de la cadena"
F=Function("F")
F(x)
G=Function("G")
G(x)
diff(F(G(x)))
f=3*x+cos(y)
g=1/f
g.diff(x) " Respeta la regla de la cadena"

"Integrales"

" Para integrar Sympy se ve limitado ya que no tiene una gran capacidad para identificar las primitivas de una función pero si puede resolver integrales de baja y mediana complejidad"
integrate(cos(x)**2)
integrate(cos(x)**2,(x,0,1)) " En este caso definimos el intervalo en donde estará x"

"Limites"

" Podemos calcular limites que no tiendan a infinito"
expr=(x/tan(x))**(1/x**2)
expr
limit(expr, x, 0)
oo " Así es como se define infinito en Sympy"
limit(expr, x, oo) " NO puede calcular limites al infinito"
Limit(expr, x, 0) " Si queremos dejar expresado el límite usamos Limit()"
