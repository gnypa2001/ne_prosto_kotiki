from random import randint


cities = {"Dnipro": -10, "Kharkiv": 13, "Odesa": 27, "Lviv": -2, "Zaporizhzhia": 16, "Uzhhorod": 4, "Pavlohrad": 30, "Zhytomyr": 19, "Poltava": -15,  "Vinnytsia": 23, "Mykolaiv": 1, "Cherkasy": 12, "Chernivtsi":  0, "Sumy": -20, "Rivne": 4, "Lutsk": 13, "Kremenchuk": 22, "Ternopil": 6, "Nikopol": -2, "Lysychansk": 4, "Irpin": 12, "Enerhodar": 3, "Izium": 26, "Varash": -4, "Volodymyr": 11, "Chuhuiv": 14, "Khust": 18, "Boryspil": -13, "Yalta": 9, "Berdiansk": 28, "Luhansk": 14, "Donetsk":1, "Kyiv": 16}


def temps_in_cities():
    print(cities["Dnipro"], cities["Kharkiv"], cities["Kyiv"])
    print()
temps_in_cities()


def coldest_and_hottest():
    lowest = cities["Dnipro"]
    highest = cities["Dnipro"]

    for city in cities.values():
        if city <= lowest:
            lowest = city

        if city >= highest:
            highest = city

    for city in cities.keys():
        if cities[city] == lowest:
            print(f"{city} is the coldest city, it`s temp is {cities[city]}")

        if cities[city] == highest:
            print(f"{city} is the hottest city, it`s temp is {cities[city]}")
    print()
coldest_and_hottest()


def less_than_0_and_higher_than_20():
    for city in cities.keys():
        if cities[city] > 20:
            print(f"{city} temp is {cities[city]}")

        if cities[city] < 0:
            print(f"{city} temp is {cities[city]}")
    print()
less_than_0_and_higher_than_20()


def cities_starting_with_K_or_L():
    for city in cities.keys():
        if city[0] == "K" or city[0] == "L":
            print(f"{city} temp is {cities[city]}")
    print()
cities_starting_with_K_or_L()


def average_temp():
    sum = 0
    for city in cities.values():
        sum += city

    print(round(sum/len(cities.values()), 1))
    print()
average_temp()


def delete_cold_cities():
    copied_cities = cities.copy()
    for city in cities:
        if cities[city] < 0:
            copied_cities.pop(city)

    print(copied_cities)
    print()
delete_cold_cities()


def add_city():
    city = input("Введите название города: ")
    temp = int(input("Введите температуру: "))
    cities[city] = temp
    print(f"Город {city} успешно добавлен в словарь.")



def even_temp_cities():
    for city in cities.keys():
        if cities[city] % 2 == 0:
            print(f"{city} temp is {cities[city]}")
    print()
even_temp_cities()


def short_name_city():
    for city in cities:
        if len(city) <= 5:
            print(f"{city} temp is {cities[city]}")
    print()
short_name_city()


def delete_city():
    city = input("Введите название города, который нужно удалить: ")
    if city in cities:
        cities.pop(city)
        print(f"Город {city} успешно удален из словаря.")
    else:
        print(f"Город {city} не найден в словаре.")


def change_temp():
    city = input("Введите название города, температуру которого нужно изменить: ")
    if city in cities:
        temp = int(input("Введите новую температуру: "))
        cities[city] = temp
        print(f"Температура города {city} успешно изменена на {temp}.")
    else:
        print(f"Город {city} не найден в словаре.")


goroda = ['Dnipro', 'Kharkiv', 'Odesa', 'Lviv', 'Zaporizhzhia', 'Uzhhorod', 'Pavlohrad', 'Zhytomyr', 'Poltava', 'Vinnytsia', 'Mykolaiv', 'Cherkasy', 'Chernivtsi', 'Sumy', 'Rivne', 'Lutsk', 'Kremenchuk', 'Ternopil', 'Nikopol', 'Lysychansk', 'Irpin', 'Enerhodar', 'Izium', 'Varash', 'Volodymyr', 'Chuhuiv', 'Khust', 'Boryspil', 'Yalta', 'Berdiansk', 'Luhansk', 'Donetsk', 'Kyiv']
goroda_dict = {}
def new_slovar():
    for city in goroda:
        goroda_dict[city] = randint(-30, 30) 
    print(goroda_dict)  
new_slovar()
gorod = {key:randint(-30,30) for key in goroda}
print(gorod)
# while True:
#     print("1. Добавить город")
#     print("2. Удалить город")
#     print("3. Изменить температуру города")
#     print("4. Вывести список городов и их температур")
#     print("5. Выйти из программы")

#     choice = input("Введите номер действия: ")

#     if choice == "1":
#         add_city()
#     elif choice == "2":
#         delete_city()
#     elif choice == "3":
#         change_temp()
#     elif choice == "4":
#         print(cities)
#     elif choice == "5":
#         break

text = input()
count = 0
text.count
letters = {key:len([1 for letter in text if letter == key]) for key in text}
print(letters)

a = lambda a,x: a * x