import mysql.connector
from mysql.connector import Error

from model.Categoria import Categoria


def conexao(hostname='localhost', database='estoque', user='root', password='12345678'):
    try:
        con = mysql.connector.connect(host=hostname, database=database, user=user, password=password)
        return con
    except Error as error:
        print("Falha ao obter a conexao do Banco de Dados: {}".format(error))


def inserir_categoria(categoria_):
    try:
        con = conexao()
        cursor = con.cursor()
        sql = "INSERT INTO categoria VALUES ({}, '{}')".format(categoria_.id_categoria, categoria_.nome)
        print("Executando a seguinte cláusula SQL: {}".format(sql))
        cursor.execute(sql)
        con.commit()
        print("")
        cursor.close()
    except Error as error:
        print("Falha ao obter a conexao do Banco de Dados: {}".format(error))
    finally:
        if con.is_connected():
            con.close()
            print("Conexao com Banco de Dados encerrada.")


if __name__ == '__main__':
    id_categoria = input("Informe o Id da Categoria: ")
    nome_categoria = input("Informe o Nome da Categoria: ")
    categoria = Categoria(id_categoria, nome_categoria)
    inserir_categoria(categoria)
