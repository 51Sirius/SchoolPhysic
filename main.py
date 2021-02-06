import pygame as pg
import sys as s


display = pg.display.set_mode((800, 600))
pg.init()
pg.display.set_caption('Physic Project')


class Circle:
    def __init__(self, color, fill=False, pos=(400, 300)):
        self.color = color
        self.fill = fill
        self.radius = 1
        self.pos = pos

    def draw(self, mass=1, speed=1, b=1, q=1):
        self.radius = mass*speed/(b*q)
        pg.draw.circle(display, self.color, self.pos, self.radius, width=2)



"R = mU/(Bq)"


def start():
    show_menu = True
    circle = Circle((0, 0, 0))
    mass = 1
    speed = 1
    b = 1
    q = 1
    while show_menu:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            s.exit()
        display.fill((255, 255, 255))
        circle.draw(mass, speed, b, q)
        pg.display.update()


start()