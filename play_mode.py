from pico2d import *

import game_framework
import game_world
from bird import BIRD_COUNT, Bird


birds = []


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    global birds

    game_world.clear()
    birds = []
    for index in range(BIRD_COUNT):
        column = index % 5
        row = index // 5
        x = 340 + column * 55 + row * 28
        y = 245 + row * 70
        bird = Bird(x, y, phase=index / BIRD_COUNT)
        birds.append(bird)
        game_world.add_oject(bird)


def pause():
    pass


def resume():
    pass


def finish():
    global birds
    game_world.clear()
    birds = []


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()
