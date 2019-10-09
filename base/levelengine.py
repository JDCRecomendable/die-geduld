"""
Script that Places GameObjects in the Level
Copyright (c) 2018 Jared Daniel Carbonell Recomendable.

Licensed under the GNU General Public License (GPL) Version 3.
"""

import base.gameobjects

class LevelUtility:
    """Aid in creating and drawing EnvironmentObjects in the level.
    Closely tied to base.gameobjects.EnvironmentObject class.
    """
    def __init__(
            self,
            wall_sprite,
            floor_gen_sprite,
            floor_src_sprite,
            floor_des_sprite,
            x_grid=1,
            y_grid=1
        ):
        """Initialise the LevelUtility object, the sprites for display, and the
        grid in the map, if any. This is suited for setting up
        EnvironmentObjects in the level.

        All Parameters:
        wall_sprite      -- Sprite of wall for drawing the wall sprites
        floor_gen_sprite -- Sprite of floor for drawing the floor sprites
        floor_src_sprite -- Sprite of floor_src for drawing the floor_src
                            sprites
        floor_des_sprite -- Sprite of floor_des for drawing the floor_des
                            sprites
        x_grid           -- Number of pixels per grid along the x-axis, to be
                            used when spawning the EnvironmentObjects with the
                            coordinates given
        y_grid           -- Number of pixels per grid along the y-axis, to be
                            used when spawning the EnvironmentObjects with the
                            coordinates given
        """
        self.walls = None
        self.floor_gen = None
        self.floor_src = None
        self.floor_des = None
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.wall_sprite = wall_sprite
        self.floor_gen_sprite = floor_gen_sprite
        self.floor_src_sprite = floor_src_sprite
        self.floor_des_sprite = floor_des_sprite

    def setup_level_layout(self, level_layout):
        """Set up the level layout.

        All Parameters:
        level_layout -- Tuple of strings that bear characters for placing the
                        GameObjects on the level
                     -- W - Wall
                        F - Floor, Generic
                        S - Floor, Starting Position/Source
                        D - Floor, Destination
        """
        self.walls = []
        self.floor_gen = []
        self.floor_src = []
        self.floor_des = []
        for y in range(len(level_layout)):
            for x in range(len(level_layout)):
                if level_layout[y][x] == 'W':
                    self.walls.append(base.gameobjects.EnvironmentObject(
                        "wall",
                        self.x_grid * x,
                        self.y_grid * y,
                        self.x_grid,
                        self.y_grid,
                        self.wall_sprite
                    ))
                elif level_layout[y][x] == 'F':
                    self.floor_gen.append(base.gameobjects.EnvironmentObject(
                        "floor_gen",
                        self.x_grid * x,
                        self.y_grid * y,
                        self.x_grid,
                        self.y_grid,
                        self.floor_gen_sprite
                    ))
                elif level_layout[y][x] == 'S':
                    self.floor_src.append(base.gameobjects.EnvironmentObject(
                        "floor_src",
                        self.x_grid * x,
                        self.y_grid * y,
                        self.x_grid,
                        self.y_grid,
                        self.floor_src_sprite
                    ))
                elif level_layout[y][x] == 'D':
                    self.floor_des.append(base.gameobjects.EnvironmentObject(
                        "floor_des",
                        self.x_grid * x,
                        self.y_grid * y,
                        self.x_grid,
                        self.y_grid,
                        self.floor_des_sprite
                    ))

    def get_walls(self):
        """Return a list of all the walls in the level."""
        return self.walls

    def get_floor_gen(self):
        """Return a list of all the generic floor tiles in the level."""
        return self.floor_gen

    def get_floor_src(self):
        """Return a list of all the source/starting position floor tiles in the
        level.
        """
        return self.floor_src

    def get_floor_des(self):
        """Return a list of all the destination floor tiles in the level."""
        return self.floor_des

    def draw_walls(self, surface):
        """Draw the walls on the inputted surface."""
        if self.walls == None: return None
        for wall in self.walls:
            wall.draw(surface)

    def draw_floor_gen(self, surface):
        """Draw the floor on the inputted surface."""
        if self.floor_gen == None: return None
        for floor_gen in self.floor_gen:
            floor_gen.draw(surface)

    def draw_floor_src(self, surface):
        """Draw the floor_src on the inputted surface. floor_src refers to the
        floor highlighted as the beginning position for the player in the game.
        """
        if self.floor_src == None: return None
        for floor_src in self.floor_src:
            floor_src.draw(surface)

    def draw_floor_des(self, surface):
        """Draw the floor_des on the inputted surface. floor_des refers to the
        floor highlighted as the destination position that the player in the
        game should aim to reach.
        """
        if self.floor_des == None: return None
        for floor_des in self.floor_des:
            floor_des.draw(surface)

    def draw_all(self, surface):
        """Draw all environment objects on the inputted surface."""
        self.draw_floor_gen(surface)
        self.draw_floor_src(surface)
        self.draw_floor_des(surface)
        self.draw_walls(surface)

