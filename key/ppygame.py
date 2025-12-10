import pygame
import sys
import random

pygame. init()

# 게임 화면 크기
screen_width = 800
screen_height = 600

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 폭발 사운드 준비
explosion_sound = pygame.mixer.Sound("C:/2025_python/key/explosion.wav")

# 추가: 게임 상태 변수
lives = 5
kill_count = 0
game_over = False

# 추가: 폰트
font = pygame.font.SysFont(None, 24)

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/2025_python/key/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 0

    def update(self):
        # 플레이어 위치 업데이트
        self.rect.x += self.speed_x
        # 화면을 벗어나지 않도록 좌, 우 이동 제한
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            
    # 총알 발사하는 경우
    def shoot(self):
        # 총알의 수직 간격 설정 (총알 높이 20px보다 약간 크게 설정)
        vertical_offset = 25 
        
        # 1. 가장 아래 총알 (기존 위치)
        bullet_bottom = Bullet(self.rect.centerx, self.rect.top)
        
        # 2. 중간 총알 (첫 번째 총알보다 위로 vertical_offset 만큼 이동)
        bullet_middle = Bullet(self.rect.centerx, self.rect.top - vertical_offset)
        
        # 3. 가장 위 총알 (두 번째 총알보다 위로 vertical_offset 만큼 이동)
        bullet_top = Bullet(self.rect.centerx, self.rect.top - (vertical_offset * 2))
        
        # 모든 총알을 그룹에 추가
        all_sprites.add(bullet_bottom, bullet_middle, bullet_top)
        bullets.add(bullet_bottom, bullet_middle, bullet_top)

# 외계인 클래스
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 외계인 이미지 생성
        self.image = pygame.image.load("C:/2025_python/key/alien.png")
        self.image = pygame.transform.scale(self.image,(30,30))

        # 외계인의 초기 위치 랜덤으로 설정
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-50, -10)
        self.speed_y = random.randint(1, 3)

    def update(self):
        # 외계인 위치 업데이트
        self.rect.y += self.speed_y
        # 화면 아래로 벗어나면 다시 위에서 나타나도록 설정
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-50, -10)
            self.speed_y = random.randint(1, 3)
            
    def explode(self):
        # 외계인이 폭발할 때 사운드 재생
        explosion_sound.play()

# 총알 클래스
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -2

    def update(self):
        # 총알 위치 업데이트
        self.rect.y += self.speed_y
        # 화면 위로 벗어나면 제거(위로갈 수록 작아짐)
        if self.rect.bottom < 0:
            self.kill()

# 추가: 게임 전체를 초기화하는 함수
def reset_game():
    global lives, kill_count, game_over, all_sprites, aliens, bullets, player

    lives = 5                  # 목숨 초기화
    kill_count = 0             # 점수 초기화
    game_over = False          # 게임 오버 해제

    # 스프라이트 그룹 재생성
    all_sprites.empty()
    aliens.empty()
    bullets.empty()

    # 플레이어 다시 생성
    player = Player()
    all_sprites.add(player)

    # 외계인 다시 생성
    for _ in range(10):
        alien = Alien()
        all_sprites.add(alien)
        aliens.add(alien)

# 게임 화면 생성, set_mode()는 가로세로 크기를 전달받음
screen = pygame.display.set_mode((screen_width, screen_height))
# set_caption()은 게임창 제목 설정
pygame.display.set_caption("Space Invader")

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 최초 1회 초기화
reset_game()   # 추가

# 게임 루프
clock = pygame.time.Clock()

# 게임 루프 시작
while True:
    # 파이게임 이벤트 루프 시작
    for event in pygame.event.get():
        # 사용자가 창 닫기를 시도하면 종료됨
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ★추가: 엔터로 게임 재시작
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                reset_game()

        # 게임오버 상태에서는 입력 금지
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                elif event.key == pygame.K_LEFT:
                    player.speed_x = -5
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speed_x = 0

    # 게임 오버가 아닐 때만 움직임/충돌 처리
    if not game_over:
        all_sprites.update()

        # 총알이 외계인 명중
        hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
        for hit in hits:
            alien = Alien()
            alien.explode()
            all_sprites.add(alien)
            aliens.add(alien)
            kill_count += 1       # 추가

        # 플레이어가 외계인에 닿음
        if pygame.sprite.spritecollide(player, aliens, False):
            lives -= 1            # 추가
            if lives <= 0:
                game_over = True  # 추가

    # 화면 출력
    screen.fill(black)
    # 스프라이트 그룹을 화면에 그리기
    all_sprites.draw(screen)

    # 추가: 점수 & 목숨 UI
    ui_text = font.render(f"Kills: {kill_count}   Lives: {lives}", True, white)
    screen.blit(ui_text, (10, 10))

    # 추가: 게임오버 메시지
    if game_over:
        over_text = font.render("GAME OVER - Press ENTER", True, red)
        x = (screen_width - over_text.get_width()) // 2
        y = (screen_height - over_text.get_height()) // 2
        screen.blit(over_text, (x, y))
    
    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()