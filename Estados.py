import pygame
from abs_path import abs_path

class TamagotchiSprite:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.states = {}
        self.anim_count = 0
        self.frame_delay = 6  # Controla la velocidad de animación

    def load_sprites(self, path, name_state, num_frames):
        # Cargar la hoja de sprites
        sprite_sheet = pygame.image.load(abs_path(path)).convert_alpha()
        sheet_width, sheet_height = sprite_sheet.get_size()
        frame_width = sheet_width // num_frames
        frame_height = sheet_height
        frames = []
        for i in range(num_frames):
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sprite_sheet.subsurface(rect)
            frame = pygame.transform.scale(frame, (self.width, self.height))
            frames.append(frame)

        self.states[name_state] = frames

    def set_frame(self, name_state):
        frames = self.states[name_state]
        index = (self.anim_count // self.frame_delay) % len(frames)
        frame = frames[index]
        self.anim_count += 1
        return frame

    def get_rect(self, name_state):
        frames = self.states[name_state]
        return frames[0].get_rect()