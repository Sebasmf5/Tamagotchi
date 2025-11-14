"""
Angela Patricia Aponte
José Sebastian Arenas
Sebastian Morales Flórez
Nicole Daniela Londoño
Andrés Felipe Saavedra
"""


import pygame
import time
import random
import MiniGame
from abs_path import abs_path
from Estados import TamagotchiSprite
from UIManager import UIManager


screen_width = 800
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pixel_font = pygame.font.Font(abs_path('font/FiraSans-SemiBoldItalic.ttf'), 27)
pygame.display.set_caption("Gatito")
pygame.display.set_icon(pygame.image.load(abs_path('images/sprites/tamagotchi_gato/logo.png')))
TamagotchiSprite = TamagotchiSprite(200,200)
TamagotchiSprite.load_sprites("images/sprites/tamagotchi_gato/Idle2.png", "idle", 10)
TamagotchiSprite.load_sprites("images/sprites/tamagotchi_gato/sleep.png", "sleep", 4)

clock = pygame.time.Clock()
action = {'satiety': 30, 'clean': 100, 'happy': 80, 'health': 100, 'logiki': 50}

day = 30000
days_event = pygame.USEREVENT + 1
pygame.time.set_timer(days_event, day)
fps  = 45
time_out = 15
text_timer = 0
random_timer = 0
random_interval = 10
night_timer = 0
days_count = 0
end_menu = False
end_game = False
is_sleep = False
cant_clear = False
cant_help = False
can_play = False
start_time = None
game_time = None
menu_anim_count = 0

event_message = ""
event_msg_timer = 0

cursor = pygame.image.load(abs_path('images/sprites/tamagotchi_gato/hand.png'))
pygame.mouse.set_visible(False)
background_menu = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/backgrounds/background_menu.png')), (screen_width, screen_height))
background = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/backgrounds/background.png')), (screen_width, screen_height))
raton_suelo_img = pygame.image.load(abs_path('images/sprites/raton/suelo.png')).convert_alpha()
raton_suelo_img = pygame.transform.scale(raton_suelo_img, (screen_width, screen_height))
game_over_image = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/backgrounds/game_over.png')), (screen_width, screen_height))
day_image = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/states/sun.png')), (50, 50))
night_image = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/states/moon.png')), (50, 50))
gameover_text = pixel_font.render('Reinicia el juego para volver a jugar', True, (75, 255, 255))

UIManager = UIManager(screen, pixel_font, action, days_count)

def tamagotchi_animation(x, y):
    if not is_sleep:
        screen.blit(TamagotchiSprite.set_frame("idle"), (x, y))
        screen.blit(day_image,(735,70))
    else:
        screen.blit(TamagotchiSprite.set_frame("sleep"), (x, y))

def score_tick():
    global start_time, time_out, random_timer, random_interval
    t_time = time.time() - start_time
    if t_time > time_out:
        action['satiety'] -= 3
        action['clean'] -= 2
        action['happy'] -= 3
        action['health'] -= random.randint(0, 5)
        start_time = time.time()
    if (time.time() - random_timer) >= random_interval:
        random_events()
        random_timer = time.time()

def clearAfter():
    global cant_clear
    if action['clean'] + 16 <= 100:
        action['clean'] += 16
    else:
        cant_clear = True

def medicine():
    global cant_help
    if action['logiki'] - 3 >= 0:
        if action['health'] + 10 <= 100:
            action['health'] += 10
            action['logiki'] -= 3
        else:
            cant_help = True

def random_events():
    global event_message, event_msg_timer
    r = random.random()
    print(r)
    if r < 0.05:  # 5% de probabilidad
        action['health'] -= int(random.uniform(5, 15))
        event_message = "¡Tu gatito ha enfermado (se mojó afuera)!"
    elif r < 0.08:  # 3% de probabilidad
        action['happy'] -= int(random.uniform(10, 20))
        action['clean'] -= int(random.uniform(5, 15))
        event_message = "¡Han asustado a tu gatito y ha hecho pis!"
    elif r < 0.10:  # 2% de probabilidad
        action['clean'] -= int(random.uniform(5, 15))
        event_message = "¡Tu gatito acaba de revolcarse en el lodo!"
    elif r < 0.12:  # 2% de probabilidad
        action['satiety'] -= int(random.uniform(5, 10))
        event_message = "Tu gatito tiene hambre."
    elif r < 0.15:  # 3%
        gain = int(random.uniform(5, 15))
        action['happy'] = min(100, action['happy'] + gain)
        event_message = "¡Tu gatito encontró un juguete!"
    else:
        event_message = ""
    event_msg_timer = 240


def game_over():
    if action['satiety'] <= 0 or action['clean'] <= 0 or action['happy'] <= 0 or action['health'] <= 0:
        pygame.mixer.music.stop()
        screen.blit(game_over_image, (0, 0))
        screen.blit(gameover_text, (35, 450))
        pygame.display.update()
        pygame.time.delay(3000)
        return True
    return False

