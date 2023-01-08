import typing as t

import pygame
from pygame.math import Vector2

from . import constants as CONST
from .entities.paddle import Paddle
from .entities.ball import Ball
from .entities.brick import BricksContainer
from .entities.border_rects import BorderRects
from .entities.text_display import TextDisplay, GameOverScreen


def check_for_death(ball_rect: pygame.Rect) -> bool:
    return True if ball_rect.bottom > CONST.SCREEN_HEIGHT else False


def reset_ball(ball: Ball) -> None:
    ball.is_sticky = True
    ball.acceleration = ball.get_first_random_acc()


def start_game() -> t.NoReturn:
    pygame.init()
    window = pygame.display.set_mode([CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT])
    pygame.display.set_caption(CONST.SCREEN_TITLE)
    clock = pygame.time.Clock()

    is_running = True

    lives_count = CONST.DEFAULT_LIVES_COUNT
    lives_display = TextDisplay(
        window, Vector2(CONST.BORDER_THICKNESS + 5, CONST.BORDER_THICKNESS + 5)
    )
    game_over_screen = GameOverScreen(window)

    paddle = Paddle(window)

    ball = Ball(
        window,
        Vector2(
            paddle.position.x + (paddle.width // 2),
            paddle.position.y - CONST.BALL_DIMENSIONS["RADIUS"],
        ),
        paddle,
        [],  # will set later
        [],  # will set later
    )

    bricks = BricksContainer(window, ball)

    borders = BorderRects(window)
    borders_rects = [rect for rect in borders.rects]

    collidable_rects = borders_rects

    ball.bricks_rects = bricks.get_bricks_rects()
    ball.collidable_rects = collidable_rects

    # event loop
    while is_running:
        window.fill(CONST.BLACK_COLOR)
        paddle.render()
        bricks.render()
        borders.render()
        ball.render()

        lives_display.render(f"LIVES: {lives_count}")

        if check_for_death(ball.rect):
            lives_count -= 1
            reset_ball(ball)
        if lives_count == 0:
            game_over_screen.render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # reset requested
                lives_count = CONST.DEFAULT_LIVES_COUNT
                paddle.position = CONST.PADDLE_START_POSITION
                bricks.reset_visibility_for_all()
                ball.bricks_rects = bricks.get_bricks_rects()
                ball.is_sticky = True

        pygame.display.update()
        clock.tick(60)  # capping the framerate at 60
    exit(0)
