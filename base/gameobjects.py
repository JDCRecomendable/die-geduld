"""
Class Definition for Game Objects
Copyright (c) 2018 Jared Daniel Carbonell Recomendable. All rights reserved.

Licensed under the GNU General Public License (GPL) Version 3.
"""

from pygame.rect import Rect

class GameObject:
    """Base class for defining in-game objects in Die Geduld."""
    def __init__(self, name, x, y, width, height):
        """Initialise the base GameObject, based on a Rectangle object from
        Pygame bearing the boundaries of the initialised GameObject.

        All Parameters:
        name         -- Name of object, useful for identification
        x            -- Initial location of object along x-axis (left)
        y            -- Initial location of object along y-axis (top)
        width        -- Initial width of object
        height       -- Initial height of object
        """
        self.nametag = name
        self.bounds = Rect(x, y, width, height)

    def name(self, flag=None):
        """Return the name of the moving object. If a parameter is inserted, set
        the variable to the inserted parameter.
        """
        if flag == None: return self.nametag
        self.nametag = flag

    def x(self, flag=None):
        """Return the position of the moving object along the x-axis (pixels).
        If a parameter is inserted, set the variable to the inserted parameter.
        To avoid errors, the parameter type should be an integer.
        """
        if flag == None: return self.bounds.x
        self.bounds.x = flag

    def y(self, flag=None):
        """Return the position of the moving object along the y-axis (pixels).
        If a parameter is inserted, set the variable to the inserted parameter.
        To avoid errors, the parameter type should be an integer.
        """
        if flag == None: return self.bounds.y
        self.bounds.y = flag

    def left(self, flag=None):
        """Return the position of the position of the left-most pixel of the
        object along the x-axis (pixels). If a parameter is inserted, set the
        variable to the inserted parameter.
        To avoid errors, the parameter type should be an integer.
        """
        if flag == None: return self.bounds.left
        self.bounds.left = flag

    def right(self, flag=None):
        """Return the position of the position of the right-most pixel of the
        object along the x-axis (pixels). If a parameter is inserted, set the
        variable to the inserted parameter.
        To avoid errors, the parameter type should be an integer.
        """
        if flag == None: return self.bounds.right
        self.bounds.right = flag

    def top(self, flag=None):
        """Return the position of the position of the upper-most pixel of the
        object along the y-axis (pixels). If a parameter is inserted, set the
        variable to the inserted parameter.
        To avoid errors, the parameter type should be an integer.
        """
        if flag == None: return self.bounds.top
        self.bounds.top = flag

    def bottom(self, flag=None):
        """Return the position of the position of the lower-most pixel of the
        object along the y-axis (pixels). If a parameter is inserted, set the
        variable to the inserted parameter.
        To avoid errors, the parameter type should be an integer.
        """
        if flag == None: return self.bounds.bottom
        self.bounds.bottom = flag

    def center(self, flag=None):
        """Return the center position of the object along both the x- and y-axis
        in a tuple. If a paramter is inserted, set the variable to the inserted
        parameter.
        To avoid errors, the parameter type should be either a tuple or a list.
        """
        if flag == None: return self.bounds.center
        self.bounds.center = flag

    def centerx(self, flag=None):
        """Return the position of the centre pixel of the object along the
        x-axis (pixels). If a parameter is inserted, set the variable to the
        inserted parameter.
        To avoid errors, the parameter type should be an integer.
        """
        if flag == None: return self.bounds.centerx
        self.bounds.centerx = flag

    def centery(self, flag=None):
        """Return the position of the centre pixel of the object along the
        y-axis (pixels). If a parameter is inserted, set the variable to the
        inserted parameter.
        To avoid errors, the parameter type should be an integer.
        """
        if flag == None: return self.bounds.centery
        self.bounds.centery = flag

    def width(self):
        """Return the width of the object."""
        return self.bounds.width

    def height(self):
        """Return the height of the object."""
        return self.bounds.height

    def is_colliding_with(self, game_object):
        """State if the GameObject is in collision with another GameObject."""
        return self.bounds.colliderect(game_object.bounds)

