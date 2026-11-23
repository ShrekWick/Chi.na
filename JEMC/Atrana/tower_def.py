import math

import pygame

pygame.init()

WIDTH = 1920
HEIGHT = 1080
FPS = 60
BG_COLOR = (69, 69, 69)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("Glory to Atrana")
clock = pygame.time.Clock()
is_running = True
is_fullscreen = True
dt = 0

font = pygame.font.Font(None, 36)
currency = 0
currency_display = font.render(f"You have {currency} AZN", True, "white")
currency_display_rect = currency_display.get_rect()
currency_display_rect.center = (screen.width / 2, screen.height / 2)
POLUCHKA = pygame.event.custom_type()
POLUCHKA_INTERVAL = 500
pygame.time.set_timer(POLUCHKA, POLUCHKA_INTERVAL)
sentries = []
shoot = False
bullets = []


class Sentry:
    def __init__(self, pos):
        self.pos = pos


class Bullet:
    def __init__(self, pos, target):
        self.pos = pos
        self.target = target


def put_a_sentry_here(pos):
    sentry = Sentry(pos)
    sentries.append(sentry)


MANN_COMING = pygame.event.custom_type()
MANN_COMING_INTERVAL = 2000
pygame.time.set_timer(MANN_COMING, MANN_COMING_INTERVAL)
manns = []


class Mann:
    def __init__(self, pos, speed, health):
        self.pos = pos
        self.speed = speed
        self.health = health


while is_running:
    screen.fill(BG_COLOR)
    pygame.draw.line(
        screen, "bisque4", (0, screen.height / 2), (screen.width, screen.height / 2), 50
    )

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
        if event.type == POLUCHKA:
            currency += 1
            currency_display = font.render(f"You have {currency} AZN", True, "white")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if currency > 5:
                put_a_sentry_here(pos=event.pos)
                currency -= 5
        if event.type == MANN_COMING:
            mann = Mann((-50, screen.height / 2), 150, 10)
            manns.append(mann)

    for s in sentries:
        pygame.draw.circle(screen, "chartreuse4", s.pos, 50)
        target = None
        for m in manns:
            if math.sqrt((s.pos[0] - m.pos[0]) ** 2 + (s.pos[1] - m.pos[1]) ** 2) < 500:
                shoot = True
                target = m
                break
        if shoot and target:
            bullets.append(Bullet(s.pos, target))
            shoot = False
    for m in manns:
        pygame.draw.circle(screen, "brown4", m.pos, 15)
        m.pos = (m.pos[0] + m.speed * dt, m.pos[1])
        if m.pos[0] > screen.width + 50:
            manns.remove(m)
    for b in bullets:
        pygame.draw.circle(screen, "chartreuse4", b.pos, 5)
        cos = (b.target.pos[0] ** 2 - b.pos[0]) ** 2 / (
            b.target.pos[1] ** 2 - b.pos[1]
        ) ** 2

        b.pos = (
            b.pos[0] + dt * 30 * cos,
            b.pos[1] + dt * 30 * 1 / cos,
        )

    screen.blit(currency_display, currency_display_rect)
    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()
