import pygame


class Ship():
    def __init__(self, ai_setting, screen):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load('D:/pythonProject/Prakticia_projekt/elien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_setting.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_setting.ship_speed


