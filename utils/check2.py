import utils.shared


def go(prlist_client):
    '''
    # проверка EXCEL
    :param prlist_client:
    :return:
    '''

    username_list = [x['username'] for x in prlist_client]
    email_list = [x['email'] for x in prlist_client]
    dupl_username = [x for x in username_list if username_list.count(x) > 1]
    dupl_email = [x for x in email_list if email_list.count(x) > 1]

    names = []
    username = []

    # -------проверка EXCEL - если есть клиенты с разными ФИО но одинаковыми телефонами - прекращение выполнения скрипта
    count = 0
    for x in prlist_client:
        if username_list.count(x['username']) > 1:
            name = x['name']
            print('name=', name)
            names.append(name)
            username = x['username']
            count = 1
    if count == 1:
        errortext = f'ОШИБКА. ВЫПОЛНЕНИЕ СКРИПТА ПРЕКРАЩЕНО.<br/> РАЗНЫЕ КЛИЕНТЫ {names} ИМЕЮТ ОДИНАКОВЫЙ ТЕЛЕФОН  {username} '
        print(errortext)
        utils.shared.notice_retr = errortext
        raise Exception(errortext)

    # -------проверка EXCEL - если есть клиенты с разными ФИО но одинаковыми EMAIL - прекращение выполнения скрипта
    count = 0
    for x in prlist_client:
        if email_list.count(x['email']) > 1:
            name = x['name']
            print('name=', name)
            names.append(name)
            email = x['email']
            count = 1
    if count == 1:
        errortext = f'ОШИБКА. ВЫПОЛНЕНИЕ СКРИПТА ПРЕКРАЩЕНО.<br/> РАЗНЫЕ КЛИЕНТЫ {names} ИМЕЮТ ОДИНАКОВЫЙ EMAIL  {email} '
        print(errortext)
        utils.shared.notice_retr = errortext
        raise Exception(errortext)

    # -------проверка EXCEL - если есть клиент без телефона или email  - прекращение выполнения скрипта
    for client in prlist_client:
        if (client['name'] == ''):
            errortext = f" клиент с email {client['email']} не принят, ошибка ФИО "
            print(errortext)
            utils.shared.notice_retr = errortext
            raise Exception(errortext)

        if (client['email'] == ''):
            errortext = f" клиент {client['name']} не принят, нет EMAIL"
            print(errortext)
            utils.shared.notice_retr = errortext
            raise Exception(errortext)

        if (client['username'] == ''):
            errortext = f" клиент {client['name']} не принят, нет ТЕЛЕФОНА"
            print(errortext)
            utils.shared.notice_retr = errortext
            raise Exception(errortext)

    ''' 
    for x in prlist_client:
        if len(   x['username'] ) == 0:
            name = x['name']
            names.append(name)
            print(names)
            count = 1
    if count == 1:
        errortext = f'ОШИБКА. ВЫПОЛНЕНИЕ СКРИПТА ПРЕКРАЩЕНО.<br/> КЛИЕНТ {names} БЕЗ ТЕЛЕФОНА '
        print(errortext)
        utils.shared.notice_retr = errortext
        raise Exception(errortext)
    '''

    ''' 
    if len(dupl_email) > 1:
        errortext = f'ОШИБКА. ВЫПОЛНЕНИЕ СКРИПТА ПРЕКРАЩЕНО.<br/> РАЗНЫЕ КЛИЕНТЫ ИМЕЮТ ОДИНАКОВЫЙ EMAIL  {dupl_email[0]} '
        print(errortext)
        utils.shared.notice_retr = errortext
        raise Exception(errortext)

    if len(dupl_username) > 1:
        errortext = f'ОШИБКА. ВЫПОЛНЕНИЕ СКРИПТА ПРЕКРАЩЕНО.<br/> РАЗНЫЕ КЛИЕНТЫ ИМЕЮТ ОДИНАКОВЫЙ ТЕЛЕФОН  {dupl_username[0]} '
        print(errortext)
        utils.shared.notice_retr = errortext
        raise Exception(errortext)
    '''
