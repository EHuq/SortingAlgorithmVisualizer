import time
import pygame
from random import randint

LARGEST_SIZE = 500
LENGTH = 250
y = 0
w = 2

pygame.init()
size = (LARGEST_SIZE, LARGEST_SIZE)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Pygame Bubble-Sort Visualization")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
color = pygame.Color(100, 100, 100)


def randomizeList(LENGTH):
    lst = []
    xList = []
    tmpX = 0
    for i in range(LENGTH):
        lst.append(randint(0, LARGEST_SIZE))
        xList.append(tmpX)
        tmpX += w

    return lst, xList


def draw(xList, y, lst, LENGTH):
    for i in range(LENGTH):
        pygame.draw.rect(window, white, (xList[i], y, w, lst[i]), 0)
    time.sleep(0.005)


def selectionSort(lst, LENGTH, window, xList, y):
    pygame.display.set_caption("SELECTION SORT")
    for i in range(LENGTH):
        min_idx = i
        for j in range(i + 1, LENGTH):
            window.fill(black)
            if lst[min_idx] > lst[j]:
                min_idx = j
                draw(xList, y, lst, LENGTH)
                pygame.display.update()

        lst[i], lst[min_idx] = lst[min_idx], lst[i]


def bubbleSort(lst, LENGTH, window, xList, y):
    pygame.display.set_caption("BUBBLE SORT")
    for i in range(LENGTH):
        for j in range(0, LENGTH - i - 1):
            window.fill(black)
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw(xList, y, lst, LENGTH)
                pygame.display.update()


def partition(lst, low, high, LENGTH, window, xList, y):
    index = (low - 1)
    pivot = lst[high]
    for j in range(low, high):
        window.fill(black)
        if lst[j] < pivot:
            index = index + 1
            lst[index], lst[j] = lst[j], lst[index]
            draw(xList, y, lst, LENGTH)
            pygame.display.update()

    lst[index + 1], lst[high] = lst[high], lst[index + 1]
    return index + 1


def quickSort(lst, low, high, LENGTH, window, xList, y):
    pygame.display.set_caption("QUICK SORT")
    if low < high:
        window.fill(black)
        part = partition(lst, low, high, LENGTH, window, xList, y)
        quickSort(lst, part + 1, high, LENGTH, window, xList, y)
        quickSort(lst, low, part - 1, LENGTH, window, xList, y)

        draw(xList, y, lst, LENGTH)
        pygame.display.update()


lst, xList = randomizeList(LENGTH)
quickSort(lst, 0, LENGTH - 1, LENGTH, window, xList, y)

lst, xList = randomizeList(LENGTH)
selectionSort(lst, LENGTH, window, xList, y)

lst, xList = randomizeList(LENGTH)
bubbleSort(lst, LENGTH, window, xList, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
