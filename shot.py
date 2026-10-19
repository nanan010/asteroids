from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        color = 'white'
        pygame.draw.circle(screen, color, (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

