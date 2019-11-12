#David ALonso Garduño Granados
#
#
#
#
#
from MisFunciones import vabs
from math import sqrt, sin
li=(6,5,4,3,2)
betas=[]
def seno(alfa):
    for h in li:
        beta=alfa/2**(h-1)
        dosbeta=2*beta*sqrt(1-(beta**2))
        betas.append(beta)
        beta=dosbeta
    return(beta)
    
if __name__ == "__main__":
    #seno(.5)
    print("Este bloque se ejecuta si el programa \
es llamado desde IDLE, la variable __name__ tiene \
almacenada la cadena '__main__' ")
    print(__name__)
else:
    print("Si el archivo se utiliza como modulo,\
 es decir se importa, la variable __name__ contiene\
el nombre nombre del archivo")
    print(__name__)
