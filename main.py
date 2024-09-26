import pygame
#sys ตัวนี้มันเป็น library ที่จัดเตรียมฟังก์ชันและตัวแปรที่ใช้เพื่อจัดการกับส่วนต่างๆของ Python Runtime Environment เอาไว้ช่วยให้เราเข้าถึงพารามิเตอร์และฟังก์ชันเฉพาะของระบบได้ง่าย
#https://docs.python.org/3/library/sys.html ข้อมูลเพิ่มเติม
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import * 
from object_handler import *

#23.37 ทำต่อ

#โครงสร้างเกม
class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(SCREEN)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()
    
    
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCassting(self)
        self.object_handler = ObjectHandler(self)
        

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        #ไว้ดู FPS ในเกม
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        #self.screen.fill('black')
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    #อันนี้เป็น main ของเกมloop
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()