import math
import random
import pygame
from pygame import mixer

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Load images
background_img = pygame.image.load('background.png')
retry_img = pygame.image.load('retry.png')

# Get the dimensions of the retry image
retry_width = retry_img.get_width()
retry_height = retry_img.get_height()

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    screen.blit(retry_img, (370, 350))  # Display the retry button

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < 27


# Game Loop
running = True
game_over = False  # Flag to track game over state
while running:
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            elif event.key == pygame.K_RIGHT:
                playerX_change = 1
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playerX_change = 0

    if not game_over:
        playerX += playerX_change
        if playerX < 0:
            playerX = 0
        elif playerX > 736:
            playerX = 736

        for i in range(num_of_enemies):
            if enemyY[i] > 440:
                game_over = True  # Set game_over flag when an enemy reaches the bottom
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] < 0 or enemyX[i] > 736:
                enemyX_change[i] = -enemyX_change[i]
                enemyY[i] += enemyY_change[i]

            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

    if game_over:
        game_over_text()
        pygame.display.update()  # Ensure the retry button is displayed

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                retry_button_rect = pygame.Rect(370, 350, retry_width, retry_height)
                if retry_button_rect.collidepoint(mouse_x, mouse_y):
                    # Reset game state
                    game_over = False
                    score_value = 0
                    for i in range(num_of_enemies):
                        enemyX[i] = random.randint(0, 736)
                        enemyY[i] = random.randint(50, 150)

                    # Allow the game loop to continue
                    continue

# Quit pygame
pygame.quit()
