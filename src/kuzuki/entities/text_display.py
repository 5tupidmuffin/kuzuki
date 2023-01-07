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


class GameOverScreen:
    window: pygame.Surface
    height: int
    width: int
    rect: pygame.Rect
    text: str
    font: pygame.font.Font
    text_display: pygame.Surface

    def __init__(self, window: pygame.Surface):
        self.window = window
        self.height = CONST.SCREEN_HEIGHT // 4
        self.width = CONST.SCREEN_WIDTH
        self.rect = pygame.Rect(Vector2(0, 0), (self.width, self.height))
        self.rect.center = self.window.get_rect().center
        self.text = "GAME OVER - PRESS [R] TO RESET"
        self.font = pygame.font.SysFont(None, 40)
        self.text_display = self.font.render(self.text, True, CONST.RED_COLOR)

    def render(self) -> None:
        pygame.draw.rect(self.window, CONST.WHITE_COLOR, self.rect)
        self.window.blit(
            self.text_display,
            self.text_display.get_rect(center=self.window.get_rect().center),
        )
