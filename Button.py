# Button.py
import pygame
from abs_path import abs_path

class Button:
    def __init__(self, x, y, width, height, path, pixel_font=None, text=None, text_color=(255,255,255),):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.pixel_font = pixel_font
        self.text_color = text_color
        self.image = pygame.transform.scale(pygame.image.load(path), (self.width, self.height))
        self.normal_image = self.image
        hover_path = abs_path('images/sprites/de_interaccion/boton_hover.png')
        try:
            self.hover_image = pygame.transform.scale(pygame.image.load(hover_path), (self.width, self.height))
        except Exception:
            self.hover_image = self.normal_image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        if self.text and self.pixel_font:
            self.btn_text = self.pixel_font.render(self.text, True, self.text_color)
            self.btn_text_rect = self.btn_text.get_rect(center=self.rect.center)
        else:
            self.btn_text = None
            self.btn_text_rect = None

    def blit_btn(self, screen):
        screen.blit(self.image, self.rect)
        if self.btn_text:
            screen.blit(self.btn_text, self.btn_text_rect)

    def hover(self, x, y):
        if self.rect.collidepoint((x, y)):
            self.image = self.hover_image
        else:
            self.image = self.normal_image

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos if hasattr(event, 'pos') else pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                return True
        return False
