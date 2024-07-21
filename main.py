import pygame
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Ping Pong Game')

    # Game loop
    game = Game(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game.run()
                elif event.key == pygame.K_e:
                    running = False

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("Welcome to Ping Pong", True, (255, 255, 255))
        screen.blit(text, (150, 200))
        text = font.render("Press 'P' to Play", True, (255, 255, 255))
        screen.blit(text, (200, 300))
        text = font.render("Press 'E' to Exit", True, (255, 255, 255))
        screen.blit(text, (200, 400))
        
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
