import turtle                           #La libreria turtle ayuda a construir la interfaz gráfica
import time                             #Para obtenier el tiempo

posponer = 0.1

#Configuración

window = turtle.Screen()                #Crea una ventana nueva
window.title('Snake')                   #Ponemos titulo
window.bgcolor('#353535')               #Color de fondo
window.setup(width=600,height=600)      #Redimensionar pantalla
window.tracer(0)                        #Ayuda a hacer la animación mas placentera

#Cabeza de la serpiente

cabeza = turtle.Turtle()                #Crea un objeto para mostrar en pantalla
cabeza.speed(0)                         #Se muestra al inciar
cabeza.shape('square')                  #Se le asigna forma de cuadrado
cabeza.color('#75C46D')                 #Color a la cabeza
cabeza.penup()                          #Elimina el rastro del objeto
cabeza.goto(0,0)                        #Centra el objeto
cabeza.direction = 'stop'               #Asigna direccion, en este caso estatico

