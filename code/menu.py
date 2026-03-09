#!/usr/bin/python
# -*- coding: utf-8 -*-
from msilib.schema import Font

import pygame.image
from pygame import Surface, Rect

from code.Const import WIN_WIDTH


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
            self.menu_text(text_size=70, text="Game Uni", text_color=(255, 255, 255), text_center_pos=(WIN_WIDTH / 2, 120))
            pygame.display.flip()
            # check for all events by click
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, shadow_color=(20, 20, 20),
                  offset=3):
        # 1. Cria a fonte
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)

        # --- CAMADA DA SOMBRA ---
        # Renderiza o texto com a cor da sombra
        shadow_surf = text_font.render(text, True, shadow_color).convert_alpha()

        # Posiciona a sombra levemente deslocada (ex: 3 pixels para direita e baixo)
        shadow_pos = (text_center_pos[0] + offset, text_center_pos[1] + offset)
        shadow_rect = shadow_surf.get_rect(center=shadow_pos)

        # Desenha a sombra primeiro (camada de baixo)
        self.window.blit(shadow_surf, shadow_rect)

        # --- CAMADA DO TEXTO PRINCIPAL ---
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)

        # Desenha o texto por cima da sombra
        self.window.blit(text_surf, text_rect)
