from pathlib import Path

from pico2d import *


open_canvas()

character = load_image(str(Path(__file__).with_name('all_64x64.png')))

frame = 0
play_count = 0
animation = 0
running = True

# 위에서부터 각 행의 프레임 수 (한 칸은 64 x 64).
frame_counts = [10, 10, 10, 9]

while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    if not running:
        break

    clear_canvas()

    # clip_draw의 세로 좌표는 이미지 아래쪽부터 계산한다.
    if animation == 0:
        character.clip_draw(frame * 64, 192, 64, 64, 400, 300, 200, 200)
    elif animation == 1:
        character.clip_draw(frame * 64, 128, 64, 64, 400, 300, 200, 200)
    elif animation == 2:
        character.clip_draw(frame * 64, 64, 64, 64, 400, 300, 200, 200)
    elif animation == 3:
        character.clip_draw(frame * 64, 0, 64, 64, 400, 300, 200, 200)

    update_canvas()
    delay(0.1)
    frame = (frame + 1) % frame_counts[animation]

    if frame == 0:
        play_count += 1
        if play_count == 5:
            # 5번 재생한 뒤 마지막 프레임에서 1초 정지한다.
            delay(1.0)
            play_count = 0
            animation = (animation + 1) % 4

close_canvas()
