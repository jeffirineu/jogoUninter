#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity

'''''''''
Projeto: Atividade Prática - Jogo 2D (Uninter)
Autor: Jefferson Irineu Felipe da Silva - RU: [5037648]
Descrição: Classe responsável por gerenciar os cenários do jogo.
           Ela implementa a movimentação das camadas de fundo para criar
           a ilusão de profundidade e movimento contínuo (efeito parallax).
'''''''''


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # Bloco que da o esfeito parallax
        self.rect.x -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass
