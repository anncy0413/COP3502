import pygame


class Button:
    def __init__(self, screen, x, y, width, height, text, button_color=(0, 255, 0), text_color=(255, 255, 255)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.button_color = button_color
        self.text_color = text_color
        self.rect = (self.x, self.y, self.width, self.height)
        self.rect_in = (self.x + 13, self.y + 10, self.width - 26, self.height - 20)

    def draw(self):
        # 绘制按钮
        pygame.draw.rect(self.screen, self.button_color, self.rect, 8)

        pygame.draw.rect(self.screen, (245, 120, 0), self.rect_in)

        # 绘制按钮文本
        font = pygame.font.SysFont(None, 22)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect()
        text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        self.screen.blit(text_surf, text_rect)

    # def is_over(self, pos):
    # 检查鼠标是否在按钮上
    # return self.rect.collidepoint(pos)

    def check_click(self, pos):
        x_match = (pos[0] > self.x) and (pos[0] < self.x + self.width)
        y_match = pos[1] > self.y and pos[1] < self.y + self.height
        return x_match and y_match