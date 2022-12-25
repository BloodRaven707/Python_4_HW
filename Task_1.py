from os import system
from random import randint


from my_store import convert_to_polynomial, python_run_file_name, append_to_file


def main():
    print( "Программа формирует случайный список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. k натуральное число.\n" )

    # Валидатор пользовательского ввода...
    while True:
        if k := int( temp ) if ( temp := input("Введите натуральную степень многочлена: ") ).isdigit() else -1  >= 0:
            break
        else:
            print( "\n[!] Подсказка: Нужно ввести число (Например: 1). Число должно было не отричательным, т.е. больше или равное 0...\n" )

    # Кто придумывает эти задачи... зачем тут от -100 до 100... для отладки от -3 до 3 за глаза...
    min = -100
    max = 100

    # Как по мне список тут не нужен...
    params = [randint( min, max ) for _ in range( k + 1 )]

    res = convert_to_polynomial( k, params )

    # Пишем в файл, если файла нет, он создастся...
    file_name = f"./{python_run_file_name(__file__)}_res.txt"
    append_to_file( file_name, res )

    print( f"\n[+] {k = }. В файл { file_name } добавлена запись -> { res }")


if __name__ == "__main__":
    system( "cls" )

    main()
