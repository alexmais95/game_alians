import pygame
from setting import Setting
import game_event as ge
from ship import Ship
from pygame.sprite import Group

def main_game():
    pygame.init()
    g_sattin = Setting()
    screen = pygame.display.set_mode((g_sattin.screen_wight, g_sattin.screen_hight))
    ship = Ship(g_sattin, screen)
    pygame.display.set_caption('Air-Plain')
    bullets = Group()

    while True:
        ge.game_event(ship, screen, bullets)
        ge.update(g_sattin, screen, ship, bullets)
        bullets.update()
        ship.update()


if __name__ == '__main__':
    main_game()
