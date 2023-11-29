from configuration import dbconf
from sqlalchemy import create_engine
from configuration import showdebug


# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_engine(
        user=dbconf['user'],
        password=dbconf['password'],
        host=dbconf['host'],
        port=dbconf['port'],
        database=dbconf['database']):
    return create_engine(
        url="mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        ), echo=showdebug
    )
