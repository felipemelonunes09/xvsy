
import pygame
from application.scene.RuneFrame import RuneFrame
from config.Configuration import Configuration


class LowerDeck(pygame.sprite.Group):
    
    def __init__(self, position: tuple[int, int], *a, **k):
        super().__init__(*a, **k)
        self.runesFrame = [RuneFrame(position=[position[0] + index*Configuration.game_style_frame_offset, position[1]]) for index in range(7)]
        self.add(*self.runesFrame)
