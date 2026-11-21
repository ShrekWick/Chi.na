import pygame

pygame.init()

WIDTH = 1920
HEIGHT = 1080
FPS = 60
BG_COLOR = (69, 69, 69)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Glory to Atrana")
clock = pygame.time.Clock()
is_running = True
is_fullscreen = True
dt = 0



while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode(
                        (WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED
                    )
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)

    screen.fill(BG_COLOR)
    pygame.draw.line(screen,"red",(0,350),(1000,920),5)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

    

pygame.quit()
