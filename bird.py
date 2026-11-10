from pico2d import load_image


SPRITE_SHEET = 'bird_animation.png'
SHEET_WIDTH = 918
SHEET_HEIGHT = 506
FRAME_COLUMNS = 5
FRAME_ROWS = (5, 5, 4)
FRAME_COUNT = sum(FRAME_ROWS)
BODY_LENGTH_PX = 22
BODY_WIDTH_RATIO = 0.8


class Bird:
    image = None

    def __init__(self, x, y, direction=1):
        if Bird.image is None:
            Bird.image = load_image(SPRITE_SHEET)

        self.x = x
        self.y = y
        self.direction = direction
        self.frame_index = 0

    @staticmethod
    def frame_rect(frame_index):
        row = 0
        column = frame_index
        while column >= FRAME_ROWS[row]:
            column -= FRAME_ROWS[row]
            row += 1

        left = round(column * SHEET_WIDTH / FRAME_COLUMNS)
        right = round((column + 1) * SHEET_WIDTH / FRAME_COLUMNS)
        top = round(row * SHEET_HEIGHT / len(FRAME_ROWS))
        bottom = round((row + 1) * SHEET_HEIGHT / len(FRAME_ROWS))

        return left, SHEET_HEIGHT - bottom, right - left, bottom - top

    def draw(self):
        source_x, source_y, source_width, source_height = self.frame_rect(
            self.frame_index)
        scale = BODY_LENGTH_PX / (source_width * BODY_WIDTH_RATIO)
        self.image.clip_composite_draw(
            source_x, source_y, source_width, source_height,
            0, 'h' if self.direction < 0 else '',
            self.x, self.y,
            source_width * scale, source_height * scale)

    def update(self):
        pass
