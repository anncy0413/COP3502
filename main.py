from button import *
from cell import *
from selectCell import *
from board import *

import sys
import pygame
from pygame.color import THECOLORS as COLORS


def draw_background_first():
    # with a photo
    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, SIZE)
    screen.blit(background, (0, 0))




def draw_background_second():
    # blue background
    screen.fill((200, 230, 245))

def draw_background_fail():
    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, SIZE)
    screen.blit(background, (0, 0))

def draw_background_win():
    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, SIZE)
    screen.blit(background, (0, 0))

    # Driver code


if __name__ == "__main__":
    '''
    N = 9
    K = 40
    sudoku = Sudoku(N, K)
    sudoku.fillValues()
    sudoku.printSudoku()
    '''
    # init pygame
    pygame.init()

    pygame.display.set_caption("Sudoku")
    # constant
    SIZE = [450, 600]
    font80 = pygame.font.SysFont('Times', 80)
    font100 = pygame.font.SysFont('Times', 100)

    # create screen 900*1000
    screen = pygame.display.set_mode(SIZE)

    # main main loop
    mainFlag = True
    while mainFlag:
        # welcome text
        font = pygame.font.SysFont(None, 50)
        Welcome_surf = font.render("Welcome to Sudoku", True, (0, 0, 0))
        Welcome_rect = Welcome_surf.get_rect()
        Welcome_rect.center = (225, 125)
        screen.blit(Welcome_surf, Welcome_rect)

        # Select text
        font = pygame.font.SysFont(None, 50)
        select_surf = font.render("Select Game Mode:", True, (0, 0, 0))
        select_rect = select_surf.get_rect()
        select_rect.center = (225, 225)
        screen.blit(select_surf, select_rect)

        # add  three button
        easyButton = Button(screen, 50, 300, 100, 50, "EASY", button_color=(160, 90, 45), text_color=(255, 255, 255))
        mediumButton = Button(screen, 180, 300, 100, 50, "MEDIUM", button_color=(160, 90, 45),
                              text_color=(255, 255, 255))
        hardButton = Button(screen, 310, 300, 100, 50, "HARD", button_color=(160, 90, 45), text_color=(255, 255, 255))

        cur_blank_size = 0  # require filled cell number
        # main loop at first screen
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if button.is_over(pygame.mouse.get_pos()):
                    if easyButton.check_click(pygame.mouse.get_pos()):
                        cur_blank_size = 30
                        running = False
                        print("Button easy clicked!")
                        break

                    elif mediumButton.check_click(pygame.mouse.get_pos()):
                        cur_blank_size = 40
                        running = False
                        print("Button mid clicked!")
                        break

                    elif hardButton.check_click(pygame.mouse.get_pos()):
                        cur_blank_size = 50
                        running = False
                        print("Button hard clicked!")
                        break

                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                    # background
                draw_background_first()

                # text
                screen.blit(Welcome_surf, Welcome_rect)
                screen.blit(select_surf, select_rect)

                # button
                easyButton.draw()
                mediumButton.draw()
                hardButton.draw()

                # flip
                pygame.display.flip()

        cur_i, cur_j = 0, 0
        cur_change_size = 0  # 已经填写的数字

        # add  three button
        resetButton = Button(screen, 50, 480, 100, 50, "RESET", button_color=(160, 90, 45), text_color=(255, 255, 255))
        restartButton = Button(screen, 180, 480, 100, 50, "RESTART", button_color=(160, 90, 45),
                               text_color=(255, 255, 255))
        exitButton = Button(screen, 310, 480, 100, 50, "EXIT", button_color=(160, 90, 45), text_color=(255, 255, 255))

        # background
        draw_background_second()

        sdBoard = board(450, 450, screen, cur_blank_size)
        running = True
        while running:
            # 1. input info get info from mouse and keyboard
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resetButton.check_click(pygame.mouse.get_pos()):
                        # reset
                        sdBoard.reset_to_original()
                        print("Button reset clicked!")
                        break

                    elif restartButton.check_click(pygame.mouse.get_pos()):
                        # re-start
                        running = False
                        print("Button restart clicked!")
                        break

                    elif exitButton.check_click(pygame.mouse.get_pos()):
                        # quit
                        pygame.quit()
                        break

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    sdBoard.click(event.pos[1], event.pos[0])

                elif event.type == pygame.KEYUP:
                    print(event.key)
                    if event.key in [49, 50, 51, 52, 53, 54, 55, 56, 57]:
                        sdBoard.sketch(event.key - 48)
                    elif event.key == 13 or event.key == 1073741912:
                        sdBoard.place_number()
                    elif event.key == 1073741906:
                        sdBoard.selectUp()
                    elif event.key == 1073741905:
                        sdBoard.selectDown()
                    elif event.key == 1073741903:
                        sdBoard.selectRight()
                    elif event.key == 1073741904:
                        sdBoard.selectLeft()

            # 2. output, flip screen
            # background
            draw_background_second()


            sdBoard.draw()

            resetButton.draw()
            restartButton.draw()
            exitButton.draw()

            # flip
            pygame.display.flip()

            # 3. check win, fail, or unfinished
            sdBoard_check = sdBoard.check_board()
            if sdBoard_check == 1:
                # win screen
                running = False
                break
            elif sdBoard_check == 2:
                # fail screen
                running = False
                break



        if sdBoard_check == 1:
            # win screen
            draw_background_win()

            # Game Over Text
            font = pygame.font.SysFont(None, 50)
            win_surf = font.render("Game Won!", True, (0, 0, 0))
            win_rect = win_surf.get_rect()
            win_rect.center = (225, 225)
            screen.blit(win_surf, win_rect)

            # restart button
            exitButton = Button(screen, 170, 280, 120, 50, "EXIT", button_color=(160, 90, 45),
                                   text_color=(255, 255, 255))

            winning = True
            while winning:
                # 1. input info get info from mouse and keyboard
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if exitButton.check_click(pygame.mouse.get_pos()):
                            # re-start
                            winning = False
                            print("Button exit clicked!")
                            pygame.quit()
                            break
                        if event.type == pygame.QUIT:
                            failing = False
                            pygame.quit()
                            break
                # 2. output, flip screen
                # background
                draw_background_win()
                # button
                exitButton.draw()
                # text
                screen.blit(win_surf, win_rect)

                # flip
                pygame.display.flip()

        elif sdBoard_check == 2:
            # fail background
            draw_background_fail()


            # Game Over Text
            font = pygame.font.SysFont(None, 50)
            fail_surf = font.render("Game Over :(", True, (0, 0, 0))
            fail_rect = fail_surf.get_rect()
            fail_rect.center = (225, 225)
            screen.blit(fail_surf, fail_rect)

            # restart button
            restartButton = Button(screen, 170, 280, 120, 50, "RESTART", button_color=(160, 90, 45),
                                   text_color=(255, 255, 255))



            failing = True
            while failing:
                # 1. input info get info from mouse and keyboard
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restartButton.check_click(pygame.mouse.get_pos()):
                            # re-start
                            failing = False
                            print("Button restart clicked!")
                            break
                    if event.type == pygame.QUIT:
                        failing = False
                        pygame.quit()
                        break
                # 2. output, flip screen
                # background
                draw_background_fail()
                # button
                restartButton.draw()
                # text
                screen.blit(fail_surf, fail_rect)


                # flip
                pygame.display.flip()







    pygame.quit()
