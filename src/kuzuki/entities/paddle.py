import pygame
from pygame.math import Vector2

from .. import constants as CONST


class Paddle:
    window: pygame.Surface
    color: pygame.Color
    width: int
    height: int
    position: Vector2
    rect: pygame.Rect
    def __init__(
            self,
            window: pygame.Surface,
            start_position: Vector2 = CONST.PADDLE_START_POSITION,
        ):
        self.window = window
        self.color = CONST.BLUE_COLOR
        self.width = CONST.PADDLE_DIMENSIONS["WIDTH"]
        self.height = CONST.PADDLE_DIMENSIONS["HEIGHT"]
        self.position = start_position
        self.rect = self.get_rect_from_position(self.position)
    
    def update_position_on_input(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.position.x != 0:
            self.position.x -= CONST.PADDLE_SPEED
        if keys[pygame.K_RIGHT] and self.position.x + self.width != CONST.SCREEN_WIDTH:
            self.position.x += CONST.PADDLE_SPEED
        

    def get_rect_from_position(self, position: Vector2) -> pygame.Rect:
        return pygame.Rect(
            position,
            (self.width, self.height)
        )

    def render(self) -> None:
        self.update_position_on_input()
        self.rect = self.get_rect_from_position(self.position)
        pygame.draw.rect(
            self.window,
            self.color,
            self.rect
        )
