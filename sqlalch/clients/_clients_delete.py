import traceback
from sqlalch.clients.clientb import Client


def go(clients_list_delete, session):
    try:
        print()

        vset = [n.id for n in clients_list_delete]

        session.query(Client).filter(Client.id.in_(vset)).delete(synchronize_session=False)
        session.commit()

    except Exception:
        traceback.print_exc()
        session.rollback()
        raise
