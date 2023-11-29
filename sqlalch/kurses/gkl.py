from sqlalch.kurses.kursb import Kurs


def get_kurs_list (prlist_kurs):
    '''
    functuion creates list of kurses (instances)
    :param nop:  list of kurses (dict)
    :return: list of kurses (instances)
    '''
    #print('len prlist_kurs',len(prlist_kurs))

    kurs_list = []
    print('          (ФОРМИРОВАНИЕ СПИСКА КУРСОВ - ЭКЗЕМПЛЯРОВ )' );
    for pr in prlist_kurs:
        kurs = Kurs()
        kurs.setpr(pr)
        kurs_list.append(kurs)
    print('          (ФОРМИРОВАНИЕ СПИСКА КУРСОВ - ЭКЗЕМПЛЯРОВ ВЫПОЛНЕНО)');
    print('          ПОЛУЧЕНО КУРСОВ - ЭКЗЕМПЛЯРОВ: ',  len(kurs_list));
    return kurs_list


