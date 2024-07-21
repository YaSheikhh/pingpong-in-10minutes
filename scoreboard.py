import pygame

class Scoreboard:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)
        self.player1_score = 0
        self.player2_score = 0

    def draw(self, screen):
        score_text = self.font.render(f"{self.player1_score} - {self.player2_score}", True, (255, 255, 255))
        screen.blit(score_text, (350, 10))
