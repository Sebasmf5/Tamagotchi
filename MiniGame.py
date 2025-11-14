import pygame
import random
import time
from abs_path import abs_path

class MiniGame:
    def __init__(self, screen, clock, pixel_font, background, action, tamagotchi):
        self.screen = screen
        self.clock = clock
        self.font = pixel_font
        self.bg = background
        self.action = action  # Diccionario con stats del Tamagotchi

        # Tamagotchi principal
        self.tama_sprite = tamagotchi

        # Configuración del minijuego
        self.game_duration = 15  # segundos
        self.fps = 45
        pygame.mouse.set_visible(True)
        # Sprite del ratón
        self.mouse_sheet = pygame.image.load(abs_path('images/sprites/raton/idling.png')).convert_alpha()
        self.num_frames = 6
        frame_width = self.mouse_sheet.get_width() // self.num_frames
        frame_height = self.mouse_sheet.get_height()
        self.mouse_frames = []
        for i in range(self.num_frames):
            frame = self.mouse_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.scale(frame, (80, 80))
            self.mouse_frames.append(frame)
        self.mouse_rect = self.mouse_frames[0].get_rect()
        self.reset_mouse()
        self.mouse_anim_count = 0
        self.frame_delay = 6

    def reset_mouse(self):
        self.mouse_rect.x = random.randint(100, 700)
        self.mouse_rect.y = random.randint(100, 500)

    def run(self):
        score = 0
        start_time = time.time()
        appear_timer = 0
        running = True

        while running:
            self.screen.blit(self.bg, (0, 0))
            # Dibujar Tamagotchi principal
            self.screen.blit(self.tama_sprite.set_frame("idle"), (315, 340))

            dt = self.clock.get_time()
            appear_timer += dt

            # Mover ratón cada segundo
            if appear_timer > 3000:
                self.reset_mouse()
                appear_timer = 0
                score -= 1  # penalización si no atrapas

            # Animación ratón
            frame_index = (self.mouse_anim_count // self.frame_delay) % self.num_frames
            self.screen.blit(self.mouse_frames[frame_index], (self.mouse_rect.x, self.mouse_rect.y))
            self.mouse_anim_count += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.mouse_rect.collidepoint(event.pos):
                        score += 2
                        self.reset_mouse()

            # Mostrar puntaje y monedas
            score_text = self.font.render(f"Puntaje: {score}", True, (255, 255, 255))
            coins_text = self.font.render(f"Monedas: {self.action.get('coins', 0)}", True, (255, 255, 0))
            self.screen.blit(score_text, (50, 50))
            self.screen.blit(coins_text, (50, 80))

            # Terminar el minijuego después de duración
            if time.time() - start_time > self.game_duration:
                running = False
                pygame.mouse.set_visible(False)

            pygame.display.update()
            self.clock.tick(self.fps)

        # Ajustar stats del Tamagotchi al final
        self.action['happy'] = min(100, self.action['happy'] + max(score, 0))
        self.action['logiki'] = self.action.get('logiki', 0) + max(score, 0)