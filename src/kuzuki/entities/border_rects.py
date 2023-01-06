import typing as t

import pygame
from pygame.math import Vector2

from .. import constants as CONST


class BorderRects:
    rects: t.List[pygame.Rect]
    window: pygame.Surface

    def __init__(self, window: pygame.Surface):
        self.window = window
        self.rects = self.get_border_rects()

    def get_border_rects(self) -> t.List[pygame.Rect]:
        left_rect = pygame.Rect(
            Vector2(0, 0), (CONST.BORDER_THICKNESS, CONST.SCREEN_HEIGHT)
        )
        right_rect = pygame.Rect(
            Vector2(CONST.SCREEN_WIDTH - CONST.BORDER_THICKNESS, 0),
            (CONST.BORDER_THICKNESS, CONST.SCREEN_HEIGHT),
        )
        top_rect = pygame.Rect(
            Vector2(0, 0),
            (CONST.SCREEN_WIDTH, CONST.BORDER_THICKNESS),
        )
        return [left_rect, top_rect, right_rect]

    def render(self) -> None:
        for rect in self.rects:
            pygame.draw.rect(self.window, CONST.BORDER_COLOR, rect)
