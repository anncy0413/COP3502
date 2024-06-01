import pygame
from cell import *
from selectCell import *
from SudokuGenerator import *

from pygame.color import THECOLORS as COLORS



class board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty  # filled with 0 numbers
        self.selectRow = 0
        self.selectCol = 0

        self.board = generate_sudoku(9, difficulty)

        self.redCell = selectCell(0, 0, self.screen)

        self.cell = []

        for row in range(1, 10):
            for col in range(1, 10):
                value = self.board[row - 1][col - 1]
                newCell = cell(value, row, col, self.screen)
                self.cell.append(newCell)

    def draw(self):
        # draw every cell
        for cell in self.cell:
            cell.draw()
        # draw the grid
        for i in range(1, 5):
            # Draw 3 horizontal lines
            pygame.draw.line(self.screen, COLORS['black'], (0, 150 * (i - 1)), (450, 150 * (i - 1)), 5)
            # draw 3 vertical lines
            pygame.draw.line(self.screen, COLORS['black'], (150 * (i - 1), 0), (150 * (i - 1), 450), 5)
        self.redCell.draw()

    def select(self, row, col):
        # row and col start from index of zero, the row and column 代表最小cell左上点点坐标
        self.selectRow = row
        self.selectCol = col
        pos = (row * 50, col * 50)
        self.redCell.set_pos(pos)

    def selectUp(self):
        if self.selectCol > 0:
            self.selectCol = self.selectCol - 1
        pos = (self.selectRow * 50, self.selectCol * 50)
        self.redCell.set_pos(pos)

    def selectDown(self):
        if self.selectCol < 8:
            self.selectCol = self.selectCol + 1
        pos = (self.selectRow * 50, self.selectCol * 50)
        self.redCell.set_pos(pos)

    def selectRight(self):
        if self.selectRow < 8:
            self.selectRow = self.selectRow + 1
        pos = (self.selectRow * 50, self.selectCol * 50)
        self.redCell.set_pos(pos)

    def selectLeft(self):
        if self.selectRow > 0:
            self.selectRow = self.selectRow - 1
        pos = (self.selectRow * 50, self.selectCol * 50)
        self.redCell.set_pos(pos)

    def click(self, x, y):
        cur_row = int(y / 50)
        cur_col = int(x / 50)
        if cur_row >= 0 and cur_row <= 8 and cur_col >= 0 and cur_col <= 8:
            self.select(cur_row, cur_col)

    def sketch(self, value):
        cellNo = self.selectRow * 9 + self.selectCol
        self.cell[cellNo].set_sketched_value(value)

    def place_number(self):
        cellNo = self.selectRow * 9 + self.selectCol
        self.cell[cellNo].set_cell_value()

    def reset_to_original(self):
        i = 0
        self.redCell.set_pos((0, 0))
        self.selectRow = 0
        self.selectCol = 0
        for row in range(1, 10):
            for col in range(1, 10):
                value = self.board[row - 1][col - 1]
                self.cell[i].set_value(value)
                i += 1


    def check_row(self, value, row, col):
        for j in range(0, 9):
            if j == col:
                continue
            index = row * 9 + j  # convert to 1D list
            if self.cell[index].get_cell_value() == value:
                return False
        return True


    def check_col(self, value, row, col):
        for i in range(0, 9):
            if i == row:
                continue
            index = i * 9 + col  # convert to 1D list # cell is a 1D list
            if self.cell[index].get_cell_value() == value:
                return False
        return True


    def check_box(self, value, row, col):
        # (0,0),(0,3),(0,6)
        # (3,0),(3,3),(3,6)
        # (6,0),(6,3),(6,6)
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        end_row = start_row + 2
        end_col = start_col + 2
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if i == row and j == col:
                    continue
                index = i * 9 + j
                if self.cell[index].get_cell_value() == value:
                    return False
        return True


    def check_board(self):

        flag_zero = True  # check whether all cells are filled with non-zero values

        for i in range(0, 9):
            for j in range(0, 9):
                value = self.cell[i * 9 + j].get_cell_value()
                if value == 0:
                    flag_zero = False  # players can still set some cells, the game is unfinished
                    continue
                if ((not self.check_row(value, i, j)) or
                        (not self.check_col(value, i, j)) or
                        (not self.check_box(value, i, j))):
                    return 2  # go to fail screen

        if flag_zero:
            return 1  # go to win screen

        else:
            return 3  # continue putting more values into the board