import pygame as p
import math as m
import random as r

screen_w = 800
screen_h = 600
p_start_x = 370
p_start_y = 380
e_start_y_max = 50
e_start_y_min = 150
e_speed_x = 4
e_speed_y = 40
b_speed_y = 10
collison_d = 30

p.init()
screen = p.display.set.mode((screen_w. screen_h))
p.display.set_caption("Space Invaders")
p.display.set_icon(icon)
playerImg = p.image.load("player.png")
player_x = p_start_x
player_y = p_start_yplayer_x_change = 0
enemyImg = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
n_enemies = 5

for i in range(n_enemies):
    
enemyImg.append(p.image.load("enemy.png"))
enemy_x.append(r.randint(0, screen_w = 64))
enemy_y.append(r.randint(e_start_y_min, e_start_y_max))
enemy_x_change.append(e_speed_x)
enemy_y_change.append(e_speed_y)
bullet_x = 0
bullet_y = p_start__y
bullet_y_change = b_speed_y
state = "ready"
score_value = 0
font = p.font.Font("freesanbold.ttf", 32)
text_x = 10
text_y = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    
    def player1(x, y):
            screen.blit(player1Ing, (x, y))
        
    def player2(x, y):
            screen.blit(player2Ing, (x, y))
            
    def enemy(x, y, i):
            screen.blit(enemyImg[i], (x, y))
        
    def fire_bullet2(x, y):
        global bullet2_state
        bullet2_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))
        
    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((enemyX - bulletX)) ** 2 + (enemyY - bulletY) ** 2)
        return distance < COLLISION_DISTANCE
        
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false

        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
              player1X_change = -5
           if event.key == pygame.K_RIGHT:
              player1X_change = 5
            if event.key == pygame.K_a:
               player2X_change = -5
            if event.key == pygame.K_d:
               player2X_change = 5
            if event.key == pygame.K_SPACE and bullet1_state == "ready":
               bullet1X = player1X
               fire_bullet1(bullet1X, bullet1Y)
            if event.key == pygame.K_w and bullet2_state == "ready":
               bullet2X = player2X
               fire_bullet2(bullet2X, bullet2Y)

           if event.type == pygame.KEYUP:
              if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                 player1X_change = 0
              if event.key in [pygame.K_a, pygame.K_d]:
                 player2X_change = 0

        player1X += player1X_change
        player2X += player2X_change
        player1X = max(0, min(player1X, SCREEN_WIDTH - 64))
        player2X = max(0, min(player2X, SCREEN_WIDTH - 64))

        for i in range(num_of_enemies):
            if enemyY[i] > 340:
               for j in range(num_of_enemies):
                   enemyY[j] = 2000
                game_over_text()
                break
            
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
               enemyX_change[i] *= -1
               enemyY[i] += enemyY_change[i]

            if isCollision(enemyX[i], enemyY[i], bullet1X, bullet1Y):
                bullet1Y = player1Y
                bullet1_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
                enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

            if isCollision(enemyX[i], enemyY[i], bullet2X, bullet2Y):
                bullet2Y = player2Y
                bullet2_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
                enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
                enemy(enemyX[i], enemyY[i], i)

            if bullet1Y <= 0:
               bullet1Y = player1Y
               bullet1_state = "ready"
            if bullet1_state == "fire":
               fire_bullet1(bullet1X, bullet1Y)
               bullet1Y -= BULLET_SPEED_Y

            if bullet2Y <= 0:
               bullet2Y = player2Y
               bullet2_state = "ready"
            if bullet2_state == "fire":
               fire_bullet2(bullet2X, bullet2Y)
               bullet2Y -= BULLET_SPEED_Y

        player1(player1X, player1Y)
        player2(player2X, player2Y)
        show_score(textX, textY)
        pygame.display.update()