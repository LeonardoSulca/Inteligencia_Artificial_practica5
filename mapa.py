# Construccion del entorno

# Librerias
import numpy as np
from random import random, randint
import time

# Paquetes Kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


from q_dl import Dqn
from q_dl2 import Dqn2

# Esta linea es para que el clic derecho no ponga un punto rojo 

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# Introduciendo last_x y last_y, usados para mantener el último punto en la memoria cuando dibujamos la arena en el mapa 
last_x = 0
last_y = 0
n_points = 0
length = 0

# Creando la mente de nuestra IA, la lista de acciones y la variable de recompensa 
brain = Dqn(4,3,0.9)
action2rotation = [0,20,-20]
reward = 0

brain2 = Dqn2(4,3,0.9)
action2rotation2 = [0,20,-20]
reward2 = 0

# Inicializando el mapa
first_update = True
def init():
    global sand
    global goal_x
    global goal_y
    global goal_x2
    global goal_y2
    global first_update
    sand = np.zeros((longueur,largeur))
    goal_x = 20
    goal_y = largeur - 20
    goal_x2 = 20
    goal_y2 = largeur - 20
    first_update = False

# Inicializando la ultima distancia del carro a la meta 
last_distance = 0
last_distance2 = 0

# La clase car

class Car(Widget):
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    sensor1_x = NumericProperty(0)
    sensor1_y = NumericProperty(0)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    sensor2_x = NumericProperty(0)
    sensor2_y = NumericProperty(0)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    sensor3_x = NumericProperty(0)
    sensor3_y = NumericProperty(0)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)
    signal1 = NumericProperty(0)
    signal2 = NumericProperty(0)
    signal3 = NumericProperty(0)
    
    def move(self, rotation):
        self.pos = Vector(*self.velocity) + self.pos
        self.rotation = rotation
        self.angle = self.angle + self.rotation
        self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos
        self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10:
            self.signal1 = 1.
        if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10:
            self.signal2 = 1.
        if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
            self.signal3 = 1.

class Car2(Widget):
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    sensor1_x = NumericProperty(0)
    sensor1_y = NumericProperty(0)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    sensor2_x = NumericProperty(0)
    sensor2_y = NumericProperty(0)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    sensor3_x = NumericProperty(0)
    sensor3_y = NumericProperty(0)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)
    signal1 = NumericProperty(0)
    signal2 = NumericProperty(0)
    signal3 = NumericProperty(0)
    
    def move(self, rotation):
        self.pos = Vector(*self.velocity) + self.pos
        self.rotation = rotation
        self.angle = self.angle + self.rotation
        self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos
        self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10:
            self.signal1 = 1.
        if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10:
            self.signal2 = 1.
        if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
            self.signal3 = 1.

class Ball1(Widget):
    pass
class Ball2(Widget):
    pass
class Ball3(Widget):
    pass
class Ball4(Widget):
    pass
class Ball5(Widget):
    pass
class Ball6(Widget):
    pass

# La clase juego

class Game(Widget):

    car = ObjectProperty(None)
    car2 = ObjectProperty(None)
    ball1 = ObjectProperty(None)
    ball2 = ObjectProperty(None)
    ball3 = ObjectProperty(None)
    ball4 = ObjectProperty(None)
    ball5 = ObjectProperty(None)
    ball6 = ObjectProperty(None)

    def serve_car(self):
        self.car.center = self.center
        self.car.velocity = Vector(6, 0)

        self.car2.center = self.center
        self.car2.velocity = Vector(6, 0)

    def update(self, dt):

        global brain
        global brain2
        global reward
        global reward2
        global last_distance
        global last_distance2
        global goal_x
        global goal_y
        global goal_x2
        global goal_y2
        global longueur
        global largeur

        longueur = self.width
        largeur = self.height
        if first_update:
            init()

        xx = goal_x - self.car.x
        yy = goal_y - self.car.y
        xx2 = goal_x2 - self.car2.x
        yy2 = goal_y2 - self.car2.y

        orientation = Vector(*self.car.velocity).angle((xx,yy))/180.
        orientation2 = Vector(*self.car2.velocity).angle((xx2,yy2))/180.
        
        state = [orientation, self.car.signal1, self.car.signal2, self.car.signal3]
        state2 = [orientation2, self.car2.signal1, self.car2.signal2, self.car2.signal3]
        
        action = brain.update(state, reward)
        action2 = brain2.update(state2,reward2)
        
        rotation = action2rotation[action]
        rotation2 = action2rotation2[action2]
        
        self.car.move(rotation)
        self.car2.move(rotation2)

        distance = np.sqrt((self.car.x - goal_x)**2 + (self.car.y - goal_y)**2)
        distance2 = np.sqrt((self.car2.x - goal_x2)**2 + (self.car2.y - goal_y2)**2)

        self.ball1.pos = self.car.sensor1
        self.ball2.pos = self.car.sensor2
        self.ball3.pos = self.car.sensor3

        self.ball4.pos = self.car2.sensor1
        self.ball5.pos = self.car2.sensor2
        self.ball6.pos = self.car2.sensor3

        if sand[int(self.car.x),int(self.car.y)] > 0:
            self.car.velocity = Vector(1, 0).rotate(self.car.angle)
            reward = -1
        else:
            self.car.velocity = Vector(6, 0).rotate(self.car.angle)
            reward = -0.2
            if distance < last_distance:
                reward = 0.1

        if sand[int(self.car2.x),int(self.car2.y)] > 0:
            self.car2.velocity = Vector(1, 0).rotate(self.car2.angle)
            reward2 = -1
        else:
            self.car2.velocity = Vector(6, 0).rotate(self.car2.angle)
            reward2 = -0.2
            if distance2 < last_distance2:
                reward2 = 0.1

        if self.car.x < 10:
            self.car.x = 10
            reward = -1
        if self.car.x > self.width - 10:
            self.car.x = self.width - 10
            reward = -1
        if self.car.y < 10:
            self.car.y = 10
            reward = -1
        if self.car.y > self.height - 10:
            self.car.y = self.height - 10
            reward = -1

        if distance < 100:
            goal_x = self.width-goal_x
            goal_y = self.height-goal_y

        last_distance = distance


        if self.car2.x < 10:
            self.car2.x = 10
            reward2 = -1
        if self.car2.x > self.width - 10:
            self.car2.x = self.width - 10
            reward2 = -1
        if self.car2.y < 10:
            self.car2.y = 10
            reward2 = -1
        if self.car2.y > self.height - 10:
            self.car2.y = self.height - 10
            reward2 = -1

        if distance2 < 100:
            goal_x2 = self.width-goal_x2
            goal_y2 = self.height-goal_y2

        last_distance2 = distance2

# Herramientas de pintura

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        global length, n_points, last_x, last_y
        with self.canvas:
            Color(0.8,0.7,0)
            d = 10.
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)
            last_x = int(touch.x)
            last_y = int(touch.y)
            n_points = 0
            length = 0
            sand[int(touch.x),int(touch.y)] = 1

    def on_touch_move(self, touch):
        global length, n_points, last_x, last_y
        if touch.button == 'left':
            touch.ud['line'].points += [touch.x, touch.y]
            x = int(touch.x)
            y = int(touch.y)
            length += np.sqrt(max((x - last_x)**2 + (y - last_y)**2, 2))
            n_points += 1.
            density = n_points/(length)
            touch.ud['line'].width = int(20 * density + 1)
            sand[int(touch.x) - 10 : int(touch.x) + 10, int(touch.y) - 10 : int(touch.y) + 10] = 1
            last_x = x
            last_y = y

# Botones de la API (clear, save y load)

class CarApp(App):

    def build(self):
        parent = Game()
        parent.serve_car()
        Clock.schedule_interval(parent.update, 1.0/60.0)
        self.painter = MyPaintWidget()
        clearbtn = Button(text = 'clear')
        savebtn = Button(text = 'save', pos = (parent.width, 0))
        loadbtn = Button(text = 'load', pos = (2 * parent.width, 0))
        clearbtn.bind(on_release = self.clear_canvas)
        savebtn.bind(on_release = self.save)
        loadbtn.bind(on_release = self.load)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(savebtn)
        parent.add_widget(loadbtn)
        return parent

    def clear_canvas(self, obj):
        global sand
        self.painter.canvas.clear()
        sand = np.zeros((longueur,largeur))

    def save(self, obj):
        print("Guardando la mente...")
        brain.save()
        brain2.save()

    def load(self, obj):
        print("Cargando la ultima mente de IA...")
        brain.load()
        brain2.load()

# Corriendo todo
if __name__ == '__main__':
    CarApp().run()
