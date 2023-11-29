from utils.convert import *

def is_not_nan(num): return num == num

def is_nan(num): return num != num

def get_record(line_, cn, cn_):
    # извлекаем из строки таблицы свойства курса

    idgroup = any_to_int(line_[cn['cn_idgroup']])
    pupil = any_to_str(line_[cn['cn_pupil']])
    google = any_to_str(line_[cn['cn_google']])
    contract = any_to_str(line_[cn['cn_kurs']])
    price = any_to_int(line_[cn['cn_price']])
    payment_done = any_to_int(line_[cn['cn_payment_done']])
    pay_recom = any_to_int(line_[cn['cn_payment_recom']])
    payment_remaining = any_to_int(line_[cn['cn_payment_remaining']])

    client_fio = any_to_str(line_[cn['cn_client_fio']])

    payments = ''
    months = {'cn_month1': 'январь', 'cn_month2': 'февраль', 'cn_month3': 'март', 'cn_month4': 'апрель',
              'cn_month5': 'май', 'cn_month6': 'июнь', 'cn_month7': 'июль', 'cn_month8': 'август',
              'cn_month9': 'сентябрь', 'cn_month10': 'октябрь', 'cn_month11': 'ноябрь', 'cn_month12': 'декабрь', }
    for month in cn_:
        if cn_[month] != -2:
            monthname = months[month]
            # print(monthname)
            # print(cn_)
            monthpay = any_to_int(line_[cn_[month]])
            if monthpay == '0' or not monthpay:
                # payments = payments+f'<p>{monthname} - nopay </p>'
                payments = payments
            else:
                monthpay_ = '{0:,}'.format(monthpay).replace(',', ' ')
                payments = payments + f'<p>{monthname} - {monthpay_} руб.</p>'

    pr_kurs = {'idgroup': idgroup,
               'idclient': client_fio,
               'pupil_fio': pupil,
               'contract': contract,
               'price': price,
               'payment_done': payment_done,
               'pay_recom': pay_recom,
               'payment_remaining': payment_remaining,
               'payments': payments,
               'google': google,

               }

    # извлекаем из строки таблицы свойства клиента

    client_phone = digits(any_to_str((line_[cn['cn_client_phone']])))

    # print("client_phone", client_phone)

    client_email = any_to_str(line_[cn['cn_client_email']])

    pr_client = {'name': client_fio,
                 'username': client_phone,
                 'email': client_email,
                 'resetCount': '',
                 'password': ''
                 }

    # print(pr_kurs)
    # print(pr_client)

    return pr_kurs, pr_client
