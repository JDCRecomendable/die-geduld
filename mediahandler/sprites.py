"""
Class Definition for Media Handler Objects
Copyright (c) 2018 Jared Daniel Carbonell Recomendable.

Licensed under the GNU General Public License (GPL) Version 3.
"""

import pygame

# GRAPHICS
class Spritesheet:
    def __init__(self, file_location):
        """Load the spritesheet.

        All Parameters:
        file_location -- Directory location of spritesheet"""
        self.spritesheet = pygame.image.load(file_location).convert()
        self.spritesheet.convert_alpha()

    def get_image(self, x, y, width, height, colourkey=(0, 0, 0, 0)):
        """Grab a particular image from the spritesheet.

        All Parameters:
        x        -- x-coordinate of the image within the spritesheet
        y        -- y-coordinate of the image within the spritesheet
        width    -- Width of the image within the spritesheet
        height   -- Height of the image within the spritesheet
        colourkey -- Colour key for transparency
        """
        # Create new blank image
        self.image = pygame.Surface((width, height)).convert()

        # Copy sprite from spritesheet onto blank image
        self.image.blit(self.spritesheet, (0, 0), (x, y, width, height))

        # Add support for transparency in the image
        self.image.set_colorkey(colourkey)

        return self.image
