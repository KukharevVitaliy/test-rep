from typing import Any
import random

def bubble_sort(lst: list[Any]) -> list:
    """ Сортирует список lst методом пузырьковой сортировки (Bubble Sort) """
    for i in range(len(lst) - 1):
        lst = bubble_sort_step(lst)
    return lst

def bubble_sort_step(lst: list[Any]) -> list:
    """ Выполняет один проход пузырьковой сортировки (Bubble Sort) """
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def random_list(n, minn=1, maxx=10):
    """ Генерирует список из n случайных целых чисел в заданном диапазоне """
    lst = []
    for i in range(n):
        lst.append(random.randint(minn, maxx))
    return lst

def check_sort(lst: list[Any]) -> bool:
    """ Проверяет, отсортирован ли список по неубыванию."""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def test_sort(sort_func, n=20):
    # Критический случай №1: пустой список
    empty_lst = []
    empty_sorted = sort_func(empty_lst)

    if empty_sorted != []:
        print("Ошибка: сортировка пустого списка")
        print("Результат =", empty_sorted)
        return
    
    # Критический случай №2: список из одного элемента
    one_element_lst = [1]
    one_element_lst_sorted = sort_func(one_element_lst)
    if one_element_lst != one_element_lst_sorted or len(one_element_lst_sorted) != 1:
        print("Ошибка: некорректная сортировка списка из одного элемента")
        print("Результат =", one_element_lst_sorted)
        return
    
    #Критический случай №3: уже отсортированный список
    already_sorted_lst = [1, 2, 3, 4]
    already_sorted_lst_sorted_again = sort_func(already_sorted_lst)
    if already_sorted_lst_sorted_again != already_sorted_lst:
        print("Ошибка: Уже отсортированный список отсортирован некорректно")
        print("Результат =", already_sorted_lst_sorted_again)
        return
    
    #Критический случай №4: отсортированный список в обратном порядке
    reverse_sorted_lst = [5, 4, 3, 2, 1]
    reverse_sorted_lst_sorted_again = sort_func(reverse_sorted_lst)
    if reverse_sorted_lst_sorted_again != [1, 2, 3, 4, 5]:
        print("Ошибка: Отсортированный список в обратном порядке не отсортирован корректно")
        print("Результат =", reverse_sorted_lst_sorted_again)
        return
    
    # Критический случай №5: список с одинаковыми элементами (дубликаты)
    duplicates_lst = [3, 3, 3, 3, 3]
    duplicates_sorted = sort_func(duplicates_lst.copy())
    if duplicates_sorted != [3, 3, 3, 3, 3] or not check_sort(duplicates_sorted):
        print("Ошибка: некорректная сортировка списка с одинаковыми элементами")
        print("Результат =", duplicates_sorted)
        return
    
    # Критический случай №6: список с отрицательными числами
    negative_lst = [-5, -1, -3, 0, 2, -10]
    negative_sorted = sort_func(negative_lst.copy())
    if not check_sort(negative_sorted) or negative_sorted != [-10, -5, -3, -1, 0, 2]:
        print("Ошибка: некорректная сортировка списка с отрицательными числами")
        print("Результат =", negative_sorted)
        return
    
    # Критический случай №7: список с нулями
    zeros_lst = [5, 0, -3, 0, 2]
    zeros_sorted = sort_func(zeros_lst.copy())
    if not check_sort(zeros_sorted) or zeros_sorted != [-3, 0, 0, 2, 5]:
        print("Ошибка: некорректная сортировка списка с нулями")
        print("Результат =", zeros_sorted)
        return
    
    # Критический случай №8: список с большими числами
    large_numbers_lst = [1000000, 999999, 1000001, 500000]
    large_numbers_sorted = sort_func(large_numbers_lst.copy())
    if not check_sort(large_numbers_sorted):
        print("Ошибка: некорректная сортировка списка с большими числами")
        print("Результат =", large_numbers_sorted)
        return

    # Основной тест: случайный список
    lst = random_list(n)
    lst_sort = sort_func(lst)

    if check_sort(lst_sort):
        print("Функция работает корректно")
    else:
        print("Функция работает не правильно")
        print("Изначальный список =", lst)
        print("Отсортированный список =", lst_sort)

test_sort(bubble_sort, 50)