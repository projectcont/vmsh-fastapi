
from sqlalch.kurses.kursb import Kurs
import traceback
import utils.shared
from configuration import listing



def go (kurs_list_add,session):
    '''
    for all 'products' in 'prod_list'
    function adds each 'product' to database
    :param prod_list: list of products
    :param session:  session
    :return:
    '''

    print()
    print('ЭКСПОРТ (ДОБАВЛЕНИЕ) КУРСОВ НА САЙТ')

    for kurs in kurs_list_add:
        try:
            if listing == 'on': print( '          добавлен курс ',  kurs );

            session.add(kurs)
            session.flush()
            session.refresh(kurs)
            session.commit()

        except:
            errortext='ОШИБКА ОТПРАВКИ КУРСОВ НА САЙТ. Возможно для некоторых курсов клиенты (ID клиента) или группы (номер группы) неправильно указаны в EXCEL-файле'
            utils.shared.notice_tosite = errortext
            print(errortext)
            traceback.print_exc()
            session.rollback()
            raise


    print('ЭКСПОРТ КУРСОВ НА САЙТ ВЫПОЛНЕН')
    print()

