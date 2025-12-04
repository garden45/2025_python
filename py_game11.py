#사과 먹기 게임
#사과가 위에서 떨어지도록
# 덕새 코드에 추가하는 방향으로 사과들을 더 많이 만들거나 (충돌) 움직임 위에서 아래, 아래에서 위로 움직이도록
# 레이저 사각형 5개가 우주선 위에 값에서 생성되도록 y축 값만 바뀜
# hit 이 되는 상황

# 플레이어 혹은 객체가 여러개 생성되게끔
# 그리고 그 객체가 움직일 수 있게(랜덤, 좌우, 위아래)
# 사운드 추가(액션)
# 객체가 부딪혔을 때 변수가 변경되도록

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥피하고 사과먹기")

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
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

        # 화면 밖으로 못 나가게
        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.Surface((40, 40))
        self.image.fill((255, 80, 80))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x, y)
        self.speed_x=2

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 50 or self.rect.right > 200:
            self.speed_x *= -1

all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

enemy = Enemy(50, 260)
all_sprites.add(enemy)
enemy_group.add(enemy)

coin_rect = pygame.Rect(430, 130, 40, 40)
score=0

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()

        if player.rect.colliderect(coin_rect):
            print("코인 충돌!")
            score += 1
            coin_rect.x = 430 if score %2 == 0 else 350

        hits = pygame.sprite.spritecollide(player, enemy_group, False)
        if hits:
            print("적과 충돌! 게임 오버")
            game_over = True

    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))
    
    pygame.draw.circle(screen, (0, 255, 0),\
                       (coin_rect.x + coin_rect.width // 2, coin_rect.y + coin_rect.height //2),\
                        20)
    
    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)

    all_sprites.draw(screen)

    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    if game_over:
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        over_x = (WIDTH - over_text.get_width()) // 2
        over_y = (HEIGHT - over_text.get_height()) // 2 
        screen.blit(over_text, (over_x, over_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()