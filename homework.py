from __future__ import annotations
class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories) -> None:


    def get_message(self) -> str:
        print(f'Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}.')


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 M_IN_KM = 1000,
                 LEN_STEP: float
                 ) -> None:
                  
        

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = round((action * LEN_STEP / M_IN_KM), 2)
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = round((distance / duration), 2)
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass 

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage() 


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        calories = round(((18 * speed – 20) * weight / M_IN_KM * duration), 2)
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 M_IN_KM = 1000,
                 LEN_STEP, heigh) -> None:
        super().__init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 M_IN_KM = 1000,
                 LEN_STEP)
        self.heigh = heigh         
    
    def get_spent_calories(self) -> float:
        calories = round(((0.035 * weigh + (speed ** 2 // heigh) * 0.029 * weigh) * duration), 2)
        return calories             


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 M_IN_KM = 1000,
                 LEN_STEP, lengh_pool, count_pool) -> None:
        super().__init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 M_IN_KM = 1000,
                 LEN_STEP)
        self.lengh_pool = lengh_pool
        self.count_pool = count_pool  
    
    def get_mean_speed(self) -> float:
        speed = round((lengh_pool * count_pool / M_IN_KM / duration), 2)
        return speed

    def get_spent_calories(self) -> float:
        calories = round(((speed + 1.1) * 2 * weigh), 2)
        return calories                       


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict = {'SWM' : Swimming, 'RUN' : Running, 'WLK' : SportWalking}
    params: list = data 
    training = dict[training_type]
    return params


def main(training: Training) -> None:
    """Главная функция."""
    return show_training_info(info: InfoMessage)
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
        