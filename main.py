import pygame as pg
import sys as s

display = pg.display.set_mode((800, 600))
pg.init()
pg.display.set_caption('Physic Project')


def give_par(par: object, event, text):
    text = str(text)
    if par.need_input and event.type == pg.KEYDOWN:
        if event.unicode == '1' or event.unicode == '2' or event.unicode == '3' or event.unicode == '4' or event.unicode == '5' \
                or event.unicode == '6' or event.unicode == '7' or event.unicode == '8' or event.unicode == '9' or event.unicode == '0' \
                or event.unicode == '.':
            valid = True
        else:
            valid = False
        if event.key == pg.K_BACKSPACE:
            text = text[0:-1]
            valid = True
        elif valid:
            if event.unicode == ',':
                event.unicode = '.'
            text += event.unicode
    return int(text)


class Font:
    def __init__(self, x, y, font_color=(0, 0, 0), font_size=30, font_type='20011.ttf',
                 message=None):
        self.x = x
        self.y = y
        self.font_color = font_color
        self.font_type = font_type
        self.font_size = font_size
        self.message = message

    def draw_text(self):
        font_type = pg.font.Font(self.font_type, self.font_size)
        text = font_type.render(self.message, True, self.font_color)
        display.blit(text, (self.x, self.y))


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
        self.font_type = '20011.ttf'
        self.line_color = (0, 0, 0)

    def draw(self, text):
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
        if text == '1':
            text_font = Font(self.text_x, self.text_y, self.font_color, self.font_size, self.font_type, self.text)
        else:
            text_font = Font(self.text_x, self.text_y, self.font_color, self.font_size, self.font_type, text)
        text_font.draw_text()


class Circle:
    def __init__(self, color, fill=False, pos=(400, 300)):
        self.color = color
        self.fill = fill
        self.radius = 1
        self.pos = pos

    def draw(self, mass=1, speed=1, b=1, q=1):
        self.radius = mass * speed / (b * q)
        pg.draw.circle(display, self.color, self.pos, self.radius, width=2)


"R = mU/(Bq)"


def start():
    show_menu = True
    circle = Circle((0, 0, 0))
    mass_entry = Entry_parameters(600, 100, 160, 50, 'Entry mass', 610, 110)
    speed_entry = Entry_parameters(600, 200, 160, 50, 'Entry speed', 610, 210)
    b_entry = Entry_parameters(600, 300, 160, 50, 'Entry B', 610, 310)
    q_entry = Entry_parameters(600, 400, 160, 50, 'Entry q', 610, 410)
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
        mass_entry.draw(str(mass))
        speed_entry.draw(str(speed))
        b_entry.draw(str(b))
        q_entry.draw(str(q))
        if mass_entry.need_input:
            mass = give_par(mass_entry, event, mass)
        elif speed_entry.need_input:
            speed = give_par(speed_entry, event, speed)
        elif b_entry.need_input:
            b = give_par(b_entry, event, b)
        elif q_entry.need_input:
            q = give_par(q_entry, event, q)
        pg.display.update()


start()
