'''
ООП - обьекто обективное програмирование
ООП - стиль програмирования

Класс - фабрика экземпляровб идея
Экземпляр - конкретная реализация объекта

class пишится с заглавной буквы
'''


class Player :
    def __init__(self, name: str, hp: int, attack_power: int) -> None:
        '''
        Кнструктор класса вызывается после экземпляра
        self - сылка на экземпляр
        '''
        self.name = name        
        self.hр = hp
        self.attack_power = 10

    def show(self) -> None:
        print(self.hр)
        print(self.name)

    def heal(self, ammount: int):
        self.hр += ammount

    def attack(self, anemy):
        if self.hp <= 0:
            return
        elif anemy.hp <= 0:
            return
        anemy.hp -= self.attack_power
        print(self.name, 'атаковал', anemy.name)
        self.show()
        self.hp -= anemy.attack_power
        print(anemy.name, 'атаковал', self.name)
        self.anemy.show()


class Game:
    def __init__(self) -> None:
        self.player = Player('вася', 100, 10)
        self.anemy = Player('ася', 100, 10) 
        self.is_running = False
        self.fight()

    def fight(self) -> None:
        while self.is_running:
            self.player.attack()
        #
    
Game()

