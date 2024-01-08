# подключаем нужные модули
import pygame
from time import sleep
# создаём константы
FPS = 60
BACK = (0,0,0)
SIZE = (1152,512)
TILE =32
YELLOW = (255,255,0)
step = 2
# включаем все init()
pygame.init()
# начинаем создавать окно
window =pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

window.fill(BACK)

rect = pygame.Rect(10, 10, 200, 100)
# заканчиваем создавать окно
map_list = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1],
            [1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1],
            [1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1],
            [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1],
            [1,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1],
            [0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
            [1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
            [1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

list_map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,4,0,0,1,0,0,0,0,0,0,0,0,0,0,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,4,0,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,4,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1],
            [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,4,0,1,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0],
            [1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,4,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,2,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_map =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,2,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,3,1,0,0,0,0,0,0,0,4,0,0,0,0,1],
            [1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
            [1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1],
            [0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0],
            [0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,4,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
            [1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1],
            [1,0,0,1,1,1,1,0,0,1,0,4,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

list_list =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

maps_list = [map_list,list_map,map_map,list_list]

blocks = list()
enemies = list()
pictures = list()

class Block():# создаём класс блок
    def __init__(self,filename,x,y,width=TILE,height = TILE,color = (0,0,0),health = 100,power = 0) ->None:
        self.image = pygame.image.load(filename)
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.health = health
        self.color = color
        self.power = power
    def update(self):# двигается не марио а карта

        self.rect.x = self.x + step 

    
    def damage(self,value):
        global game_runing
        self.health -=value
        if self.health <= 0:
            self.health = 0
            game_runing = False
    def hit(self,enemy):
        enemy.damage(self.power)
    def collide(self, obj):
        return self.rect.colliderect(obj.rect)    
    def draw(self):  

        window.blit(self.image, (self.rect.x,self.rect.y))

class Pacman(Block):
    def __init__(self,filename, x, y, width=TILE, height=TILE, color=(YELLOW), points = 0):
        self.image = pygame.image.load(filename)
        super().__init__(filename,x, y, width, height, color)
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
        if self.rect.x <=-10:
            self.rect.x = 1140
        if self.rect.x >=1150:
            self.rect.x = -9
        if self.rect.x == 256 and self.rect.y >= 128 and self.rect.y <=160 and map_index == 0:
            self.rect.x = 1056
            self.rect.y = 224
        if self.rect.x == 576 and self.rect.y == 448 and map_index == 1:
            self.rect.x = 608
            self.rect.y =128
        for block in blocks:
            if block.collide(self):
                self.rect.x = original_x
                self.rect.y = original_y
                break

        
        for enemy in enemies:
            global game_runing
            if self.collide(enemy):
                maps(maps_list[map_index])

dx,dy = 2,2

class Enemy(Pacman):
    def __init__(self,filename, x, y, width=TILE, height=TILE, color=YELLOW):
        self.image = pygame.image.load(filename)
        super().__init__(filename,x, y, width, height, color)
        self.dx = 2
        self.dy = 2
    def collidetop(self):# проверка соприкосновений с верху
        flag = False
        for block in blocks:
            if self.rect.top == block.rect.bottom and (self.rect.left in range(block.rect.left,block.rect.right) or self.rect.right in range(block.rect.left+1,block.rect.right)):
                flag = True
        return flag   
    def collidebottom(self):# проверка соприкосновений снизу
        flag = False
        for block in blocks:
            if self.rect.bottom == block.rect.top and (self.rect.left in range(block.rect.left,block.rect.right) or self.rect.right in range(block.rect.left+1,block.rect.right)):
                flag = True
                self.rect.bottom = block.rect.top 
        return flag
    def collideleft(self):# проверка соприкосновений слева
        flag = False
        for block in blocks:
            if self.rect.left in range( block.rect.right -2,block.rect.right +2) and (self.rect.top in range (block.rect.top,block.rect.bottom) or self.rect.bottom in range(block.rect.top+1,block.rect.bottom)):
                flag = True
        return flag
              
    def collideright(self):# проверка соприкосновений справа
        flag = False
        for block in blocks:
            if self.rect.right in range( block.rect.left -2,block.rect.left +2) and (self.rect.top in range (block.rect.top,block.rect.bottom) or self.rect.bottom in range(block.rect.top+1,block.rect.bottom)):
                flag = True
        return flag
    def update(self):
        global dx,dy
        self.rect.x +=self.dx
        self.rect.y +=self.dy
        
        if self.collidetop() or self.collidebottom():
            self.dy =-self.dy
        if self.collideleft() or self.collideright():
            self.dx =-self.dx
        if self.rect.x <=0:
            self.dx =-self.dx
            self.dy =-self.dy
        if self.rect.x >=1140:
            self.dx =-self.dx
            self.dy =-self.dy


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
            global game_runing,map_index,go
            go = True
            map_index+=1


go = False
timel = Lable(400,0,1,1,(12,87,90))
timel.set_text("Минут:0"+" Секунд:0",40)
timer = 1
time = 0
time1 = 0
time_water = 1
timew = 30
timew1 = 2

def maps(couch):
    global pacman,blocks,enemies,pictures
    blocks = list()
    enemies = list()
    pictures = list()
    for i,row in enumerate(couch):# рисовка карты
            for j, el in enumerate(row):
                if el == 2:
                    pacman = Pacman("images/mashroom32.png",TILE*j, TILE*i,color = (YELLOW))
                elif el == 1:
                    block = Block("images/block32.png",TILE*j,TILE*i,color = (0,0,255))
                    blocks.append(block)# элементы списка зоздаются как блоки
                elif el == 3:
                    finish = Picture("images/pixil-frame-0.png",TILE*j,TILE*i)
                    pictures.append(finish)
                elif el == 4:
                    enemy = Enemy("images/enemy.png",TILE*j,TILE*i,color = (255,0,0))
                    enemies.append(enemy)

map_index = 0
game_runing = True
timer = 1
time = 0
maps(maps_list[map_index])
background=pygame.transform.scale(pygame.image.load("images/bg.jpg"),SIZE)

while game_runing:
    window.fill(BACK) # заливка фона
    window.blit(background,(0,0))
    for event in pygame.event.get():# выход из игры(не доработано)
        if event.type == pygame.QUIT:
            game_runing = False
    if map_index == 0:
        teleport = Lable(246,155,1,1,(12,87,90))
    elif map_index ==1:
        teleport = Lable(572,455,1,1,(12,87,90))
    elif map_index == 3:
        win = Lable(246,250,1,1,(12,87,90))
        win.set_text("ПОБЕДА!!!",100)
        win.draw()
        leave = Lable(246,350,1,1,(12,87,90))
        leave.set_text("Выход - ESCAPE",30)
        leave.draw()
    teleport.set_text('телепорт',15)
    keys = pygame.key.get_pressed()# разришение на нажимание клавиш
    if keys[pygame.K_ESCAPE]:# выход из игры
        game_runing = False
    if keys[pygame.K_l]:# выход из игры
        game_runing = False

    for block in blocks:
        block.draw()
    for enemy in enemies:
        enemy.draw()
        enemy.update()
    for picture in pictures:
        picture.draw()
        picture.update()

    if keys[pygame.K_r]:
        maps(maps_list[map_index])

    pacman.draw()
    pacman.update()

    #print(pacman.rect.x,pacman.rect.y)
    if map_index >=0 and map_index <=1:
        teleport.draw()
    
    if go == True:
        
        maps(maps_list[map_index])
        go = False

    if map_index != 3:
        if timer == FPS:
            time += 1
            if time == 60:
                time = 0
                time1 +=1
            timel.set_text("Минут:"+ str(time1) +" Секунд:"+str(time),40)
        
        timer = (timer % FPS) +1
    timel.draw()
    clock.tick(FPS)
    pygame.display.flip()# обновление всего экранаa

#