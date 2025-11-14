import pygame

import Estadistica
from Button import Button
from abs_path import abs_path
import Panel
import Food
import Estadistica

class UIManager:
    def __init__(self, screen, pixel_font, action, days_count):
        self.screen = screen
        self.font = pixel_font
        self.action = action
        self.days_count = days_count
        # --- 1. Botones y Elementos del Menú Principal ---
        self.cat_label = Button(120, 60, 300, 230, abs_path('images/sprites/backgrounds/letrero.png'), self.font)
        self.start_btn = Button(120, 180, 300, 150, abs_path('images/sprites/de_interaccion/boton_menu_principal.png'), self.font,
                                'Comenzar')
        self.rule_btn = Button(120, 280, 300, 150, abs_path('images/sprites/de_interaccion/boton_menu_principal.png'), self.font,
                               'Ayuda')
        self.exit_btn = Button(120, 380, 300, 150, abs_path('images/sprites/de_interaccion/boton_menu_principal.png'), self.font,
                               'Salir')
        self.info_satiety = Button(45, 50, 110, 110, abs_path('images/sprites/indicadores/saciedad.png'),
                                   self.font)
        self.info_toilet = Button(180, 50, 90, 100, abs_path('images/sprites/indicadores/baño.png'), self.font)  # X=180
        self.info_happy = Button(300, 50, 90, 90, abs_path('images/sprites/indicadores/felicidad.png'),
                                 self.font)  # X=300
        # Indicador de salud (separado)
        self.info_health = Button(450, 50, 90, 100, abs_path('images/sprites/indicadores/salud.png'), self.font)

        # --- 3. Botones de Interacción (Barra de Acción) ---
        # Botón de estadísticas (Esquina superior derecha)
        self.btn_statistic = Button(715, 40, 300, 150,
                                    abs_path('images/sprites/de_interaccion/boton_menu_principal.png'), self.font,
                                    'Estadísticas')
        # Botones de acción principales (Fila inferior)
        action_btn_img = abs_path('images/sprites/de_interaccion/boton_hover.png')  # Reutiliza la ruta del sprite
        y_pos = 575  # Posición Y fija para todos los botones de acción

        self.btn_satiety = Button(85, y_pos, 290, 150, action_btn_img, self.font, 'Alimentar', (150, 75, 0))
        self.btn_toilet = Button(285, y_pos, 290, 150, action_btn_img, self.font, 'Limpiar', (150, 75, 0))
        self.btn_play = Button(515, y_pos, 290, 150, action_btn_img, self.font, 'Jugar', (150, 75, 0))
        self.btn_health = Button(715, y_pos, 290, 150, action_btn_img, self.font, 'Curar', (150, 75, 0))

        # --- 4. Paneles y Menús (Popups) ---
        # Menú de Ayuda
        self.help_menu = Panel.Panel(
            400, 250, 900, 900,
            abs_path('images/sprites/backgrounds/panel_info.png'),
            self.font,
            'Debes mantener los indicadores normales.',
            'Si al menos uno es igual a cero, perderás. ¡Diviértete!',
            "",
            (150, 75, 0)
        )

        # Menú de Comida
        self.food = Food.Food(
            400, 250, 750, 900,
            self.screen,
            self.action,
            self.font,
            abs_path('images/sprites/backgrounds/panel_info.png'),
            abs_path('images/sprites/de_interaccion/boton_hover.png'),
            abs_path('images/sprites/tamagotchi_gato/manzana.png'),
            abs_path('images/sprites/tamagotchi_gato/pizza.png'),
            abs_path('images/sprites/tamagotchi_gato/carne.png')
        )

        self.estadistica = Estadistica.Estadistica(400,250,
            self.screen,
            self.font,
            750, 900,
            abs_path('images/sprites/backgrounds/panel_info.png'),
            str(action['logiki'])+ '$',
            'Name: Gatito',
            f'Days: {days_count}'
        )

    def draw_main_menu(self):
        self.cat_label.blit_btn(self.screen)
        self.start_btn.blit_btn(self.screen)
        self.rule_btn.blit_btn(self.screen)
        self.exit_btn.blit_btn(self.screen)

    def can_feed(self):
        self.food.clicked_feed = True

    def cant_feed(self):
        self.food.clicked_feed = False

    def draw_info(self):
        # Dibujo de iconos
        self.info_satiety.blit_btn(self.screen)
        self.info_toilet.blit_btn(self.screen)
        self.info_happy.blit_btn(self.screen)
        self.info_health.blit_btn(self.screen)

        # Dibujo de textos
        satiety_text = self.font.render(str(self.action.get('satiety', 0)), True, (255, 255, 255))
        self.screen.blit(satiety_text, (70, 40))
        toilet_text = self.font.render(str(self.action.get('clean', 0)), True, (255, 255, 255))
        self.screen.blit(toilet_text, (210, 40))
        happy_text = self.font.render(str(self.action.get('happy', 0)), True, (255, 255, 255))
        self.screen.blit(happy_text, (330, 40))
        health_text = self.font.render(str(self.action.get('health', 0)), True, (255, 255, 255))
        self.screen.blit(health_text, (480, 40))

    def update_days_count(self, days_count):
        self.estadistica.set_days_count(days_count)

    def draw_action_buttons(self):
        self.btn_statistic.blit_btn(self.screen)
        self.btn_satiety.blit_btn(self.screen)
        self.btn_toilet.blit_btn(self.screen)
        self.btn_play.blit_btn(self.screen)
        self.btn_health.blit_btn(self.screen)

    def draw_help(self):
        self.help_menu.blit_panel(self.screen)

    def draw_food_menu(self):
        self.food.blit_food_menu(self.screen)

    def draw_estadistica(self):
        self.estadistica.blit_statistics()

    def handle_hover(self, mouse_pos):
        x, y = mouse_pos
        self.start_btn.hover(x, y)
        self.rule_btn.hover(x, y)
        self.exit_btn.hover(x, y)
        self.btn_statistic.hover(x, y)
        self.btn_satiety.hover(x, y)
        self.btn_toilet.hover(x, y)
        self.btn_play.hover(x, y)
        self.btn_health.hover(x, y)
        self.food.hover(x, y)