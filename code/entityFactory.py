#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT, LIMIT_SPAWN_WIDTH, LIMIT_SPAWN_HEIGHT, LIMIT_SPAWN_TOP
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'DemoBg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'DemoBg{i}', (0, 0)))
                    list_bg.append(Background(f'DemoBg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'PlayerMan':
                return Player('PlayerMan', (10, WIN_HEIGHT/2))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH +10, random.randint(LIMIT_SPAWN_TOP, LIMIT_SPAWN_HEIGHT)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH +10, random.randint(LIMIT_SPAWN_TOP, LIMIT_SPAWN_HEIGHT)))
            # case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH +10, random.randint(0, WIN_HEIGHT)))

        return None