class MovingObjectUtility:
    """Aid in creating moving objects for the level.
    Closely tied to base.gameobjects.MovingObject class.
    """
    def __init__(
            self,
            movingobject_sprites,
            movingobject_width,
            movingobject_height,
            movingobject_speed=1,
            animation_ticks=1,
            x_grid=1,
            y_grid=1
        ):
        """Initialise the MovingObjectUtility object, the sprites for display,
        the speed at which the objects move, the number of game ticks to pass
        before the object changes its sprite during movement, and the grid in
        the map for spawning objects at certain locations, if any.

        All Parameters:
        sprites             -- Series of sprites of the objects in the
                               following order:
                               1. Looking upwards, stationary
                               2. Looking downwards, stationary
                               3. Looking leftwards, stationary
                               4. Looking rightwards, stationary
                               5. Looking upwards, moving
                               6. Looking downwards, moving
                               7. Looking leftwards, moving
                               8. Looking rightwards, moving
        movingobject_speed -- The default speed for the objects when moving
                               about the level (by default, 1)
        animation_ticks     -- Integer that defines how often to the number of
                               game ticks to pass before transiting to next
                               sprite in the sprite animation (by default, 1)
        width               -- Width of the objects for this MovingObjectUtility
                               object in pixels
        height              -- Height of the objects for this
                               MovingObjectUtility object in pixels
        x_grid              -- Number of pixels per grid along the x-axis, to be
                               used when spawning the MovingObjects with the
                               coordinates given (by default, 1)
        y_grid              -- Number of pixels per grid along the y-axis, to be
                               used when spawning the MovingObjects with the
                               coordinates given (by default, 1)
        """
        self.hmovingobjects = None
        self.vmovingobjects = None
        self.movingobject_speed = movingobject_speed
        self.animation_ticks = animation_ticks
        self.movingobject_width = movingobject_width
        self.movingobject_height = movingobject_height
        self.movingobject_sprites = movingobject_sprites
        self.x_grid = x_grid
        self.y_grid = y_grid

    def setup_movingobjects(self, hobjects, vobjects):
        """Create the moving objects.

        All Parameters:
        hobjects  -- Tuple of tuples, each containing the grid position in the
                     map where the horizontally-moving object will spawn as
                     well as the initial direction that the object will face
                     during initialisation
                  -- Three elements in each tuple:
                     1st - x-coordinate within the grid where the object will
                           spawn
                     2nd - y-coordinate within the grid where the object will
                           spawn
                     3rd - Initial direction where object is facing--2 for
                           leftwards, 3 for rightwards
        vobjects  -- Tuple of tuples, each containing the grid position in the
                     map where the vertically-moving object will spawn as well
                     as the initial direction that the object will face during
                     initialisation
                  -- Three elements in each tuple:
                     1st - x-coordinate within the grid where the object will
                           spawn
                     2nd - y-coordinate within the grid where the object will
                           spawn
                     3rd - Initial direction where object is facing--0 for
                           upwards, 1 for downwards
        """
        self.hmovingobjects = []
        for specs in hobjects:
            if specs == None:
                continue
            if specs[2] == 2:
                speed = -1 * self.movingobject_speed
            elif specs[2] == 3:
                speed = self.movingobject_speed
            self.hmovingobjects.append(base.gameobjects.MovingObject(
                "hobject",
                specs[0] * self.x_grid,
                specs[1] * self.y_grid,
                self.movingobject_width,
                self.movingobject_height,
                self.movingobject_speed,
                specs[2],
                speed,
                0,
                self.animation_ticks,
                *self.movingobject_sprites
            ))

        self.vmovingobjects = []
        for specs in vobjects:
            if specs == None:
                continue
            if specs[2] == 0:
                speed = -1 * self.movingobject_speed
            elif specs[2] == 1:
                speed = self.movingobject_speed
            self.vmovingobjects.append(base.gameobjects.MovingObject(
                "vobject",
                specs[0] * self.x_grid,
                specs[1] * self.y_grid,
                self.movingobject_width,
                self.movingobject_height,
                self.movingobject_speed,
                specs[2],
                0,
                speed,
                self.animation_ticks,
                *self.movingobject_sprites
            ))

    def get_hmovingobjects(self):
        """Return a list of all horizontally-moving objects in the level."""
        return self.hmovingobjects

    def get_vmovingobjects(self):
        """Return a list of all vertically-moving objects in the level."""
        return self.vmovingobjects

    def get_all_movingobjects(self):
        """Return a list of all moving objects in the level."""
        return self.hmovingobjects + self.vmovingobjects
