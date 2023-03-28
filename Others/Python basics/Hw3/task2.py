# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить
# вывод данных о пользователе одной строкой.

def print_user_data(name, surname, year_of_birth, city, email, phone):
    """Функция обработки и вывода данных о пользователе.

    :param name: Имя
    :param surname: Фамилия
    :param year_of_birth: Год рождения
    :param city: Город проживания
    :param email: Email
    :param phone: Номер телефона
    :return: Полное описание одной строкой (str)
    """
    return f"Имя: {name} | Фамилия: {surname} | Год рождения: {year_of_birth} | Город проживания: {city} | E-mail: " \
           f"{email} | Телефон: {phone}"


print(print_user_data(name="Николай", surname="Пахомов", year_of_birth="1996", city="Москва", phone="8-800-555-35-35",
                      email="npakhomov@gmail.com"))
