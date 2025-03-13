import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Часовая стрелка")

clock = pygame.time.Clock()

# Загружаем картинку стрелки
hand_image = pygame.image.load("handq.png")  # Замени на свою картинку
hand_image = pygame.transform.scale(hand_image, (80, 300))  # Измени размер, если нужно

# Центр часов (место, где основание стрелки остаётся)
clock_center = (400, 300)  

# Опорная точка (нижний центр стрелки)
pivot_x, pivot_y = hand_image.get_width() // 2, hand_image.get_height()

angle = 0  # Начальный угол

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Вращаем стрелку
    rotated_hand = pygame.transform.rotate(hand_image, -angle)  # Минус, чтобы вращалось правильно

    # Новый прямоугольник после поворота
    rotated_rect = rotated_hand.get_rect()

    # Корректируем позицию: двигаем, чтобы pivot-точка оставалась в центре часов
    rotated_rect.center = clock_center

    # Увеличиваем угол (1 градус = 1/60 секунды, 6 градусов = 1 секунда)
    angle += 6  

    # Очищаем экран
    screen.fill((0, 0, 0))  
    screen.blit(rotated_hand, rotated_rect.topleft)  # Рисуем стрелку

    pygame.display.flip()  # Обновляем экран
    clock.tick(10)  # 1 FPS = 1 тиканье в секунду

pygame.quit()
