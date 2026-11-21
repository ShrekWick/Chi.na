# region extensions

import os
import math
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
other_konami = 0
cheat = False
block = False

# endregion grundlagen

# region functions

#? uncomment 4 below

def pathmaker(x1,y1,x2,y2):
    return pygame.draw.line(screen,"green",(x1,y1),(x2,y2),1)

# def path_f1(x):
#     return math.floor((0.1196*x**3)-(1.2048*x**2)+(2.7896*x)+1.9058)

# endregion functions

# region do not remove

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == next_key:
            if block:
                print("blocked")
            elif not block:
                print("unblocked")
            print(konami)
            print(pygame.key.name(next_key))
            block = False
        if event.type == pygame.KEYDOWN and event.key != next_key and event.key == pygame.K_UP and konami == other_konami:
            konami = other_konami
        elif event.type == pygame.KEYDOWN and event.key != next_key:
                    konami = 0
        elif not block and event.type == pygame.KEYDOWN and event.key != next_key:
            konami = 0

    # endregion do not remove

    # region sharvnutrikotorogobilkvadratskajdoystoronikotorogolejalkonus

    screen.fill("light blue")

    mann_secret = pygame.image.load(os.path.join("media","mann.png"))

    mann_orig = pygame.image.load(os.path.join("media","mann-orig.png"))

    if cheat:
        skin = mann_secret
    else:
        skin = mann_orig

    skin = pygame.transform.scale(skin,(160,160))

    player = skin.get_rect()
    player.x = pos.x
    player.y = pos.y

    # screen.blit(skin,(0,0))

    screen.blit(skin,player)
    
    # pygame.draw.circle(screen, "gold", pos, 40)
    # pygame.draw.polygon(
    #     screen,
    #     "navy blue",
    #     [(pos.x - 40, pos.y - 40), (pos.x, pos.y - 80), (pos.x + 40, pos.y - 40)],
    # )
    # pygame.draw.polygon(
    #     screen,
    #     "salmon",
    #     [(pos.x - 40, pos.y - 40), (pos.x - 80, pos.y), (pos.x - 40, pos.y + 40)],
    # )
    # pygame.draw.polygon(
    #     screen,
    #     "light green",
    #     [(pos.x + 40, pos.y + 40), (pos.x + 80, pos.y), (pos.x + 40, pos.y - 40)],
    # )
    # pygame.draw.polygon(
    #     screen,
    #     "light blue",
    #     [(pos.x - 40, pos.y + 40), (pos.x, pos.y + 80), (pos.x + 40, pos.y + 40)],
    # )

    # endregion sharvnutrikotorogobilkvadratskajdoystoronikotorogolejalkonus

    # region 10pixellongroad

    #? uncomment 2 below

    # for x in range (0,800):
    #     pathmaker(x,path_f1(x),x+1,path_f1(x+1))

    #* delete lower when done pleasing junaycoolboy

    for x in range (0,1280):
        pathmaker(x,720-math.sin(x)*40,x+1,720-math.sin(x+1)*40)

    # endregion 10pixellongroad

#! DRAWINGS BEFORE THIS

    # region spoontamer

    pygame.display.flip()

    dt = clock.tick(60) /  1000

    # endregion spoontamer

#! MOVEMENT AFTER THIS

    # region iliketomoveitmoveit

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


    # endregion iliketomoveitmoveit

    # region pussycat

    konami_keys = pygame.key.get_pressed()
    konami_sequence = [pygame.K_UP,pygame.K_UP,pygame.K_DOWN,pygame.K_DOWN,pygame.K_LEFT,
                       pygame.K_RIGHT,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_b,pygame.K_a]

    first_konami = konami_sequence[0]
    for x in konami_sequence:
         if x != first_konami:
              other_konami = konami_sequence.index(x)
              break
         
    

    if konami >= len(konami_sequence):
        continue
    else:
        next_key = konami_sequence[konami]

    if konami_keys[next_key] and not block:
        block = True
        konami += 1

    if konami == len(konami_sequence):
                cheat = True


    # if konami == 0:
    #     next_key = pygame.K_UP

    # if konami_keys[pygame.K_UP] and konami == 0 and not block:
    #     block = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_UP

    # if konami_keys[pygame.K_UP] and konami == 1 and not block:
    #     block = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_DOWN

    # if konami_keys[pygame.K_DOWN] and konami == 2 and not block:
    #     block = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_DOWN

    # if konami_keys[pygame.K_DOWN] and konami == 3 and not block:
    #     block = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_LEFT

    # if konami_keys[pygame.K_LEFT] and konami == 4 and not block:
    #     block = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_RIGHT

    # if konami_keys[pygame.K_RIGHT] and konami == 5 and not block:
    #     block = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_LEFT

    # if konami_keys[pygame.K_LEFT] and konami == 6 and not block:
    #     block = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_RIGHT

    # if konami_keys[pygame.K_RIGHT] and konami == 7 and not block:
    #     block = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_b

    # if konami_keys[pygame.K_b] and konami == 8 and not block:
    #     block = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_a

    # if konami_keys[pygame.K_a] and konami == 9 and not block:
    #     block = True
    #     konami += 1

    # if konami == 10:
    #     cheat = True


# endregion pussycat

# region end

pygame.quit()

# endregion end
