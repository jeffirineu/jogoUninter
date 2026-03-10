#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH


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
