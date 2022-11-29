# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
info = ''
# taxes info
ogrnip = 0
inn = 0
# bank info
payment_account = 0
bank_name = ''
bik = 0
correspondent_account = 0
# post_address info
post_address = ''
post_index = ''


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, info_parameter):
    print(SEPARATOR)
    print('Имя:    {0}'.format(name_parameter))
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст: {0} {1}'.format(age_parameter, years_parameter))
    print('Телефон: {0}'.format(phone_parameter))
    print('E-mail: {0}'.format(email_parameter))
    if info:
        print('Дополнительная информация: \n{0}'.format(info_parameter))
    print()


def taxes_info(ogrnip_parameter, inn_parameter):
    print("ОГРНИП: {0}".format(ogrnip_parameter))
    print("ИНН: {0}".format(inn_parameter))
    print()


def bank_info(payment_account_parameter, bank_name_parameter, bik_parameter, correspondent_account_parameter):
    print("Расчетный счет: {0}".format(payment_account_parameter))
    print("Название банка: {0}".format(bank_name_parameter))
    print("БИК: {0}".format(bik_parameter))
    print("Корреспондентский счет: {0}".format(correspondent_account_parameter))
    print()


def post_address_info(post_address, post_index):
    print('Почтовый адрес: {0}'.format(post_address))
    print('Почтовый индекс: {0}'.format(post_index))


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
            print('2 - Налоговая информация')
            print('3 - Банковские реквизиты')
            print('4 - Почтовый адрес')
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

                user_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in user_phone:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')
                info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input taxes info
                while True:
                    ogrnip = input('Введите ОГРНИП: ')
                    if len(ogrnip) == 15:
                        break
                    else:
                        print('Проверьте ввод. Ожидалось 15 знаков, вместо {0}.'.format(len(ogrnip)))

                inn = input('Введите ИНН: ')

            elif option2 == 3:
                # input bank info
                while True:
                    payment_account = input('Введите расчетный счет: ')
                    if len(payment_account) == 20:
                        break
                    else:
                        print('Проверьте ввод. Ожидалось 20 знаков, вместо {0}.'.format(len(payment_account)))

                bank_name = input('Введите название банка: ')
                bik = input('Введите БИК: ')
                correspondent_account = input('Введите корреспондентский счет: ')

            elif option2 == 4:
                # input post post_address info
                post_address = input('Введите почтовый адрес: ')
                temp_index = input('Введите почтовый индекс: ')
                for ch in temp_index:
                    if '0' <= ch <= '9':
                        post_index += ch

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
                taxes_info(ogrnip, inn)
                bank_info(payment_account, bank_name, bik, correspondent_account)
                post_address_info(post_address, post_index)
            else:
                print('Введите корректный пункт меню')

    else:
        print('Введите корректный пункт меню')
