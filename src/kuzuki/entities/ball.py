import typing as t

import pygame
from pygame.math import Vector2

from .paddle import Paddle
from .. import constants as CONST


class Ball:
    window: pygame.Surface
    is_sticky: bool
    paddle: Paddle
    bricks: t.List[pygame.Rect]
    color: pygame.Color
    radius: int
    center_position: Vector2
    acceleration: Vector2
    rect: pygame.Rect
    def __init__(
            self,
            window: pygame.Surface,
            start_position: Vector2,
            paddle: Paddle,
            bricks: t.List[pygame.Rect],
        ):
        self.window = window
        self.is_sticky = True
        self.paddle = paddle
        self.bricks = bricks
        self.color = CONST.BLUE_COLOR
        self.radius = CONST.BALL_DIMENSIONS["RADIUS"]
        self.center_position = start_position
        self.acceleration = Vector2(0, -1) * CONST.BALL_SPEED # upward
        self.rect = self.get_rect_from_center_position(self.center_position)
    
    def get_stick_position(self) -> Vector2:
        return Vector2(
            (self.paddle.position.x + (self.paddle.width // 2)),
            (self.paddle.position.y - (self.radius)) 
        )
    
    def get_rect_from_center_position(self, center: Vector2) -> pygame.Rect:
        return pygame.Rect(
            Vector2(center.x - self.radius, center.y - self.radius),
            (self.radius, self.radius)
        )
    
    def update_position_on_input(self) -> None:
        if (not self.is_sticky): return
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE]): 
            self.is_sticky = False

    def get_collided_with(self) -> t.Union[pygame.Rect, None]:
        did_collide_with_paddle = self.rect.colliderect(self.paddle.rect)
        if did_collide_with_paddle: return self.paddle.rect
        collided_brick_idx = self.rect.collidelist(self.bricks)
        if collided_brick_idx != -1: return self.bricks[collided_brick_idx]
        return None
    
    def get_collision_normal(self, entity: pygame.Rect) -> Vector2:
        # https://math.stackexchange.com/questions/13261/how-to-get-a-reflection-vector
        # https://gamedev.stackexchange.com/questions/136073/how-does-one-calculate-the-surface-normal-in-2d-collisions
        # https://stackoverflow.com/questions/60213103/use-vector2-in-pygame-collide-with-the-window-frame-and-restrict-the-ball-to-th
        # https://www.varsitytutors.com/precalculus-help/find-a-direction-vector-when-given-two-points
        collision_point = Vector2(self.rect.clip(entity).center)
        collision_normal = (self.center_position - collision_point)
        return collision_normal
        ...

    
    def change_direction_on_collide(self, entity: pygame.Rect) -> None:
        # https://www.gamedev.net/blogs/entry/2269564-arkanoid-and-pygame-collision-detection/
        # https://math.stackexchange.com/questions/13261/how-to-get-a-reflection-vector
        # https://stackoverflow.com/a/59658289
        collision_normal = self.get_collision_normal(entity)
        reflection_vector = self.acceleration.reflect(collision_normal).normalize()
        self.acceleration = reflection_vector * CONST.BALL_SPEED
    
    def render(self) -> None:
        self.update_position_on_input()

        self.rect = self.get_rect_from_center_position(self.center_position)
        collided_entity = self.get_collided_with()

        if collided_entity:
            self.change_direction_on_collide(collided_entity)
        
        if self.is_sticky:
            self.center_position = self.get_stick_position()
        else:
            self.center_position += self.acceleration

        pygame.draw.circle(
            self.window, self.color, self.center_position, self.radius
        )
