import pygame
import random

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(400, 300, 15, 15)
        self.speed_x = random.choice((5, -5))
        self.speed_y = random.choice((5, -5))

    def move(self, paddle1, paddle2, scoreboard):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1
        
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.speed_x *= -1

        if self.rect.left <= 0:
            scoreboard.player2_score += 1
            self.reset()
        elif self.rect.right >= 800:
            scoreboard.player1_score += 1
            self.reset()

    def reset(self):
        self.rect.center = (400, 300)
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
