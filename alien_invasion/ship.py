import pygame


class Ship:
    """"管理飞船的类"""
    def __init__(self,ai_game):       #ai_game即AlienInvasion实例的引用，让Ship能够访问AlienInvasion中定义的所有资源
        """"初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()        #get_rect()获取相应surface的属性rect
        #加载飞船图片并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')     #pygame.image.load(）加载图像，相对路径读取图片
        self.rect = self.image.get_rect()                     #读取飞船的属性，以便于指定飞船位置
        #对于每艘新飞船，都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom     #飞船的底部中央对应屏幕的底部中央

        #rect的x等属性只能存储整数值，因为需要做些修改,在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """"根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #更新的是飞船位置而不是rect对象的x值
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #根据self.x更新rect对象
        self.rect.x = self.x
        #print(self.x)
        #print(self.rect.x)  self.rect.x只能够存储self.x的整数部分


    def blitme(self):         #定义blitme()方法，用于将图像绘制到self.rect指定的位置
        """"在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)