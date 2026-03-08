#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load("./asset/Menu.png")
        self.rect = self.surf.get_rect(left=0, top=0) #

    def run(self, ):
        self.window.blit(source=self.surf, rect=self.rect)
        pg.display.flip()
        pass
