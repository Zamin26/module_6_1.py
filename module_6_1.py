class Animal:
    alive = True                # атрибуты животного
    fed = False
    def __init__(self,name):
        self.name = name

    def eat(self, food):
        if food.edible:                         # если растение съедобное
            print(f'{self.name} съел {food.name} ')
            self.fed = True  # питомец накормлен
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False                  # питомец неживой

class Mammal(Animal):
    pass
class Predator(Animal):
    pass


class Plant:
    edible = False                  # атрибуты растения, несъедобное
    def __init__(self,name):
        self.name = name

class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True              # переопределён при наследовании на съедобное по условию




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.