from sqlalch.clients.clientb import Client
import traceback
import utils.shared
from configuration import listing
import logit.logsetting
import traceback

logger=logit.logsetting.logger


def dispence(session, clients_list):
    '''
    функуия  распределяет список клиентов на три списка
    список тех кто уже есть на сайте (их данные обновляются на сайте)
    список новых клиентов (их данные добавляются на сайт)
    список лишних клиентов (их данные удаляются с сайта)
    :param session, clients_list
    :return: clients_list_add
    '''

    print()
    print('DISPENCE CLIENTS')
    countouter = 0
    counter_change = 0
    counter_delete = 0

    clients_list_add = []
    clients_list_change = []
    clients_list_delete = []

    # ----  получение клиентов с сайта
    try:
        dbclients = session.query(Client).all()
    except Exception:
        traceback.print_exc()
        errortext = '<br/><br/><br/><br/><br/>ОШИБКА ПОЛУЧЕНИЯ session.query(Client).all()'
        tb = traceback.format_exc()
        logger.error(f" NO ACCESS TO DATABASE {tb}")
        utils.shared.notice_tosite = errortext
        print(errortext)
        session.rollback()
        raise

    # -----------  формирование списков (клиентов на коррекцию и добавление)  -------------------
    try:

        for excl in clients_list:
            prev_ex = 0
            countouter = countouter + 1

            for dbcl in dbclients:

                if (dbcl.name == excl.name):
                    # если клиент уже есть в DB - меняются его свойства
                    dbcl.username = excl.username
                    dbcl.email = excl.email
                    dbcl.password = excl.password
                    dbcl.resetCount = excl.resetCount

                    counter_change = counter_change + 1
                    prev_ex = 1
                    clients_list_change.append(dbcl)
                    # клиент заносится в список на коррекцию

            if prev_ex == 0:
                # если этого клиента нет на сайте, то он заносится в список на добавление
                if listing == 'on':
                    print("          на сайт добавляется клиент ", excl)
                clients_list_add.append(excl)


    except Exception:
        traceback.print_exc()
        errortext = '<br/><br/><br/><br/><br/>ОШИБКА ПОДКЛЮЧЕНИЯ К БАЗЕ ДАННЫХ САЙТА. Возможно неправильный IP'
        utils.shared.notice_tosite = errortext
        print(errortext)
        session.rollback()
        raise
    # -----------  формирование списков (клиентов на коррекцию и добавление)   -------------------

    # -----------  формирование списка (удаление клиентов которые есть в DB, но нет в EXCEL)   -------------------
    for dbcl in dbclients:
        prev_db = 0
        for excl in clients_list:
            if (dbcl.name == excl.name):
                prev_db = 1
        if (prev_db == 0) and (dbcl.id > 3831):
            # если этого клиента нет на EXCEL, то он заносится в список на удаление
            if listing == 'on':
                print("          с сайта удаляется клиент ", dbcl);
            counter_delete = counter_delete + 1
            clients_list_delete.append(dbcl)

    # -----------  удаление клиентов которые есть в DB, но нет в EXCEL   -------------------

    out1 = f' с сайта удаляется   клиентов {len(clients_list_delete)}'
    print(out1)
    out2 = f' на сайте меняется   клиентов  {len(clients_list_change)}'
    print(out2)
    out3 = f' на сайт добавляется клиентов {len(clients_list_add)}'
    print(out3)
    utils.shared.notice_tosite = utils.shared.notice_tosite + '<br/>' + out1 + '<br/>' + out2 + '<br/>' + out3 + '<br/>'

    # проверка что в добавляемых клиентах нет телефонов или email как у прежних клиентов
    for excl in list(clients_list_add):
        for dbcl in dbclients:
            if dbcl.username == excl.username:
                errortext = f" <strong>ошибка для клиента <br/> ({excl}) <br/>- добавляемый из EXCEL клиент имеет такой же телефон,<br/>как  клиент который уже на сайте</strong>"
                utils.shared.notice_tosite = errortext
                print(errortext)
                session.rollback()
                raise
            if dbcl.email == excl.email:
                errortext = f" <strong>ошибка для клиента <br/> ({excl}) <br/>- добавляемый из EXCEL клиент  имеет такой же email,<br/>как и клиент, который уже на сайте</strong>"
                utils.shared.notice_tosite = errortext
                print(errortext)
                session.rollback()
                raise

    return clients_list_add, clients_list_delete, clients_list_change
