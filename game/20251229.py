import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥피하고 사과먹기")

clock = pygame.time.Clock() 
white = (255, 255, 255)

# 이미지
apple_img = pygame.image.load("c:/2025_python/game/apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))

poop_img = pygame.image.load("c:/2025_python/game/poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("c:/2025_python/game/dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) 
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 3

    def update(self): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    # x, y 매개변수 제거하고 랜덤 시작 위치 설정
    def __init__(self):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        
        # 화면의 랜덤한 위치에서 시작
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)

        # 랜덤한 방향과 속도 설정
        self.speed_x = random.choice([-1, 1]) * random.randint(2, 4)
        self.speed_y = random.choice([-1, 1]) * random.randint(2, 4)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1

            if self.rect.left < 0: self.rect.left = 0
            if self.rect.right > WIDTH: self.rect.right = WIDTH
            
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1

            if self.rect.top < 0: self.rect.top = 0
            if self.rect.bottom > HEIGHT: self.rect.bottom = HEIGHT


all_sprites = pygame.sprite.Group() 
enemy_group = pygame.sprite.Group() 

player = Player()
all_sprites.add(player)

# 똥 4개 생성
NUM_ENEMIES = 4
for _ in range(NUM_ENEMIES):
    new_enemy = Enemy()
    all_sprites.add(new_enemy)
    enemy_group.add(new_enemy)

apples = []
apple_spawn_timer = 0
APPLE_SPAWN_INTERVAL = 30 

score = 0
lives = 3
running = True
game_over = False

def spawn_apple():
    side = random.choice(["left", "right", "top", "bottom"])
    size = 40
    if side == "left":
        x, y = -size, random.randint(0, HEIGHT - size)
        vx, vy = random.randint(2, 4), random.randint(-2, 2)
    elif side == "right":
        x, y = WIDTH, random.randint(0, HEIGHT - size)
        vx, vy = -random.randint(2, 4), random.randint(-2, 2)
    elif side == "top":
        x, y = random.randint(0, WIDTH - size), -size
        vx, vy = random.randint(-2, 2), random.randint(2, 4)
    else:
        x, y = random.randint(0, WIDTH - size), HEIGHT
        vx, vy = random.randint(-2, 2), -random.randint(2, 4)

    rect = pygame.Rect(x, y, size, size)
    apples.append({"rect": rect, "vx": vx, "vy": vy}) 

def reset_game():
    """게임 상태를 초기화하고 똥의 위치를 재설정"""
    global game_over, score, lives, apples, apple_spawn_timer
    game_over = False
    score = 0
    lives = 3
    
    player.rect.center = (WIDTH // 2, HEIGHT // 2)
    
    # 모든 똥의 위치와 속도 초기화
    for enemy in enemy_group:
        enemy.rect.x = random.randint(0, WIDTH - enemy.rect.width)
        enemy.rect.y = random.randint(0, HEIGHT - enemy.rect.height)
        enemy.speed_x = random.choice([-1, 1]) * random.randint(2, 4)
        enemy.speed_y = random.choice([-1, 1]) * random.randint(2, 4)
    
    apples.clear()
    apple_spawn_timer = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_RETURN:
                reset_game()

    if not game_over:
        all_sprites.update() 

        # 사과 생성
        apple_spawn_timer += 1
        if apple_spawn_timer >= APPLE_SPAWN_INTERVAL:
            apple_spawn_timer = 0
            spawn_apple()

        # 사과 이동 & 충돌 처리(목숨 증가)
        new_apples = []
        for apple in apples:
            rect = apple["rect"]
            rect.x += apple["vx"]
            rect.y += apple["vy"]

            if rect.right < 0 or rect.left > WIDTH or rect.bottom < 0 or rect.top > HEIGHT:
                continue

            if player.rect.colliderect(rect):
                score += 1
                lives = min(lives + 1, 99) 
                continue 

            new_apples.append(apple)

        apples = new_apples

        # 똥 충돌 & 목숨 감소 (4개의 똥 중 하나라도 닿으면)
        hits = pygame.sprite.spritecollide(player, enemy_group, False)
        if hits:
            lives -= 1
            
            if lives <= 0:
                game_over = True
            else:
                # 충돌 직후 튕겨나가도록 플레이어와 닿은 똥을 잠시 재배치
                player.rect.center = (WIDTH // 2, HEIGHT // 2)
                for enemy_hit in hits:
                     enemy_hit.rect.x = random.randint(0, WIDTH - enemy_hit.rect.width)
                     enemy_hit.rect.y = random.randint(0, HEIGHT - enemy_hit.rect.height)


    screen.fill((170, 200, 255)) 
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

    for apple in apples:
        screen.blit(apple_img, apple["rect"])

    all_sprites.draw(screen)


    font = pygame.font.SysFont(None, 24)
    text_score = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text_score, (10, 10))

    text_lives = font.render(f"Lives: {lives}", True, (0, 0, 0))
    screen.blit(text_lives, (WIDTH - text_lives.get_width() - 10, 10))

    if game_over:
        over_text = font.render("GAME OVER (Press Enter to Restart)", True, (255, 0, 0))
        over_x = (WIDTH - over_text.get_width()) // 2
        over_y = (HEIGHT - over_text.get_height()) // 2 
        screen.blit(over_text, (over_x, over_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()