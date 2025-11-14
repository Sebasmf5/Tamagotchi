# Food.py
import pygame
from abs_path import abs_path

class Food:
    def __init__(self, x, y, width, height, screen, action, pixel_font, panel_path, box_path, food_1_path, food_2_path, food_3_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.action = action
        self.pixel_font = pixel_font
        self.clicked_feed = False
        #PAnel central, contiene las comidas
        self.panel = pygame.transform.scale(pygame.image.load(panel_path), (self.width, self.height))
        self.panel_rect = self.panel.get_rect(center=(self.x, self.y))
        self.box_1 = pygame.transform.scale(pygame.image.load(box_path), (280, 310))
        self.box_2 = pygame.transform.scale(pygame.image.load(box_path), (280, 310))
        self.box_3 = pygame.transform.scale(pygame.image.load(box_path), (280, 310))
        self.normal_image = self.box_1
        self.box_1_rect = self.box_1.get_rect(center=(self.x - 200, self.y))
        self.box_2_rect = self.box_2.get_rect(center=(self.x, self.y))
        self.box_3_rect = self.box_3.get_rect(center=(self.x + 200, self.y))
        self.food_1 = pygame.transform.scale(pygame.image.load(food_1_path), (100, 100))
        self.food_2 = pygame.transform.scale(pygame.image.load(food_2_path), (75, 100))
        self.food_3 = pygame.transform.scale(pygame.image.load(food_3_path), (100, 100))
        self.food_1_rect = self.food_1.get_rect(center=(self.x - 200, self.y))
        self.food_2_rect = self.food_2.get_rect(center=(self.x, self.y - 10))
        self.food_3_rect = self.food_3.get_rect(center=(self.x + 200, self.y))
        self.exit = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/de_interaccion/exit.png')), (40, 40))
        self.exit_rect = self.exit.get_rect(center=(75, 65))

    def blit_food_menu(self, screen):
        if self.clicked_feed:
            screen.blit(self.panel, self.panel_rect)
            screen.blit(self.box_1, self.box_1_rect)
            screen.blit(self.box_2, self.box_2_rect)
            screen.blit(self.box_3, self.box_3_rect)
            screen.blit(self.food_1, self.food_1_rect)
            screen.blit(self.food_2, self.food_2_rect)
            screen.blit(self.food_3, self.food_3_rect)
            screen.blit(self.exit, self.exit_rect)

    def hover(self, x, y):
        if not self.clicked_feed:
            return

        # Coordenada central del panel (te deja el texto arriba en medio)
        text_center_x = self.panel_rect.centerx
        text_center_y = self.panel_rect.centery + 200  # puedes ajustar + o -

        # BOX 1
        if self.box_1_rect.collidepoint((x, y)):
            text = self.pixel_font.render('Cuesta: 8$  Efecto: +3', True, (74, 52, 38))
            text_rect = text.get_rect(center=(text_center_x, text_center_y))
            self.screen.blit(text, text_rect)

        # BOX 2
        elif self.box_2_rect.collidepoint((x, y)):
            text = self.pixel_font.render('Cuesta: 11$  Efecto: +6', True, (74, 52, 38))
            text_rect = text.get_rect(center=(text_center_x, text_center_y))
            self.screen.blit(text, text_rect)

        # BOX 3
        elif self.box_3_rect.collidepoint((x, y)):
            text = self.pixel_font.render('Cuesta: 15$  Efecto: +10', True, (74, 52, 38))
            text_rect = text.get_rect(center=(text_center_x, text_center_y))
            self.screen.blit(text, text_rect)

    def pressed(self, x, y, event):
        if not self.clicked_feed:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.box_1_rect.collidepoint((x, y)):
                if self.action['satiety'] + 3 <= 100 and self.action['logiki'] - 5 >= 0:
                    self.action['satiety'] += 3
                    self.action['clean'] -= 3
                    self.action['logiki'] -= 5
            if self.box_2_rect.collidepoint((x, y)):
                if self.action['satiety'] + 6 <= 100 and self.action['logiki'] - 10 >= 0:
                    self.action['satiety'] += 6
                    self.action['clean'] -= 6
                    self.action['logiki'] -= 10
            if self.box_3_rect.collidepoint((x, y)):
                if self.action['satiety'] + 10 <= 100 and self.action['logiki'] - 15 >= 0:
                    self.action['satiety'] += 10
                    self.action['clean'] -= 10
                    self.action['logiki'] -= 15
            if self.exit_rect.collidepoint((x, y)):
                self.clicked_feed = False
