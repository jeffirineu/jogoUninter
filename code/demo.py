#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_HALF_BLACK, WIN_WIDTH, WIN_HEIGHT, C_HALF_RED
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.mediatorEntity import MediatorEntity
from code.player import Player


# Classe responsável por gerir a tela do Game
class Demo:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(
            EntityFactory.get_entity('DemoBg'))  # adiciona à lista o retorno do caso DeboBg vindo da fábrica
        self.entity_list.append(
            EntityFactory.get_entity('PlayerMan'))  # adiciona à lista o retorno do caso PlayerMan vindo da fábrica
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        self.life_player = True
        self.life_player = True
        self.end = False

    # Bloco executável
    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')  # Musica de fundo
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        timeout = 30000  # Tem máximo que dura uma partida do demo em milissegundos
        start_time = pygame.time.get_ticks()
        # Loop principal que roda a demonstração com personagens e inimigos
        while True:
            if self.life_player:
                clock.tick(60)  # Definição de quadros que o jogo roda
                for list_item in self.entity_list:  # varre a lista em buca das entidades que serão impressas
                    self.window.blit(source=list_item.surf, dest=list_item.rect)
                    list_item.move()  # Chama a função de movimento de cada entidade da lista
                    if isinstance(list_item, (Player, Enemy)):
                        shoot = list_item.shoot()  # Variável que recebe a função de disparo de cada entidade da lista
                        if shoot is not None:
                            self.entity_list.append(
                                shoot)  # Se a função não nula ele adiciona o disparo na lista de impressão
                    # Imprime a vida do jogador
                    if list_item.name == 'PlayerMan':
                        self.demo_text(20,
                                       f'LIFE: {list_item.life}',
                                       C_GREEN,
                                       (10, 10),
                                       C_HALF_BLACK
                                       )
                    # imprime a quantidade de inimigos mortos
                    if list_item.name == 'PlayerMan':
                        self.demo_text(20,
                                       f'ABATES: {list_item.score}',
                                       C_GREEN,
                                       (10, 30),
                                       C_HALF_BLACK
                                       )
            if self.life_player and not self.end:
                tempo_passado = pygame.time.get_ticks() - start_time
                seconds_remaining = max(0, (timeout - tempo_passado) // 1000)
                self.demo_text(20, f'TEMPO: {seconds_remaining}s', C_GREEN,
                               (WIN_WIDTH / 2, 10), center_text=True)
                if tempo_passado >= timeout:
                    self.end = True

            else:  # Imprime a tela de GAME OVER
                self.demo_end('GAME OVER')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            pygame.display.flip()

            MediatorEntity.verify_collision(entity_list=self.entity_list)
            MediatorEntity.verify_collision(entity_list=self.entity_list)

            # Se a verificação retornar True (player morreu)
            if MediatorEntity.verify_life(entity_list=self.entity_list):
                self.life_player = False
            pass

    def demo_end(self, text: str):
        pelicula = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        pelicula.fill((0, 0, 0))
        pelicula.set_alpha(150)
        self.window.blit(pelicula, (0, 0))
        self.demo_text(50,
                       text,
                       C_HALF_RED,
                       (WIN_WIDTH / 2, WIN_HEIGHT / 2),
                       center_text=True
                       )

    # Função para imprimir texto na tela
    def demo_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple,
                  bg_color: tuple = None, bold: bool = None, center_text: bool = False):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size, bold=bold)
        text_surf: Surface = text_font.render(text, True, text_color, bg_color).convert_alpha()
        if center_text:
            text_rect: Rect = text_surf.get_rect(center=text_pos)
        else:
            text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)
