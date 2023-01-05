import typing as t

import pygame
from pygame.math import Vector2

from . import constants as CONST
from .entities.paddle import Paddle
from .entities.ball import Ball
from .entities.brick import get_bricks
from .entities.border_rects import BorderRects


def start_game() -> t.NoReturn:
    pygame.init()
    window = pygame.display.set_mode([CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT])
    pygame.display.set_caption(CONST.SCREEN_TITLE)
    clock = pygame.time.Clock()

    is_running = True
    paddle = Paddle(window)
    bricks = get_bricks(window)
    borders = BorderRects(window)
    collidable_rects = [brick.rect for brick in bricks] + [
        rect for rect in borders.rects
    ]
    ball = Ball(
        window,
        Vector2(
            paddle.position.x + (paddle.width // 2),
            paddle.position.y - CONST.BALL_DIMENSIONS["RADIUS"],
        ),
        paddle,
        collidable_rects,
    )

    # event loop
    while is_running:
        window.fill(CONST.BLACK_COLOR)
        paddle.render()
        for brick in bricks:
            brick.render()
        borders.render()
        ball.render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        pygame.display.update()
        clock.tick(60)  # capping the framerate at 60
    exit(0)
