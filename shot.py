from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), ((self.position.x), (self.position.y)), self.radius)
    
    def update(self, delta_time):
        self.position += self.velocity * delta_time