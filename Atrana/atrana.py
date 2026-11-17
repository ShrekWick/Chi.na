import pygame
from pygame.typing import SequenceLike

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("grey")

    pygame.draw.circle(screen, "purple", pos, 40)
    pygame.draw.polygon(
        screen,
        "purple",
        [(pos.x - 40, pos.y - 40), (pos.x, pos.y - 80), (pos.x + 40, pos.y - 40)],
    )
    pygame.draw.polygon(
        screen,
        "purple",
        [(pos.x - 40, pos.y - 40), (pos.x - 80, pos.y), (pos.x - 40, pos.y + 40)],
    )
    pygame.draw.polygon(
        screen,
        "purple",
        [(pos.x + 40, pos.y + 40), (pos.x + 80, pos.y), (pos.x + 40, pos.y - 40)],
    )
    pygame.draw.polygon(
        screen,
        "purple",
        [(pos.x - 40, pos.y + 40), (pos.x, pos.y + 80), (pos.x + 40, pos.y + 40)],
    )

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
