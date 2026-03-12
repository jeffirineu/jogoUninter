#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code import entityFactory
from code.const import EVENT_ENEMY, SPAWN_TIME, C_WHITE, WIN_HEIGHT, C_GREEN
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.mediatorEntity import MediatorEntity


class Demo:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('DemoBg'))
        self.entity_list.append(EntityFactory.get_entity('PlayerMan'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)


    def run(self):
        # pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        # pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            #contagem de entity
            self.demo_text(20,
                           f'{len(self.entity_list)} - Entitys',
                           False,
                           C_GREEN,
                           (10, WIN_HEIGHT - 50)
                           )
            pygame.display.flip()

            MediatorEntity.verify_collision(entity_list=self.entity_list)
            MediatorEntity.verify_life(entity_list=self.entity_list)
            pass

    def demo_text(self, text_size: int, text: str,bold: bool, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size, bold=bold, italic=False)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)
