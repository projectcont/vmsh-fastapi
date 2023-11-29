import traceback


def go(clients_list_change, session):
    try:
        session.add_all(clients_list_change)
        session.commit()
        print('corrected clients')

    except Exception:
        traceback.print_exc()
        session.rollback()
        raise
