from sqlalch.kurses.kursb import Kurs
from sqlalch.groupb import Group, get_groupb
import traceback
import utils.shared
import utils.check3_
from configuration import listing



def dispencek (session, kurs_list):
    '''
    функуия  распределяет список курсов на три списка
    список курсов, которые уже есть на сайте (их данные  обновляются на сайте)
    список новых курсов (их данные добавляются на сайт)
    список лишних курсов (их данные удаляются с сайта)
    :param session, kurs_list
    :return: kurs_list_add
    '''

    print()
    print('DISPENCE KURSES')

    count=0
    countouter = 0

    kurs_list_add = []
    kurs_list_delete = []
    kurs_list_change = []

    # ----  получение курсов с сайта
    dbkurses = session.query(Kurs).all()


    # ----проверка что внешние ссылки на ID-группы корректны
    allgroups = session.query(Group)
    utils.check3_.check3(kurs_list,allgroups)
    # ----проверка что внешние ссылки  на ID-группы корректны


    # -----------  коррекция курсов которые есть на сайте и в EXCEL   -------------------
    try:
        for exk in kurs_list:
            #print('disp kurses',n, exk.idclient)
            prev=0
            for dbk in dbkurses:
                #print(dbk)
                if (  dbk.contract==exk.contract   ):
                    #print('disp chance kurses', n, exk.idclient)

                    dbk.price=exk.price
                    dbk.idgroup =exk.idgroup
                    dbk.idclient= exk.idclient
                    dbk.idpupil=exk.idpupil
                    dbk.payments=exk.payments
                    dbk.pay_recom=exk.pay_recom
                    dbk.payment_done=exk.payment_done
                    dbk.payment_remaining=exk.payment_remaining
                    dbk.exclude_number=exk.exclude_number
                    dbk.exclude_sum=exk.exclude_sum
                    dbk.published=exk.published
                    dbk. contract=exk.contract
                    dbk.pupil_fio=exk.pupil_fio
                    dbk.google=exk.google
                    prev = 1
                    kurs_list_change.append(dbk)
                    # курс заносится в список на коррекцию

            # end inner

            if prev == 0:
                # если этого курса нет на сайте, то он заносится в список на добавление
                kurs_list_add.append(exk)

        # end outer

    except:
        traceback.print_exc()
        print(
            'ОШИБКА ОТПРАВКИ КУРСОВ НА САЙТ. Возможно для некоторых курсов клиенты (ID клиента) или группы (номер группы) неправильно указаны в EXCEL-файле')
        session.rollback()
        raise
    # -----------  коррекция курсов которые есть на сайте и в EXCEL   -------------------




    # -----------  формирование списка (удаление курсов которые есть на сайте, но нет в EXCEL)   ----------
    for dbk in dbkurses:
        prev_db = 0
        for exk in kurs_list:
            if (dbk.contract == exk.contract):
                prev_db = 1
        if prev_db == 0 :
            # если этого курса нет на EXCEL, то он вносится в список удаления
            if listing == 'on': print("          из сайта удаляется курс ", dbk);
            kurs_list_delete.append(dbk)
    # -----------  формирование списка (удаление курсов которые есть на сайте, но нет в EXCEL)   ---------

    if listing == 'on':
        for n in kurs_list_add: print("          на сайт добавляется курс ", n);
        for n in kurs_list_change: print("       на сайте меняется курс ", n);
        for n in kurs_list_delete: print("       на сайтe удаляется курс ", n);


    print()
    out1 = f' с сайта удаляется   курсов {  len(kurs_list_delete)  }';  print(out1)
    out2 = f' на сайте меняется   курсов  {  len(kurs_list_change)  }';  print(out2)
    out3 = f' на сайт добавляется курсов {  len(kurs_list_add)  }';  print(out3)
    utils.shared.notice_tosite = utils.shared.notice_tosite + '<br/>' + out1 + '<br/>' + out2 + '<br/>' + out3 + '<br/>'

    return kurs_list_add, kurs_list_delete, kurs_list_change






