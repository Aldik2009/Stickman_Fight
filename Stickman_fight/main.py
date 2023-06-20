from pygame import *

init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, max_left, max_right):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (150, 250))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.max_left = max_left
        self.max_right = max_right

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > self.max_left:
            self.rect.x -= 5
        if keys[K_s] and self.rect.x < self.max_right:
            self.rect.x += 5

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.x > self.max_left:
            self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.x < self.max_right:
            self.rect.x += 5

class Weapon(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, max_left, max_right):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 125))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.max_left = max_left
        self.max_right = max_right

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

fighter_image = 'fighter.png'
sword_image = 'sword.png'
shield_image = 'shield.png'

mixer.init()
sound_of_miss = mixer.Sound('miss.ogg')
sound_of_shield = mixer.Sound('shield_sound.ogg')
sound_of_hit1 = mixer.Sound('sound_1.ogg')
sound_of_hit2 = mixer.Sound('sound_2.ogg')

font.init()
font_score = font.SysFont('Arial', 50)

win_width = 900
win_height = 550
window = display.set_mode((win_width, win_height))
display.set_caption('Stickman_fight')
background = transform.scale(image.load('forest_background.jpg'), (win_width, win_height))
instruction_1 = transform.scale(image.load('instruction.png'), (200, 150))
instruction_2 = transform.scale(image.load('instruction2.png'), (200, 150))
instruction_of_game1 = transform.scale(image.load('instruction_game.png'), (200, 150))
instruction_of_game2 = transform.scale(image.load('instruction_game2.png'), (200, 150))
logo = transform.scale(image.load('game_logo.png'), (100, 150))

player1 = Player(fighter_image, 150, 150, 5, 20, win_width-170)
player2 = Player(fighter_image, win_width-300, 150, 5, 20, win_width-170)
sword1 = Weapon(sword_image, 265, 125, 5, 135, win_width-55)
sword2 = Weapon(sword_image, win_width-315, 125, 5, 5, win_width-185)
shield1 = Weapon(shield_image, 135, 125, 5, 5, win_width-185)
shield2 = Weapon(shield_image, win_width-185, 125, 5, 135, win_width-55)
hh1 = 10
hh2 = 10
correct_image1 = sword1.image
correct_image2 = sword2.image
correct_max_left = sword2.max_left
correct_max_right = sword2.max_right
correct_image_shield1 = shield1.image
correct_image_shield2 = transform.flip(shield2.image, True, False)
shield2.image = correct_image_shield2
correct_max_left_shield1 = shield1.max_left
correct_max_right_shield1 = shield1.max_right
correct_max_left_1 = sword1.max_left
correct_max_right_1 = sword1.max_right
correct_max_left_shield2 = shield2.max_left
correct_max_right_shield2 = shield2.max_right
score1 = 0
score2 = 0

