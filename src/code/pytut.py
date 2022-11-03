import pygame
import pytmx
from pytmx.util_pygame import load_pygame

def display_score():
    current_time =int( pygame.time.get_ticks()/ 1000)- start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)



pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Nostalgia')
clock = pygame.time.Clock()
test_font = pygame.font.Font('C:/Users/arush/OneDrive/Documents/GVSU/Fall 22/641/Github 641/GVSU-CIS641_NostalgiaDevelopment/src/font/Pixeltype.ttf', 50)
game_active = True
fps = 60
start_time = 0


sky_surface = pygame.image.load('C:/Users/arush/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surface = pygame.image.load('C:/Users/arush/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/ground.png').convert()


# score_surf = test_font.render('Scoreboard', False, (255,160,122))
# score_rect = score_surf.get_rect(center = (400,50))


snail_surface = pygame.image.load('C:/Users/arush/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
snail_rect = snail_surface.get_rect(bottomright = (600,300)) #position


player_surf = pygame.image.load('C:/Users/arush/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0 

def blit_all_tiles(window, tmxdata, world_offset):
	for layer in tmxdata:
		for tile in layer.tiles():
			#tile[0]...x grid location
			#tile[1]...y grid location
			#tiles[2]...image data for blitting
			x_pixel = tile[0] * 64 + world_offset[0]
			y_pixel = tile[1] * 64 + world_offset[1]
			window.blit(tile[2], (x_pixel, y_pixel))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            # tracks position of players mouse 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            # check if player is pressing any keys 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

        else: # restarts game, at press of any key after player collides with enemy
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)
    

    if game_active:

        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen,(250,235,215), score_rect)
        # pygame.draw.rect(screen, (250,235,215), score_rect,0,13,15) # draws the score rect
        # screen.blit(score_surf, score_rect) # tells game where to write score_Surf text
        display_score()
        
        snail_rect.x -= 4    
        if snail_x_pos <= 0: snail_x_pos = 800
        # screen.blit(snail_surface,(snail_x_pos,270))
        screen.blit(snail_surface,snail_rect)


        # player movement 
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # game over state- if player touches enemy 
        if snail_rect.colliderect(player_rect):
            game_active = False
    # else:
    #     screen.fill('grey')

    blit_all_tiles(window = pygame.display.set_mode((1280, 720)),tmxdata = load_pygame("C:/Users/arush/OneDrive/Documents/GVSU/Fall 22/641/Github 641/GVSU-CIS641_NostalgiaDevelopment/src/code/tutorial/level_0.tmx"),world_offset =[0,0])


    pygame.display.update()
    clock.tick(fps)

