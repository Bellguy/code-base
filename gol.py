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
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]), dtype=int)
    
    for row, col in np.ndindex(cells.shape):
        checkRow = 0
        checkCol = 0
        alive = 0

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
                saveGame(cells)
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells)
                    pygame.display.update()

                if event.key == pygame.K_DELETE:
                    cells = np.zeros((TILES, TILES))
                    update(screen, cells)
                    pygame.display.update()

                if event.mod & pygame.KMOD_LSHIFT:
                    if event.key == pygame.K_h:
                        pos = pygame.mouse.get_pos()
                        horLine(cells, pos[1] // TILE_SIZE)
                        update(screen, cells)
                        pygame.display.update()

                if event.mod & pygame.KMOD_LSHIFT:
                    if event.key == pygame.K_v:
                        pos = pygame.mouse.get_pos()
                        vertLine(cells, pos[0] // TILE_SIZE)
                        update(screen, cells)
                        pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // TILE_SIZE, pos[0] // TILE_SIZE] = 1
                update(screen, cells)
                pygame.display.update()

            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // TILE_SIZE, pos[0] // TILE_SIZE] = 0
                update(screen, cells)
                pygame.display.update()
                
        screen.fill(COLOR_GRID)
        
        if running:
            cells = update(screen, cells, with_progress=True)
            pygame.display.update()

def saveGame(cells):
    saveCells = ''
    for i in range(0, TILES):
        for j in range(0, TILES):
           saveCells += str(int(cells[i][j]))

    f = open("golsave.txt", "w")
    f.write(saveCells)
    f.close()
            
def readGame(cells):
    my_file = Path("golsave.txt")
    if my_file.is_file():
        f = open("golsave.txt", "r")
        values = f.read()

        if len(values) >= TILES*TILES:
            for i in range(0, TILES):
                for j in range(0, TILES):
                    cells[i][j] = int(values[i*TILES + j])
        
        f.close()

def vertLine(cells, col):
    for i in range(0, TILES):
        cells[i][col] = 1.0

def horLine(cells, row):
    for i in range(0, TILES):
        cells[row][i] = 1.0

class cordinates():
    x = 0
    y = 0

def main():
    createBoard()
 
if __name__ == '__main__':
    main()