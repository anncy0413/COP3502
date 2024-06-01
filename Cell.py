import pygame
from pygame.color import THECOLORS as COLORS

CELLWIDTH = 50
CELLHEIGHT = 50
CELLLINEWIDTH = 1  # Cell line width


class cell:
    def __init__(self, value, row, col, screen):

        self.screen = screen
        self.value = value
        self.sketched_value = value

        self.modify = False  # default:can not modify
        if self.value == 0:
            self.modify = True  # may be modify

        self.row = row
        self.col = col

        self.x = CELLWIDTH * (row - 1)
        self.y = CELLHEIGHT * (col - 1)

        self.width = CELLWIDTH
        self.height = CELLHEIGHT

        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self):
        # draw text
        pygame.draw.rect(self.screen, COLORS['black'], self.rect, CELLLINEWIDTH)
        font = pygame.font.SysFont(None, 40)
        if self.modify:
            if self.sketched_value == 0:
                text_surf = font.render(' ', True, COLORS['gray'])
                text_rect = text_surf.get_rect()
                text_rect.center = ((self.x + (self.width / 3)), (self.y + (self.height / 3)))
            else:
                text_surf = font.render(str(self.sketched_value), True, COLORS['gray'])
                text_rect = text_surf.get_rect()
                text_rect.center = ((self.x + (self.width / 3)), (self.y + (self.height / 3)))
        else:
            text_surf = font.render(str(self.value), True, COLORS['black'])
            text_rect = text_surf.get_rect()
            text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))

        self.screen.blit(text_surf, text_rect)

    def set_cell_value(self):
        if self.modify and self.sketched_value != 0:
            self.value = self.sketched_value
            self.modify = False

    def get_cell_value(self):
        return self.value

    def set_sketched_value(self, value):
        if self.modify:
            self.sketched_value = value

    def set_value(self, value):
        self.value = value
        self.sketched_value = value  # all sketched values become value
        if value == 0:
            self.modify = True
        else:
            self.modify = False
