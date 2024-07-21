import pygame

class Paddle:
    def __init__(self, x, y, up_key, down_key):
        self.rect = pygame.Rect(x, y, 10, 100)
        self.speed = 5
        self.up_key = up_key
        self.down_key = down_key

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
            self.rect.y -= self.speed
        if keys[self.down_key]:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
