from pygame import *
init()
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        virtual_surface.blit(self.image, (self.rect.x, self.rect.y))

WIDTH = 1280
HEIGHT = 720
ASPECT_RATIO = WIDTH / HEIGHT

FPS = 60

window = display.set_mode((WIDTH, HEIGHT), RESIZABLE)
clock = time.Clock()

virtual_surface = Surface((WIDTH, HEIGHT))
current_size = window.get_size()

game = True
finish = False
while game:
    virtual_surface.fill((255, 255, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
        if e.type == VIDEORESIZE:
            new_width = e.w
            new_height = int(new_width / ASPECT_RATIO)
            window = display.set_mode((new_width, new_height), RESIZABLE)
            current_size = window.get_size()


    scaled_surface = transform.scale(virtual_surface, current_size)
    window.blit(scaled_surface, (0, 0))
    display.update()
    clock.tick(FPS)
