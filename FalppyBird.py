import pygame
import os, random

GAME_WIDTH = 500
GAME_HEIGHT = 800

IMG_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMG_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMG_BACCKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMGS_BIRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]
IMG_APP = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'Background.jpg')),(500,800))

pygame.font.init()
FONT_SCORE = pygame.font.SysFont('consolas', 40)
FONT_TITLE = pygame.font.SysFont('arial', 60)
FONT_OPTIONS = pygame.font.SysFont('arial', 30)

class Bird:
    IMGS = IMGS_BIRD

    MAX_ROTATION = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.count_img = 0
        self.image = self.IMGS[0]

    def jump(self):
        self.speed = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
        self.time += 1
        # Formula Sorvetão S = so + ( vo . t) 2 + a. t².
        deslocamento = 1.5 * (self.time**2) + self.speed * self.time

        if deslocamento > 16:
            deslocamento =16
        elif deslocamento <0:
            deslocamento -=2

        self.y += deslocamento

        #angulo
        if deslocamento <0 or self.y < (self.height + 50):
            if self.angle < self.MAX_ROTATION:
                self.angle = self.MAX_ROTATION
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED

    def draw(self, canvas):
        self.count_img += 1

        if self.count_img < self.ANIMATION_TIME:
            self.image = self.IMGS[0]
        elif self.count_img < self.ANIMATION_TIME*2:
            self.image = self.IMGS[1]
        elif self.count_img <self.ANIMATION_TIME*3:
            self.image = self.IMGS[2]
        elif self.count_img < self.ANIMATION_TIME*4:
            self.image = self.IMGS[1]
        elif self.count_img < self.ANIMATION_TIME*4 + 1:
            self.image = self.IMGS[0]
            self.count_img = 0

        

        if self.angle <= -80:
            self.image = self.IMGS[1]
            self.count_img = self.ANIMATION_TIME*2
        

        rotated_image = pygame.transform.rotate(self.image, self.angle)
        pos_center_image = self.image.get_rect(topleft=(self.x, self.y)).center
        rectangle = rotated_image.get_rect(center=pos_center_image)
        canvas.blit(rotated_image, rectangle.topleft)
        
    def get_mask(self):
        return   pygame.mask.from_surface(self.image)


class Pipe:
    DISTANCE = 200
    SPEED = 5


    def __init__(self, x):
        self.x = x
        self.height = 0
        self.pos_top = 0
        self.pos_base = 0
        self.PIPE_TOP = pygame.transform.flip(IMG_PIPE, False, True)
        self.PIPE_BASE = IMG_PIPE
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.height = random.randrange(50 , 450)
        self.pos_top = self.height - self.PIPE_TOP.get_height()
        self.pos_base = self.height + self.DISTANCE

    def move(self):
        self.x -= self.SPEED

    def draw(self, canvas):
        canvas.blit(self.PIPE_TOP, (self.x, self.pos_top))
        canvas.blit(self.PIPE_BASE, (self.x, self.pos_base))

    def collision(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        base_mask = pygame.mask.from_surface(self.PIPE_BASE)

        distance_top = (self.x - bird.x, round(self.pos_top) - round(bird.y))
        distance_base = (self.x - bird.x, round(self.pos_base) - round(bird.y))

        top_point = bird_mask.overlap(top_mask, distance_top)
        base_point = bird_mask.overlap(base_mask, distance_base)

        if top_point or base_point:
            return True
        else:
            return False



class Floor:
    SPEED = 5
    WIDTH = IMG_BASE.get_width()
    IMAGE = IMG_BASE

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    
    def move(self):
        self.x1 -= self.SPEED
        self.x2 -= self.SPEED

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, canvas):
        canvas.blit(self.IMAGE, (self.x1, self.y))
        canvas.blit(self.IMAGE, (self.x2, self.y))

def draw_screen(canvas, birds, pipes, floor, score):
    canvas.blit(IMG_BACCKGROUND, (0,0))
    for bird in birds:
        bird.draw(canvas)
    for pipe in pipes:
        pipe.draw(canvas)

    text = FONT_SCORE.render(f"Score: {score}", 1, (255, 255, 255))
    canvas.blit(text, (GAME_WIDTH - 10 - text.get_width(), 10))
    floor.draw(canvas)
    pygame.display.update()





def main():
    canvas = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    app(canvas)

    while True:

        birds = [Bird(230,250)]
        pipes = [Pipe(700)]
        floor = Floor(730)
        score = 0
        clock = pygame.time.Clock()


        loop = True
        while loop:
            clock.tick(30)

            #ler as teclas
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for bird in birds:
                            bird.jump()

            #mover as coisas
            for bird in birds:
                bird.move()
            floor.move()

            add_pipe = False
            remove_pipes = []
            for pipe in pipes:
                for i, bird in enumerate(birds):
                    if pipe.collision(bird):
                        birds.pop(i)
                    if not pipe.passou and  bird.x > pipe.x:
                        pipe.passou = True
                        add_pipe = True
                pipe.move()
                if pipe.x + pipe.PIPE_TOP.get_width() <0:
                    remove_pipes.append(pipe)
            
            if add_pipe:
                score += 1
                pipes.append(Pipe(600))
            for pipe in remove_pipes:
                pipes.remove(pipe)

            for i, bird in enumerate(birds):
                if (bird.y + bird.image.get_height()) > floor.y or bird.y < 0:
                    birds.pop(i)

            draw_screen(canvas, birds, pipes, floor, score)

            if len(birds) == 0:
                break

def app(canvas):
    loop = True
    while loop:
        # canvas.fill((0, 0, 0))
        canvas.blit(IMG_APP, (0,0))
        text_title = FONT_TITLE.render("Flappy", True, (255, 255, 255))
        text_play = FONT_OPTIONS.render("Pressine ENTER para começar", 1, (255, 255, 255))
        text_exit = FONT_OPTIONS.render("Pressione ESC para Sair", 1, (255, 255, 255))
       
        canvas.blit(text_title, (GAME_WIDTH//2 - text_title.get_width()//2, 10))
        canvas.blit(text_play, (GAME_WIDTH//2 - text_play.get_width()//2, 350))
        canvas.blit(text_exit, (GAME_WIDTH//2 - text_exit.get_width()//2, 420))
        

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    loop = False 
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

if __name__ == "__main__":
    main()