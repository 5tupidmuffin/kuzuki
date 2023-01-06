# flake8: noqa
from pygame import Color
from pygame.math import Vector2

from . import __version__
from . import typing as kuzuki_types

# fmt: off
NAME                     = "KUZUKI"
VERSION                  = __version__
SCREEN_SIZE              = 200
SCREEN_WIDTH_ASPECT      = 4
SCREEN_HEIGHT_ASPECT     = 3
SCREEN_WIDTH             = SCREEN_SIZE * SCREEN_WIDTH_ASPECT
SCREEN_HEIGHT            = SCREEN_SIZE * SCREEN_HEIGHT_ASPECT
SCREEN_TITLE             = f"{NAME} {VERSION}"

# colors taken from original breakout: https://upload.wikimedia.org/wikipedia/en/c/cd/Breakout_game_screenshot.png
BLACK_COLOR              = Color(0, 0, 0)
WHITE_COLOR              = Color(204, 204, 204)
RED_COLOR                = Color(163, 30, 10)
GOLD_COLOR               = Color(194, 133, 10)
GREEN_COLOR              = Color(10, 133, 51)
LIME_COLOR               = Color(194, 194, 41)
BLUE_COLOR               = Color(10, 133, 194)
# fmt: on

BRICK_DIMENSIONS: kuzuki_types.Dimension = {
    "WIDTH": 50,
    "HEIGHT": 20,
}
BRICKS_TOP_MARGIN = SCREEN_HEIGHT // 8
BRICKS_COLUMN_COUNT = 8
BRICK_ROW_MARGIN = 5
BRICK_COLUMN_MARGIN = 5
# fmt: off
COLOR_MAP = {
    0: RED_COLOR,    1: RED_COLOR,
    2: GOLD_COLOR,   3: GOLD_COLOR,
    4: GREEN_COLOR,  5: GREEN_COLOR,
    6: LIME_COLOR,   7: LIME_COLOR,
}
# fmt: on

PADDLE_DIMENSIONS = BRICK_DIMENSIONS
PADDLE_COLOR = BLUE_COLOR
PADDLE_START_POSITION = Vector2(
    (SCREEN_WIDTH // 2) - PADDLE_DIMENSIONS["WIDTH"],
    SCREEN_HEIGHT - (SCREEN_HEIGHT // 5),
)
PADDLE_SPEED = 10

BALL_DIMENSIONS = {"RADIUS": 7}
BALL_COLOR = WHITE_COLOR
BALL_SPEED = 4

BORDER_THICKNESS = 10
BORDER_COLOR = WHITE_COLOR

DEFAULT_LIVES_COUNT = 3

FONT_SIZE = 30
FONT_COLOR = WHITE_COLOR
