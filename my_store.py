def convert_to_polynomial( size: int, lt: list ) -> str:
    result = ""

    for i, x in enumerate( lt ):
        # x = randint( min, max + 1 )  # будет тоже но без списка
        if x == 0:
            continue

        if result == "":
            if x in [1, -1]:
                if x == -1:
                    result += "-"
            else:
                result += f"{ x }"
        else:
            result += " + " if x >= 0 else " - "
            if x not in [1, -1]:
                result += f"{ abs( x ) }"

        if size != i and result != "" and result[-1].isdigit():
            result += "*"

        if size - i == 1:
            result += f"x"
        elif size != i:
            result += f"x^{ size - i }"

    return result + " = 0\n"


def append_to_file( file_name: str, data: str ):
    with open( file_name, "a" ) as f:
        f.write( data )


def python_run_file_name( path: str ):
    return path[path.rfind( "/" ) + 1:path.rfind( "." )]
