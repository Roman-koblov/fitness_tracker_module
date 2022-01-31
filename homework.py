from typing import Dict


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        training_info = (f'Тип тренировки: {self.training_type}; '
                         f'Длительность: {self.duration} ч.; '
                         f'Дистанция: {self.distance} км; '
                         f'Ср. скорость: {self.speed} км/ч; '
                         f'Потрачено ккал: {self.calories}.')
        return training_info


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        M_IN_KM = 1000
        LEN_STEP = 1
        m = LEN_STEP / M_IN_KM
        distance: float = round((self.action * m), 3)
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed: float = round((self.get_distance() / self.duration), 3)
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    training_type = 'RUN'

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        M_IN_KM = 1000
        x = self.weight / M_IN_KM * self.duration
        calories = (coeff_calorie_1 * self.get_mean_speed()) - coeff_calorie_2 * x
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    training_type = 'WLK'

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 heigh: float) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.heigh = heigh

    def get_spent_calories(self) -> float:
        y = 0.029 * self.weight * self.duration
        z = self.get_mean_speed() ** 2 // self.heigh
        calories = round((0.035 * self.weight + z * y), 3)
        return calories

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        M_IN_KM = 1000
        LEN_STEP = 0.65
        m = LEN_STEP / M_IN_KM
        distance: float = round((self.action * m), 3)
        return distance


class Swimming(Training):
    """Тренировка: плавание."""
    training_type = 'SWM'

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 lengh_pool,
                 count_pool) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.lengh_pool = lengh_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        M_IN_KM = 1000
        n = self.count_pool / M_IN_KM / self.duration
        speed: float = round((self.lengh_pool * n), 3)
        return speed

    def get_spent_calories(self) -> float:
        calories = round(((self.get_mean_speed() + 1.1) * 2 * self.weight), 3)
        return calories

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        M_IN_KM = 1000
        LEN_STEP = 1.38
        m = LEN_STEP / M_IN_KM
        distance: float = round((self.action * m), 3)
        return distance


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    read: Dict[str, Training] = {'SWM': Swimming,
                                 'RUN': Running,
                                 'WLK': SportsWalking}
    if workout_type in read:
        return read[workout_type](*data)


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
