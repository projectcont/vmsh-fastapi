from sqlalchemy import Table, Column
from sqlalchemy.dialects.mysql import INTEGER


# ----- COM_CONTENT  ( Groups  ) ---------------------------------

def get_groupb(metadata):
    groupb = Table(
        'e92gs_content', metadata,
        Column('id', INTEGER(10), primary_key=True, nullable=False, default='1'),
    )
    return groupb


class Group(object):
    def __str__(self):
        sum = "ID группы=" + str(getattr(self, "id"))
        return sum
