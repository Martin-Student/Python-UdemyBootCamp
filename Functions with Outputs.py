# Functions with outputs

name = input("Podaj imię: ")
surname = input("Podaj nazwisko: ")
def format_name(first_name, second_name):
    first = first_name.title()
    second = second_name.title()
    final_result = first + " " + second
    return print(final_result)

format_name(name, surname)


