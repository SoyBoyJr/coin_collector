
import pygame


WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
GOLD = (255, 215, 0)
GRAY = (120, 120, 120)
RED = (255, 0, 0)


def draw_game(screen, player, coins, walls, score, debug):
    screen.fill(WHITE)

    for wall in walls:
        pygame.draw.rect(screen, GRAY, wall)
        if debug:
            pygame.draw.rect(screen, RED, wall, 2)

    for coin in coins:
        pygame.draw.ellipse(screen, GOLD, coin)
        if debug:
            pygame.draw.rect(screen, RED, coin, 1)

    pygame.draw.rect(screen, BLUE, player)
    if debug:
        pygame.draw.rect(screen, RED, player, 2)

    font = pygame.font.SysFont(None, 24)
    hud = font.render(f"Punkte: {score} | Münzen übrig: {len(coins)}", True, (0, 0, 0))
    screen.blit(hud, (10, 10))

