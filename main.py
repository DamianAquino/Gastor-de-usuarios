import Crud

host="127.0.0.1"
user = "user"
passwd = "passwd"
db = "db"
tabla = "tabla"


if __name__ == '__main__':
    api = Crud.Api(host, db, tabla, user, passwd)
    crud = Crud.Crud(api)
    crud.iniciarInterfaz()
