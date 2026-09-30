from pathlib import Path

from pico2d import *

open_canvas()

character = load_image(str(Path(__file__).with_name('all_64x64.png')))

clear_canvas()
character.clip_draw(0, 192, 64, 64, 400, 300, 200, 200)
update_canvas()
delay(0.1)

close_canvas()
