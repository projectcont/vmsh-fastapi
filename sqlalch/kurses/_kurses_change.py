import traceback
from sqlalch.kurses.kursb import Kurs
import utils.shared

def go (kurs_list_change,session):
    try:
        session.add_all(kurs_list_change)
        session.commit()
        print('corrected kurses')

    except:
        traceback.print_exc()
        session.rollback()
        raise
