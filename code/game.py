#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, M_MENU_SELECT
from code.demo import Demo
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            m_return = menu.run()

            if m_return == M_MENU_SELECT[0]:
                demo = Demo(self.window, 'Demo')
                demo_return = demo.run()
            elif m_return == M_MENU_SELECT[1]:
                pygame.quit()
                quit()
            else:
                pass
