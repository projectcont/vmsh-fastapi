def acceptance(pr_kurs, pr_client):
    import utils.shared
    accept = 1

    if (pr_client['name'] == ''):
        not_accepted_error = f"            курс N {pr_kurs['contract']} - строка не принята, ошибка ФИО клиента "
        print(not_accepted_error)
        accept = 0
        utils.shared.notice_retr = utils.shared.notice_retr + '<br/>' + not_accepted_error

    if (pr_client['email'] == ''):
        not_accepted_error = f"            курс N {pr_kurs['contract']} - строка не принята, ошибка EMAIL клиента "
        print(not_accepted_error)
        accept = 0
        utils.shared.notice_retr = utils.shared.notice_retr + '<br/>' + not_accepted_error

    if (pr_kurs['pupil_fio'] == ''):
        not_accepted_error = f"            курс N {pr_kurs['contract']} - строка не принята, ошибка ФИО ученика "
        print(not_accepted_error)
        accept = 0
        utils.shared.notice_retr = utils.shared.notice_retr + '<br/>' + not_accepted_error

    if ((pr_kurs['price'] == '') or (pr_kurs['price'] == '0')):
        not_accepted_error = f"            курс N {pr_kurs['contract']} - строка не принята, ошибка в сумме договора "
        print(not_accepted_error)
        accept = 0
        utils.shared.notice_retr = utils.shared.notice_retr + '<br/>' + not_accepted_error

    return accept
