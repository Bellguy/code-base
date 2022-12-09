import time
from pathlib import Path
import pygame
import numpy as np

COLOR_BG = (10, 10 , 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

TILES = 100
TILE_SIZE = 10
SCREEN_SIZE = TILES * TILE_SIZE

def update(screen, cells, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        checkRow = 0
        checkCol = 0
        alive = 0

        # Checks Rows and Columns, and loops around when cells reach an edge
        for i in range(-1, 2):
            checkRow = row + i

            if checkRow < 0:
                checkRow = TILES-1

            if checkRow > TILES-1:
                checkRow = 0

            for j in range(-1, 2):
                checkCol = col + j

                if checkCol < 0:
                    checkCol = TILES-1

                if checkCol > TILES-1:
                    checkCol = 0

                if not(checkRow == row and checkCol == col):
                    alive += cells[checkRow, checkCol]

        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        # Game of Life Rules
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
                    
        pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
        
    return updated_cells

def createBoard():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) # width, height
    
    cells = np.zeros((TILES, TILES)) # height, width
    readGame(cells)
    screen.fill(COLOR_GRID)
    update(screen, cells)
    
    pygame.display.flip()
    pygame.display.update()
    
    running = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                saveGame(cells) # Saves game before quitting
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN: # Used for key pressing
                if event.key == pygame.K_SPACE: # When spacebar is pressed, play/pause game
                    running = not running
                    update(screen, cells)
                    pygame.display.update()

                if event.key == pygame.K_DELETE: # When delete key is pressed, the board is completely reset
                    cells = np.zeros((TILES, TILES))
                    update(screen, cells)
                    pygame.display.update()

                if event.mod & pygame.KMOD_LSHIFT:
                    if event.key == pygame.K_h: # When h key is pressed, a horizontal line spawns where the mouse cursor is hovering
                        pos = pygame.mouse.get_pos()
                        horLine(cells, pos[1] // TILE_SIZE)
                        update(screen, cells)
                        pygame.display.update()

                if event.mod & pygame.KMOD_LSHIFT:
                    if event.key == pygame.K_v: # When v key is pressed, a vertical line spawns where the mouse cursors is hovering
                        pos = pygame.mouse.get_pos()
                        vertLine(cells, pos[0] // TILE_SIZE)
                        update(screen, cells)
                        pygame.display.update()
                    
            if pygame.mouse.get_pressed()[0]: # Places individual cells with left click
                pos = pygame.mouse.get_pos()
                cells[pos[1] // TILE_SIZE, pos[0] // TILE_SIZE] = 1
                update(screen, cells)
                pygame.display.update()
                
            if pygame.mouse.get_pressed()[2]: # Deletes individual cells with right click
                pos = pygame.mouse.get_pos()
                cells[pos[1] // TILE_SIZE, pos[0] // TILE_SIZE] = 0
                update(screen, cells)
                pygame.display.update()
                
        screen.fill(COLOR_GRID)
        
        if running:
            cells = update(screen, cells, with_progress=True)
            pygame.display.update()

def saveGame(cells): # Function that is used to save the current game state to a file
    saveCells = ''
    for i in range(0, TILES):
        for j in range(0, TILES):
           saveCells += str(int(cells[i][j])) # Game state is converted to a string

    # Writes the game state string to txt file
    f = open("golsave.txt", "w")
    f.write(saveCells)
    f.close()
            
def readGame(cells): # Function that reads the last saved game state
    my_file = Path("golsave.txt")
    if my_file.is_file(): # If file exists, read file
        # Reads last saved game state
        f = open("golsave.txt", "r")
        values = f.read()

        # Prevents errors if game size is changed
        if len(values) >= TILES*TILES:
            for i in range(0, TILES):
                for j in range(0, TILES):
                    cells[i][j] = int(values[i*TILES + j])
        
        f.close()

def vertLine(cells, col): # Function that creates vertical line
    for i in range(0, TILES):
        cells[i][col] = 1.0

def horLine(cells, row): # Function that creates horizontal line
    for i in range(0, TILES):
        cells[row][i] = 1.0

class cordinates(): # will be used to make GOL structures
    x = 0
    y = 0

def main():
    createBoard()

    
if __name__ == '__main__':
    main()
