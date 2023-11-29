import utils.shared


def go(prlist_kurs):
    contract_list = [x['contract'] for x in prlist_kurs]
    dupl_contract = [x for x in contract_list if contract_list.count(x) > 1]

    if len(dupl_contract) > 1:
        errortext = f'EXCEL - THERE ARE KURSES WITH SAME NUMBER  {dupl_contract} '
        print(errortext)
        utils.shared.notice_retr = errortext
        raise Exception(errortext)

    for kurs in prlist_kurs:

        if ((kurs['price'] == '') or (kurs['price'] == '0')):
            errortext = f"error for kurs N {kurs['contract']}: PRICE EMPTY"
            print(errortext)
            utils.shared.notice_retr = errortext
            raise Exception(errortext)

        if (kurs['pupil_fio'] == ''):
            errortext = f"error for kurs N {kurs['contract']}: pupil FIO"
            print(errortext)
            utils.shared.notice_retr = errortext
            raise Exception(errortext)
