import os

import webbrowser
from pathlib import Path
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import mapper
from sqlalchemy.schema import MetaData

from excel_retrieve.excel1 import excel1_go
from sqlalch.agreg_ import agregate
from sqlalch.clients.clientb import get_clientb, Client, get_usergroupb, Usergroup
from sqlalch.groupb import Group, get_groupb
from sqlalch.kurses.kursb import Kurs, get_kursb

import traceback

metadata = MetaData()
kursb = get_kursb(metadata)
clientb = get_clientb(metadata)
usergroupb = get_usergroupb(metadata)
groupb = get_groupb(metadata)
mapper(Kurs, kursb)
mapper(Client, clientb)
mapper(Usergroup, usergroupb)
mapper(Group, groupb)

BASE_PATH = Path(__file__).resolve().parent
print("BASE_PATH=", BASE_PATH)
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
app = FastAPI(title="API")
app = FastAPI()
from fastapi.staticfiles import StaticFiles

staticfiles = StaticFiles(directory="templates")
folder = os.path.dirname(__file__)
app.mount("/templates", StaticFiles(directory="templates"), name="static2")

# ---------------- Закачка EXCEL-файла на сервер

# --------------- показ формы закачки EXCEL-файла с локального компьютера

@app.get("/", response_class=HTMLResponse)
def show_upload(request: Request):
    import urllib.request
    print()
    print('---------------------------------------------------------------------------------------------')
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(external_ip)
    notice = f'IP сервера: {external_ip}'

    title = "Стадия 1. Закачка EXCEL-файла на сервер"
    return templates.TemplateResponse("upload.html", {"request": request, "title": title, "notice": notice})


# --------------- выполнение закачки EXCEL-файла с локального компьютера
@app.post("/upload")
async def upload(request: Request, file: UploadFile = File(...), pin: str = Form(default="0")):
    try:
        import utils.shared
        utils.shared.notice_retr = ""
        utils.shared.notice_tosite = ""

        contents = await file.read()

        import paths_
        rootfolder = paths_.path(1)
        excelpath = rootfolder / 'files' / '1.xlsx'
        print('excelpath=', excelpath)

        with open(excelpath, 'wb') as f:
            f.write(contents)

        #  показ формы для взятия данных из EXCEL-файла
        title = "Стадия 2. Взятие данных из EXCEL-файла"
        result = 2

        result_text = f" С компьютера на сервер закачан файл {file.filename} "

        return templates.TemplateResponse("retrieve.html",
                                          {"request": request, "title": title, "result": result,
                                           "result_text": result_text})
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()


# ------------------- выполнение извлечения данных из EXCEL-файла

@app.post("/retrieve")
# def do_retrieve (request: Request, retr:str="very"):
def do_retrieve(request: Request, retr: str = Form(default="0"), button_tosite: str = Form(default="0")):
    #  при клике кнопку формы взятия данных из EXCEL-файла - выполнение извлечения данных
    import paths_
    rootfolder = paths_.path(1)
    excelpath = rootfolder / 'files' / '1.xlsx'
    print('excelpath=', excelpath)

    import utils.shared
    # -----------  когда нажали кнопку ИЗВЛЕТЬ ДАННЫЕ   -----------------------
    if (retr == "1" and button_tosite == "0"):
        try:

            # ----------- retrieving from excel --------------
            prlist_kurs, prlist_client = excel1_go(excelpath, 0)
            print('курс',prlist_kurs[0])
            print('клиент', prlist_client[0])
            # ----------- retrieving from excel --------------

            print('КУРСОВ ИЗВЛЕЧЕНО =', len(prlist_kurs))

            app.state.prlist_kurs = prlist_kurs
            app.state.prlist_client = prlist_client

            notice = utils.shared.notice_retr
            result = 3
            title = "Стадия 3. Отправка данных на сайт"
            result_text = "Данные из EXCEL-файла извлечены"

        except Exception:
            notice = utils.shared.notice_retr
            error_str = traceback.format_exc()
            print("error trace =", error_str)
            return templates.TemplateResponse("error.html",
                                              {"request": request, "result": error_str,
                                               "notice": notice})

    # -----------  stage4 when TOSITE_BUTTON  clicked  -----------------------

    elif (retr == "0" and button_tosite == "1"):
        try:
            prlist_kurs = app.state.prlist_kurs
            prlist_client = app.state.prlist_client

            # ----------- send to db --------------
            agregate(prlist_kurs, prlist_client)
            # ----------- send to db --------------

            notice = utils.shared.notice_tosite
            title = "Стадия 4. Выполнена отправка данных на сайт"
            result_text = "Данные отправлены на сайт"
            result = 4

        except Exception:
            error_str = traceback.format_exc()
            print("error trace =", error_str)

            notice = utils.shared.notice_tosite
            # return error_str
            return templates.TemplateResponse("error.html",
                                              {"request": request, "result": error_str,
                                               "notice": notice})

    # -----------  stage4 finished  -----------------------

    else:
        print()

    return templates.TemplateResponse("retrieve.html",
                                      {"request": request, "title": title, "result": result,
                                       "result_text": result_text, "notice": notice})


# -------------------------------------------------------------------


if __name__ == "__main__":
    print('before app if')

    webbrowser.open('http://127.0.0.1:8001/', new=1, autoraise=True)
    # webbrowser.open('http://127.0.0.1:8001/upload', new=1, autoraise=True)
    # webbrowser.open('http://127.0.0.1:8001/retrieve', new=1, autoraise=True)

    # webbrowser.open('http://127.0.0.1:8001/docs', new=1, autoraise=True)

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")
