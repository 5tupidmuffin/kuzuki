import typing as t

import pygame
from pygame.math import Vector2

from .. import constants as CONST
from ..typing import Dimension


class Brick:
    window: pygame.Surface
    color: pygame.Color
    position: Vector2
    width: int
    height: int
    rect: pygame.Rect

    def __init__(
        self,
        window: pygame.Surface,
        color: pygame.Color,
        position: Vector2,
        dimentions: Dimension,
    ):
        self.window = window
        self.color = color
        self.position = position
        self.width = dimentions["WIDTH"]
        self.height = dimentions["HEIGHT"]
        self.rect = pygame.Rect(self.position, (self.width, self.height))

    def render(self) -> None:
        pygame.draw.rect(self.window, self.color, self.rect)


def get_bricks(window: pygame.Surface) -> t.List[Brick]:
    column_count = CONST.BRICKS_COLUMN_COUNT
    start_position = Vector2(0, 0 + (CONST.BRICKS_TOP_MARGIN))
    # fmt: off
    color_map = {
        0: CONST.RED_COLOR,    1: CONST.RED_COLOR,
        2: CONST.GOLD_COLOR,   3: CONST.GOLD_COLOR,
        4: CONST.GREEN_COLOR,  5: CONST.GREEN_COLOR,
        6: CONST.LIME_COLOR,   7: CONST.LIME_COLOR,
    }
    # fmt: on
    bricks = []

    for i in range(column_count):
        while (start_position.x + CONST.BRICK_DIMENSIONS["WIDTH"]) < CONST.SCREEN_WIDTH:
            brick = Brick(window, color_map[i], start_position, CONST.BRICK_DIMENSIONS)
            bricks.append(brick)
            start_position.x += (
                CONST.BRICK_DIMENSIONS["WIDTH"] + CONST.BRICK_COLUMN_MARGIN
            )

        start_position.x = 0
        start_position.y += CONST.BRICK_DIMENSIONS["HEIGHT"] + CONST.BRICK_ROW_MARGIN

    return bricks
