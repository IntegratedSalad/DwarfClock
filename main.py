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

ddigits = []

def init():
    global font, scr, hash_SYMBOL, dwarf_SYMBOL_ACTIVE, dwarf_SYMBOL_UNACTIVE, grid, clock, dwarf_MONTH_COLOR, ddigits

    pygame.init()
    pygame.font.init()
    scr = pygame.display.set_mode((SCREEN_WIDTH_SIZE, SCREEN_HEIGHT_SIZE))
    font = pygame.font.Font("Px437_IBM_BIOS.ttf", FONT_SIZE)
    hash_SYMBOL = font.render('#', True, WHITE)
    dwarf_MONTH_COLOR = WHITE
    dwarf_SYMBOL_ACTIVE = font.render(u"☻", True, WHITE)
    dwarf_SYMBOL_UNACTIVE = font.render(u"☻", True, GREY)
    pygame.display.set_caption('Dwarf Clock')

    ddigits = [make_digit(), make_digit(), make_digit(), make_digit()]

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

    scr.blit(hash_SYMBOL, (2 * FONT_SIZE, 9 * FONT_SIZE))
    #                      x              y

def fill_rectangle():
    # coresponding with the grid
    for row in range(SCREEN_WIDTH - 2):
        for column in range(SCREEN_HEIGHT - 4):
            if grid[column][row] == 0:
                scr.blit(dwarf_SYMBOL_UNACTIVE, ((1 * FONT_SIZE) + (row * FONT_SIZE),
                                            (1 * FONT_SIZE) + (column * FONT_SIZE)))
            else:
                scr.blit(dwarf_SYMBOL_ACTIVE, ((1 * FONT_SIZE) + (row * FONT_SIZE),
                                                 (1 * FONT_SIZE) + (column * FONT_SIZE)))


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
    month = str(now.month)
    month_name = str(calendar.month_name[now.month])

    # insert 0 if needed
    if len(minutes) == 1:
        minutes = '0{0}'.format(minutes)
    if len(hours) == 1:
        hours = '0{0}'.format(hours)

    # TODO this is ugly too
    return [hours, minutes, day, month, week_day, month_name]

def place_digits():
    # maps digits to the board of unlit faces

    full_date = get_date()
    digit_dates = [
        [ddigits[0], int(full_date[0][0]), 1, 4],
        [ddigits[1], int(full_date[0][1]), 1, 9],
        [ddigits[2], int(full_date[1][0]), 1, 16],
        [ddigits[3], int(full_date[1][1]), 1, 21]
        ]

    for digit_date in digit_dates:
        dateval = digit_date[1]
        digit = digits.display_digits[dateval]
        x = digit_date[2]
        y = digit_date[3]
        map_digit(x, y, digit)

# TODO ^ this is horrible code, i know

def map_digit(y, x, digit):
    # maps digit to grid
    for column in range(len(grid)):
        for row in range(len(grid[0])):
            for column2 in range(len(digit)):
                for row2 in range(len(digit[0])):
                    grid[y + column2][x + row2] = digit[0 + column2][0 + row2]

    # TODO this is very ugly

def put_dwarf():
    dwarf_MONTH_COLOR = get_dwarf_color()
    dwarf_SYMBOL_MONTH = font.render(u"☻", True, dwarf_MONTH_COLOR)
    scr.blit(dwarf_SYMBOL_MONTH, ((1 * FONT_SIZE), 9 * FONT_SIZE))

def get_dwarf_color():
    global dwarf_MONTH_COLOR

    month = get_date()[3]

    if (month >= 4) and (month < 6):
        return  (124, 252, 0)

    if (month < 9) and (month >= 6):
        return (255,255,102)

    if (month >= 9) and (month <= 11):
        return (255, 140, 0)

    if month < 4 or (month > 11):
        return (0,191,255)


def dwarf_talk():
    date = get_date()

    if int(date[2][1]) not in [1, 2, 3]:
        ordinal_indicator = 'th'
    else:

        if int(date[2][1]) == 1:
            ordinal_indicator = 'st'
        elif int(date[2][1]) == 2:
            ordinal_indicator = 'nd'
        else:
            ordinal_indicator = 'rd'

    text = font.render("It is: {0}{1} of {2}".format(date[2], ordinal_indicator, date[-1]), True, dwarf_MONTH_COLOR)
    scr.blit(text, ((3 * FONT_SIZE), 9 * FONT_SIZE))


def main():

    while True:
        handle_keys()
        clock.tick(60)
        scr.fill(BLACK)
        draw_border()
        fill_rectangle()
        place_digits()
        put_dwarf()
        dwarf_talk()
        pygame.display.flip()


if __name__ == '__main__':
    init()
    main()