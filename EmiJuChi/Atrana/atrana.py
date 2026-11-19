# region extensions

import pygame
from pygame.typing import SequenceLike

# endregion extensions

# region grundlagen

#! Author = "Emil Maharramov"

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

konami = 0
cheat = False
block = False

# endregion grundlagen

# region do not remove

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            block = False
        if not block and event.type == pygame.KEYDOWN and event.key != next_key :
            konami = 0

# endregion do not remove

# region sharvnutrikotorogobilkvadratskajdoystoronikotorogolejalkonus

    screen.fill((69,69,69))

    pygame.draw.circle(screen, "gold", pos, 40)
    pygame.draw.polygon(
        screen,
        "navy blue",
        [(pos.x - 40, pos.y - 40), (pos.x, pos.y - 80), (pos.x + 40, pos.y - 40)],
    )
    pygame.draw.polygon(
        screen,
        "salmon",
        [(pos.x - 40, pos.y - 40), (pos.x - 80, pos.y), (pos.x - 40, pos.y + 40)],
    )
    pygame.draw.polygon(
        screen,
        "light green",
        [(pos.x + 40, pos.y + 40), (pos.x + 80, pos.y), (pos.x + 40, pos.y - 40)],
    )
    pygame.draw.polygon(
        screen,
        "light blue",
        [(pos.x - 40, pos.y + 40), (pos.x, pos.y + 80), (pos.x + 40, pos.y + 40)],
    )

# endregion sharvnutrikotorogobilkvadratskajdoystoronikotorogolejalkonus

#region iliketomoveitmoveit

    keys = pygame.key.get_pressed()

    if cheat:
         speed = 2000
    else:
         speed = 300



    if keys[pygame.K_UP]:
        pos.y -= speed * dt
    if keys[pygame.K_DOWN]:
        pos.y += speed * dt
    if keys[pygame.K_LEFT]:
        pos.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        pos.x += speed * dt


    if keys[pygame.K_x]:
            cheat = False
            konami = 0
    pygame.display.flip()

    dt = clock.tick(60) / 1000

#endregion iliketomoveitmoveit

# region pussycat

    konami_keys = pygame.key.get_pressed()

    if konami == 0:
         next_key = pygame.K_UP

    if konami_keys[pygame.K_UP] and konami == 0 and not block :
        block = True
        konami += 1
        next_key = pygame.K_UP


    if konami_keys[pygame.K_UP] and konami == 1 and not block :
        block = True
        konami += 1
        next_key = pygame.K_DOWN

    if konami_keys[pygame.K_DOWN] and konami == 2 and not block :
        block = True
        konami += 1
        next_key = pygame.K_DOWN

    if konami_keys[pygame.K_DOWN] and konami == 3 and not block :
            block = True
            konami += 1
            next_key = pygame.K_LEFT

    if konami_keys[pygame.K_LEFT] and konami == 4 and not block :
            block = True
            konami += 1
            next_key = pygame.K_RIGHT

    if konami_keys[pygame.K_RIGHT] and konami == 5 and not block :
            block = True
            konami += 1
            next_key = pygame.K_LEFT

    if konami_keys[pygame.K_LEFT] and konami == 6 and not block :
            block = True
            konami += 1
            next_key = pygame.K_RIGHT

    if konami_keys[pygame.K_RIGHT] and konami == 7 and not block :
            block = True
            konami += 1
            next_key = pygame.K_b

    if konami_keys[pygame.K_b] and konami == 8 and not block :
            block = True
            konami += 1
            next_key = pygame.K_a

    if konami_keys[pygame.K_a] and konami == 9 and not block :
            block = True
            konami += 1

    if konami == 10:
        cheat = True

# endregion pussycat

# region end

pygame.quit()

# endregion end