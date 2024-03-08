import pgzrun
import random
import pygame

WIDTH = 800
HEIGHT = 600

basket = Actor('basket')
basket.x = WIDTH // 2
basket.y = HEIGHT - 40

apple = Actor('apple')
bomb = Actor('bomb')

is_game_over = False
game_timer = 10
score = 0
apple_count = 0
bomb_count = 0
start_game = False
timer=5

def position_fruit():
    apple.x = random.randint(40, WIDTH - 40)
    apple.y = -70

def position_bomb():
    bomb.x = random.randint(20, WIDTH - 20)
    bomb.y = -60

def draw_score():
    screen.draw.text("Score: " + str(score), (45, 30))
    screen.draw.text("Time: " + str(round(game_timer)), (45, 60))

    if is_game_over:
        display_text = "Game Over\nScore: " + str(score) + "\nApple Count: " + str(apple_count) + " & Bomb Count: " + str(bomb_count)
        position = ((WIDTH // 2) - 100, (HEIGHT // 2))
        screen.draw.text(display_text, position, fontsize=30, color=(255, 255, 255))
        screen.draw.text("Click to Restart", center=(WIDTH // 2, HEIGHT // 2 + 100), fontsize=40, color="white")

def move_basket():
    if keyboard.left:
        basket.x -= 10
    elif keyboard.right:
        basket.x += 10

def apple_fall():
    if apple.y > HEIGHT + 40:
        position_fruit()
    else:
        apple.y += 10
    check_collision()

def bomb_fall():
    if bomb.y > HEIGHT + 40:
        position_bomb()
    else:
        bomb.y += 10
    check_collision()  

def check_collision():
    global score
    global apple_count
    global bomb_count

    if apple.colliderect(basket):
        sounds.pop.play()
        score += 1
        apple_count += 1
        position_fruit()
    elif bomb.colliderect(basket):
        sounds.pop.play()
        score -= 1
        bomb_count += 1
        position_bomb()

def draw():
    global timer
    global start_game
    
    screen.clear()
    
    screen.blit('skybg', (0, 0))
    draw_score()
    basket.draw()
    apple.draw()
    bomb.draw()

    if not start_game:
        if timer <= 0:
            start_game=True
            #sounds.gameover.play()
            #is_game_over = True
        else:
            timer -= 0.017
        screen.draw.text("Game start in " + str(round(timer))+" s", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="white")

def update():
    global game_timer, is_game_over, start_game

    if start_game:
        if not is_game_over:
            move_basket()
            apple_fall()
            bomb_fall()

            if game_timer <= 0:
                sounds.gameover.play()
                is_game_over = True
            else:
                game_timer -= 0.017

def on_mouse_down(pos):
    global start_game, is_game_over, score, apple_count, bomb_count,game_timer,timer
    timer=5
    #if not start_game:
    #    start_game = True
    if is_game_over:
        is_game_over = False
        if timer <= 0:
            start_game=True
            #sounds.gameover.play()
            #is_game_over = True
        else:
            timer -= 0.017
        screen.draw.text("Game start in " + str(round(timer))+" s", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="white")

        start_game = False
        score = 0
        apple_count = 0
        bomb_count = 0
        game_timer = 10
    
        position_fruit()
        position_bomb()

position_fruit()
position_bomb()
pgzrun.go()
