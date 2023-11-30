import pytest
import os
from excel_retrieve.excel1 import excel1_go


def test_excel_kurs():

    result ={'contract': '77777777',
  'google': '',
  'idclient': 'Лиева Лия Амосовна',
  'idgroup': 34,
  'pay_recom': 4000,
  'payment_done': 11000,
  'payment_remaining': 13000,
  'payments': '<p>октябрь - 6 000 руб.</p><p>ноябрь - 2 000 руб.</p><p>декабрь - 3 000 руб.</p>',
  'price': 24000,
  'pupil_fio': 'Мангалов Шампур Углевич'}

    assert excel1_go('test_excel.xlsx', 0)[0][0]  == result


def test_excel_clients():

    result =   {'name': 'Лиева Лия Амосовна', 'username': '9167777770', 'email': 'fhjfh@zxc.ru', 'resetCount': '', 'password': ''}
    assert excel1_go('test_excel.xlsx', 0)[1][0] == result


def test_wrong_excel():
    with pytest.raises(Exception):
        assert excel1_go("wrong_excel.xlsx", number_or_lines=0)











