import pygame
import sys
from bullet import Bullet


def game_event(ship, screen, bullets):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:   #выход из игры
            sys.exit()

        if event.type == pygame.KEYDOWN:    #при нажатии клавиши
            keydown(event, screen, ship, bullets)

        if event.type == pygame.KEYUP:    #при нажатии клавиши
            keyup(event, ship)


def update(g_satting, screen, ship, bullets):
    screen.fill(g_satting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def keydown(event, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, ship)
        bullets.add(new_bullet)

def keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_UP:
        ship.moving_up = False