from sqlalchemy.orm import mapper, sessionmaker
from sqlalch.engine import get_engine


def get_session():
    try:
        engine = get_engine()
        print('------------------------------------')
        print()
        print(f"Engine created successfully.")

        # metadata.create_all(engine)
        # print(f"Table created successfully.")

        DBSession = sessionmaker(bind=engine, autoflush=True)
        print(f"sessionmaker successfully.")

        session = DBSession()
        print(f"DBSession successfully.")

        return session, engine

    except Exception as ex:
        print("ОШИБКА SQL: \n", ex)
