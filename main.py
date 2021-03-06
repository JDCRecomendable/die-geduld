#!/usr/bin/env python3

"""
Main File for Game
Copyright (c) 2018 Jared Daniel Carbonell Recomendable.

Licensed under the GNU General Public License (GPL) Version 3.
"""

import sys
from base.game import *
import levels.level1 as level1
import levels.level2 as level2
import levels.level3 as level3
import levels.level4 as level4
import levels.level5 as level5
import levels.level6 as level6
import levels.level7 as level7
import levels.level8 as level8

levels = [level1, level2, level3, level4, level5, level6, level7, level8]

mute_status = SND_IS_MUTE

if __name__ == "__main__":
    game_control = GameControl()
    game_control.initialise_pygame()
    game_control.initialise_display()
    r = game_control.display_screen(LOC_INSTRUCTIONS)
    if r == -1:
        game_control.uninitialise_all()
        exit(0)
    game_control.initialise_sounds()
    for level in levels:
        r, mute_status = game_control.run(level, mute_status)
        if r == -1:
            break
    game_control.uninitialise_all()
    sys.exit(0)
