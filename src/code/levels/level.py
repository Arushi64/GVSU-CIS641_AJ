import pygame
from support import import_csv_layout, import_cut_graphic
from settings import tile_size, screen_height, screen_width
from tiles import Tile, StaticTile, Crate, Coin, Palm
from enemy import Enemy
from decoration import Sky, Water, Clouds
from player import Player
from game_data import levels
from particle import ParticleEffect

class Level:
    def __init__(self, current_level, surface, create_overworld, change_coins, change_health):
        # general setup
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = None

        #audio 
        self.coin_sound = pygame.mixer.Sound(r'src/code/levels/audio/effects/coin.wav')
        self.stomp_sound = pygame.mixer.Sound(r'src/code/levels/audio/effects/stomp.wav')

        # overworld connection
        self.create_overworld = create_overworld
        self.current_level = current_level
        level_data = levels[self.current_level]
        self.new_max_level = level_data['unlock']


        # player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout, change_health)

        # user interface
        self.change_coins = change_coins

        # explosion particles
        self.explosion_sprites = pygame.sprite.Group()

        # terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        # crates
        crate_layout = import_csv_layout(level_data['crates'])
        self.crate_sprites = self.create_tile_group(crate_layout, 'crates')

        # coins
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprites = self.create_tile_group(coin_layout, 'coins')

        # foreground palms
        fg_palm_layout = import_csv_layout(level_data['fg palms'])
        self.fg_palm_sprites = self.create_tile_group(fg_palm_layout, 'fg palms')

        # background palms
        bg_palm_layout = import_csv_layout(level_data['bg palms'])
        self.bg_palm_sprites = self.create_tile_group(bg_palm_layout, 'bg palms')

        # enemy
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')

        # constraint
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout, 'constraints')

        # decoration
        self.sky = Sky(8)
        level_width = len(terrain_layout[0]) * tile_size
        self.water = Water(screen_height - 60, level_width)
        self.clouds = Clouds(400, level_width, 25)



    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphic('src/code/levels/graphics/terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)


                    if type == 'crates':
                        sprite = Crate(tile_size, x, y)
                        sprite_group.add(sprite)


                    if type == 'coins':
                        sprite = Coin(tile_size, x, y, 'src/code/levels/graphics/coins/gold', 1)
                        sprite_group.add(sprite)


                    if type == 'fg palms':
                        if val == '0': 
                            sprite = Palm(tile_size, x, y, 'src/code/levels/graphics/terrain/palm_small', 38)
                            sprite_group.add(sprite)

                        if val == '1': 
                            sprite = Palm(tile_size, x, y, 'src/code/levels/graphics/terrain/palm_large', 64)
                            sprite_group.add(sprite)

                    if type == 'bg palms':
                        sprite = Palm(tile_size, x, y, 'src/code/levels/graphics/terrain/palm_bg', 64)
                        sprite_group.add(sprite)


                    if type == 'enemies':
                        sprite = Enemy(tile_size, x, y)
                        sprite_group.add(sprite)


                    if type == 'constraints':
                        sprite = Tile(tile_size, x, y)
                        sprite_group.add(sprite)


        return sprite_group
    
    def player_setup(self, layout, change_health):
            for row_index, row in enumerate(layout):
                for col_index, val in enumerate(row):
                    x = col_index * tile_size
                    y = row_index * tile_size
                    if val == '0':
                        sprite = Player((x, y), change_health)
                        self.player.add(sprite)
                    if val == '1':
                        hat_surface = pygame.image.load('src/code/levels/graphics/overworld/peach.png').convert_alpha()
                        sprite = StaticTile(tile_size, x, y, hat_surface)
                        self.goal.add(sprite)

    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        collidable_sprites = self.terrain_sprites.sprites() + self.crate_sprites.sprites() + self.fg_palm_sprites.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
            
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right < self.current_x or player.direction.x <= 0):
            player.on_right = False



    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites = self.terrain_sprites.sprites() + self.crate_sprites.sprites() + self.fg_palm_sprites.sprites()


        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
				
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def check_death(self):
        if self.player.sprite.rect.top > screen_height:
            self.create_overworld(self.current_level, 0)
    
    def check_win(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.goal, False):
            self.create_overworld(self.current_level, self.new_max_level)

    def check_coin_collisions(self):
        collided_coins = pygame.sprite.spritecollide(self.player.sprite, self.coin_sprites, True)
        if collided_coins:
            self.coin_sound.play()
            for coin in collided_coins:
                self.change_coins(coin.value)

    def check_enemy_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player.sprite, self.enemy_sprites, False)

        if enemy_collisions:
            for enemy in enemy_collisions:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                player_bottom = self.player.sprite.rect.bottom
                if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y >= 0:
                    self.stomp_sound.play()
                    self.player.sprite.direction.y = -15
                    explosion_sprite = ParticleEffect(enemy.rect.center, 'explosion')
                    self.explosion_sprites.add(explosion_sprite)
                    enemy.kill()
                else:
                    self.player.sprite.get_damage()

    def run(self):
        # run the entire game / level

        # sky
        self.sky.draw(self.display_surface)
        self.clouds.draw(self.display_surface, self.world_shift)

        # background palms
        self.bg_palm_sprites.update(self.world_shift)
        self.bg_palm_sprites.draw(self.display_surface)

        # terrain
        self.terrain_sprites.update(self.world_shift)  
        self.terrain_sprites.draw(self.display_surface)

        # enemy
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy_sprites.draw(self.display_surface)
        self.explosion_sprites.update(self.world_shift)
        self.explosion_sprites.draw(self.display_surface)

        # crate
        self.crate_sprites.update(self.world_shift)
        self.crate_sprites.draw(self.display_surface)

        # foreground palms
        self.fg_palm_sprites.update(self.world_shift)
        self.fg_palm_sprites.draw(self.display_surface)

        # coins
        #self.coin_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)
        self.coin_sprites.update(self.world_shift)

        # player sprites
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.scroll_x()

        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

        self.check_death()
        self.check_win()

        self.check_coin_collisions()
        self.check_enemy_collisions()

        # water
        self.water.draw(self.display_surface, self.world_shift)