class EnvironmentObject(GameObject):
    """Subclass for defining stationary objects in Die Geduld.

    This class is inherited from the base class GameObject.
    It expects a single sprite image for drawing the stationary sprite.
    It adds the ability to draw the object's sprite on the screen.
    """
    def __init__(self, name, x, y, width, height, sprite_image=None):
        """Initialise the EnvironmentObject, based on the GameObject, and take
        in a single sprite image for displaying the object (by default, None).

        All Parameters:
        name         -- Name of object, useful for identification
        x            -- Initial location of object along x-axis (left)
        y            -- Initial location of object along y-axis (top)
        width        -- Initial width of object
        height       -- Initial height of object
        sprite_image -- Image depecting the environment object
        """
        super().__init__(name, x, y, width, height)
        self.sprite_image = sprite_image

    def draw(self, surface):
        """Draw the EnvironmentObject on the inputted surface, provided that
        a sprite_image was provided during initialisation.
        """
        if self.sprite_image != None:
            surface.blit(self.sprite_image, (self.x(), self.y()))

class MovingObject(GameObject):
    """Subclass for defining moving objects in Die Geduld.

    This class is inherited from the base class GameObject.
    It expects a series of sprite images for drawing the moving object on the
    screen, as well as settings that define the initial speed and direction of
    the moving object.
    It adds the ability to draw the object on the screen, as well as the ability
    to change the transform position of the object.
    """
    def __init__(self, name, x, y, width, height,
                 default_speed,
                 initial_direction,
                 initial_h_speed=0,
                 initial_v_speed=0,
                 animation_ticks=1,
                 sprite_img_sta_up=None,
                 sprite_img_sta_down=None,
                 sprite_img_sta_left=None,
                 sprite_img_sta_right=None,
                 sprite_img_mov_up=None,
                 sprite_img_mov_down=None,
                 sprite_img_mov_left=None,
                 sprite_img_mov_right=None):
        """Initialise the PlayerObject, based on the GameObject, and take in a
        series of images for displaying the object.

        All Parameters:
        name                 -- Name of object, useful for identification
        x                    -- Initial location of object along x-axis (left)
        y                    -- Initial location of object along y-axis (top)
        width                -- Initial width of object
        height               -- Initial height of object
        default_speed        -- Integer that defines the default speed of object
                                in pixels per game tick/frame
        initial_direction    -- Integer that defines the initial direction to
                                be faced by the object. Useful for drawing.
                                0 - up
                                1 - down
                                2 - left
                                3 - right
        initial_h_speed      -- Integer that defines the initial horizontal
                                velocity of the object (see documentation for
                                move_horizontally method)
        initial_v_speed      -- Integer that defines the initial vertical
                                velocity of the object (see documentation for
                                move_vertically method)
        animation_ticks      -- Integer that defines how often to the number of
                                game ticks to pass before transiting to next
                                image in the sprite animation (by default, 1)
        sprite_img_sta_up    -- Series of images when character is facing
                                upwards and is stationary (by default, None)
        sprite_img_sta_down  -- Series of images when character is facing
                                downwards and is stationary (by default, None)
        sprite_img_sta_left  -- Series of images when character is facing
                                leftwards and is stationary (by default, None)
        sprite_img_sta_right -- Series of images when character is facing
                                rightwards and is stationary (by default, None)
        sprite_img_mov_up    -- Series of images when character is moving
                                upwards (by default, None)
        sprite_img_mov_down  -- Series of images when character is moving
                                downwards (by default, None)
        sprite_img_mov_left  -- Series of images when character is moving
                                leftwards (by default, None)
        sprite_img_mov_right -- Series of images when character is moving
                                rightwards (by default, None)
        """
        super().__init__(name, x, y, width, height)
        self.default_speed = default_speed
        self.h_speed = 0
        self.v_speed = 0
        self.h_to_move = 0
        self.v_to_move = 0
        self.direction = initial_direction
        self.animation_ticks = animation_ticks

        self.sprite_images = []
        self.sprite_images_max_index = []
        self.sprite_images_index = [0] * 8
        self.sprite_images_animation_ticks = [animation_ticks] * 8

        self.sprite_images.append(sprite_img_sta_up)
        self.sprite_images.append(sprite_img_sta_down)
        self.sprite_images.append(sprite_img_sta_left)
        self.sprite_images.append(sprite_img_sta_right)
        self.sprite_images.append(sprite_img_mov_up)
        self.sprite_images.append(sprite_img_mov_down)
        self.sprite_images.append(sprite_img_mov_left)
        self.sprite_images.append(sprite_img_mov_right)

        self.sprite_images_max_index.append(len(sprite_img_sta_up))
        self.sprite_images_max_index.append(len(sprite_img_sta_down))
        self.sprite_images_max_index.append(len(sprite_img_sta_left))
        self.sprite_images_max_index.append(len(sprite_img_sta_right))
        self.sprite_images_max_index.append(len(sprite_img_mov_up))
        self.sprite_images_max_index.append(len(sprite_img_mov_down))
        self.sprite_images_max_index.append(len(sprite_img_mov_left))
        self.sprite_images_max_index.append(len(sprite_img_mov_right))

        self.move_horizontally(initial_h_speed)
        self.move_vertically(initial_v_speed)

    def get_horizontal_speed(self):
        """Return the current horizontal speed of the object. To be used in the
        game mainloop, when updating the object's coordinates.
        """
        return self.h_speed

    def get_vertical_speed(self):
        """Return the current vertical speed of the object. To be used in the
        game mainloop, when updating the object's coordinates.
        """
        return self.v_speed

    def get_direction(self):
        """Return the last direction of movement of the object, an integer.
        0 - up
        1 - down
        2 - left
        3 - right
        """
        return self.direction

    def set_direction(self, direction):
        """Set the last direction of movement of the object, an integer.
        0 - up
        1 - down
        2 - left
        3 - right
        """
        self.direction = direction

    def _detect_direction(self):
        # "Private" Method
        # Return the true direction of the object based on movement, without
        # setting self.direction itself.
        if self.h_speed == self.v_speed: return self.direction
        elif abs(self.v_speed) > abs(self.h_speed):
            if self.v_speed > 0:  return 1
            else:                 return 0
        else:
            if self.h_speed > 0:  return 3
            else:                 return 2

    def is_moving(self):
        """Return True if object is moving else return False."""
        return True if (self.h_speed or self.v_speed) else False

    def move_horizontally(self, flag=0):
        """Move the object horizontally on the screen, based on the inputted
        flag. Also set the direction based on movement.

        All Parameters:
        flag -- {-1, 0, 1}, Define the direction of horizontal movement of the
                object
                -1 -- move leftwards
                0  -- make the object stationary
                1  -- move rightwards
             -- Entering a number lower than -1 will increase the leftward
                speed. Entering a number higher than 1 will increase the
                rightward speed.
        """
        if flag <= -1:   self.direction = 2
        elif flag >= 1:  self.direction = 3

        self.h_speed = flag * self.default_speed

    def move_vertically(self, flag=0):
        """Move the object vertically on the screen, based on the inputted
        flag. Also set the direction based on movement.

        All Parameters:
        flag -- {-1, 0, 1}, Define the direction of vertical movement of the
                object
                -1 -- move upwards
                0  -- make the object stationary
                1  -- move downwards
             -- Entering a number lower than -1 will increase the upward
                speed. Entering a number higher than 1 will increase the
                downward speed.
        """
        if flag <= -1:   self.direction = 0
        elif flag >= 1:  self.direction = 1

        self.v_speed = flag * self.default_speed

    def draw_still(self, surface, moving_sprite, direction_index, frame_index):
        """Draw the object's sprite on the inputtted surface, non-animated. The
        drawing occurs when the desired series of images has been provided
        during initialisation.

        All Parameters:
        surface         -- The surface in which to draw the object's sprite on
        moving_sprite   -- An integer or boolean to indicate if rendering a
                           still from one of the moving sprites is desired
                           0 or False -- get still from non-moving sprite
                           1 or True  -- get still from moving sprite
        direction_index -- An integer to indicate what direction of the object
                           to render for the still image
                           0 -- up
                           1 -- down
                           2 -- left
                           3 -- right
        frame_index     -- An integer to indicate which frame to render for the
                           still image. The first frame is 0, the second frame
                           is 1, the third frame is 2, and so on.
        """
        if moving_sprite == True:   moving_sprite = 1
        if moving_sprite == False:  moving_sprite = 0

        if self.sprite_images[moving_sprite * 4 + direction_index] != None:
            surface.blit(
                self.sprite_images[moving_sprite * 4 +
                direction_index][frame_index],
                (self.x(), self.y())
            )

    def draw_still_direction_automatic(self, surface, moving_sprite,
        frame_index):
        """Draw the object's sprite on the inputtted surface, non-animated. The
        drawing occurs when the desired series of images has been provided
        during initialisation. The direction is automatically set.

        All Parameters:
        surface         -- The surface in which to draw the object's sprite on
        moving_sprite   -- An integer or boolean to indicate if rendering a
                           still from one of the moving sprites is desired
                           0 or False -- get still from non-moving sprite
                           1 or True  -- get still from moving sprite
        frame_index     -- An integer to indicate which frame to render for the
                           still image. The first frame is 0, the second frame
                           is 1, the third frame is 2, and so on.
                        -- To prevent errors, the range of frame_index should be
                           from 0 to the highest frame_index of the sprite
                           series with the least number of frames.
        """
        self.direction = self._detect_direction()
        self.draw_still(surface, moving_sprite, self.direction, frame_index)

    def draw_animated(self, surface, moving_sprite, direction_index):
        """Draw the object's sprite on the inputtted surface, animated. The
        drawing occurs when the desired series of images has been provided
        during initialisation.

        All Parameters:
        surface         -- The surface in which to draw the object's sprite on
        moving_sprite   -- An integer or boolean to indicate if rendering a
                           still from one of the moving sprites is desired
                           0 or False -- get still from non-moving sprite
                           1 or True  -- get still from moving sprite
        direction_index -- An integer to indicate what direction of the object
                           to render for the still image
                           0 -- up
                           1 -- down
                           2 -- left
                           3 -- right
        """
        if moving_sprite == True:   moving_sprite = 1
        if moving_sprite == False:  moving_sprite = 0

        self.sprite_images_animation_ticks[moving_sprite * 4 +
            direction_index] -= 1
        if self.sprite_images_animation_ticks[moving_sprite * 4 +
            direction_index] == 0:
            self.sprite_images_index[moving_sprite * 4 + direction_index] += 1
            if (self.sprite_images_index[moving_sprite * 4 + direction_index] >=
                self.sprite_images_max_index[moving_sprite * 4 +
                    direction_index]):
                self.sprite_images_index[moving_sprite * 4 +
                    direction_index] = 0
            self.sprite_images_animation_ticks[moving_sprite * 4 +
                direction_index] = self.animation_ticks

        index = self.sprite_images_index[moving_sprite * 4 + direction_index]

        if self.sprite_images[moving_sprite * 4 + direction_index] != None:
            surface.blit(
                self.sprite_images[moving_sprite * 4 + direction_index][index],
                (self.x(), self.y())
            )

    def draw_animated_direction_automatic(self, surface, moving_sprite):
        """Draw the object's sprite on the inputtted surface, animated. The
        drawing occurs when the desired series of images has been provided
        during initialisation. The direction is automatically set.

        All Parameters:
        surface         -- The surface in which to draw the object's sprite on
        moving_sprite   -- An integer or boolean to indicate if rendering a
                           still from one of the moving sprites is desired
                           0 or False -- get still from non-moving sprite
                           1 or True  -- get still from moving sprite
        """
        self.direction = self._detect_direction()
        self.draw_animated(surface, moving_sprite, self.direction)

    def draw_automatic(self, surface):
        """Draw the object's sprite on the inputted surface, animated. The
        drawing occurs when the desired series of images has been provided
        during initialisation. The direction of the sprite as well as whether to
        draw from a moving sprite or not is automatically set.
        """
        self.draw_animated_direction_automatic(surface, self.is_moving())
