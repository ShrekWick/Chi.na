# region extensions

import os
import math
import pygame
from pygame.typing import SequenceLike

# endregion extensions

# region grundlagen

#! Author = "Emil Maharramov"

pygame.init()

resolution_x = 1280
resolution_y = 720
screen = pygame.display.set_mode((resolution_x, resolution_y))
clock = pygame.time.Clock()
running = True

dt = 0
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

konami = 0
other_konami = 0
block_konami = False
cheat_konami = False

returnal = 0
other_returnal = 0
block_returnal = False
cheat_returnal = False

# endregion grundlagen

# region functions

#? uncomment 4 below

func_x_max = 40
func_y_max = 35
ratio_x = screen.width/func_x_max
ratio_y = screen.height/func_y_max

def pathmaker(x1,y1,x2,y2):
    return pygame.draw.line(screen,"brown",(x1,y1),(x2,y2),50)

def path_f1(x):
    return math.floor((0.1196*x**3)-(1.2048*x**2)+(2.7896*x)+1.9058)

def path_f2(x):
    return math.floor((-0.0729*x**3)+(1.1875*x**2)-(6.8333*x)+25)

def path_f3(x):
    return math.floor((0.0002*x**4)-(0.0083*x**3)+(0.1030*x**2)-(0.4324*x)+18.5110)

def path_f4(x):
    return math.floor((-0.00004*x**5)+(0.0031*x**4)-(0.0983*x**3)+(1.2259*x**2)-(4.9379*x)+28.17)

# endregion functions

# region do not remove

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == next_key:
            block_konami = False
        if event.type == pygame.KEYDOWN and event.key != next_key and event.key == pygame.K_UP and konami == other_konami:
            konami = other_konami
        elif event.type == pygame.KEYDOWN and event.key != next_key:
                    konami = 0
        elif not block_konami and event.type == pygame.KEYDOWN and event.key != next_key:
            konami = 0

        if event.type == pygame.KEYDOWN and event.key == next_key:
            block_returnal = False
        if event.type == pygame.KEYDOWN and event.key != next_key and event.key == pygame.K_UP and returnal == other_returnal:
            konami = other_konami
        elif event.type == pygame.KEYDOWN and event.key != next_key:
            konami = 0
        elif not block_konami and event.type == pygame.KEYDOWN and event.key != next_key:
            konami = 0

    # endregion do not remove

    # region sharvnutrikotorogobilkvadratskajdoystoronikotorogolejalkonus

    screen.fill((69, 69, 69))

    mann_secret = pygame.image.load(os.path.join("media","mann.png"))

    mann_orig = pygame.image.load(os.path.join("media","mann-orig.png"))

    if cheat_konami:
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

    for x in range (0,8):
        pathmaker(x*ratio_x,path_f1(x)*ratio_y,(x+1)*ratio_x,(path_f1(x+1)*ratio_y))

    for x in range (0,8):
       pathmaker(x*ratio_x,path_f2(x)*ratio_y,(x+1)*ratio_x,(path_f2(x+1)*ratio_y))

    for x in range (0,35):
        pathmaker(x*ratio_x,path_f3(x)*ratio_y,(x+1)*ratio_x,(path_f3(x+1)*ratio_y))
    
    for x in range (0,35):
        pathmaker(x*ratio_x,path_f4(x)*ratio_y,(x+1)*ratio_x,(path_f4(x+1)*ratio_y))
    



    # for x in range (0,math.floor(8*ratio_x)):
    #     pathmaker(x,(path_f1(x)/ratio_x)*ratio_y,(x+1),(path_f1(x+1)/ratio_x)*ratio_y)

    # for x in range (0,math.floor(8*ratio_x)):
    #    pathmaker(x,(path_f2(x)/ratio_x)*ratio_y,(x+1),(path_f2(x+1)/ratio_x)*ratio_y)

    # for x in range (0,math.floor(35*ratio_x)):
    #     pathmaker(x,(path_f3(x)/ratio_x)*ratio_y,(x+1),(path_f3(x+1)/ratio_x)*ratio_y)
    
    # for x in range (0,math.floor(35*ratio_x)):
    #     pathmaker(x,(path_f4(x)/ratio_x)*ratio_y,(x+1),(path_f4(x+1)/ratio_x)*ratio_y)

    # endregion 10pixellongroad

#! DRAWINGS BEFORE THIS

    # region spoontamer

    pygame.display.flip()

    dt = clock.tick(60) /  1000

    # endregion spoontamer

#! MOVEMENT AFTER THIS

    # region iliketomoveitmoveit

    keys = pygame.key.get_pressed()

    if cheat_konami:
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
        cheat_konami = False
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

    if konami_keys[next_key] and not block_konami:
        block_konami = True
        konami += 1

    if konami == len(konami_sequence):
                cheat_konami = True


    # if konami == 0:
    #     next_key = pygame.K_UP

    # if konami_keys[pygame.K_UP] and konami == 0 and not block_konami:
    #     block_konami = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_UP

    # if konami_keys[pygame.K_UP] and konami == 1 and not block_konami:
    #     block_konami = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_DOWN

    # if konami_keys[pygame.K_DOWN] and konami == 2 and not block_konami:
    #     block_konami = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_DOWN

    # if konami_keys[pygame.K_DOWN] and konami == 3 and not block_konami:
    #     block_konami = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_LEFT

    # if konami_keys[pygame.K_LEFT] and konami == 4 and not block_konami:
    #     block_konami = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_RIGHT

    # if konami_keys[pygame.K_RIGHT] and konami == 5 and not block_konami:
    #     block_konami = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_LEFT

    # if konami_keys[pygame.K_LEFT] and konami == 6 and not block_konami:
    #     block_konami = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_RIGHT

    # if konami_keys[pygame.K_RIGHT] and konami == 7 and not block_konami:
    #     block_konami = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_b

    # if konami_keys[pygame.K_b] and konami == 8 and not block_konami:
    #     block_konami = True
    #     konami += 1
    #     current_key = next_key
    #     next_key = pygame.K_a

    # if konami_keys[pygame.K_a] and konami == 9 and not block_konami:
    #     block_konami = True
    #     konami += 1

    # if konami == 10:
    #     cheat_konami = True


# endregion pussycat

    # region retrieve

    konami_keys = pygame.key.get_pressed()
    konami_sequence = [pygame.K_r,pygame.K_e,pygame.K_t,pygame.K_u,pygame.K_r,pygame.K_n]
    
    first_konami = konami_sequence[0]
    for x in konami_sequence:
        if x != first_konami:
            other_konami = konami_sequence.index(x)
            break
             
        
    
    if konami >= len(konami_sequence):
        continue
    else:
        next_key = konami_sequence[konami]
    
    if konami_keys[next_key] and not block_konami:
        block_konami = True
        konami += 1
    
    if konami == len(konami_sequence):
        cheat_returnal = True

    # endregion retrieve

# region end

pygame.quit()

# endregion end
