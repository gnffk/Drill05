from pico2d import *
import random
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
i, j = TUK_WIDTH // 2, TUK_HEIGHT // 2
x,y = random.randint(0, TUK_WIDTH),random.randint(0, TUK_HEIGHT)
x1,y1,x2,y2 = i,j,x,y
frame = 0
hide_cursor()

def move():
    for k in range(0, 100+1, 1):
        t = k /100
        i = (1-t)* x1 + t * x2
        j = (1-t)* y1 + t * y2
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.clip_draw(0, 0, 50, 52, x, y)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, i, j)
        update_canvas()
        handle_events()
        delay(0.1)

while running:
    if(x == i and y == j):
        x,y = random.randint(0, TUK_WIDTH),random.randint(0, TUK_HEIGHT)
        x1, y1, x2, y2 = i, j, x, y
    for k in range(0, 100+1, 1):
        t = k /100
        i = (1-t)* x1 + t * x2
        j = (1-t)* y1 + t * y2
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.clip_draw(0, 0, 50, 52, x, y)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, i, j)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        handle_events()

close_canvas()




