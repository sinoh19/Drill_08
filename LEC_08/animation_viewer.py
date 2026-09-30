from pathlib import Path

from pico2d import *

open_canvas()

character = load_image(str(Path(__file__).with_name('all_64x64.png')))

close_canvas()
