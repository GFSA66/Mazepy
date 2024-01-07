# подключаем нужные модули
import pygame
# создаём константы
FPS = 60
BACK = (0,0,0)
SIZE = (1152,512)
TILE =32
YELLOW = (255,255,0)
step = 2
pygame.init()
# начинаем создавать окно
window =pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

window.fill(BACK)

rect = pygame.Rect(10, 10, 200, 100)
# заканчиваем создавать окно
map_list = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,1],
            [1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1],
            [1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1],
            [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1],
            [1,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1],
            [0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
            [1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
            [1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

blocks = list()
enemies = list()
pictures = list()

class Block():
    def __init__(self,x,y,width = TILE,height = TILE, color = (0,0,255)):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
    def collide(self, obj):# проверка соприкосновения с другим объэктом
        return self.rect.colliderect(obj.rect) 
    def draw(self):  
        pygame.draw.rect(surface = window, rect = self.rect,color = self.color)

class Pacman(Block):
    def __init__(self, x, y, width=TILE, height=TILE, color=(YELLOW), points = 0):
        super().__init__(x, y, width, height, color)
        self.points = points
    def collide(self, obj):# проверка соприкосновения с другим объэктом
        return self.rect.colliderect(obj.rect) 
    def update(self):
        original_x = self.rect.x
        original_y = self.rect.y
        if keys[pygame.K_w]:
            self.rect.y -= step
        if keys[pygame.K_s]:
            self.rect.y += step
        if keys[pygame.K_a]:
            self.rect.x -= step
        if keys[pygame.K_d]:
            self.rect.x += step
        if keys[pygame.K_UP]:
            self.rect.y -= step
        if keys[pygame.K_DOWN]:
            self.rect.y += step
        if keys[pygame.K_LEFT]:
            self.rect.x -= step
        if keys[pygame.K_RIGHT]:
            self.rect.x += step
        if self.rect.x <=0:
            self.rect.x = 1140
        if self.rect.x >=1150:
            self.rect.x = 10
        if self.rect.x == 256 and self.rect.y == 160:
            self.rect.x = 1056
            self.rect.y = 224
        for block in blocks:
            if block.collide(self):
                self.rect.x = original_x
                self.rect.y = original_y
                break

        
        for enemy in enemies:
            global game_runing
            if self.collide(enemy):
                game_runing = False

dx,dy = 2,2

class Area():# копируем от сюда функции
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def set_color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    def collide(self, obj):
        return self.rect.colliderect(obj.rect)

class Lable(Area):# копируем от сюда функции
    def set_text(self, text, size):
       font1 = pygame.font.Font(None,size)
       self.text = font1.render(text,True,(255,255,255))
    def draw(self, shift_x = 0, shift_y = 0):
       self.fill()
       window.blit(self.text,(self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):# копируем от сюда функции
    def  __init__(self,filename,x=0,y=0,width = 10, height = 10):
        super().__init__(x=x,y=y,width=width,height=height,color= None)
        self.image = pygame.image.load(filename)
    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
    def update(self):
        if self.collide(pacman):
            win = Lable(400,200,1,1,(255,255,255))
            win.set_text('YOU WIN!!!',100)   
            win.draw()


timel = Lable(400,0,1,1,(12,87,90))
timel.set_text('time:0',40)        

for i,row in enumerate(map_list):# рисовка карты
        for j, el in enumerate(row):
            if el == 2:
                pacman = Pacman(TILE*j, TILE*i,color = (YELLOW))
            elif el == 1:
                block = Block(TILE*j,TILE*i,color = (0,0,255))
                blocks.append(block)# элементы списка зоздаются как блоки
            elif el == 3:
                finish = Picture("pixil-frame-0.png",TILE*j,TILE*i)
                pictures.append(finish)


game_runing = True
timer = 1
time = 0

while game_runing:
    window.fill(BACK) # заливка фона
    for event in pygame.event.get():# выход из игры(не доработано)
        if event.type == pygame.QUIT:
            game_runing = False

    keys = pygame.key.get_pressed()# разришение на нажимание клавиш
    
    if keys[pygame.K_ESCAPE]:# выход из игры
        game_runing = False

    for block in blocks:
        block.draw()
    
    for picture in pictures:
        picture.draw()
        picture.update()

    pacman.draw()
    pacman.update()

    

    #print(pacman.rect.x,pacman.rect.y)
    
    if timer == FPS:
        time += 1
        timel.set_text("time:"+ str(time),40)
    timel.draw()

    timer = (timer % FPS) +1

    clock.tick(FPS)
    pygame.display.flip()# обновление всего экранаa