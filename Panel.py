import pygame
from abs_path import abs_path

class Panel:
    def __init__(self, x, y, width, height, path, pixel_font,
                 text_1=None, text_2=None, text_3=None, text_color=(255, 255, 255)):
        # Posición y dimensiones
        self.x, self.y = x, y
        self.width, self.height = width, height

        # Estado
        self.clicked_help = False
        self.text_color = text_color

        # Imagen de fondo del panel
        self.image = pygame.transform.scale(
            pygame.image.load(path),
            (self.width, self.height)
        )
        self.image_rect = self.image.get_rect(center=(self.x, self.y))

        # Botón de salida
        self.exit_image = pygame.transform.scale(
            pygame.image.load(abs_path('images/sprites/de_interaccion/exit.png')),
            (90,90)
        )
        self.exit_rect = self.exit_image.get_rect(center=(70, 70))

        # Textos del panel
        self.texts = []
        self.text_positions = [self.y - 50, self.y, self.y + 100]
        for i, text in enumerate([text_1, text_2, text_3]):
            if text:
                rendered = pixel_font.render(text, True, self.text_color)
                rect = rendered.get_rect(center=(self.x, self.text_positions[i]))
                self.texts.append((rendered, rect))

    def blit_panel(self, screen):
        if not pygame.display.get_init() or not self.clicked_help:
            return
        screen.blit(self.image, self.image_rect)
        for text_surface, text_rect in self.texts:
            screen.blit(text_surface, text_rect)
        screen.blit(self.exit_image, self.exit_rect)
