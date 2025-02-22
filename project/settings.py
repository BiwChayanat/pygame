import math
#ตั้งค่าต่างๆ

#คั้งค่าหน้าจอ
SCREEN = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH//2
HALF_HEIGHT = HEIGHT//2
#ตั้งค่าFPS
FPS = 60

#mini_map
PLAYER_POS = 1.5, 5

PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004 #ความเร็วผู้เล่น
PLAYER_ROT_SPEED = 0.002 #ความเร็วในการหันหน้า

#ตั้งค่าของ raycasting
FOV = math.pi /3
HALF_FOV = FOV /2
NUM_RAYS = WIDTH //2
HALF_NUM_RAYS = NUM_RAYS //2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS