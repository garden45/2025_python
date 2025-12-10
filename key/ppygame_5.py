# ★ 수정된 부분: 총알 5개가 수직으로 이어지도록 발사
    def shoot(self):
        # 총알의 수직 간격 설정 (총알 높이 20px보다 약간 크게 설정)
        vertical_offset = 25 
        
        # 1. 가장 아래 총알 (기존 위치, 0 * offset)
        bullet_1 = Bullet(self.rect.centerx, self.rect.top)
        
        # 2. 총알 2 (1 * offset)
        bullet_2 = Bullet(self.rect.centerx, self.rect.top - vertical_offset)
        
        # 3. 총알 3 (2 * offset)
        bullet_3 = Bullet(self.rect.centerx, self.rect.top - (vertical_offset * 2))
        
        # 4. 총알 4 (3 * offset)
        bullet_4 = Bullet(self.rect.centerx, self.rect.top - (vertical_offset * 3))

        # 5. 가장 위 총알 (4 * offset)
        bullet_5 = Bullet(self.rect.centerx, self.rect.top - (vertical_offset * 4))
        
        # 모든 총알을 그룹에 추가
        all_sprites.add(bullet_1, bullet_2, bullet_3, bullet_4, bullet_5)
        bullets.add(bullet_1, bullet_2, bullet_3, bullet_4, bullet_5)