import pygame
from settings import *

class Button():
    def __init__(self, text, width, height, pos, elevation, img):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        gui_font = pygame.font.Font(None, 30)
        self.image = 0
        self.texto = 0
        
        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#141B1B'

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        #bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#212B2B'

        # text
        if text is not None:
            self.text_surf = gui_font.render(text, True, '#FFFFFF')
            self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        else:
            self.texto = None

        # image if applicable
        if img is not None:
            self.img_surf = pygame.image.load(img).convert_alpha()
            self.img_rect = self.img_surf.get_rect(center = self.top_rect.center)
        else:
            self.image = None

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        if self.texto is not None and self.image is None:
            self.text_rect.center = self.top_rect.center
        else:
            self.text_rect.center = self.top_rect.midtop
        if self.image is not None:
            self.img_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.screen, self.bottom_color, self.bottom_rect, border_radius = 12)
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, border_radius = 12)
        if self.image is not None:
            self.screen.blit(self.img_surf, self.img_rect)
        if self.texto is not None:
            self.screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
                return True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                return False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#141B1B'
            return False