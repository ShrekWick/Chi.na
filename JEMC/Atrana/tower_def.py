import math
from datetime import datetime, timedelta

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
currency = 5
currency_display = font.render(f"You have {currency} AZN", True, "white")
currency_display_rect = currency_display.get_rect()
currency_display_rect.center = (screen.width / 2, screen.height / 2)
POLUCHKA = pygame.event.custom_type()
POLUCHKA_INTERVAL = 500
pygame.time.set_timer(POLUCHKA, POLUCHKA_INTERVAL)
sentries = []
shoot = False

FIRE_SPEED = 2000
BULLET_SPEED = 300


class Sentry:
    def __init__(self, pos, bullets, last_shoot_time):
        self.pos = pos
        self.bullets = bullets
        self.last_shoot_time = last_shoot_time


class Bullet:
    def __init__(self, pos, target, birth_time, mother):
        self.pos = pos
        self.target = target
        self.birth_time = birth_time
        self.mother = mother


def put_a_sentry_here(pos):
    sentry = Sentry(pos, [], datetime.now() - timedelta(milliseconds=FIRE_SPEED))
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


def distance(sentry, mann):
    return math.sqrt(
        (sentry.pos[0] - mann.pos[0]) ** 2 + (sentry.pos[1] - mann.pos[1]) ** 2
    )


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
        if len(manns) > 0:
            min_mann = manns[0]
            for m in manns:
                if distance(s, m) < distance(s, min_mann):
                    min_mann = m
            shoot = True
            target = min_mann

        if shoot and target:
            now = datetime.now()
            if (now - s.last_shoot_time).total_seconds() > FIRE_SPEED / 1000:
                s.bullets.append(Bullet(s.pos, target, now, s))
                s.last_shoot_time = now
            shoot = False
        for b in s.bullets:
            pygame.draw.circle(screen, "chartreuse4", b.pos, 5)
            uxStep = BULLET_SPEED
            xStep = uxStep if b.target.pos[0] > s.pos[0] else -uxStep
            yStep = (b.target.pos[1] - s.pos[1]) / (b.target.pos[0] - s.pos[0]) * xStep
            b.pos = (
                b.pos[0] + dt * xStep,
                b.pos[1] + dt * yStep,
            )

    for m in manns:
        pygame.draw.circle(screen, "brown4", m.pos, 15)
        m.pos = (m.pos[0] + m.speed * dt, m.pos[1])
        if m.pos[0] > screen.width + 50:
            manns.remove(m)

    screen.blit(currency_display, currency_display_rect)
    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()
