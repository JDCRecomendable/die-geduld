"""
Game Handler
Copyright (c) 2018 Jared Daniel Carbonell Recomendable. All rights reserved.

Licensed under the GNU General Public License (GPL) Version 3.
"""

import pygame
import base.levelengine
import mediahandler.sprites
import base.gameobjects
from time import sleep
from base.config import *
from mediahandler.spritesvars import *

class GameControl:
    """Consists of 3 Main Stages:
       1. Initialisation
       2. Running of the Game
       3. Uninitialisation
    """
    def __init__(self):
        """Create a GameControl object and print out information about the
        game.
        """
        print()
        print(TITLE)
        print(VERSION)
        print(COPYRIGHT)
        print()
        print(DESCRIPTION)
        print()

    def display_screen(self, img_location):
        """Display a screen for the game. Expects the file location of an image
        of dimensions 512 pixels by 512 pixels.
        """
        to_display = pygame.image.load(img_location).convert()
        to_display.convert_alpha()
        self.display.blit(to_display, (0, 0))
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        running = False
                    if event.key in (pygame.K_BREAK,
                                     pygame.K_ESCAPE,
                                     pygame.K_PAUSE):
                        return -1
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        if event.key in (pygame.K_q,):
                            return -1

    # Stage 1: Initialisation
    ## General Initialisation
    def initialise_all(self):
        """Initialise all necessary Pygame modules and resources for the
        game.
        """
        self.initialise_pygame()
        self.initialise_display()
        self.initialise_sounds()

    def initialise_pygame(self):
        """Initialise Pygame standard modules to prepare for the game."""
        pygame.init()
        self.clock = pygame.time.Clock()

    def initialise_display(self):
        """Initialise Pygame display modules and sprites to prepare for the
        game.
        """
        pygame.display.set_caption(WIN_TITLE)
        if WIN_START_FULLSCREEN:
            self.display = pygame.display.set_mode(WIN_SIZE, pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode(WIN_SIZE)
        self.sprites_handler = mediahandler.sprites.Spritesheet(LOC_SPRITESHEET)

        # Specific to the Game
        pygame.mouse.set_visible(False)
        environment_sprites = self.initialise_environment_sprites()
        player_sprites = self.initialise_player_sprites()
        monster_sprites = self.initialise_monster_sprites()
        self.all_sprites = (
            environment_sprites,
            player_sprites,
            monster_sprites
        )

    def initialise_sounds(self):
        """Initialise Pygame sound modules, music and sound effects to prepare
        for the game.
        """
        pygame.mixer.pre_init(frequency=SND_FREQUENCY,
                              size=SND_SIZE,
                              channels=SND_CHANNELS,
                              buffer=SND_BUFFER)
        pygame.mixer.init()

        # Specific to the Game
        self.all_sfx = self.initialise_game_sounds()

    ## Specific Initialisation
    ### Specific to Display
    def initialise_environment_sprites(self):
        """Create and return environment_sprites consisting a wall_sprite,
        a floor_gen_sprite, a floor_src_sprite and a floor_des_sprite.
        """
        wall_sprite = self.sprites_handler.get_image(
            *SPR_WALL,
            SPR_GLOBAL_WIDTH,
            SPR_GLOBAL_HEIGHT,
            COL_TRANSPARENT
        )
        floor_gen_sprite = self.sprites_handler.get_image(
            *SPR_FLOOR_GEN,
            SPR_GLOBAL_WIDTH,
            SPR_GLOBAL_HEIGHT,
            COL_TRANSPARENT
        )
        floor_src_sprite = self.sprites_handler.get_image(
            *SPR_FLOOR_SRC,
            SPR_GLOBAL_WIDTH,
            SPR_GLOBAL_HEIGHT,
            COL_TRANSPARENT
        )
        floor_des_sprite = self.sprites_handler.get_image(
            *SPR_FLOOR_DES,
            SPR_GLOBAL_WIDTH,
            SPR_GLOBAL_HEIGHT,
            COL_TRANSPARENT
        )
        environment_sprites = (
            wall_sprite,
            floor_gen_sprite,
            floor_src_sprite,
            floor_des_sprite
        )
        return environment_sprites

    def initialise_player_sprites(self):
        """Create and return the player_sprites."""
        player_sprites = []
        for image_series in SPR_PLAYER_IMAGES:
            temp = []
            for image in image_series:
                temp.append(self.sprites_handler.get_image(
                    *image,
                    SPR_GLOBAL_WIDTH,
                    SPR_GLOBAL_HEIGHT,
                    COL_TRANSPARENT
                ))
            player_sprites.append(temp)
        return player_sprites

    def initialise_monster_sprites(self):
        """Create and return the monster_sprites."""
        monster_sprites = []
        for image_series in SPR_MONSTER_IMAGES:
            temp = []
            for image in image_series:
                temp.append(self.sprites_handler.get_image(
                    *image,
                    SPR_GLOBAL_WIDTH,
                    SPR_GLOBAL_HEIGHT,
                    COL_TRANSPARENT
                ))
            monster_sprites.append(temp)
        return monster_sprites

    ### Specific to Sounds
    def initialise_game_sounds(self):
        """Create and return sfx_bomb and sfx_finish."""
        sfx_bomb = pygame.mixer.Sound(LOC_SFX_BOMB)
        sfx_finish = pygame.mixer.Sound(LOC_SFX_FINISH)
        pygame.mixer.music.load(LOC_MUSIC)
        pygame.mixer.music.play()
        return sfx_bomb, sfx_finish

    # Stage 2: Running of the Game (based on Game class)
    def run(self, level, mute_status=False, show_instructions=False):
        """Run the game, based on the level input."""
        game = Game(
            self.clock,
            self.display,
            self.all_sprites,
            self.all_sfx,
            level,
            mute_status
        )
        r = game.mainloop()
        return r

    # Stage 3: Uninitialisation
    def uninitialise_all(self):
        """Uninitialise Pygame after the game before ending off."""
        pygame.mixer.fadeout(800)
        pygame.mixer.music.fadeout(800)
        sleep(1)
        pygame.mouse.set_visible(True)
        pygame.mixer.stop()
        pygame.mixer.quit()
        pygame.quit()

class Game:
    """Handles each level in the game."""
    def __init__(self, clock, display, sprites, sounds, level, mute_status):
        """Initialise before the running the game.

        All Parameters:
        clock       -- Pygame Clock object
        display     -- Pygame Surface object
        sprites     -- Sprites for the game in the following order:
                       1. Environment Sprites
                          a. Wall
                          b. Generic Floor
                          c. Source Floor (Starting Position)
                          d. Destination Floor
                       2. Player Sprites
                       3. Monster Sprites
        sounds      -- Sound effects for the game in the following order:
                       1. Monster hits player
                       2. Player reaches destination floor
        level       -- Configuration for level
        mute_status -- Initialising factor to determine whether to launch the
                       game muted or not
        """
        self.mainclock = clock
        self.mainsurface = display
        self.environment_sprites = sprites[0]
        self.player_sprites = sprites[1]
        self.monster_sprites = sprites[2]
        self.sfx_bomb = sounds[0]
        self.sfx_finish = sounds[1]
        self.level = level
        self.is_mute = mute_status
        self.is_finished = False
        self.move_state = -1

        # Setup Environment
        self.environment = base.levelengine.LevelUtility(
            *self.environment_sprites,
            SPR_GLOBAL_WIDTH,
            SPR_GLOBAL_HEIGHT
        )
        self.environment.setup_level_layout(self.level.LEVEL)

        # Setup Player
        self.player = base.gameobjects.MovingObject(
            "player",
            self.level.PLAYER_INITIAL_X * SPR_GLOBAL_WIDTH,
            self.level.PLAYER_INITIAL_Y * SPR_GLOBAL_HEIGHT,
            SPR_GLOBAL_WIDTH,
            SPR_GLOBAL_HEIGHT,
            PLAYER_DEF_SPEED,
            self.level.PLAYER_INITIAL_DIRECTION,
            0,
            0,
            ANIMATION_TICKS,
            *self.player_sprites
        )

        # Setup Monsters
        monsters = base.levelengine.MovingObjectUtility(
            self.monster_sprites,
            SPR_GLOBAL_WIDTH,
            SPR_GLOBAL_HEIGHT,
            MONSTER_DEF_SPEED,
            ANIMATION_TICKS,
            SPR_GLOBAL_WIDTH,
            SPR_GLOBAL_HEIGHT
        )
        monsters.setup_movingobjects(self.level.MONSTERS_HORIZONTAL,
                                     self.level.MONSTERS_VERTICAL)
        self.hmonsters = monsters.get_hmovingobjects()
        self.vmonsters = monsters.get_vmovingobjects()

    # Standard Main Loop Function
    def mainloop(self):
        """Define the mainloop in which the program will run on.
        This method has to be called so that the program runs the mainloop.

        The idea of the mainloop is as follows:
        1. Handle user input and game events
        2. Update the objects on the screen, and quit if desired by the user
           before screen rendition
        3. Render the screen once updated and set the clock forward
        4. Control music and sounds
        """
        running = True
        while running:
            # [1] Handle user input and game events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.end_mainloop(-1)
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_m,):
                        if self.is_mute:
                            self.is_mute = False
                        else:
                            self.is_mute = True
                    if event.key in (pygame.K_r,):
                        self.reset_player_position()
                    if event.key in (pygame.K_w, pygame.K_UP, pygame.K_KP8,
                                     pygame.K_s, pygame.K_DOWN, pygame.K_KP2,
                                     pygame.K_a, pygame.K_LEFT, pygame.K_KP4,
                                     pygame.K_d, pygame.K_RIGHT, pygame.K_KP6):
                        self.player_handle_movement_intent(event)
                    if event.key in (pygame.K_BREAK,
                                     pygame.K_ESCAPE,
                                     pygame.K_PAUSE):
                        return self.end_mainloop(-1)
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        if event.key in (pygame.K_q,):
                            return self.end_mainloop(-1)
                if event.type == pygame.KEYUP:
                    self.move_state = -1

            # [2] Update the objects on the screen and quit if desired by the
            # user before screen rendition
            self.environment.draw_all(self.mainsurface)

            self.player_movement()

            self.player_wall_collision()
            self.player.x(self.player.x() + self.player.get_horizontal_speed())
            self.player.y(self.player.y() + self.player.get_vertical_speed())
            self.player_edge_collision()
            self.player_floor_des_collision()
            self.player.draw_automatic(self.mainsurface)

            for monster in self.hmonsters:
                monster.x(monster.x() + monster.get_horizontal_speed())

            for monster in self.vmonsters:
                monster.y(monster.y() + monster.get_vertical_speed())

            for monster in (self.hmonsters + self.vmonsters):
                self.monster_wall_collision(monster)
                self.monster_edge_collision(monster)
                self.player_monster_collision(monster)
                monster.draw_automatic(self.mainsurface)

            if self.is_finished:
                return self.end_mainloop(0)

            # [3] Render the screen once updated and set the clock forward
            pygame.display.flip()
            self.mainclock.tick(WIN_FRAMERATE)

            # [4] Control music and sounds
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()

            if not self.is_mute:
                self.set_sfx_volume(SND_VOL_SFX)
                if pygame.mixer.get_busy():
                    self.set_music_volume(SND_VOL_MUSIC / 2)
                else:
                    self.set_music_volume(SND_VOL_MUSIC)
            elif self.is_mute:
                self.set_sfx_volume(0)
                self.set_music_volume(0)

    # Game-Specific Main Loop Function(s)
    def reset_player_position(self):
        """Reset the position of the player to the starting point."""
        self.player.x(self.level.PLAYER_INITIAL_X * SPR_GLOBAL_WIDTH)
        self.player.y(self.level.PLAYER_INITIAL_Y * SPR_GLOBAL_HEIGHT)

    def set_sfx_volume(self, value):
        """Set the volume of all sound effects to the input value."""
        self.sfx_bomb.set_volume(value)
        self.sfx_finish.set_volume(value)

    def set_music_volume(self, value):
        pygame.mixer.music.set_volume(value)

    def player_handle_movement_intent(self, event):
        """Input handler in mainloop for controlling player movement."""
        for floor_gen in self.environment.get_floor_gen():
            if self.player.is_colliding_with(floor_gen):
                if (abs(self.player.centerx() -
                        floor_gen.centerx()) <= 4 and
                    abs(self.player.centery() -
                        floor_gen.centery()) <= 4):
                    self.player.center(floor_gen.center())
            if event.key in (pygame.K_w, pygame.K_UP, pygame.K_KP8):
                self.move_state = 0
            if event.key in (pygame.K_s, pygame.K_DOWN, pygame.K_KP2):
                self.move_state = 1
            if event.key in (pygame.K_a, pygame.K_LEFT, pygame.K_KP4):
                self.move_state = 2
            if event.key in (pygame.K_d, pygame.K_RIGHT, pygame.K_KP6):
                self.move_state = 3

    def player_movement(self):
        """Update the position of the player on the screen for movement."""
        if self.move_state == -1:
                if self.player.x() % 32 == 0 and self.player.y() % 32 == 0:
                    self.player.move_horizontally(0)
                    self.player.move_vertically(0)
        elif self.move_state == 0:
            self.player.move_vertically(-1)
        elif self.move_state == 1:
            self.player.move_vertically(1)
        elif self.move_state == 2:
            self.player.move_horizontally(-1)
        elif self.move_state == 3:
            self.player.move_horizontally(1)

    def player_wall_collision(self):
        """Correct the player movement update on the screen such that the player
        does not move when colliding with the walls in the level.
        """
        for wall in self.environment.get_walls():
            ### Wall Above
            if self.player.top() == wall.bottom():
                if wall.left() < self.player.left() < wall.right():
                    if self.player.get_vertical_speed() < 0:
                        self.player.move_vertically(0)

                if wall.left() < self.player.centerx() < wall.right():
                    if self.player.get_vertical_speed() < 0:
                        self.player.move_vertically(0)

                if wall.left() < self.player.right() < wall.right():
                    if self.player.get_vertical_speed() < 0:
                        self.player.move_vertically(0)

            ### Wall Below
            if self.player.bottom() == wall.top():
                if wall.left() < self.player.left() < wall.right():
                    if self.player.get_vertical_speed() > 0:
                        self.player.move_vertically(0)

                if wall.left() < self.player.centerx() < wall.right():
                    if self.player.get_vertical_speed() > 0:
                        self.player.move_vertically(0)

                if wall.left() < self.player.right() < wall.right():
                    if self.player.get_vertical_speed() > 0:
                        self.player.move_vertically(0)

            ### Wall to the Left
            if self.player.left() == wall.right():
                if wall.top() < self.player.top() < wall.bottom():
                    if self.player.get_horizontal_speed() < 0:
                        self.player.move_horizontally(0)

                if wall.top() < self.player.centery() < wall.bottom():
                    if self.player.get_horizontal_speed() < 0:
                        self.player.move_horizontally(0)

                if wall.top() < self.player.bottom() < wall.bottom():
                    if self.player.get_horizontal_speed() < 0:
                        self.player.move_horizontally(0)

            ### Wall to the Right
            if self.player.right() == wall.left():
                if wall.top() < self.player.top() < wall.bottom():
                    if self.player.get_horizontal_speed() > 0:
                        self.player.move_horizontally(0)

                if wall.top() < self.player.centery() < wall.bottom():
                    if self.player.get_horizontal_speed() > 0:
                        self.player.move_horizontally(0)

                if wall.top() < self.player.bottom() < wall.bottom():
                    if self.player.get_horizontal_speed() > 0:
                        self.player.move_horizontally(0)

            ### Wall to the Top-Left
            if (self.player.left() == wall.right() and
                  self.player.top() == wall.bottom()):
                if (self.player.get_horizontal_speed() < 0 and
                    self.player.get_vertical_speed() < 0):
                    self.player.move_horizontally(0)
                    self.player.move_vertically(0)

            ### Wall to the Top-Right
            if (self.player.right() == wall.left() and
                  self.player.top() == wall.bottom()):
                if (self.player.get_horizontal_speed() > 0 and
                    self.player.get_vertical_speed() < 0):
                    self.player.move_horizontally(0)
                    self.player.move_vertically(0)

            ### Wall to the Bottom-Left
            if (self.player.left() == wall.right() and
                  self.player.bottom() == wall.top()):
                if (self.player.get_horizontal_speed() < 0 and
                    self.player.get_vertical_speed() > 0):
                    self.player.move_horizontally(0)
                    self.player.move_vertically(0)

            ### Wall to the Bottom-Right
            if (self.player.right() == wall.left() and
                  self.player.bottom() == wall.top()):
                if (self.player.get_horizontal_speed() > 0 and
                    self.player.get_vertical_speed() > 0):
                    self.player.move_horizontally(0)
                    self.player.move_vertically(0)

    def player_monster_collision(self, monster):
        """Bring the player to the starting position if the player hits one of
        the monsters.
        """
        if self.player.is_colliding_with(monster):
            if not pygame.mixer.get_busy():
                self.sfx_bomb.play()
            self.reset_player_position()

    def player_edge_collision(self):
        """Correct the player movement update on the screen such that the player
        does not move when colliding with the edges in the level.
        """
        if self.player.top() <= 0:
            self.player.top(0)
            self.player.move_vertically(0)
        if self.player.bottom() >= WIN_SIZE[1]:
            self.player.bottom(WIN_SIZE[1])
            self.player.move_vertically(0)
        if self.player.left() <= 0:
            self.player.left(0)
            self.player.move_horizontally(0)
        if self.player.right() >= WIN_SIZE[0]:
            self.player.right(WIN_SIZE[0])
            self.player.move_horizontally(0)

    def player_floor_des_collision(self):
        for floor_des in self.environment.floor_des:
            if (self.player.is_colliding_with(floor_des) and
                not self.is_finished):
                self.sfx_finish.play()
                self.is_finished = True

    def monster_wall_collision(self, monster):
        for wall in self.environment.walls:
            if monster.is_colliding_with(wall):
                if monster.get_vertical_speed() < 0:
                    monster.move_vertically(MONSTER_DEF_SPEED)
                elif monster.get_vertical_speed() > 0:
                    monster.move_vertically(-1 * MONSTER_DEF_SPEED)
                if monster.get_horizontal_speed() < 0:
                    monster.move_horizontally(MONSTER_DEF_SPEED)
                elif monster.get_horizontal_speed() > 0:
                    monster.move_horizontally(-1 * MONSTER_DEF_SPEED)

    def monster_edge_collision(self, monster):
        """Correct the monster movement update on the screen such that the
        monster does not move when colliding with the edges in the level.
        """
        if monster.top() <= 0:
            monster.top(0)
            monster.move_vertically(MONSTER_DEF_SPEED)
        if monster.bottom() >= WIN_SIZE[1]:
            monster.bottom(WIN_SIZE[1])
            monster.move_vertically(-1 * MONSTER_DEF_SPEED)
        if monster.left() <= 0:
            monster.left(0)
            monster.move_horizontally(MONSTER_DEF_SPEED)
        if monster.right() >= WIN_SIZE[0]:
            monster.right(WIN_SIZE[0])
            monster.move_horizontally(-1 * MONSTER_DEF_SPEED)

    def end_mainloop(self, status=0):
        """Exit from the mainloop.

        All Parameters:
        status -- Status to return when exiting.
                  -1 - Quit the game
                  0  - Go to the next level (or quit the game if at last level)
        """
        return status, self.is_mute
