import traceback
from sqlalch.kurses.kursb import Kurs
import utils.shared
from sqlalchemy import delete
from sqlalchemy import or_



def go (kurs_list_delete,session):
    try:
        print()

        vset=[n.id for n in kurs_list_delete]

        #print('vset', vset)
        #session.delete(clients_list_delete)
        #session.query(Client).filter(or_(Client.id == 1422, Client.id == 1423)).delete(synchronize_session=False)
        #session.query(Client).filter(or_(Client.id == v for v in vset).delete(synchronize_session=False)

        session.query(Kurs).filter(Kurs.id.in_(vset)).delete(synchronize_session=False)
        session.commit()

    except:
        traceback.print_exc()
        session.rollback()
        raise