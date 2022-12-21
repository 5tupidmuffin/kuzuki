import pygame
from pygame.math import Vector2

from .paddle import Paddle
from .. import constants as CONST


class Ball:
    window = pygame.Surface
    is_sticky = bool
    paddle = Paddle
    color = pygame.Color
    radius = int
    center_position = Vector2
    def __init__(
            self,
            window: pygame.Surface,
            start_position: Vector2,
            paddle: Paddle,
            is_sticky = True,
        ):
        self.window = window
        self.is_sticky = is_sticky
        self.paddle = paddle
        self.color = CONST.BLUE_COLOR
        self.radius = CONST.BALL_DIMENSIONS["RADIUS"]
        self.center_position = start_position
        self.acceleration = Vector2(0, -2) # upward
    
    def get_stick_position(self) -> Vector2:
        return Vector2(
            (self.paddle.position.x + (self.paddle.width // 2)),
            (self.paddle.position.y - (self.radius)) 
        )
    
    def update_position_on_input(self) -> None:
        if (not self.is_sticky): return
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE]): 
            self.is_sticky = False
    
    def render(self) -> None:
        self.update_position_on_input()
        if self.is_sticky:
            self.center_position = self.get_stick_position()
        else:
            self.center_position += self.acceleration

        pygame.draw.circle(
            self.window, self.color, self.center_position, self.radius
        )
