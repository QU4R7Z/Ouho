import pygame


def load(path, SCALE_X, SCALE_Y):
    image_file = pygame.image.load(path).convert_alpha()
    image_file = pygame.transform.smoothscale(image_file, (SCALE_X, SCALE_Y))
    return image_file, image_file.get_width(), image_file.get_height()


def smooth_scale(img, SCALE_X, SCALE_Y):
    return pygame.transform.smoothscale(img, (SCALE_X, SCALE_Y))
