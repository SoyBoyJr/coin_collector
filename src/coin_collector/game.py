
import pygame
from pygame import Rect
from .config import load_level
from .draw import draw_game


PLAYER_SIZE = 40
PLAYER_SPEED = 5


def run_game(level_path: str, fps: int, debug: bool):
    pygame.init()

    level = load_level(level_path)
    screen = pygame.display.set_mode((level.width, level.height))
    pygame.display.set_caption("Coin Collector")

    clock = pygame.time.Clock()

    player = Rect(
        level.player_start[0],
        level.player_start[1],
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    coins = [
        pygame.Rect(c.x - c.r, c.y - c.r, c.r * 2, c.r * 2)
        for c in level.coins
    ]
    walls = [Rect(w.x, w.y, w.w, w.h) for w in level.walls]

    score = 0
    running = True

    while running:
        dt = clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += PLAYER_SPEED

        # Bewegung + Wandkollision
        player.x += dx
        if any(player.colliderect(w) for w in walls):
            player.x -= dx

        player.y += dy
        if any(player.colliderect(w) for w in walls):
            player.y -= dy

        # Münzen einsammeln
        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                score += 1

        if not coins:
            pygame.display.set_caption("Alle Münzen gesammelt! ESC zum Beenden")

        draw_game(screen, player, coins, walls, score, debug)
        pygame.display.flip()

    pygame.quit()

