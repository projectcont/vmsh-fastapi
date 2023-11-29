from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, Text, ForeignKey, DateTime, Boolean, DECIMAL
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, DECIMAL, TINYINT, SMALLINT, DATETIME, MEDIUMINT, FLOAT


def get_clientb(metadata):
    clientb = Table(
        'e92gs_users', metadata,
        Column('id', INTEGER(11), primary_key=True, nullable=False, index=True),
        Column('name', VARCHAR(400), nullable=False),
        Column('username', VARCHAR(150), nullable=False),
        Column('email', VARCHAR(100), nullable=False),
        Column('resetCount', INTEGER(11), nullable=False),
        Column('password', VARCHAR(100), nullable=False),
        Column('registerDate', DateTime, nullable=False, default='2023-12-12 12:12:12'),
        Column('lastvisitDate', DateTime, nullable=False, default='2023-12-12 12:12:12'),
        Column('lastResetTime', DateTime, nullable=False, default='2023-12-12 12:12:12'),
        Column('params', Text, nullable=False,
               default='{"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":""}'),

    )
    return clientb


class Client(object):
    def setpr(self, prlist_client):
        for key_ in list(prlist_client.keys()):
            setattr(self, key_, prlist_client[key_])

    def __str__(self):
        str_name = "ФИО клиента=" + str(getattr(self, "name")).ljust(30, ' ')
        str_username = " логин клиента=" + str(getattr(self, "username")).ljust(30, ' ')
        str_email = " email клиента=" + str(getattr(self, "email"))
        sum = f' {str_name}   {str_username}  {str_email}    '
        return sum


# ----- USERGROUP - REGISTED  ---------------------------------


def get_usergroupb(metadata):
    usergroupb = Table(
        'e92gs_user_usergroup_map', metadata,
        Column('user_id', INTEGER(10), primary_key=True, nullable=False, default='2'),
        Column('group_id', INTEGER(10), nullable=False, default='2')
    )
    return usergroupb


class Usergroup(object):
    def __str__(self):
        sum = "Usergroup =" + str(getattr(self, "user_id")) + str(getattr(self, "group_id"))
        return sum
