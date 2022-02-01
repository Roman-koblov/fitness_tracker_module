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
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance: float = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed: float = self.get_distance() / self.duration
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
    M_IN_KM = 1000

    def get_spent_calories(self) -> float:
        coeff_1 = 18
        coeff_2 = 20
        run_cal_x = (coeff_1 * self.get_mean_speed() - coeff_2)
        run_cal_y = (self.duration * 60)
        calories: float = run_cal_x * self.weight / self.M_IN_KM * run_cal_y
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    training_type = 'WLK'
    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.height = height

    def get_spent_calories(self) -> float:
        wlk = self.duration * 60
        wlk_2 = self.get_mean_speed()
        wlk_3 = self.weight
        wlk_4 = self.height
        calories = (0.035 * wlk_3 + wlk_2 ** 2 // wlk_4 * 0.029 * wlk_3) * wlk
        return calories

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        wlk_dist_x = self.LEN_STEP / self.M_IN_KM
        distance: float = self.action * wlk_dist_x
        return distance


class Swimming(Training):
    """Тренировка: плавание."""
    training_type = 'SWM'
    M_IN_KM = 1000
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool,
                 count_pool) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        swm_1 = self.length_pool * self.count_pool
        speed: float = swm_1 / self.M_IN_KM / self.duration
        return speed

    def get_spent_calories(self) -> float:
        cal_x = (self.get_mean_speed() + 1.1)
        calories: float = cal_x * 2 * self.weight
        return calories

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        m = self.LEN_STEP / self.M_IN_KM
        distance: float = self.action * m
        distance = round((distance), 3)
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
