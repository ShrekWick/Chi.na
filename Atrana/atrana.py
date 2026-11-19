import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

BIG_SPEED = 3000
DEF_SPEED = 300
konami = [
    pygame.K_UP,
    pygame.K_UP,
    pygame.K_DOWN,
    pygame.K_DOWN,
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_b,
    pygame.K_a,
]
speed = DEF_SPEED
cur_konami = []
block = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if len(cur_konami) < len(konami) and event.key == konami[len(cur_konami)]:
                block = False
            if len(cur_konami) < len(konami) and event.key != konami[len(cur_konami)]:
                cur_konami = []

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

    if cur_konami == konami:
        speed = BIG_SPEED
    else:
        speed = DEF_SPEED

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pos.y -= speed * dt
    if keys[pygame.K_DOWN]:
        pos.y += speed * dt
    if keys[pygame.K_LEFT]:
        pos.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        pos.x += speed * dt

    for key in list(set(konami)):
        if not block and (
            cur_konami == konami[: len(cur_konami)] and konami[len(cur_konami)] == key
        ):
            cur_konami.append(key)
        block = True
    if keys[pygame.K_x]:
        cur_konami = []

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
