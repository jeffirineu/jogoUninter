#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED, ENTITY_DELAY_SHOT
from code.entity import Entity
from code.shotEnemy import ShotEnemy


# Entidade que traz as características dos inimigos

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_DELAY_SHOT

    def move(self, ):
        self.rect.x -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_DELAY_SHOT  # Essa linha aplica o delay entre um disparo e outro
            return ShotEnemy(name='Plasma2', position=(self.rect.left - 30, self.rect.bottom - 40))
        return None
