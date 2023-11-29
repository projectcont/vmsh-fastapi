def hashset(clientphone):
    import bcrypt

    pwd = clientphone[len(clientphone) - 3:len(clientphone) - 0]
    bytePwd = pwd.encode('utf-8')
    hashedpwd = bcrypt.hashpw(bytePwd, bcrypt.gensalt())

    return pwd, hashedpwd