import pygame
from base.game import Game
from base.configuration import Configuration
from paddle import Paddle
from ball import Ball
from brick import Brick


class Breakout(Game):
    def __init__(self):
        super().__init__()
        self.setup()
        self.mainloop()

    def setup(self):
        super().setup()
        self.settings = Configuration().settings
        self.player = Paddle(
            x=self.renderer.screen.get_width() / 2 - self.settings["paddle_width"] / 2,
            y=self.renderer.screen.get_height()
            - self.settings["paddle_vertical_offset"],
        )
        self.bricks = [
            Brick(x=i % self.renderer.screen.get_width(), y=(i//100) * 3)
            for i in range(
                0, self.renderer.screen.get_width() * 10, self.settings["brick_width"] + 10
            )
        ]
        self.ball = Ball(self)

        self.renderer.set_drawables([self.player, self.ball, self.bricks])

    def update(self):
        self.player.update()
        self.ball.update()

    def render(self):
        self.renderer.draw()

    def mainloop(self):
        self.input.get_input()
        self.update()
        self.render()
        self.frame_delta = self.clock.tick(self.settings["FPS"])

    def cleanup(self):
        pygame.font.init()
        pygame.quit()
