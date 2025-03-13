from pygame import *

init()
size = w, h = 500, 500 
window = display.set_mode(size)
display.set_caption("Ball")

x, y = 110,110
radius = 25
move = 20

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

        elif e.type == KEYDOWN:
            if e.key == K_LEFT and x - radius > 0:
                x -= move 
            if e.key == K_RIGHT and x + radius < w:
                x+= move
            if e.key == K_UP and y - radius > 0:
                y -= move
            if e.key == K_DOWN and x - radius < h:
                y += move
        
        window.fill((0, 0, 0))
        draw.circle(window, (255,255,255), (x,y), radius)
        display.flip()
