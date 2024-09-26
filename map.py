import pygame

# 1 เป็นรหัสภาพกำแพง และ _เป็นที่ว่างๆ # pos คือ พิกัด ตย. รูป ุ อยู๋ที่พิกัด 1,4 ตามที่เข้าใจ
_ = False
mini_map = [
[1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
[6, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
[1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
[1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, _, _, 3, _, _, 4, 4, _, _, _, _, _, _, _, 1],
[1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1],
]

class Map:
    def __init__(self,game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
    
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
    
    #ฟังก์ชั้นนี้ไว้ทดลองวาดแมพ
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', (pos[0] *100, pos[1] *100, 100, 100), 2)
         for pos in self.world_map]    