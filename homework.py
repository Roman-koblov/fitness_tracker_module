from __future__ import annotations
class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories) -> None:
        self.training_type = training_type
        self.duration = duration 
        self.distance = distance 
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        training_info = (f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}.')
        return training_info

class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 LEN_STEP: float, 
                 M_IN_KM = 1000
                 ) -> None:
        self.actions = action
        self.duration = duration
        self.weight = weight
        self.M_IN_KM = M_IN_KM
        self.LEN_STEP = LEN_STEP
        

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = round((self.action * self.LEN_STEP / self.M_IN_KM), 3)
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed: float = round((self.distance / self.duration), 3)
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass 

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage() 


class Running(Training):
    """Тренировка: бег."""
    training_type = 'RUN'
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        calories = (coeff_calorie_1 * self.speed) - coeff_calorie_2  * self.weight / self.M_IN_KM * self.duration
        
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    training_type = 'WLK'
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 LEN_STEP, 
                 heigh, 
                 hM_IN_KM = 1000) -> None:
        super().__init_(self,
                 action: int, 
                 duration: float,
                 weight: float, 
                 M_IN_KM = 1000,
                 LEN_STEP)
        self.heigh = heigh         
    
    def get_spent_calories(self) -> float:
        calories = round(((0.035 * self.weigh + (self.speed ** 2 // self.heigh) * 0.029 * self.weigh) * self.duration), 3)
        return calories             


class Swimming(Training):
    """Тренировка: плавание."""
    training_type = 'SWM'
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 LEN_STEP, 
                 lengh_pool, 
                 count_pool, 
                 M_IN_KM = 1000) -> None:
        super().__init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 M_IN_KM = 1000,
                 LEN_STEP)
        self.lengh_pool = lengh_pool
        self.count_pool = count_pool  
    
    def get_mean_speed(self) -> float:
        speed: float = round((self.lengh_pool * self.count_pool / self.M_IN_KM / self.duration), 3)
        return speed

    def get_spent_calories(self) -> float:
        calories = round(((self.speed + 1.1) * 2 * self.weigh), 3)
        return calories                       


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    read: dict = {'SWM' : Swimming, 'RUN' : Running, 'WLK' : SportsWalking}
    if read.get(workout_type) is None: 
        return read[workout_type](*data) 


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
