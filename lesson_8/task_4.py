class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль марки {str(self.name).title()} поехал.'

    def stop(self):
        return f'Автомобиль марки {str(self.name).title()} остановился.'

    def turn(self, direction):
        return f'{str(self.color).title()} автомобиль повернул на {direction}.'

    def show_speed(self):
        return f'Скорость автомобиля {self.speed} км/ч.'


class TownCar(Car):
    def presentation(self):
        return f'{str(self.name).title()} лучший городской автомобиль.'

    def show_speed(self):
        if self.speed < 60:
            return f'Скорость автомобиля {self.speed} км/ч.'
        else:
            return f'Превышение скорости!'


class SportCar(Car):
    def presentation(self):
        return f'{str(self.name).title()} отличный спортивный автомобиль.'


class WorkCar(Car):
    def presentation(self):
        return f'{str(self.name).title()} рабочая лошадка.'

    def show_speed(self):
        if self.speed < 40:
            return f'Скорость автомобиля {self.speed} км/ч.'
        else:
            return f'Превышение скорости!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(PoliceCar, self).__init__(speed, color, name, is_police)
        if not self.is_police:
            raise TypeError("Автомобиль должен быть полицейским.")

    def presentation(self):
        return f'{str(self.name).title()} автомобиль МВД.'


if __name__ == '__main__':
    pc = PoliceCar('120', 'синий', 'Skoda', True)
