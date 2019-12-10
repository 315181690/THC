from fltk import *
import sys
"""
def theCancelButtonCallback(ptr):
	sys.exit(0)

window = Fl_Window(100,100,200,90) #Dimensiones de la ventana
window.label("Ventana ejemplo") #Nombre de la ventana 
button = Fl_Button(9,20,180,50) #Dimensiones del botón
button.label("Hola a todos :C") #Leyenda del botón
button.callback(theCancelButtonCallback)
window.end()
window.show(len(sys.argv), sys.argv) #Los argumentos que mostrará la ventana
Fl.run() #Como en matplot este comando corre la ventana

def btn_cb(ptr):
    sys.exit(0) #Define lo que hará el botón

window = Fl_Window(200, 90, "Hola 2") #DImensiones y leyenda de la ventana
button = Fl_Button(9, 20, 180, 50, "Hola a todos 2")
button.callback("btn_cb") #Define lo que hará el botón
window.end()
window.show()
#Estará en un loop ya que el callback es una cadena así que no puede llamar esa función
Fl.run() #Si quitamos las comillas el programa correra de manera correcta
"""
from fltk import *
class MyApp:
    def __init__(self):
        #Creamos la ventana con las dimensiones y el nombre que mostrará
        self.window = Fl_Window(150, 40)
        self.window.label("Callbacks")
        #Create el botón
        self.button1 = Fl_Button(5, 10, 140, 20)
        self.button1.label("Click me! ;)")
        #Definimos que es lo que hará nuestro botón al ser "tocado"
        self.button1.callback(self.clicked)
        self.window.end()
        self.window.show()
        #Cuando el botón sea "tocado" esta función será llamada
    def clicked(self, widget):
        widget.label("I’ve been clicked!")
app = MyApp()
Fl.run()

""" #Mío
from fltk import *
class MyApp:
    def __init__(self):
        #Creamos la ventana igual que en los anteriores
        self.window = Fl_Window(400, 185)
        self.window.label("Entrada y salida de texto")
        #EL buffer de texto almacenará lo que escribamos
        self.textbuffer = Fl_Text_Buffer()
        #Un estado inicial del texto almacenado
        self.textbuffer.text("Usar FLTK es complicado desde su instalación, KISS")
        #Muestra el texto pero no permite editarlo
        self.textdisplay = Fl_Text_Display(5, 20, 190, 70)
        #Esta ventana mostrará el texto almacenado en el buffer
        self.textdisplay.buffer(self.textbuffer)
        self.textdisplay.label("Ventana de texto")
        #Esta ventana nos dejará editar el texto almacenado
        self.textedit = Fl_Text_Editor(5, 110, 190, 70)
        #Definimos el editor de texto para mostrar el mismo texto almacenado
        self.textedit.buffer(self.textbuffer)
        self.textedit.label("Editor de texto")
        button = Fl_Button(200,100,180,50) #Dimensiones del botón
        button.label("Hola a todos :C")
        def btn_cb(ptr):
            sys.exit(0)
        button.callback(btn_cb)
        
        self.window.end()
        self.window.show()
app = MyApp()
Fl.run()
"""
