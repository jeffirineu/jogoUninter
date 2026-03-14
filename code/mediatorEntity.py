from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.entity import Entity
from code.player import Player
from code.shotEnemy import ShotEnemy
from code.shotPlayer import ShotPlayer


class MediatorEntity:
    @staticmethod
    def __collision_window(ent: Entity):  # Método que só funciona dentro do mediator (__)
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.life = 0
        if isinstance(ent, ShotPlayer):
            if ent.rect.left >= WIN_WIDTH:
                ent.life = 0
        if isinstance(ent, ShotEnemy):
            if ent.rect.left <= 0:
                ent.life = 0

    @staticmethod
    def __collision_entity(ent1, ent2):
        interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, ShotPlayer):
            interaction = True
        elif isinstance(ent1, ShotPlayer) and isinstance(ent2, Enemy):
            interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, ShotEnemy):
            interaction = True
        elif isinstance(ent1, ShotEnemy) and isinstance(ent2, Player):
            interaction = True

        if interaction:  # if interaction: é o mesmo que if interaction == True
            if (ent1.rect.left >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.life -= ent2.damage
                ent2.life -= ent1.damage
                ent1.last_damage = ent2.name
                ent2.last_damage = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_damage == 'Plasma1':
            for ent in entity_list:
                if ent.name == 'PlayerMan':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_t1 = entity_list[i]
            MediatorEntity.__collision_window(entity_t1)
            for j in range(i + 1, len(entity_list)):
                entity_t2 = entity_list[j]
                MediatorEntity.__collision_entity(entity_t1, entity_t2)

    @staticmethod
    def verify_life(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.life <= 0:
                if isinstance(ent, Enemy):
                    MediatorEntity.__give_score(ent, entity_list)
                entity_list.remove(ent)
