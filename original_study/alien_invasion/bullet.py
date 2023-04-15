import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所发射的子弹的类。"""

    def __init__(self,ai_game):
        """在飞船当前位置创建一个子对象。"""
        super().__init__()
        self.screen = ai_game.screen
        self.settins = ai_game.settings
        self.color = self.settins.bullet_color

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置。
        self.rect = pygame.Rect(0,0,self.settins.bullet_width,
            self.settins.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数表示的子弹位置。
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹。"""
        # 更新表示子弹位置的小数值。
        self.y -= self.settins.bullet_speed
        # 更新表示子弹的rect位置。
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹。"""
        pygame.draw.rect(self.screen,self.color,self.rect)