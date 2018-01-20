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
    clock, dwarf_MONTH_COLOR

    pygame.init()
    pygame.font.init()
    scr = pygame.display.set_mode((SCREEN_WIDTH_SIZE, SCREEN_HEIGHT_SIZE))
    font = pygame.font.Font("Px437_IBM_BIOS.ttf", FONT_SIZE)
    hash_SYMBOL = font.render('#', True, WHITE)
    dwarf_MONTH_COLOR = WHITE
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

    set_digit1()
    set_digit2()
    set_digit3()
    set_digit4()

    map_digit(1, 4, digit1)
    map_digit(1, 9, digit2)
    map_digit(1, 16, digit3)
    map_digit(1, 21, digit4)


def set_digit1():
    global digit1
    full_date = get_date()
    if int(full_date[0][0]) == 0: digit1 = digits.ZERO
    if int(full_date[0][0]) == 1: digit1 = digits.ONE
    if int(full_date[0][0]) == 2: digit1 = digits.TWO
    if int(full_date[0][0]) == 3: digit1 = digits.THREE
    if int(full_date[0][0]) == 4: digit1 = digits.FOUR
    if int(full_date[0][0]) == 5: digit1 = digits.FIVE
    if int(full_date[0][0]) == 6: digit1 = digits.SIX
    if int(full_date[0][0]) == 7: digit1 = digits.SEVEN
    if int(full_date[0][0]) == 8: digit1 = digits.EIGHT
    if int(full_date[0][0]) == 9: digit1 = digits.NINE

def set_digit2():
    global digit2
    full_date = get_date()
    if int(full_date[0][1]) == 0: digit2 = digits.ZERO
    if int(full_date[0][1]) == 1: digit2 = digits.ONE
    if int(full_date[0][1]) == 2: digit2 = digits.TWO
    if int(full_date[0][1]) == 3: digit2 = digits.THREE
    if int(full_date[0][1]) == 4: digit2 = digits.FOUR
    if int(full_date[0][1]) == 5: digit2 = digits.FIVE
    if int(full_date[0][1]) == 6: digit2 = digits.SIX
    if int(full_date[0][1]) == 7: digit2 = digits.SEVEN
    if int(full_date[0][1]) == 8: digit2 = digits.EIGHT
    if int(full_date[0][1]) == 9: digit2 = digits.NINE

def set_digit3():
    global digit3
    full_date = get_date()
    if int(full_date[1][0]) == 0: digit3 = digits.ZERO
    if int(full_date[1][0]) == 1: digit3 = digits.ONE
    if int(full_date[1][0]) == 2: digit3 = digits.TWO
    if int(full_date[1][0]) == 3: digit3 = digits.THREE
    if int(full_date[1][0]) == 4: digit3 = digits.FOUR
    if int(full_date[1][0]) == 5: digit3 = digits.FIVE
    if int(full_date[1][0]) == 6: digit3 = digits.SIX
    if int(full_date[1][0]) == 7: digit3 = digits.SEVEN
    if int(full_date[1][0]) == 8: digit3 = digits.EIGHT
    if int(full_date[1][0]) == 9: digit3 = digits.NINE

def set_digit4():
    global digit4
    full_date = get_date()
    if int(full_date[1][1]) == 0: digit4 = digits.ZERO
    if int(full_date[1][1]) == 1: digit4 = digits.ONE
    if int(full_date[1][1]) == 2: digit4 = digits.TWO
    if int(full_date[1][1]) == 3: digit4 = digits.THREE
    if int(full_date[1][1]) == 4: digit4 = digits.FOUR
    if int(full_date[1][1]) == 5: digit4 = digits.FIVE
    if int(full_date[1][1]) == 6: digit4 = digits.SIX
    if int(full_date[1][1]) == 7: digit4 = digits.SEVEN
    if int(full_date[1][1]) == 8: digit4 = digits.EIGHT
    if int(full_date[1][1]) == 9: digit4 = digits.NINE

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