from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from enum import Enum
import matplotlib.pyplot as plt


def PR(*args):

    for a in args:

        print(a)

class User:

    def __init__(self, name, surname) -> None:
        
        self.name = name
        self.surname = surname


# Регистрируем обработчики
if __name__ == '__main__':
    
    

    # Данные о доходах по категориям
    income_by_category = {
        'Зарплата': 5000,
        'Аренда': 2000,
        'Инвестиции': 1500
    }

    # Получение категорий и сумм доходов
    categories = list(income_by_category.keys())
    incomes = list(income_by_category.values())

    # Создание более нейтральной палитры цветов
    colors = ['#d24a43', '#f6d4a0', '#a1ad82', '#33464c']

    # Создание круговой диаграммы с настройками для отображения только секторов и надписей внутри
    plt.figure(figsize=(8, 8), facecolor='#d2d2d2')
    plt.pie(incomes, labels=categories, colors=colors, wedgeprops={'edgecolor': '#d2d2d2', 'linewidth': 2}, autopct='', startangle=140)
    plt.axis('equal')  # Сделать круговую диаграмму круглой


    plt.show()


    pass

    
