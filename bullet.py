import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 12)
        self.color = 139, 0, 0
        self.bullet_speed = 1
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = self.rect.y

    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

