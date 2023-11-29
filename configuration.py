# DEFINE THE DATABASE CREDENTIALS
# webrel
__dbconf = dict(
    user='vkcntoread_vm',
    password='n26suNeg9',
    host='VH222.sweb.ru',
    port=3306,
    database='vkcntoread_vm'
)

dbconf = dict(
    user='',
    password='',
    host='VH297.sweb.ru',
    port=3306,
    database=''
)

# showdebug=True
showdebug = False

listing = 'on'

erroraction = 0
'''
Проверка данных курса в файле  project/excel_retrieve/acceptance_.py
Если в курсах (строках) EXCEL-файла есть ошибки, то 2 варианта действия
erroraction=0 - скрипт прекращает работу
erroraction=1 - скрипт продолжает работу, исключая ошибочные строки

ошибками считается, если не указано
- ФИО клиента
- ФИО ученика
- цена курса
- ID клиента
'''

'''
Проверка данных клиентов
Если в EXCEL-файле несколько клиентов с одинаковым ID (остальные данные могут отличаться) - оставляется оди клиент
Если в EXCEL-файле несколько клиентов с разными ID, но одинаковыми телефонами или email - скрипт прекращает работу 
'''

'''
Установка пароля клиента - последние 3 цифры телефона
с 39 строки файла  project/sqlalch/clients/dispence_clients.py
'''

# echo : engine.py   (echo=False)
# debug: main.py   app.run(debug=True)
