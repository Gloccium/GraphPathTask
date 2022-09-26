# Библиотека алгоритмов поиска пути на графе
Версия: 1

Автор: Сергеев Егор

# Описание
Данное приложение реализует алгоритмы поиска пути на графе с поддержкой весов,
в том числе отрицательных

# Требования
Python версии **3.10**

# Состав
Главный модуль c алгоритмами: `main.py`

Модули **edge**, **vertex**: `graph/`

Тесты: `test.py`

# Подробности реализации
В каталоге `graph` находятся модули **edge** и **vertex**.

Модуль **edge** отвечает за логику ребер графа,

а модуль **vertex** – за логику вершин.

В модуле `main` находится класс **Graph** с реализацией алгоритмов:
1) _Поиск в глубину_
2) _Поиск в ширину_
3) _Дейкстра_
4) _Беллман–Форд_

В модуле `test` тестируем алгоритмы на корректность работы