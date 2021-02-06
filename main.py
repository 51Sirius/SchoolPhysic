import pygame as pg
import sys as s


display = pg.display.set_mode((800, 600))
pg.init()
pg.display.set_caption('Physic Project')


class Entry_parameters:
    def __init__(self, x, y, width, height, text, mess_x, mess_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_x = mess_x
        self.text_y = mess_y
        self.bg_color = (94, 94, 94)
        self.need_input = False
        self.font_color = (0, 247, 255)
        self.active_line_color = (26, 26, 176)
        self.font_size = 30
        self.font_type = 'Arial'
        self.line_color = (0, 0, 0)

    def draw(self):
        click = pg.mouse.get_pressed()
        mouse = pg.mouse.get_pos()
        if click[0] == 1 and self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            self.need_input = True
        if click[0] == 1 and not (
                self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height):
            self.need_input = False
        rect_1 = (self.x, self.y, self.width, self.height)
        rect = pg.draw.rect(display, self.bg_color, rect_1)
        if self.need_input:
            left_line = pg.draw.line(display, self.active_line_color, [self.x, self.y], [self.x, self.y + self.height],
                                     6)
            top_line = pg.draw.line(display, self.active_line_color, [self.x, self.y], [self.x + self.width, self.y],
                                    6)
            down_line = pg.draw.line(display, self.active_line_color, [self.x, self.y + self.height],
                                     [self.x + self.width, self.y + self.height], 6)
            right_line = pg.draw.line(display, self.active_line_color, [self.x + self.width, self.y],
                                      [self.x + self.width,
                                       self.y + self.height], 6)
        else:
            left_line = pg.draw.line(display, self.line_color, [self.x, self.y], [self.x, self.y + self.height], 8)
            top_line = pg.draw.line(display, self.line_color, [self.x, self.y], [self.x + self.width, self.y], 8)
            down_line = pg.draw.line(display, self.line_color, [self.x, self.y + self.height],
                                     [self.x + self.width, self.y + self.height], 8)
            right_line = pg.draw.line(display, self.line_color, [self.x + self.width, self.y],
                                      [self.x + self.width, self.y + self.height], 8)
        text_font = Font(self.text_x, self.text_y, self.font_color, self.font_size, self.font_type, self.text)
        text_font.draw_text()


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