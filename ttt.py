#!/usr/local/bin/python

"""
ttt.py
Purpose: My implementation of Tic-Tac-Toe using Python and Pygame
Author: Kendrick Ledet
Date: 12/26/12
"""
"""
Copyright 2012 Kendrick Ledet
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import sys, random
import pygame
from pygame.locals import *

# Check win/lose status
def check_status(grid, screen):
    # Check horizontally (rows)
    for row in range(0,3):
        if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0]:
            pygame.draw.line(screen,(0,0,0),(0,(row+1)*100-50),(300,(row+1)*100-50),2) 
            return grid[row][0]

    # Check vertically (columns)
    for col in range(0,3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col]:
            pygame.draw.line(screen,(0,0,0),((col+1)*100-50,0),((col+1)*100-50,300),2) 
            return grid[0][col]

    # Check diagonally
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0]:
        pygame.draw.line(screen,(0,0,0),(50,50),(250,250),2) 
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2]:
        pygame.draw.line(screen,(0,0,0),(250,50),(50,250),2) 
        return grid[0][2]

    return False

# Determine row & column the player clicked
def get_row_col(x, y):
    if x < 100:
        col = 0
    elif x < 200:
        col = 1
    else:
        col = 2

    if y < 100:
        row = 0
    elif y < 200:
        row = 1
    else:
        row = 2

    return row, col

# Draw a move on the playing field
def draw_move(screen, row, col, turn):
    cx = col * 100+50
    cy = row * 100+50

    if turn == 'X':
        pygame.draw.line(screen, (0,0,0), (cx-25, cy-25),(cx+25, cy+25), 2)
        pygame.draw.line(screen, (0,0,0), (cx+25, cy-25),(cx-25, cy+25), 2) 
    else:
        pygame.draw.circle(screen, (0,0,0), (cx, cy), 40, 2) 

# Determine move on the playing field, mark off spot on grid
def make_move(screen, grid, turn, sim=False):
    if sim == False:
        x, y = pygame.mouse.get_pos()
        row, col = get_row_col(x, y)
    else:  # Simulate a move for the computer
        row = random.randint(0,2)
        col = random.randint(0,2)
        while grid[row][col]:
            row = random.randint(0,2)
            col = random.randint(0,2)

    if grid[row][col] != 'X' and grid[row][col] != 'O':  # If not already in play
        draw_move(screen, row, col, turn)  # Call draw_move to draw the appropriate move
        grid[row][col] = turn  # Spot is now in play
        turn = 'O' if turn == 'X' else 'X'  # Switch turn
    else:  # Let player choose another spot
        return grid, turn

    return grid, turn

def main():
    # Initialize player/first turn
    player = turn = sys.argv[1].upper()

    # Initialize pygame and pygame window
    pygame.init()
    pygame.display.set_caption("Kenny's Tic-Tac-Toe")
    screen = pygame.display.set_mode((300,300))

    # Set up white playing field
    screen.fill((255,255,255))
    pygame.draw.line(screen, (0,0,0), (100,0), (100,300), 2)
    pygame.draw.line(screen, (0,0,0), (200,0), (200,300), 2)
    pygame.draw.line(screen, (0,0,0), (0,100), (300,100), 2)
    pygame.draw.line(screen, (0,0,0), (0,200), (300,200), 2)

    # Initialize row, col grid
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    # Initialize win/lose status
    status = 0

    # Run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type is MOUSEBUTTONDOWN:
                if not status:
                    grid, turn = make_move(screen, grid, turn)
                    status = check_status(grid, screen)
                if not status:
                    if turn != player:  # Just in case player clicked in a played spot
                        grid, turn = make_move(screen, grid, turn, sim=True)
                        status = check_status(grid, screen)
        pygame.display.update()

if __name__ == '__main__':
    main()
