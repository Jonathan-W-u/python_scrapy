#-*- conding:utf-8 -*-
import pygame
from pygame.locals import *
import time

from pygame.constants import K_LEFT, K_RIGHT, K_SPACE, K_a, K_d
from pygame.event import Event
"""
    搭建界面，主要完成窗口和背景图的显示
"""
class Plane(object):
    def key_control(self):
        for event in pygame.event.get():
            # 判断是否点击了退出按键
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                # 检测按键是否是 a 或者 left
                if event.key == K_a or event.key == K_LEFT:
                    # print("left")
                    self.move_left()
                # 检测按键是否是 d 或者 right
                elif event.key == K_d or event.key == K_RIGHT:
                    # print("right")              
                    self.move_right()
                # 检测是否是 空格键
                elif event.key == K_SPACE:
                    print("space")
                    # 发射子弹
                    self.action()


class HeroPlane(Plane):
    def __init__(self, screen_tmp):
        self.x = 210
        self.y = 700
        self.screen = screen_tmp
        self.image = pygame.image.load("./pic/hero1.png")
        self.bullet_list = [] #存储发射出去的子弹对象引用
    
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))

        for bullet in self.bullet_list:
            # 显示创建的子弹
            bullet.display()
            # 创建后的子弹自动移动
            bullet.move()

    def move_left(self):
        self.x -= 5
    
    def move_right(self):
        self.x += 5
    
    def action(self):
        # 创建一个子弹
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
        

    

class EnemyPlane(Plane):
    def __init__(self, screent_tmp):
        self.x = 0
        self.y = 0
        self.screen =screent_tmp
        self.image = pygame.image.load("./pic/enemy0.png")
   
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))
        

class Bullet(object):
    def __init__(self, screen_tmp, x, y):
        self.x = x
        self.y = y
        self.screen = screen_tmp
        self.image = pygame.image.load("./pic/bullet.png")

    def display(self):
        # print("打印子弹")
        self.screen.blit(self.image,(self.x, self.y))

    def move(self):
        self.y -= 5   

def main():
    
    # 1：创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,852),0,32)
    # 2：创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./pic/background.png")

    # 3：创建一个飞机图片
    hero = HeroPlane(screen)

    # 4：创建一个敌人飞机
    enemy = EnemyPlane(screen)

    # ：把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(background,(0,0))

        # 设定需要显示的飞机图片
        hero.display()

        # 设定需要显示的敌人图片
        enemy.display()

        # 更新需要显示的内容
        pygame.display.update()

        # 获取事件，比如按键等
        hero.key_control()

        time.sleep(0.05)

if __name__ == "__main__":
    main()
