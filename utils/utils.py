
import pygame


def isRectCollidingWithPoint(rect: pygame.Rect, point: tuple[int, int]) -> bool:
    return rect.collidepoint(point)