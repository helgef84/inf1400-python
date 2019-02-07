import pygame as pg 
from settings import *



class InputBox:
	
    def __init__(self, xpos, ypos, width, height, textfile, score, name=''):
        self.font = pg.font.Font(None, 32)
        self.rect = pg.Rect(xpos, ypos, width, height)
        self.color = GREEN
        self.name = name
        self.txt_surface = self.font.render(name, True, self.color)
        self.active = False
        self.textfile = textfile
        self.score = score

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = BLACK if self.active else GREEN
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.textfile.write(self.name +" " + str(self.score) + "\n")
                    self.textfile.close()
                    self.name = ''
                elif event.key == pg.K_BACKSPACE:
                    self.name = self.name[:-1]
                else:
                    self.name += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.name, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

