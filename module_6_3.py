class Horse:
    """Класс Horse"""
    def __init__(self): # Конструктор класса Horse
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx): # Метод run
        self.x_distance += dx # увеличение дистанции на dx
        return self.x_distance


class Eagle:
    """Класс Eagle"""
    def __init__(self): # Конструктор класса Eagle
        self.y_distance = 0
        self.sound = 'I train, eat,sleep, and repeat'

    def fly(self, dy): # Метод fly
        self.y_distance += dy # увеличиваем высоту полета
        return self.y_distance


class Pegasus(Horse, Eagle):
    """Класс Pegasus, наследуемый от Horse и Eagle"""
    def __init__(self): # Конструктор класса Pegasus
        #super().__init__() # наследование атрибутов классов родителей
        Horse.__init__(self)
        Eagle.__init__(self)


    def move(self, dx, dy): # Метод move
        return super().run(dx), super().fly(dy)

    def get_pos(self): # Метод get_pos
        return self.x_distance, self.y_distance

    def voice(self): # Метод voice
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
print(Eagle.mro())
p1.voice()