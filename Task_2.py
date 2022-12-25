from os import system


from my_store import convert_to_polynomial, python_run_file_name, append_to_file


def main():
    print( "Программа читает 2 файла,в каждом из которых находится запись многочлена и записывает их сумму в новый файл.\n" )

    data = []
    k = 0
    for i in range( 2 ):
        with open( f"./Task_2.{i + 1}_data.txt" ) as f:
            new_data = f.readline()

        new_k = int( new_data[new_data.find( "x^" ) + 2:new_data.find( " ", new_data.find( "x^" )) ] )
        data.append( new_data.strip() )

        if new_k > k:
            k = new_k

    params = [0 for _ in range( k + 1 )]
    for el in data:
        print(el)
        for i in range( k + 1 ):
            x = 0
            # Если минус, запимнить, что число отрицательное
            if el[0] == "-":
                x = -1
                # отступ у второго и последующих
                if el[1] == " ":
                    el = el[2:]
                else:
                    el = el[1:]
            # Отрезаем +
            elif el[0] == "+":
                x = 1
                el = el[2:]
            # Первый без минуса, отрезать не нужно
            else:
                x = 1

            # Получаем элемент для списка значений
            if el[0] == "x":
                x *= 1
            elif el.find( "*" ) != -1:
                x *= int( el[:el.find( "*" )] )
            else:
                x *= int( el[:el.find( " " )] )

            if el.find( "x" ) == -1:
                params[k] += x
                break

            # Получить степень (k - степень = индекс)
            if el[el.find( "x" ) + 1] == "^":
                params[k - int( el[el.find( "x" ) + 2:el.find( " " )] )] += x
            else:
                params[k - 1] += x

            el = el[el.find(" ") + 1:]


    res = convert_to_polynomial( k, params )

    # Пишем в файл, если файла нет, он создастся...
    file_name = f"./{python_run_file_name(__file__)}_res.txt"
    append_to_file( file_name, res )

    print( f"\n[+] {k = }. В файл { file_name } добавлена запись -> { res }")


if __name__ == "__main__":
    system( "cls" )

    main()
