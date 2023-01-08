import typing as t

import pygame
from pygame.math import Vector2

from .. import constants as CONST
from .ball import Ball
from ..typing import Dimension


class Brick:
    window: pygame.Surface
    color: pygame.Color
    position: Vector2
    width: int
    height: int
    rect: pygame.Rect
    ball: Ball

    def __init__(
        self,
        window: pygame.Surface,
        color: pygame.Color,
        position: Vector2,
        dimentions: Dimension,
        ball: Ball,
    ):
        self.window = window
        self.color = color
        self.position = position
        self.width = dimentions["WIDTH"]
        self.height = dimentions["HEIGHT"]
        self.rect = pygame.Rect(self.position, (self.width, self.height))
        self.ball = ball
        self.is_visible = True

    def update_visibility_on_collide(self) -> None:
        if not self.is_visible:
            return
        did_collide_with_ball = self.rect.colliderect(self.ball.rect)
        if did_collide_with_ball:
            self.is_visible = False

    def render(self) -> None:
        self.update_visibility_on_collide()
        if self.is_visible:
            pygame.draw.rect(self.window, self.color, self.rect)


class BricksContainer:
    window: pygame.Surface
    ball: Ball
    bricks: t.List[Brick]

    def __init__(self, window: pygame.Surface, ball: Ball):
        self.window = window
        self.ball = ball
        self.bricks = self.get_bricks()

    def get_bricks(self) -> t.List[Brick]:
        space_without_borders = CONST.SCREEN_WIDTH - (2 * CONST.BORDER_THICKNESS)
        left_over_space_after_bricks = space_without_borders % (
            CONST.BRICK_DIMENSIONS["WIDTH"] + CONST.BRICK_ROW_MARGIN
        )
        margin = left_over_space_after_bricks / 2
        offset = CONST.BORDER_THICKNESS + margin
        column_count = CONST.BRICKS_COLUMN_COUNT
        start_position = Vector2(offset, CONST.BRICKS_TOP_MARGIN)
        bricks = []

        for i in range(column_count):
            while (
                start_position.x + CONST.BRICK_DIMENSIONS["WIDTH"]
            ) < CONST.SCREEN_WIDTH - offset:
                brick = Brick(
                    self.window,
                    CONST.COLOR_MAP[i],
                    start_position,
                    CONST.BRICK_DIMENSIONS,
                    self.ball,
                )
                bricks.append(brick)
                start_position.x += (
                    CONST.BRICK_DIMENSIONS["WIDTH"] + CONST.BRICK_COLUMN_MARGIN
                )

            start_position.x = offset
            start_position.y += (
                CONST.BRICK_DIMENSIONS["HEIGHT"] + CONST.BRICK_ROW_MARGIN
            )
        return bricks

    def reset_visibility_for_all(self) -> None:
        for brick in self.bricks:
            brick.is_visible = True

    def get_bricks_rects(self) -> t.List[pygame.Rect]:
        return [brick.rect for brick in self.bricks]

    def render(self) -> None:
        for brick in self.bricks:
            brick.render()
