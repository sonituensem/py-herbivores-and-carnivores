class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

        if key == "health" and hasattr(self, "health"):
            if value <= 0:
                object.__setattr__(self, "health", 0)
                if self in Animal.alive:
                    Animal.alive.remove(self)

    def __repr__(self):
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal):
        if not isinstance(animal, Herbivore):
            return
        if animal.hidden:
            return
        animal.health -= 50
