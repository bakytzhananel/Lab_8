import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)

car_img = pygame.image.load("car.png")
car_width, car_height = 50, 100
car_img = pygame.transform.scale(car_img, (car_width, car_height))

car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 150
car_speed = 5
coin_radius = 10
coins = []
coin_spawn_time = 30
frames = 0
collected_coins = 0

font = pygame.font.Font(None, 36)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed
    
    frames += 1
    if frames % coin_spawn_time == 0:
        coin_x = random.randint(50, WIDTH - 50)
        coin_y = -20
        coins.append([coin_x, coin_y])
    
    for coin in coins:
        coin[1] += 5
    
    for coin in coins[:]:
        if (car_x < coin[0] < car_x + car_width) and (car_y < coin[1] < car_y + car_height):
            collected_coins += 1
            coins.remove(coin)
    
    coins = [coin for coin in coins if coin[1] < HEIGHT]
    
    screen.blit(car_img, (car_x, car_y))
    
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), coin_radius)
    
    score_text = font.render(f"Coins: {collected_coins}", True, BLACK)
    screen.blit(score_text, (WIDTH - 120, 10))
    
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
