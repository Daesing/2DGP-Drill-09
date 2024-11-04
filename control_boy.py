from pico2d import *

import game_world
from boy import Boy
from grass import Grass


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if event.type in (SDL_KEYDOWN,SDL_KEYUP):
                boy.handle_event(event) # input event


def reset_world():
    global running
    global grass,grass1
    global team
    global world
    global boy

    running = True

    grass = Grass(400,40)
    game_world.add_object(grass,0)

    boy = Boy()
    game_world.add_object(boy,1)

    grass1 = Grass(400,20)
    game_world.add_object(grass1,1)


def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()

# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
