#!/usr/bin/python
# -*- coding: utf-8 -*-
from msilib.schema import Font

import pygame.image
from pygame import Surface, Rect

from code.Const import WIN_WIDTH, C_WHITE, C_HALF_RED, C_HALF_BLACK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuIMG.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load("./asset/MenuMSC.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # Chamada no seu código principal:
            self.menu_text(
                text_size=80,
                text="Game Uni",
                text_color=C_WHITE,
                text_center_pos=(WIN_WIDTH / 2, 90),
                shadow_color=C_HALF_BLACK,
                offset_x=-4,  # Sombra no eixo X
                offset_y=5  # Sombra no eixo Y
            )

            self.menu_text(
                text_size=30,
                text="INICIAR DEMO",
                text_color=C_HALF_RED,
                text_center_pos=(WIN_WIDTH / 2, 200),
                shadow_color=C_WHITE,
                offset_x=-1,  # Sombra no eixo X
                offset_y=1)  # Sombra no eixo Y
            pygame.display.flip()
            # check for all events by click
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, shadow_color: tuple,
                  offset_x=-5, offset_y=5, ):
        # 1. Cria a fonte
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)

        # --- CAMADA DA SOMBRA ---
        # Renderiza a sombra (pode trocar (40,40,40) pela cor que quiser)
        shadow_surf = text_font.render(text, True, shadow_color).convert_alpha()

        # Aqui controlamos X e Y separadamente
        # Lembre-se: X negativo vai para ESQUERDA, Y positivo vai para BAIXO
        shadow_pos = (text_center_pos[0] + offset_x, text_center_pos[1] + offset_y)

        shadow_rect = shadow_surf.get_rect(center=shadow_pos)
        self.window.blit(shadow_surf, shadow_rect)

        # --- CAMADA DO TEXTO ---
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
