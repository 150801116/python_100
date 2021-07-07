import sys
import pygame

from Settings import Setting    #调用自定义类，要与python自带的中间空两行以示区别
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        """"初始化游戏并创建游戏资源"""
        pygame.init()
        # self.screen=pygame.display.set_mode((1200,800))   #设置窗口宽，高，但未输出。配合pygame.display.flip()才可显示
        # self.bg_color = (230,230,230)        #赋值背景颜色（灰色）,但未输出。配合self.screen.fill(self.bg_color)才可显示
        """"通过Settings类来设置屏幕基础信息"""
        self.settings = Setting()      #调用Setting类，初始化屏幕
        # 从setting里面传入窗口的宽和高
        #self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)   #设置全屏模式
        self.settings.screen_width = self.screen.get_rect().width        #获取显示器的屏幕宽和高
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")  # 设置窗口标题，但未输出。配合pygame.display.flip()才可显示
        self.ship = Ship(self)       #调用Ship类，生成一个飞船实例，初始化飞船，self就是AlienInvasion实例，让Ship能够访问到游戏资源
        self.bullets = pygame.sprite.Group()  #创建用于存储子弹的编组



    def run_game(self):
        """"开始游戏的主循环"""
        while True:
            self._check_events()       #更新事件
            self.ship.update()      #更新飞船位置
            self._update_bullets()  #更新子弹位置
            self._update_screen()  # 更新屏幕


    def _check_events(self):         #辅助方法，将管理事件的方法抽离出来
        """"响应按键和鼠标事件"""
        # 监视键盘和鼠标事件
        for event in pygame.event.get():  # 事件循环
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:        #每次按键都被注册为一个KEYDOWN事件,KEYDOEN与KEYUP的配套使用实现了持续移动
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)




    def _check_keydown_events(self,event):
        """"响应按键"""
        if event.key == pygame.K_RIGHT:  # 检查按下的键（event.key）为右箭头
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  #添加一个结束游戏的键盘按键快捷键Q
            sys.exit()
        elif event.key == pygame.K_SPACE:  # 发射子弹的事件监听
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """"响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):           #发射子弹的动作
        """"创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """"更新子弹的位置并删除消失的子弹"""
        #更新子弹的位置
        self.bullets.update()
        # 删除超过边界的子弹
        for bullet in self.bullets.copy():  # 列表长度在整个循环中保持不变，因此遍历删除的时候需要遍历整个副本
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_screen(self):        #辅助方法，将屏幕更新抽离出来
        """"更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环时候重绘屏幕
        self.screen.fill(self.bg_color)
        # 绘制飞船
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()