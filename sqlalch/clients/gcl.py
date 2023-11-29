from sqlalch.clients.clientb import Client
import pickle


def get_clients_list(prlist_clients):
    '''
    functuion creates list of clients (instances)
    :param prlist_clients :  list of clients (dict)
    :return: list of clients (instances)
    '''

    # ------------------------ установка пароля по цифрам телефона------

    import paths_
    rootfolder = paths_.path(1)
    hashespath = rootfolder / 'utils' / 'hashes.dat'
    print('hashespath=', hashespath)
    with open(hashespath, 'rb') as f:
        hashes = pickle.load(f)
    for cl in prlist_clients:
        clientphone = cl['username']
        pwd = clientphone[len(clientphone) - 4:len(clientphone) - 0]
        hashedpwd = hashes[pwd]
        cl['password'] = hashedpwd
        cl['resetCount'] = pwd

    # ------------------------ установка пароля по цифрам телефона

    clients_list = []
    print('          (ФОРМИРОВАНИЕ СПИСКА КЛИЕНТОВ-ЭКЗЕМПЛЯРОВ ИЗ EXCEL )')
    for pr in prlist_clients:
        client = Client()
        client.setpr(pr)
        clients_list.append(client)
    print('          (ФОРМИРОВАНИЕ СПИСКА КЛИЕНТОВ-ЭКЗЕМПЛЯРОВ ИЗ EXCEL ВЫПОЛНЕНО)')
    print('          ПОЛУЧЕНО КЛИЕНТОВ-ЭКЗЕМПЛЯРОВ: ', len(clients_list))
    return clients_list
