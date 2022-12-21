import pygame
from pygame.math import Vector2

from .. import constants as CONST
from ..typing import Dimension


class Brick:
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
        self.width = dimentions['WIDTH']
        self.height = dimentions['HEIGHT']
    
    def render(self):
        pygame.draw.rect(
            self.window,
            self.color,
            pygame.Rect(
                self.position,
                (
                    self.width,
                    self.height,
                )
            )
        )


def draw_bricks(window: pygame.Surface) -> None:
    column_count = CONST.BRICKS_COLUMN_COUNT
    start_position = Vector2(
        0,
        0 + (CONST.BRICKS_TOP_MARGIN)
    )
    color_map = {
        0: CONST.RED_COLOR,    1: CONST.RED_COLOR,
        2: CONST.GOLD_COLOR,   3: CONST.GOLD_COLOR,
        4: CONST.GREEN_COLOR,  5: CONST.GREEN_COLOR,
        6: CONST.LIME_COLOR,   7: CONST.LIME_COLOR,
    }

    for i in range(column_count):
        while (start_position.x + CONST.BRICK_DIMENSIONS["WIDTH"]) < CONST.SCREEN_WIDTH:
            brick = Brick(window, color_map[i], start_position, CONST.BRICK_DIMENSIONS)
            brick.render()
            start_position.x += CONST.BRICK_DIMENSIONS["WIDTH"] + CONST.BRICK_COLUMN_MARGIN
    
        start_position.x = 0
        start_position.y += CONST.BRICK_DIMENSIONS["HEIGHT"] + CONST.BRICK_ROW_MARGIN    
