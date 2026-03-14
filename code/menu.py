#!/usr/bin/python
# -*- coding: utf-8 -*-
from msilib.schema import Font

import pygame.image
from pygame import Surface, Rect

from code.const import WIN_WIDTH, C_WHITE, C_HALF_RED, C_HALF_BLACK, M_COMMAND_KEYS, C_GOLD, M_MENU_SELECT, C_GREEN, \
    WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuIMG.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_select = 0
        pygame.mixer_music.load("./asset/MenuMSC.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(
                text_size=80,
                text="Game Uni",
                text_color=C_WHITE,
                text_center_pos=(WIN_WIDTH / 2, 90),
                shadow_color=C_HALF_BLACK,
                offset_x=-4,  # Sombra no eixo X
                offset_y=5  # Sombra no eixo Y
            )
            for i in range(len(M_MENU_SELECT)):
                if i == menu_select :
                    self.menu_text(35,
                                   M_MENU_SELECT[i],
                                   C_GREEN, (WIN_WIDTH / 2, 175 + 40 * i),
                                   C_HALF_BLACK,
                                   offset_x=-1,
                                   offset_y=1)
                else:
                    self.menu_text(35,
                                   M_MENU_SELECT[i],
                                   C_HALF_RED, (WIN_WIDTH / 2, 175 + 40 * i),
                                   C_HALF_BLACK,
                                   offset_x=-1,
                                   offset_y=1)

            for i in range(len(M_COMMAND_KEYS)):
                self.menu_text(25, M_COMMAND_KEYS[i], C_GOLD,
                               ((WIN_WIDTH / 3) + 200 * i, WIN_HEIGHT - 50),
                               C_HALF_BLACK,
                               -1,
                               1)
            pygame.display.flip()
            # all check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # keyboard event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_select < len(M_MENU_SELECT) - 1:
                            menu_select += 1
                        else:
                            menu_select = 0
                    if event.key == pygame.K_UP:
                        if menu_select >= len(M_MENU_SELECT) - 1:
                            menu_select -= 1
                        else:
                            menu_select = len(M_MENU_SELECT) -1
                    if event.key == pygame.K_RETURN:
                        return M_MENU_SELECT[menu_select]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, shadow_color: tuple,
                  offset_x=0, offset_y=0, ):
        # 1. Cria a fonte
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)

        # --- CAMADA DA SOMBRA ---
        shadow_surf = text_font.render(text, True, shadow_color).convert_alpha()
        shadow_pos = (text_center_pos[0] + offset_x, text_center_pos[1] + offset_y)
        shadow_rect = shadow_surf.get_rect(center=shadow_pos)
        self.window.blit(shadow_surf, shadow_rect)

        # --- CAMADA DO TEXTO ---
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
