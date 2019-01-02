"""
Configuration for Game
Copyright (c) 2018 Jared Daniel Carbonell Recomendable. All rights reserved.

Licensed under the GNU General Public License (GPL) Version 3.
"""

import os

# METADATA
TITLE                  = "Die Geduld"
AUTHOR                 = "Jared Daniel Carbonell Recomendable"
AUTHOR_INITIALS        = "JDCR"
VERSION                = "1.2b"
COPYRIGHT              = "Copyright (c) 2018 Jared Daniel Carbonell \
Recomendable. All rights reserved."
YEAR                   = "2018"
DESCRIPTION            = "Die Geduld is patience in German, and the game is \
named as such because it requires good hand-eye coordination and a good deal \
of patience in order to complete."

# WINDOW SETTINGS
WIN_TITLE              = TITLE
WIN_SIZE               = (512, 512)
WIN_FRAMERATE          = 60
WIN_START_FULLSCREEN   = True

# SYSTEM COLOURS
COL_TRANSPARENT        = (  0,   0,   0,   0)

# SOUND SETTINGS
SND_VOL_SFX            = 1.0
SND_VOL_MUSIC          = 1.0
SND_FREQUENCY          = 48000
SND_SIZE               = -16
SND_CHANNELS           = 2
SND_BUFFER             = 4096
SND_IS_MUTE            = False

# FILE LOCATIONS (from parent directory)
LOC_INSTRUCTIONS       = os.path.join("res", "pictures", "inst.png")
LOC_SPRITESHEET        = os.path.join("res", "pictures", "img.png")
LOC_MUSIC              = os.path.join("res", "sounds", "music.ogg")
LOC_SFX_BOMB           = os.path.join("res", "sounds", "bomb.ogg")
LOC_SFX_FINISH         = os.path.join("res", "sounds", "finish.ogg")

# GLOBAL OBJECT SETTINGS
PLAYER_DEF_SPEED       = 1
MONSTER_DEF_SPEED      = 1
ANIMATION_TICKS        = 10
