import pygame
from abs_path import abs_path

class Estadistica:
    def __init__(self, x, y, screen, pixel_font, width, height, path, text_lg=None, text_name=None, text_days=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.pixel_font = pixel_font

        self.text_lg = text_lg
        self.text_name = text_name
        self.days_count = 0

        self.image = pygame.transform.scale(pygame.image.load(path), (self.width, self.height))
        self.image_rect = self.image.get_rect(center=(self.x, self.y))

        self.exit = pygame.transform.scale(
            pygame.image.load(abs_path('images/sprites/de_interaccion/exit.png')),
            (40, 40)
        )
        self.exit_rect = self.exit.get_rect(center=(75, 65))
        self.clicked_statistics = False

        self.gato_image = pygame.transform.scale(
            pygame.image.load(abs_path('images/sprites/tamagotchi_gato/cabeza_gato.png')),
            (60, 60)
        )

        self.gato_text = self.pixel_font.render(self.text_lg, True, (255, 255, 255))
        self.gato_text_rect = self.gato_text.get_rect(center=(710, 75))

        self.name_text = self.pixel_font.render(self.text_name, True, (255, 255, 255))
        self.name_text_rect = self.name_text.get_rect(center=(400, 200))
        self.update_days_text()

    def update_days_text(self):
        self.days_text = self.pixel_font.render(f"Days: {self.days_count}", True, (150, 75, 0))
        self.days_text_rect = self.days_text.get_rect(center=(400, 250))

    def update_money_text(self):
        self.gato_text = self.pixel_font.render(f"$ : {self.text_lg}", True, (150, 75, 0))
        self.gato_text_rect = self.gato_text.get_rect(center=(400, 300))

    def set_days_count(self, days):
        self.days_count = days
        self.update_days_text()

    def set_money_count(self, text_lg):
        self.text_lg = text_lg
        self.update_money_text()

    def blit_statistics(self):
        if self.clicked_statistics:
            self.screen.blit(self.image, self.image_rect)
            self.screen.blit(self.gato_text, self.gato_text_rect)
            self.screen.blit(self.name_text, self.name_text_rect)
            self.screen.blit(self.days_text, self.days_text_rect)
            self.screen.blit(self.exit, self.exit_rect)
            self.screen.blit(self.gato_image, (620, 45))
