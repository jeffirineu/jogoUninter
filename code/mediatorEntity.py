from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.entity import Entity
from code.shotEnemy import ShotEnemy
from code.shotPlayer import ShotPlayer


class MediatorEntity:
    @staticmethod
    def __collision_window(ent: Entity):  # Método que só funciona dentro do mediator (__)
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.life = 0
        if isinstance(ent, ShotPlayer):
            if ent.rect.left  >= WIN_WIDTH:
                ent.life = 0
        if isinstance(ent, ShotEnemy):
            if ent.rect.left  <= 0:
                ent.life = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_t6 = entity_list[i]
            MediatorEntity.__collision_window(entity_t6)

    @staticmethod
    def verify_life(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.life <= 0:
                entity_list.remove(ent)


