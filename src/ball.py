import pygame
import math
import random
from pygame.sprite import Group
from base.entity import Entity


class Ball(Entity):
    def __init__(self, game):
        Entity.__init__(self)
        surface = pygame.Surface(
            (self.settings["ball_size"], self.settings["ball_size"])
        )
        surface.fill(
            (
                self.settings["ball_color_r"],
                self.settings["ball_color_g"],
                self.settings["ball_color_b"],
            )
        )
        self.game = game
        self.paddles = Group(game.player)
        self.bricks = Group(game.bricks)
        self.image = surface
        self.rect = self.image.get_rect()
        self.ball_speed = int(self.settings["ball_speed"])
        self.reset()

    def reset(self):
        self.rect.x = (
            pygame.display.get_surface().get_width() / 2 - self.image.get_width() / 2
        )
        self.rect.y = (
            pygame.display.get_surface().get_height() / 2 - self.image.get_height() / 2
        )
        self.vx = (1 if random.random() >= 0.5 else -1) * self.ball_speed
        self.vy = (1 if random.random() >= 0.5 else -1) * self.ball_speed

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.check_collision()

    def check_collision(self):
        paddle = pygame.sprite.spritecollide(self, self.paddles, False)
        brick = pygame.sprite.spritecollide(self, self.bricks, True)
        if paddle:
            self.change_direction(paddle[0])
            return
        elif brick:
            self.change_direction(brick[0])
            return            

        if (
            self.rect.y <= 0
            or self.rect.y + self.rect.h > pygame.display.get_surface().get_height()
        ):
            self.vy *= -1
        elif (
            self.rect.x <= 0
            or self.rect.x + self.rect.w > pygame.display.get_surface().get_width()
        ):
            self.vx *= -1

    def change_direction(self, paddle):
        paddle_hit_x = paddle.rect.x
        ball_hit_x = self.rect.x
        percentage = (ball_hit_x - paddle_hit_x) / paddle.rect.w
        if percentage <= 0.5:
            self.vx = -1 * self.ball_speed * math.cos(percentage)
        else:
            self.vx = self.ball_speed * math.cos(percentage)
        self.vy = -1 * self.ball_speed * math.sin(percentage)
