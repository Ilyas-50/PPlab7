from pygame import *
import os

init()
size = w, h = 500, 500 
window = display.set_mode(size)
display.set_caption("Clock")

clock_img = transform.scale(image.load("clock1.jpg"), (500, 500))
mickey = transform.scale(image.load("mik.png"), (260, 260))
hand = transform.scale(image.load("handq.png"), (61, 270))

clock = time.Clock()
pivot_x, pivot_y = hand.get_width() // 2, hand.get_height()

clock_center = (w // 2, h // 2)  
angle_sec = 0
angle_min = 0

#музыка
mixer.init()

playlist = [file for file in os.listdir("music")]

current_track = 0
playing = False

def play_track(index):
    global playing
    mixer.music.load(os.path.join("music", playlist[index]))
    mixer.music.play()
    playing = True

play_track(current_track)

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if playing:
                    mixer.music.pause()
                    playing = False
                else:
                    mixer.music.unpause()
                    playing = True

            elif e.key == K_RIGHT:
                current_track += 1
                if current_track >= len(playlist):
                    current_track = 0
                play_track(current_track)

            elif e.key == K_LEFT:
                current_track -= 1
                if current_track < 0:
                    current_track = len(playlist) - 1
                play_track(current_track)


    angle_sec += 6
    if angle_sec == 360:
        angle_min += 6
        angle_sec = 0

    second_hand = transform.rotate(hand, -angle_sec)
    minute_hand = transform.rotate(hand, -angle_min)
    rect_second = second_hand.get_rect()
    # rect_second.midbottom = clock_center  
    rect_second.center = clock_center

    rect_minute = minute_hand.get_rect()
    # rect_minute.midbottom = clock_center
    rect_minute.center = clock_center

    window.fill((0, 0, 0))
    window.blit(clock_img, (0, 0))
    window.blit(mickey, (125, 110))
    window.blit(second_hand, (rect_second.x, rect_second.y))
    window.blit(minute_hand, (rect_minute.x, rect_minute.y))
    
    display.flip()
    clock.tick(10)


quit()