# ﻿Die Geduld
Version 1.2  
Copyright (c) 2018-2019 Jared Daniel Carbonell Recomendable.  

## What is this?
The product of a project assignment by the Computing lecturers/tutors of Yishun Innova Junior College.

## License
All code included in this game is licensed under the GNU General Public License (GPL) Version 3, included in the root directory as the file `LICENSE`.

All sprites, sound effects and music included in this game are licensed under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0), included as the file `res/LICENSE_RES`.

## Pre-Requisites
The game's dependencies are only Python 3 and Pygame. To install Pygame, simply enter the following in a terminal:
```
pip install pygame
```  
Depending on your system, you may have to change `pip` to `pip3` to install Pygame for Python 3. Please note that the game is not guranteed to run in Python 2.

## Playing the Game
Playing the game is straightforward and, as of current, only involves navigating around a maze. The key to winning is get to the checkpoint, avoiding the monsters around. For now, the monsters merely move either horizontally or vertically, and when the player gets hit by one, he simply returns to the starting point.

Use the arrow keys, WASD on the keyboard or the numpad keys listed below to navigate around the levels.
* `W`, `Up` or `Numpad 8`: Move Up
* `S`, `Down` or `Numpad 2`: Move Down
* `A`, `Left` or `Numpad 4`: Move Left
* `D`, `Right` or `Numpad 6`: Move Right

There are other controls included. Quitting from the game takes roughly a second, as a nice touch to fade out the music and sound effects was added when the user tries to quit.
* `R`: Reset Player Position
* `M`: Toggle Mute
* `Esc` or `Control` + `Q`: Quit from the Game

The controls will be shown everytime the game is launched.
