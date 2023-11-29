import time
import sqlalch.clients._clients_add
import sqlalch.clients._clients_change
import sqlalch.clients._clients_delete
import sqlalch.clients.dispence_clients
import sqlalch.kurses._kurses_add
import sqlalch.kurses._kurses_change
import sqlalch.kurses._kurses_delete
from sqlalch.clients.gcl import get_clients_list
from sqlalch.kurses.dispence_kurses import dispencek
from sqlalch.kurses.gkl import get_kurs_list


def agregate(prlist_kurs, prlist_client):
    #   получение сессии
    from sqlalch.get_session_ import get_session
    session, engine = get_session()

    if session:
        print('session= ', session)

    t1 = time.time()

    #   конвертация: список клиентов dict - в список клиентов instance
    clients_list = get_clients_list(prlist_client)
    t2 = time.time()

    #   распределение клиентов - на список добавления и список коррекции
    clients_list_add, clients_list_delete, clients_list_change = sqlalch.clients.dispence_clients.dispence(session,
                                                                                                           clients_list)
    t3 = time.time()

    #   коррекция клиентов на сайт
    sqlalch.clients._clients_change.go(clients_list_change, session)
    t4 = time.time()

    #   удаление клиентов с сайта
    sqlalch.clients._clients_delete.go(clients_list_delete, session)
    t5 = time.time()

    #   добавление клиентов на сайт
    sqlalch.clients._clients_add.go(clients_list_add, session)
    t6 = time.time()

    #   список курсов dict -в список курсов instance
    kurs_list = get_kurs_list(prlist_kurs)
    t7 = time.time()

    #   распределение курсов - на список добавления и список коррекции
    kurs_list_add, kurs_list_delete, kurs_list_change = dispencek(session, kurs_list)
    t8 = time.time()

    #   курсы корректируются на сайте
    sqlalch.kurses._kurses_change.go(kurs_list_change, session)
    t9 = time.time()

    #   курсы удаляются на сайте
    sqlalch.kurses._kurses_delete.go(kurs_list_delete, session)
    t10 = time.time()

    #   курсы добавляются на сайт
    sqlalch.kurses._kurses_add.go(kurs_list_add, session)
    t11 = time.time()

    print('interval2 get_client_list= ', round((t2 - t1)))
    print('interval3 клиент дисп=  ', round((t3 - t2)))
    print('interval4 клиент кор= ', round((t4 - t3)))
    print('interval5 клиент удал= ', round((t5 - t4)))
    print('interval6 клиент доб= ', round((t6 - t5)))
    print('interval7 get_kurs_list= ', round((t7 - t6)))
    print('interval8 курс дисп= ', round((t8 - t7)))
    print('interval9 курс кор= ', round((t9 - t8)))
    print('interval10 курс удал= ', round((t10 - t9)))
    print('interval11 курс доб= ', round((t11 - t10)))
    print('interval= ', round((t11 - t2)))

    try:

        session.close()
        # print('3333',session, session.is_active)

        engine.dispose()

        # print('4444', session, session.is_active)

        import utils.shared
        utils.shared.notice_tosite = utils.shared.notice_tosite + f'<br/><p>Выполнено за {round((t11 - t2))} с.</p> '
    except Exception as ex:
        print("ОШИБКА  SESSION: \n", ex)

    return 'ЭКСПОРТ КУРСОВ НА САЙТ ВЫПОЛНЕН'
