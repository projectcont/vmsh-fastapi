def printf(text="", v=0):
    if v == 0:
        print(text)
    else:
        print(text, v)


def printf2(text="", v=0):
    if v == 0:
        print('           ', text)
    else:
        print('           ', text, v)


def printlist(text="", prod_list=[], ean=""):
    print()
    if ean == "":
        print(text)
        for v in prod_list:
            v.printit()
    else:
        print(text)
        for v in prod_list:
            if ean in v.pr['product_ean']: print('ext spec ean=', v.printit())
