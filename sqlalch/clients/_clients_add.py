from sqlalch.clients.clientb import Client, Usergroup
import traceback


def go(clients_list_add, session):
    '''
    for all 'clients' in 'clients_list_ad'
    function adds each 'product' to database
    :param prod_list: list of products
    :param session:  session
    :return:
    '''

    print()
    print('ЭКСПОРТ (ДОБАВЛЕНИЕ) КЛИЕНТОВ НА САЙТ')
    usergrouplist = []

    try:
        for client in clients_list_add:
            session.add(client)
            session.flush()
            session.refresh(client)

            client_ID = client.id
            # print('client_ID=', client_ID)
            usergr = Usergroup()
            usergr.user_id = client_ID
            usergr.group_id = 2
            usergrouplist.append(usergr)
            # session.add(usergr)

            # print('          на сайт добавлен клиент ', client)

        session.add_all(usergrouplist)
        session.commit()
        # session.close()

    except Exception:
        traceback.print_exc()
        error_txt = 'ОШИБКА ЭКСПОРТА КЛИЕНТОВ НА САЙТ. Возможно в эксель есть клиенты с разными  ФИО но при этом дублируются телефон или email'
        import utils.shared
        utils.shared.notice_tosite = error_txt
        print(error_txt)
        session.rollback()

    print(' ЭКСПОРТ КЛИЕНТОВ НА САЙТ ВЫПОЛНЕН')
    print()
