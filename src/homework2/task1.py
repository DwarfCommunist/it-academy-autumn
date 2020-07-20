"""Напишите программу, которая считает общую цену.

   Вводится M рублей и N копеек цена, а также количество S товара Посчитайте
   общую цену в рублях и копейках за L товаров.
"""


def total_sum(m, n, s):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here

    rub_count = m * s
    cents_count = n * s

    cents_to_rub = cents_count // 100

    result_cents = cents_count % 100
    result_rub = rub_count + cents_to_rub
    return '%d rubles %d kopecks' % (result_rub, result_cents)   # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = '', '', ''
    print(total_sum(m, n, s))
