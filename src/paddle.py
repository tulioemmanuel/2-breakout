import pygame
from base.entity import Entity


class Paddle(Entity):
    def __init__(self, name="paddle", x=0, y=0):
        Entity.__init__(self)
        self.name = name
        surface = pygame.Surface(
            (self.settings["paddle_width"], self.settings["paddle_height"])
        )
        surface.fill(
            (
                self.settings["paddle_color_r"],
                self.settings["paddle_color_g"],
                self.settings["paddle_color_b"],
            )
        )
        self.image = surface
        self.rect = self.image.get_rect()
        self.init_x = x
        self.init_y = y
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.screen = pygame.display.get_surface()

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        self.rect.x += self.vx

    def move_left(self):
        if self.rect.x + self.vx >= 0:
            self.vx -= self.settings["paddle_vx"]

    def move_right(self):
        if self.rect.x + self.rect.w + self.vx >= self.screen.get_width():
            self.vx += self.settings["paddle_vx"]

    def move_touch(self, pos):
        if pos[0] >= self.screen.get_width()/2:
            self.move_right()            
        else:
            self.move_left()

    def stop(self):
        self.vx = 0

    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y
