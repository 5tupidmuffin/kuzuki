import math
from random import randrange
import typing as t

import pygame
from pygame.math import Vector2

from .paddle import Paddle
from .. import constants as CONST


sides = ["bottom", "top", "left", "right"]
surface_map = {
    k: v
    for (k, v) in zip(
        sides, [Vector2(0, 1), Vector2(0, 1), Vector2(-1, 0), Vector2(1, 0)]
    )
}


class Ball:
    window: pygame.Surface
    is_sticky: bool
    paddle: Paddle
    collidable_rects: t.List[pygame.Rect]
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
        collidable_rects: t.List[pygame.Rect],
    ):
        self.window = window
        self.is_sticky = True
        self.paddle = paddle
        self.collidable_rects = collidable_rects
        self.color = CONST.BALL_COLOR
        self.radius = CONST.BALL_DIMENSIONS["RADIUS"]
        self.center_position = start_position
        self.acceleration = self.get_first_random_acc()
        self.rect = self.get_rect_from_center_position(self.center_position)

    def get_stick_position(self) -> Vector2:
        return Vector2(
            (self.paddle.position.x + (self.paddle.width // 2)),
            (self.paddle.position.y - (self.radius)),
        )

    def get_rect_from_center_position(self, center: Vector2) -> pygame.Rect:
        return pygame.Rect(
            Vector2(center.x - self.radius, center.y - self.radius),
            (self.radius, self.radius),
        )

    def update_position_on_input(self) -> None:
        if not self.is_sticky:
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_sticky = False

    def get_collided_with(self) -> t.Union[pygame.Rect, None]:
        did_collide_with_paddle = self.rect.colliderect(self.paddle.rect)
        if did_collide_with_paddle:
            return self.paddle.rect
        collided_brick_idx = self.rect.collidelist(self.collidable_rects)
        if collided_brick_idx != -1:
            return self.collidable_rects[collided_brick_idx]
        return None

    def get_first_random_acc(self) -> Vector2:
        up_vec = Vector2(0, -1)
        random_angle_rad = math.radians(randrange(-15, 15))
        random_direction_vec = Vector2()
        random_direction_vec.x = (up_vec.x * math.cos(random_angle_rad)) - (
            up_vec.y * math.sin(random_angle_rad)
        )
        random_direction_vec.y = (up_vec.x * math.sin(random_angle_rad)) + (
            up_vec.y * math.cos(random_angle_rad)
        )
        return random_direction_vec.normalize() * CONST.BALL_SPEED

    def get_reflection_vector(self, entity: pygame.Rect) -> Vector2:
        clip = self.rect.clip(entity)

        hitting_edge = [
            edge for edge in sides if getattr(clip, edge) == getattr(entity, edge)
        ]
        surface_normal = surface_map[hitting_edge[0]]
        reflected = self.acceleration.reflect(surface_normal)
        return reflected

    def change_direction_on_collide(self, entity: pygame.Rect) -> None:
        # https://stackoverflow.com/a/55412058
        # https://matthew-brett.github.io/teaching/rotation_2d.html
        reflection_vector = self.get_reflection_vector(entity).normalize()
        self.acceleration = reflection_vector * CONST.BALL_SPEED

    def render(self) -> None:
        self.update_position_on_input()

        if self.is_sticky:
            self.center_position = self.get_stick_position()
        else:
            self.center_position += self.acceleration

        self.rect = self.get_rect_from_center_position(self.center_position)
        collided_entity = self.get_collided_with()

        if collided_entity:
            self.change_direction_on_collide(collided_entity)

        self.rect = self.get_rect_from_center_position(self.center_position)

        pygame.draw.circle(self.window, self.color, self.center_position, self.radius)
