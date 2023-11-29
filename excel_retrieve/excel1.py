import pandas as pd
import excel_retrieve.get_column_numbers as gcn
from configuration import listing
from excel_retrieve.record import get_record
import logit.logsetting
import traceback

logger=logit.logsetting.logger

def excel1_go(file, number_or_lines):
    import utils.shared
    import os.path
    if os.path.isfile(file):
        print('ФАЙЛ ПРИСУТСТВУЕТ ')
    else:
        print('ОШИБКА: ФАЙЛА НЕТ ')
        utils.shared.notice_retr = 'ОШИБКА: ФАЙЛА НЕТ '
        raise Exception('ОШИБКА: ФАЙЛА НЕТ')

    index2 = number_or_lines

    def is_not_nan(num):
        return num == num

    def is_nan(num):
        return num != num

    try:
        df = pd.read_excel(file)


    except Exception:

        print('ОШИБКА: ВЕРОЯТНО, EXCEL-ФАЙЛ НЕПРАВИЛЬНОГО ФОРМАТА ')

        # логирование
        tb = traceback.format_exc()
        logger.error(f" WRONG FORMAT OF EXCEL-FILE {tb}")
        utils.shared.notice_retr = 'ОШИБКА: ВЕРОЯТНО, EXCEL-ФАЙЛ НЕПРАВИЛЬНОГО ФОРМАТА '
        raise Exception('ОШИБКА: ВЕРОЯТНО, EXCEL-ФАЙЛ НЕПРАВИЛЬНОГО ФОРМАТА')


    rows_nubmer = df.shape[0]
    columns_nubmer = df.shape[1]
    print('Excel-файл строк =', rows_nubmer)
    print('Excel-файл колонок =', columns_nubmer)


    # определение номеров колонок в эксель-файле
    cn, cn_ = gcn.get_cn(df)

    prlist_kurs = []
    prlist_client = []

    print()
    print('EXCEL всего анкет       =', rows_nubmer)
    if index2 == 0:
        index2 = rows_nubmer
    if index2 > rows_nubmer:
        index2 = rows_nubmer
    print('EXCEL анкет извлекается =', index2)
    print()

    for rx in range(index2):

        line_ = df.iloc[rx]

        # print('pupil=',  line_[cn['cn_pupil']] )

        # проверка, что эта строка - действительно строка курса
        if (is_not_nan(line_[cn['cn_kurs']])):

            # print('pupil=', line_[cn['cn_pupil']])

            # формирование параметров курса и клиента  из  каждой строки эксель файта
            pr_kurs, pr_client = get_record(line_, cn, cn_)

            # print("pr_kurs=",pr_kurs)
            # print("pr_client=",pr_client)

            # if (  acceptance(pr_kurs, pr_client)==1 ):
            if (1 == 1):
                prlist_kurs.append(pr_kurs)
                prlist_client.append(pr_client)

                # print('accepted ', rx, fio, line_[cn['number']], line_[cn['expire']])

    if not prlist_kurs:
        print('ОШИБКА EXCEL-ФАЙЛА - ВЕРОЯТНО НЕТ ДАННЫХ В ФАЙЛЕ')
        quit()

    utils.shared.notice_retr = utils.shared.notice_retr + f'<h5>Всего принято строк курсов: {len(prlist_kurs)}</h5> '

    print('до отсеивания дублей клиентов, количество ', len(prlist_client))
    # удаление строк клиентов с одинаковыми ID
    client_names_list = []
    for client_ in list(prlist_client):
        if client_['name'] in client_names_list:
            prlist_client.remove(client_)
        client_names_list.append(client_['name'])
    print('после отсеивания дублей, количество клиентов: ', len(prlist_client))
    utils.shared.notice_retr = utils.shared.notice_retr + f'<h5>Всего принято клиентов: {len(prlist_client)}</h5> '

    # проверка - если есть клиенты с разными ФИО но одинаковыми телефонами - прекращение выполнения скрипта
    import utils.check2, utils.check23

    utils.check2.go(prlist_client)
    utils.check23.go(prlist_kurs)

    if listing == 'on':
        for cl in prlist_client:
            print("          из эксэль клиенты ", cl)
        for kurs in prlist_kurs:
            print("          из эксэль курсы ", kurs)

    return prlist_kurs, prlist_client
