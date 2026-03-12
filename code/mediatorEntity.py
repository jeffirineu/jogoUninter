from code.enemy import Enemy
from code.entity import Entity


class MediatorEntity:
    @staticmethod
    def __collision_window(ent: Entity):  # Método que só funciona dentro do mediator (__)
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
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


