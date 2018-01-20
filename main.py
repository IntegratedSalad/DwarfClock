#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import datetime
import calendar
import digits

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)

FONT_SIZE = 14
SCREEN_WIDTH = 31
SCREEN_HEIGHT = 11

SCREEN_WIDTH_SIZE = SCREEN_WIDTH * FONT_SIZE
SCREEN_HEIGHT_SIZE = SCREEN_HEIGHT * FONT_SIZE

# u'px437ibmbios'


def init():
    global font, scr, hash_SYMBOL, dwarf_SYMBOL_ACTIVE, dwarf_SYMBOL_UNACTIVE, grid, digit1, digit2, digit3, digit4, \
    clock

    pygame.init()
    pygame.font.init()
    scr = pygame.display.set_mode((SCREEN_WIDTH_SIZE, SCREEN_HEIGHT_SIZE))
    font = pygame.font.SysFont("px437ibmbios", FONT_SIZE)
    hash_SYMBOL = font.render('#', True, WHITE)
    dwarf_SYMBOL_ACTIVE = font.render(u"☻", True, WHITE)
    dwarf_SYMBOL_UNACTIVE = font.render(u"☻", True, GREY)
    pygame.display.set_caption('Dwarf Clock')

    digit1 = make_digit()
    digit2 = make_digit()
    digit3 = make_digit()
    digit4 = make_digit()

    grid = [[0 for x in range(SCREEN_WIDTH - 2)] for y in range(SCREEN_HEIGHT - 4)]
    clock = pygame.time.Clock()
    # SEMICOLON #
    grid[2][14] = 1
    grid[4][14] = 1

    #for n in grid: print n
    #grid[2][8] = 1


    #            y  x
    #print digit1[0][1]

    #for n in digit1:
    #    print n


def draw_border():
    for row in range(SCREEN_WIDTH):
        for column in range(SCREEN_HEIGHT):
            if (row and column) == 0 or column == SCREEN_HEIGHT - 1 or \
                            row == SCREEN_WIDTH - 1 or column == SCREEN_HEIGHT - 3:
                scr.blit(hash_SYMBOL, (0 + (row * FONT_SIZE),
                                       0 + (column * FONT_SIZE)))

    scr.blit(dwarf_SYMBOL_ACTIVE, (1 * FONT_SIZE, 9 * FONT_SIZE))
    scr.blit(hash_SYMBOL, (2 * FONT_SIZE, 9 * FONT_SIZE))
    #                      x              y

def fill_rectangle():
    # corespond with the grid - if grid[row][column] 0: scr.blit(dwarf_SYMBOL_UNACTIVE)
    for row in range(SCREEN_WIDTH - 2):
        for column in range(SCREEN_HEIGHT - 4):
            if grid[column][row] == 0:
                scr.blit(dwarf_SYMBOL_UNACTIVE, ((1 * FONT_SIZE) + (row * FONT_SIZE),
                                            (1 * FONT_SIZE) + (column * FONT_SIZE)))
            else:
                scr.blit(dwarf_SYMBOL_ACTIVE, ((1 * FONT_SIZE) + (row * FONT_SIZE),
                                                 (1 * FONT_SIZE) + (column * FONT_SIZE)))


    # if [x][y] == 0, pass - aby nie rysował dwa razy szarego
    # make so that all rectangle is on the grid, and there's no more than one dwarf being drawn


def handle_keys():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


def make_digit():
    # digit has 16 active places (1 or 0), + 4 that are always off (0)
    return [[0 for x in range(4)] for y in range(5)]


def get_date():
    now = datetime.datetime.now()
    today = datetime.datetime.today()
    week_day = calendar.day_name[today.weekday()]
    hours = str(now.hour)
    minutes = str(now.minute)
    day = str(now.day)
    return [hours, minutes, day, week_day]


def set_date():
    # will get the function that "lits" the points on the screen
    full_date = get_date()

def place_digits():
    # maps digits to the board of unlit faces

    digit1 = digits.ZERO
    digit2 = digits.ZERO
    digit3 = digits.ZERO
    digit4 = digits.ZERO

    map_digit(1, 4, digit1)
    map_digit(1, 9, digit2)
    map_digit(1, 16, digit3)
    map_digit(1, 21, digit4)



def map_digit(y, x, digit):
    # maps digit to grid
    for column in range(len(grid)):
        for row in range(len(grid[0])):
            for column2 in range(len(digit)):
                for row2 in range(len(digit[0])):
                    grid[y + column2][x + row2] = digit[0 + column2][0 + row2]

def main():

    while True:
        handle_keys()
        clock.tick(60)
        scr.fill(BLACK)
        draw_border()
        fill_rectangle()
        place_digits()
        set_date()
        pygame.display.flip()


if __name__ == '__main__':
    init()
    main()