game = True
finish_game = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:
            if e.key == K_c:
                if sword1.rect.x > shield1.rect.x:
                    if hh1 == 10:
                        sword1.image = transform.rotate(sword1.image, 270)
                        sword1.rect.x = sword1.rect.x + 75
                        sword1.rect.y = 200
                        hh1 = 9
                        sound1 = sound_of_miss
                    elif hh1 == 9:
                        sword1.image = correct_image1
                        sword1.rect.y = 125
                        hh1 = 10
                        sound1 = sound_of_miss
                    if sprite.collide_rect(sword1, shield2):
                        time.wait(50)
                        player1.rect.x = player1.rect.x - 150
                        sword1.rect.x = sword1.rect.x - 150
                        shield1.rect.x = shield1.rect.x - 150
                        player2.rect.x = player2.rect.x + 50
                        sword2.rect.x = sword2.rect.x + 50
                        shield2.rect.x = shield2.rect.x + 50
                        sound1 = sound_of_shield
                    if sprite.collide_rect(sword1, player2) and hh1 == 10:
                        player1.rect.x = 150
                        sword1.rect.x = 265
                        player2.rect.x = win_width-300
                        sword2.rect.x = win_width-315
                        sword1.image = correct_image1
                        sword1.rect.y = 125
                        sword2.image = correct_image2
                        sword2.rect.y = 125
                        hh2 = 10
                        shield1.rect.x = 135
                        shield2.rect.x = win_width-185
                        shield2.image = correct_image_shield2
                        shield2.max_left = correct_max_left_shield2
                        shield2.max_right = correct_max_right_shield2
                        score1 = score1 + 1
                        sound1 = sound_of_hit1
                    if sprite.collide_rect(sword1, player2) and hh1 == 9:
                        player1.rect.x = 150
                        sword1.rect.x = 265
                        player2.rect.x = win_width-300
                        sword2.rect.x = win_width-315
                        hh1 = 10
                        sword1.image = correct_image1
                        sword1.rect.y = 125
                        sword2.image = correct_image2
                        sword2.rect.y = 125
                        hh2 = 10
                        shield1.rect.x = 135
                        shield2.rect.x = win_width-185
                        shield2.image = correct_image_shield2
                        shield2.max_left = correct_max_left_shield2
                        shield2.max_right = correct_max_right_shield2
                        score1 = score1 + 1
                        sound1 = sound_of_hit1
                    if hh1 == 9:
                        sword1.rect.x = sword1.rect.x - 75
                    sound1.play()

            if e.key == K_v and hh1 == 10:
                shield1.image = transform.flip(shield1.image, True, False)
                shield1_x = shield1.rect.x
                shield1.rect.x = sword1.rect.x
                sword1.rect.x = shield1_x
                shield1_l = shield1.max_left
                shield1.max_left = sword1.max_left
                sword1.max_left = shield1_l
                shield1_r = shield1.max_right
                shield1.max_right = sword1.max_right
                sword1.max_right = shield1_r

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if sword2.rect.x < shield2.rect.x:
                    if hh2 == 10:
                        sword2.image = transform.rotate(sword2.image, 90)
                        sword2.rect.y = 200
                        hh2 = 9
                        sword2.rect.x = sword2.rect.x - 75
                        sound2 = sound_of_miss
                    elif hh2 == 9:
                        sword2.image = correct_image2
                        sword2.rect.y = 125
                        hh2 = 10
                        sword2.rect.x = sword2.rect.x + 75
                        sound2 = sound_of_miss
                    if sprite.collide_rect(sword2, shield1):
                        time.wait(50)
                        player1.rect.x = player1.rect.x - 50
                        sword1.rect.x = sword1.rect.x - 50
                        shield1.rect.x = shield1.rect.x - 50
                        player2.rect.x = player2.rect.x + 150
                        sword2.rect.x = sword2.rect.x + 150
                        shield2.rect.x = shield2.rect.x + 150
                        sound2 = sound_of_shield
                    if sprite.collide_rect(sword2, player1) and hh2 == 10:
                        player1.rect.x = 150
                        sword1.rect.x = 265
                        player2.rect.x = win_width-300
                        sword2.rect.x = win_width-315
                        sword2.image = correct_image2
                        sword2.rect.y = 125
                        sword1.image = correct_image1
                        sword1.rect.y = 125
                        hh1 = 10
                        shield1.rect.x = 135
                        shield2.rect.x = win_width-185
                        shield1.image = correct_image_shield1
                        shield1.max_left = correct_max_left_shield1
                        shield1.max_right = correct_max_right_shield1
                        sword1.max_left = correct_max_left_1
                        sword1.max_right = correct_max_right_1
                        score2 = score2 + 1
                        sound2 = sound_of_hit2
                    if sprite.collide_rect(sword2, player1) and hh2 == 9:
                        player1.rect.x = 150
                        sword1.rect.x = 265
                        player2.rect.x = win_width-300
                        sword2.rect.x = win_width-315
                        hh2 = 10
                        sword2.image = correct_image2
                        sword2.rect.y = 125
                        sword1.image = correct_image1
                        sword1.rect.y = 125
                        hh1 = 10
                        shield1.rect.x = 135
                        shield2.rect.x = win_width-185
                        shield1.image = correct_image_shield1
                        shield1.max_left = correct_max_left_shield1
                        shield1.max_right = correct_max_right_shield1
                        sword1.max_left = correct_max_left_1
                        sword1.max_right = correct_max_right_1
                        score2 = score2 + 1
                        sound2 = sound_of_hit2
                    sound2.play()

            if e.button == 3 and hh2 == 10:
                shield2.image = transform.flip(shield2.image, True, False)
                shield2_x = shield2.rect.x
                shield2.rect.x = sword2.rect.x
                sword2.rect.x = shield2_x
                shield2_l = shield2.max_left
                shield2.max_left = sword2.max_left
                sword2.max_left = shield2_l
                shield2_r = shield2.max_right
                shield2.max_right = sword2.max_right
                sword2.max_right = shield2_r

    if sword2.rect.x < shield2.rect.x:
        if hh2 == 10:
            sword2.max_left = correct_max_left
            sword2.max_right = correct_max_right
        if hh2 == 9:
            sword2.max_left = correct_max_left - 75
            sword2.max_right = correct_max_right - 75

    if finish_game != True:
        window.blit(background, (0, 0))
        round_score = font_score.render(str(score1) + ' Score ' + str(score2), 1, (70, 110, 240))
        window.blit(round_score, (400, 20))
        player1.update_1()
        player2.update_2()
        keys = key.get_pressed()
        if keys[K_a] and sword1.rect.x > sword1.max_left and shield1.rect.x > shield1.max_left:
            sword1.rect.x -= sword1.speed
            shield1.rect.x -= shield1.speed
        if keys[K_s] and sword1.rect.x < sword1.max_right and shield1.rect.x < shield1.max_right:
            sword1.rect.x += sword1.speed
            shield1.rect.x += shield1.speed
        if keys[K_DOWN] and sword2.rect.x > sword2.max_left and shield2.rect.x > shield2.max_left:
            sword2.rect.x -= sword2.speed
            shield2.rect.x -= shield2.speed
        if keys[K_RIGHT] and sword2.rect.x < sword2.max_right and shield2.rect.x < shield2.max_right:
            sword2.rect.x += sword2.speed
            shield2.rect.x += shield2.speed

        player1.reset()
        player2.reset()
        sword1.reset()
        sword2.reset()
        shield1.reset()
        shield2.reset()

        if score1 == 3:
            finish_game = True
        if score2 == 3:
            finish_game = True

    window.blit(instruction_1, (0, 400))
    window.blit(instruction_2, (700, 400))
    window.blit(instruction_of_game1, (200, 400))
    window.blit(instruction_of_game2, (500, 400))
    window.blit(logo, (400, 400))

    display.update()
    clock.tick(FPS)