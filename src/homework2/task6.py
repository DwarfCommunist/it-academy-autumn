"""Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).  Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)
"""


def palindrom(n):
    """Поиск числа фибоначчи.

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """

    # write your code here

    temp = n
    result_number = 0
    while temp != 0:
        result_number = result_number * 10 + (temp % 10)
        temp //= 10

    if n != result_number:
        return False
    else:
        return True


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    print(palindrom(n))
