import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):     #pygame.sprite.Sprite 精灵，一个会动的图片
    """"管理飞船所发射的子弹的类"""
    def __init__(self,ai_game):
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()     #调用super()来继承Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #在（0，0）处设置一个表示子弹的矩阵，再设置正确的位置。
        #子弹非基本图像，因此必须使用pygame.Rect()类从头开始创建一个矩形
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)  #创建矩形（子弹）
        self.rect.midtop = ai_game.ship.rect.midtop  #将矩形（子弹）移动到指定位置
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        """"向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.settings.bullet_speed
        #更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):              #使得self.color的颜色填充到子弹rect对应的屏幕部分
        """"在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
