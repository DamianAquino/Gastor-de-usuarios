import Crud

host="127.0.0.1"
user = "da"
passwd = "71384762"
db = "salvadora"
tabla = "usuarios"


if __name__ == '__main__':
    api = Crud.Api(host, db, tabla, user, passwd)
    crud = Crud.Crud(api)
    crud.iniciarInterfaz()
