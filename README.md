# Модуль расчёта и отображения полной информации о тренировках по данным от блока датчиков.

Программный модуль по методологии ООП для расчёта и отображения информации
о прошедшей тренировке по данным от блока датчиков.

Над проектом трудился
[Роман Коблов](https://github.com/Roman-koblov/)

## Какие технологии и пакеты использовались:

* Python 3.8
* attrs 21.2.0
* flake8 4.0.1
* importlib-metadata 4.8.1
* iniconfig 1.1.1
* mccabe 0.6.1
* packaging 21.0
* pluggy 1.0.0
* py 1.10.0
* pycodestyle 2.8.0
* pyflakes 2.4.0
* pyparsing 2.4.7
* pytest 6.2.5
* pytest-tldr 0.2.4
* toml 0.10.2
* typing-extensions 3.10.0.2
* zipp 3.6.0

## Функционал проекта

### __Базовый класс__
```python
class Training
```
##### Свойства класса

* action — основное считываемое действие во время тренировки (шаг — бег, ходьба; гребок — плавание);
* duration — длительность тренировки;
* weight — вес спортсмена;
* M_IN_KM = 1000 — константа для перевода значений из метров в километры;
* LEN_STEP — расстояние, которое спортсмен преодолевает за один шаг или гребок. Один шаг — это  `0.65` метра, один гребок — `1.38` метра.

##### Методы класса

* get_distance() — метод возвращает значение дистанции, преодолённой за тренировку.
```python
# базовая формула расчёта
шаг * LEN_STEP / M_IN_KM
```
* get_mean_speed() — метод возвращает значение средней скорости движения во время тренировки.
```python
# базовая формула расчёта
дистанция / длительность
```
* get_spent_calories() — метод возвращает число потраченных калорий.
* show_training_info() — метод возвращает объект класса сообщения.

### Классы-наследники:
__Класс беговой тренировки__
```python
class Running
```
##### Свойства класса
наследуются

##### Методы класса
переопределить метод:
* get_spent_calories() — метод возвращает число потраченных калорий.
```python
# формула расчёта
(18 * средняя_скорость – 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
```
---
---
__Класс спортивной ходьбы__
```python
class SportsWalking
```
##### Свойства класса
Добавляемые свойства:
* height — рост

##### Методы класса
переопределить метод:
* get_spent_calories() — метод возвращает число потраченных калорий.
```python
# формула расчёта
(0.035 * вес + (скорость ** 2 // рост) * 0.029 * вес) * время_тренировки_в_минутах
```
---
---
__Класс тренировки в бассейне__
```python
class Swimming
```
##### Свойства класса
Добавляемые свойства:
* length_pool — длина бассейна;
* count_pool — количество проплытых бассейнов.

##### Методы класса
переопределить метод:
* get_mean_speed() — метод возвращает значение средней скорости движения во время тренировки.
```python
# формула расчёта
длина_бассейна * count_pool / M_IN_KM / время_тренировки
```
* get_spent_calories() — метод возвращает число потраченных калорий.
```python
# формула расчёта
(скорость + 1.1) * 2 * вес
```
### __Класс информационного сообщения__
```python
class InfoMessage
```
##### Свойства класса
* training_type — тип тренировки;
* duration — длительность тренировки;
* distance — дистанция, преодолённая за тренировку;
* speed — средняя скорость движения;
* calories — потраченные за время тренировки килокалории.


##### Методы класса

* get_message() — метод возвращает строку сообщения.
```python
# выводимое сообщение
# все значения типа float округляются до 3 знаков после запятой
'Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}'.
```

### Функции модуля
```python
def read_package()
```
* Функция read_package() принимает на вход код тренировки и список её параметров.
* Функция должна определить тип тренировки и создать объект соответствующего класса,
передав ему на вход параметры, полученные во втором аргументе. Этот объект функция должна вернуть.

---
---
```python
def main(training)
```
Функция `main()` должна принимать на вход экземпляр класса `Training`.

– При выполнении функции `main()`для этого экземпляра должен быть вызван метод `show_training_info()`;
результатом выполнения метода должен быть объект класса `InfoMessage`, его нужно сохранить в переменную `info`.
– Для объекта `InfoMessage`, сохранённого в переменной `info`, должен быть вызван метод,
который вернёт строку сообщения с данными о тренировке; эту строку нужно передать в функцию `print()`.

## Как разместить и запустить проект

Клонировать репозиторий и перейти в него в командной строке:

<pre><code>git clone [https://github.com/Roman-koblov/fitness_tracker_module]</code>

<code>cd fitness_tracker_module</code></pre>

Cоздать и активировать виртуальное окружение:

<pre><code>python3 -m venv venv source venv/bin/activate</code></pre>

Установить зависимости из файла requirements.txt:

<pre><code>python -m pip install --upgrade pip</code>

<code>pip install -r requirements.txt</code></pre>
