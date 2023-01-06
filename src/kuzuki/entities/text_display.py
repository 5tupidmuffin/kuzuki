import pygame
from pygame.math import Vector2

from .. import constants as CONST


class TextDisplay:
    window: pygame.Surface
    font: pygame.font.Font
    text: str
    position: Vector2

    def __init__(self, window: pygame.Surface, position: Vector2, text: str = ""):
        self.window = window
        self.font = pygame.font.SysFont(None, CONST.FONT_SIZE)
        self.position = position
        self.text = text

    def render(self, text: str = None) -> None:
        if text:
            self.text = text
        text_display = self.font.render(self.text, True, CONST.FONT_COLOR)
        self.window.blit(text_display, self.position)