button_sound = pygame.mixer.Sound(abs_path('sounds/button.wav'))
button_sound.set_volume(0.05)

def game():
    global is_sleep, cant_clear, days_count, text_timer, cant_help, end_game, night_timer, start_time
    global event_message, event_msg_timer, mini_game

    pygame.mixer.music.load(abs_path('sounds/game.mp3'))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    start_time = time.time()
    while not end_game:
        screen.blit(background, (0, 0))
        UIManager.draw_info()
        tamagotchi_animation(315, 340)
        UIManager.draw_action_buttons()
        pos_x, pos_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                end_game = True
            if event.type == days_event:
                night_timer = 0
                is_sleep = True
            if not is_sleep:
                if UIManager.btn_statistic.is_clicked(event):
                    UIManager.estadistica.clicked_statistics = True
                    button_sound.play()
                if UIManager.btn_satiety.is_clicked(event):
                    UIManager.can_feed()
                UIManager.food.pressed(pos_x, pos_y, event)
                if action['logiki'] >= 0:
                    UIManager.food.pressed(pos_x, pos_y, event)
                    button_sound.play()
                if UIManager.btn_toilet.is_clicked(event):
                    clearAfter()
                if UIManager.btn_play.is_clicked(event):
                    mini_game = MiniGame.MiniGame(screen, clock, pixel_font, pygame.image.load(
                        abs_path('images/sprites/raton/suelo.png')).convert_alpha(), action, TamagotchiSprite)
                    button_sound.play()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(abs_path('sounds/game_2.ogg'))
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play()
                    mini_game.run()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(abs_path('sounds/game.mp3'))
                    pygame.mixer.music.play(loops=-1)
                    UIManager.estadistica.set_money_count(action['logiki'])
                if UIManager.btn_health.is_clicked(event):
                    medicine()
            if UIManager.estadistica.exit_rect.collidepoint(pos_x, pos_y):
                UIManager.estadistica.clicked_statistics = False
                button_sound.play()
            if UIManager.food.exit_rect.collidepoint((pos_x, pos_y)) and event.type == pygame.MOUSEBUTTONDOWN:
                UIManager.cant_feed()
                button_sound.play()

        UIManager.handle_hover((pos_x, pos_y))

        if is_sleep and night_timer > 700:
            is_sleep = False
            night_timer = 0
            days_count += 1
            UIManager.estadistica.set_days_count(days_count)
        night_timer += 1

        if cant_clear:
            text = pixel_font.render("No puedes limpiarlo", True, (255, 255, 255))
            screen.blit(text, (280, 300))
            if text_timer > 75:
                cant_clear = False
                text_timer = 0
            text_timer += 1

        if cant_help:
            text = pixel_font.render('No puedes ayudarlo', True, (255, 255, 255))
            screen.blit(text, (280, 300))
            if text_timer > 75:
                cant_help = False
                text_timer = 0
            text_timer += 1

        if UIManager.estadistica.clicked_statistics:
            UIManager.draw_estadistica()

        if UIManager.food.clicked_feed:
            UIManager.draw_food_menu()

        if event_msg_timer > 0 and event_message != "":
            msg = pixel_font.render(event_message, True, (255, 255, 255))
            screen.blit(msg, (150, 260))
            event_msg_timer -= 1

        if pygame.mouse.get_focused():
            screen.blit(cursor, (pos_x, pos_y))
        UIManager.estadistica.set_money_count(action['logiki'])

        score_tick()
        clock.tick(fps)
        pygame.display.update()

        if game_over():
            break

def menu():
    global end_menu, start_time, menu_anim_count
    pygame.mixer.music.load(abs_path('sounds/musica.mp3'))
    pygame.mixer.music.play(loops=-1)
    while not end_menu:
        screen.blit(background_menu, (0, 0))
        UIManager.draw_main_menu()
        pos_x, pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_menu = True
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                end_menu = True
                pygame.quit()
            if UIManager.start_btn.is_clicked(event):
                end_menu = True
                game()
            if UIManager.rule_btn.is_clicked(event):
                UIManager.help_menu.clicked_help = True
            if UIManager.exit_btn.is_clicked(event):
                pygame.mouse.set_visible(True)
                end_menu = True
        UIManager.start_btn.hover(pos_x, pos_y)
        UIManager.rule_btn.hover(pos_x, pos_y)
        UIManager.exit_btn.hover(pos_x, pos_y)
        if UIManager.help_menu.clicked_help:
            UIManager.draw_help()
            if UIManager.help_menu.exit_rect.collidepoint((pos_x, pos_y)):
                for ev in pygame.event.get([pygame.MOUSEBUTTONDOWN]):
                    if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                        UIManager.help_menu.clicked_help = False
        if pygame.mouse.get_focused():
            screen.blit(cursor, (pos_x, pos_y))

        clock.tick(fps)
        pygame.display.update()

if __name__ == '__main__':
    menu()
    pygame.quit()
