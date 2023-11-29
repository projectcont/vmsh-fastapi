import utils.shared


def check3(kurs_list, allgroups):
    '''
    функция сравнивает список  "ID групп EXCEL-файла" и список "ID групп на сайте"
    если в EXCEL-файле есть лишние ID групп, которых нет на сайте, выполнение скрипта прекращается
    :param kurs_list:
    :param allgroups:
    :return:
    '''
    group_IDs = [x.id for x in allgroups]

    for kurs_ in kurs_list:
        if kurs_.idgroup not in group_IDs:
            errortext = f'ОШИБКА ! ВЫПОЛНЕНИЕ СКРИПТА ПРЕКРАЩЕНО <br/>для курса (номер = {kurs_.contract} ) неправильное idgroup = {kurs_.idgroup}'
            utils.shared.notice_tosite = errortext
            print(errortext)
            raise Exception(errortext)
