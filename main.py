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

#Funciones

#Definir cada movimiento
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def izquierda():
    cabeza.direction = 'left'
def derecha():
    cabeza.direction = 'right'

#Ejecuta el movimiento
def movimiento():
    if cabeza.direction == 'up':        #Si la direccion es hacia arriba
        y =  cabeza.ycor()              #Obtiene la coordena Y
        cabeza.sety(y + 20)             #Actualiza la posición Y

    elif cabeza.direction == 'down':
        y =  cabeza.ycor()              #Obtiene la coordena Y
        cabeza.sety(y - 20)

    elif cabeza.direction == 'left':
        x =  cabeza.xcor()              #Obtiene la coordena X
        cabeza.setx(x - 20)

    elif cabeza.direction == 'right':
        x =  cabeza.xcor()              #Obtiene la coordena X
        cabeza.setx(x + 20)

#Conexion con teclado
window.listen()                         #Está pendiente si se oprime una tecla
window.onkeypress(arriba,'Up')        #Ejecuta la función arriba() cuando detecta up
window.onkeypress(abajo,'Down')
window.onkeypress(izquierda,'Left')
window.onkeypress(derecha,'Right')

#Ciclo permanente
while True:
    window.update()                     #Actualizar la pantalla
    movimiento()                        #Hace el respectivo movimiento
    time.sleep(posponer)                #Hace que se posponga por el tiempo establecido
