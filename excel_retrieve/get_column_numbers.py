import pandas as pd


def get_cn(df):
    rows_nubmer = df.shape[0]
    columns_nubmer = df.shape[1]
    ctl = df.columns.tolist()

    # в таблице должны быть эти колонки
    cn_numbers = dict.fromkeys(['cn_idgroup', 'cn_pupil', 'cn_kurs', 'cn_price', 'cn_payment_done',
                                'cn_payment_remaining', 'cn_payment_recom', 'cn_client_fio', 'cn_client_phone',
                                'cn_client_email', 'cn_google', ], -1)

    # в таблице эти колонки могут отсутствовать
    cn_numbers_ = dict.fromkeys(
        ['cn_month9', 'cn_month10', 'cn_month11', 'cn_month12', 'cn_month1', 'cn_month2', 'cn_month3', 'cn_month4',
         'cn_month5', 'cn_month6', 'cn_month7', 'cn_month8', ], -2)

    # определение новеров каждой колонки
    for i in range(columns_nubmer):
        column_title_raw = ctl[i]
        column_title_ = ''.join(column_title_raw.split())  # удаление пробелов
        column_title = column_title_.lower()

        if 'idгруппы' in column_title:
            cn_numbers['cn_idgroup'] = i
            print('Колонка - ID группы, позиция= ', i)  # 1

        if 'фиоребенка' in column_title:
            cn_numbers['cn_pupil'] = i
            print('Колонка - ФИО ребенка, позиция= ', i)  # 2

        if 'номердоговора' in column_title:
            cn_numbers['cn_kurs'] = i
            print('Колонка - номер договора, позиция= ', i)  # 3

        if 'суммадоговора' in column_title:
            cn_numbers['cn_price'] = i
            print('Колонка - сумма договора, позиция= ', i)  # 4

        if 'оплачено' in column_title:
            cn_numbers['cn_payment_done'] = i
            print('Колонка - оплачено, позиция= ', i)  # 5

        if 'остаток' in column_title:
            cn_numbers['cn_payment_remaining'] = i
            print('Колонка - остаток, позиция= ', i)  # 6

        if 'фиородителя' in column_title:
            cn_numbers['cn_client_fio'] = i
            print('Колонка - ФИО родителя, позиция= ', i)  # 7

        if 'телефон' in column_title:
            cn_numbers['cn_client_phone'] = i
            print('Колонка - телефон, позиция= ', i)  # 8

        if 'емейл' in column_title:
            cn_numbers['cn_client_email'] = i
            print('Колонка - email, позиция= ', i)  # 9

        if 'аккаунтдлягугл' in column_title:
            cn_numbers['cn_google'] = i
            print('Колонка - гугл, позиция= ', i)  # 10

        if 'рекомендуемый' in column_title:
            cn_numbers['cn_payment_recom'] = i
            print('Колонка - остаток, позиция= ', i)  # 12

        # колонки по месяцам

        if 'сентябрь' in column_title:
            cn_numbers_['cn_month9'] = i
            print('Колонка - сентябрь, позиция= ', i)

        if 'октябрь' in column_title:
            cn_numbers_['cn_month10'] = i
            print('Колонка - октябрь, позиция= ', i)

        if 'ноябрь' in column_title:
            cn_numbers_['cn_month11'] = i
            print('Колонка - ноябрь, позиция= ', i)

        if 'декабрь' in column_title:
            cn_numbers_['cn_month12'] = i
            print('Колонка - декабрь, позиция= ', i)

        if 'январь' in column_title:
            cn_numbers_['cn_month1'] = i
            print('Колонка - январь, позиция= ', i)

        if 'февраль' in column_title:
            cn_numbers_['cn_month2'] = i
            print('Колонка - февраль, позиция= ', i)

        if 'март' in column_title:
            cn_numbers_['cn_month3'] = i
            print('Колонка - март, позиция= ', i)

        if 'апрель' in column_title:
            cn_numbers_['cn_month4'] = i
            print('Колонка -апрель , позиция= ', i)

        if 'май' in column_title:
            cn_numbers_['cn_month5'] = i
            print('Колонка - май, позиция= ', i)

        if 'июнь' in column_title:
            cn_numbers_['cn_month6'] = i
            print('Колонка - июнь, позиция= ', i)

        if 'июль' in column_title:
            cn_numbers_['cn_month7'] = i
            print('Колонка - июль, позиция= ', i)

        if 'август' in column_title:
            cn_numbers_['cn_month8'] = i
            print('Колонка - август, позиция= ', i)

    empty = []
    for key in cn_numbers:
        if cn_numbers[key] == -1:
            empty.append(key)

    if -1 in cn_numbers.values():
        print()
        print('ОШИБКА В ФОРМАТЕ EXCEL-ФАЙЛА, НЕ ОПРЕДЕЛЕНЫ КОЛОНКИ', empty)
        import utils.shared
        utils.shared.notice_retr = "НЕТ КОЛОНОК"
        raise Exception('ОШИБКА В ФОРМАТЕ EXCEL-ФАЙЛА, НЕ ОПРЕДЕЛЕНЫ КОЛОНКИ')
    else:
        print('НОМЕРА КОЛОНОК EXCEL-ФАЙЛА ОПРЕДЕЛЕНЫ')

    return cn_numbers, cn_numbers_
