import pygame
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.paddle1 = Paddle(30, 250, pygame.K_q, pygame.K_w)
        self.paddle2 = Paddle(740, 250, pygame.K_o, pygame.K_p)
        self.ball = Ball()
        self.scoreboard = Scoreboard()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        running = False

            self.screen.fill((0, 0, 0))
            self.paddle1.move()
            self.paddle2.move()
            self.ball.move(self.paddle1, self.paddle2, self.scoreboard)
            self.paddle1.draw(self.screen)
            self.paddle2.draw(self.screen)
            self.ball.draw(self.screen)
            self.scoreboard.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        print(f"Player 1: {self.scoreboard.player1_score} - Player 2: {self.scoreboard.player2_score}")
