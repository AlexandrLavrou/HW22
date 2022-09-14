# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self):
        self.field = (50, 50)
        self.x = 0
        self.y = 0
        self.speed = 1

    def _get_speed(self, type_move):
        self.type_move = type_move
        if self.type_move == 'fly':
            return self.speed * 1.2
        elif self.type_move == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')

    def move(self, direction):

        if direction == 'UP':
            self.field.set_unit(y=self.y+self.speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y-self.speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x-self.speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x+self.speed, unit=self)