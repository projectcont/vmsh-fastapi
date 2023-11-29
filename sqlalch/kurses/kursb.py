
from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, Text, ForeignKey, DateTime, Boolean, DECIMAL
from sqlalchemy.dialects.mysql import VARCHAR,INTEGER, DECIMAL, TINYINT, SMALLINT, DATETIME, MEDIUMINT, FLOAT


def get_kursb (metadata):
    #__tablename__ = "e92gs_allrecords"

    kurs = Table('e92gs_allrecords', metadata,

    Column('id', INTEGER(11), primary_key=True,nullable=False),
    Column('idclient', VARCHAR(255),  default='', index=True, nullable=False),
    Column('idgroup', INTEGER(10),    default='', index=True, nullable=False),
    Column('idpupil', INTEGER(11), default='', index=True),
    Column('price', DECIMAL(14, 4), nullable=False, default='0'),
    Column('payment_done', DECIMAL(14, 4), nullable=False, default='0'),
    Column('pay_recom', DECIMAL(14, 4), nullable=False, default='0'),
    Column('payment_remaining', DECIMAL(14, 4), nullable=False, default='0'),
    Column('payments', VARCHAR(255),  default=''),
    Column('exclude_number', INTEGER(11), default='', index=True),
    Column('exclude_sum', DECIMAL(14, 4),  default='0'),
    Column('published', TINYINT(1),  default='1', index=True),
    Column('contract', VARCHAR(128), nullable=False, default=''),
    Column('pupil_fio', VARCHAR(255), nullable=False, default=''),
    Column('google', VARCHAR(255), default=''),

    )
    return kurs


class Kurs (object):
    def setpr(self,prlist_kurs):
        setattr(self, "idpupil", 2)
        setattr(self, "idclient", '')
        setattr(self, "exclude_number", 0)
        setattr(self, "exclude_sum", 0)
        setattr(self, "published", 1)
        for key_ in list(prlist_kurs.keys()):
            setattr(self, key_, prlist_kurs[key_])

    def __str__(self):
        str_contract = "Номер договора=" + str ( getattr(self, "contract") )
        str_fio = " ФИО ученика=" + str( getattr(self, "pupil_fio") ).ljust(30, ' ')
        str_idclient = " ID клиента=" + str(getattr(self, "idclient")).ljust(30, ' ')
        str_idgroup = " ID группы=" + str(getattr(self, "idgroup"))
        str_price = " Сумма =" + str(getattr(self, "price"))
        str_months = " По месяцам =" + str(getattr(self, "payments"))
        str_google = " гугл =" + str(getattr(self, "google"))
        sum = f' {str_contract}  {str_idclient} {str_fio}    {str_idgroup} {str_price}  {str_google} {str_months}  '
        return sum


































