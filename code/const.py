#C
import pygame

C_WHITE = (255, 255, 255)
C_HALF_BLACK = (20, 20, 20)
C_HALF_RED = (255, 0, 0)
C_GOLD = (212, 175, 55)
C_GREEN = (0, 240, 0)

#E
EVENT_ENEMY = pygame.USEREVENT
ENTITY_SPEED = {
    'DemoBg0': 0,
    'DemoBg1': 0.55,
    'DemoBg2': 1,
    'DemoBg3': 2,
    'PlayerMan': 5,
    'Enemy1': 4,
    'Enemy2': 3,
    'Plasma1': 12,
    'Plasma2': 11
}
ENTITY_LIFE = {
    'DemoBg0': 999,
    'DemoBg1': 999,
    'DemoBg2': 999,
    'DemoBg3': 999,
    'PlayerMan': 300,
    'Enemy1': 30,
    'Enemy2': 80,
    'Plasma1': 1,
    'Plasma2': 1
}

ENTITY_DELAY_SHOT = 50

#M
M_MENU_SELECT = ('INICIAR DEMO', 'SAIR')
M_COMMAND_KEYS = ('ESPAÇO: ATIRAR', 'SETAS: MOVER')



#W
WIN_WIDTH = 576
WIN_HEIGHT = 324


#SPAWN
SPAWN_TIME = 5000
LIMIT_SPAWN_WIDTH = (WIN_WIDTH + 10)
LIMIT_SPAWN_HEIGHT = (WIN_HEIGHT - 80)
LIMIT_SPAWN_TOP = 50