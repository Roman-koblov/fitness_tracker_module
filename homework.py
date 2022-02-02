from typing import Dict, Optional
from dataclasses import dataclass, asdict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    info_message: str = ('Тип тренировки: {training_type}; '
                         + 'Длительность: {duration:.3f} ч.; '
                         + 'Дистанция: {distance:.3f} км; '
                         + 'Ср. скорость: {speed:.3f} км/ч; '
                         + 'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        return self.info_message.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: float = 1000
    LEN_STEP: float = 0.65
    HR_TO_MIN: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action_count = action
        self.duration_hr = duration
        self.weight_kg = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance_km: float = self.action_count * self.LEN_STEP / self.M_IN_KM
        return distance_km

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed_kph: float = self.get_distance() / self.duration_hr
        return speed_kph

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(
            'Данные о потраченных каллориях не получены.')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration_hr,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
    CALORIES_MEAN_SPEED_SUBSTRACT: int = 20
    # Были проблемы с присвоением названий этим коэффицентам
    # было не всегда понятно, что они значат в формулах.

    def get_spent_calories(self) -> float:
        calories_kkal: float = (
            (self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
             - self.CALORIES_MEAN_SPEED_SUBSTRACT) * self.weight_kg
            / self.M_IN_KM * (self.duration_hr * self.HR_TO_MIN)
        )
        return calories_kkal


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    WEIGHT_MULTIPLIER: float = 0.035
    HEIGHT_MULTIPLIER: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.height_m: float = height

    def get_spent_calories(self) -> float:
        calories_kkal: float = (
            (self.WEIGHT_MULTIPLIER * self.weight_kg + self.get_mean_speed()
             ** 2 // self.height_m * self.HEIGHT_MULTIPLIER * self.weight_kg)
            * (self.duration_hr * self.HR_TO_MIN)
        )
        return calories_kkal

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance_km: float = self.action_count * self.LEN_STEP / self.M_IN_KM
        return distance_km


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    MEAN_SPEED_SUMMAND: float = 1.1
    CALORIES_MEAN_SPEED_MULTIPLIER: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool,
                 count_pool) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.length_pool_m: float = length_pool
        self.count_pool: float = count_pool

    def get_mean_speed(self) -> float:
        speed_kph: float = (
            self.length_pool_m * self.count_pool
            / self.M_IN_KM / self.duration_hr
        )
        return speed_kph

    def get_spent_calories(self) -> float:
        calories_kkal: float = (
            (self.get_mean_speed() + self.MEAN_SPEED_SUMMAND)
            * self.CALORIES_MEAN_SPEED_MULTIPLIER * self.weight_kg
        )
        return calories_kkal

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance_km: float = self.action_count * self.LEN_STEP / self.M_IN_KM
        return distance_km


def read_package(workout_type: str, data: Optional[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    trainings: Dict[str, Training] = {'SWM': Swimming,
                                      'RUN': Running,
                                      'WLK': SportsWalking}
    if workout_type in trainings:
        return trainings[workout_type](*data)
    if workout_type not in trainings:
        raise ValueError('Не удалось определить тип тренировки')


def main(training: Training):
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
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
