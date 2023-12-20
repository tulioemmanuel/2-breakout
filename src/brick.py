import pygame
from base.entity import Entity


class Brick(Entity):
    def __init__(self, name="brick", x=0, y=0):
        Entity.__init__(self)
        self.name = name
        surface = pygame.Surface(
            (self.settings["brick_width"], self.settings["brick_height"])
        )
        surface.fill(
            (
                self.settings["brick_color_r"],
                self.settings["brick_color_g"],
                self.settings["brick_color_b"],
            )
        )
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
