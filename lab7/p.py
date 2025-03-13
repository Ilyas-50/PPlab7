import pygame
from datetime import datetime

# Инициализация Pygame
pygame.init()

# Создание окна
size = w, h = 500, 500
window = pygame.display.set_mode(size)
pygame.display.set_caption("Clock")

# Загрузка изображений
clock_img = pygame.transform.scale(pygame.image.load("clock1.jpg"), (500, 500))
hand_img = pygame.image.load("hand1.png")  # Изображение стрелки

clock_center = (w // 2, h // 2)  # Центр часов

# Pygame clock для контроля FPS
fps_clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время
    now = datetime.now()
    sec_angle = -now.second * 6 - now.microsecond * 0.000006  # Плавное движение
    min_angle = -now.minute * 6 - now.second * 0.1  # 6° в минуту + влияние секунд

    # Поворачиваем стрелки
    rotated_sec = pygame.transform.rotate(hand_img, sec_angle)
    rotated_min = pygame.transform.rotate(hand_img, min_angle)

    # Центрируем стрелки
    sec_rect = rotated_sec.get_rect(midbottom=clock_center)
    min_rect = rotated_min.get_rect(midbottom=clock_center)

    # Отрисовка
    window.fill((0, 0, 0))
    window.blit(clock_img, (0, 0))
    window.blit(rotated_min, min_rect.topleft)  # Минутная стрелка
    window.blit(rotated_sec, sec_rect.topleft)  # Секундная стрелка

    pygame.display.flip()
    fps_clock.tick(1)  # 60 FPS

pygame.quit()
