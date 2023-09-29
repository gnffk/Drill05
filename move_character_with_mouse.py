from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

switch = True
def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type != SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass

def hand_random():
    global x,y, x1,y1, x2,y2
    x2 = random.randint(0,TUK_WIDTH)
    y2 = random.randint(0,TUK_HEIGHT)
    x1,y2 = x, y
    switch = False



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    if(switch):
        hand_random()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(0, 0, 50, 52, x2, y2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()

    frame = (frame + 1) % 8
    handle_events()
    delay(0.03)

close_canvas()




