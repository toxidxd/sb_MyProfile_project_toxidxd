# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
info = ''
# social links
vk = ''
telegram = ''
tiktok = ''


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    if info:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    elif option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Социальные сети и мессенджеры')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break

            elif option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')
                info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input social links
                vk = input('Введите адрес профиля Вконтакте: ')
                telegram = input('Введите логин Telegram: ')
                tiktok = input('Введите логин Tiktok: ')
            else:
                print('Введите корректный пункт меню')

    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break

            elif option2 == 1:
                general_info_user(name, age, phone, email, info)

            elif option2 == 2:
                general_info_user(name, age, phone, email, info)

                # print social links
                print('')
                print('Социальные сети и мессенджеры')
                print('Вконтакте:', vk)
                print('Telegram: ', telegram)
                print('Tiktok:   ', tiktok)
            else:
                print('Введите корректный пункт меню')

    else:
        print('Введите корректный пункт меню')
