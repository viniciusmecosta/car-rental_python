import sqlite3
from db.queries import *
import db.queries as queries

class DBManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def _execute_query(self, query, params=None):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            conn.commit()
            return result
        except Exception as e:
            print(f"Database error: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    def get_funcionarios(self):
        return self._execute_query(queries.SELECT_FUNCIONARIOS_DETALHADOS)

    def get_clientes(self):
        return self._execute_query(queries.SELECT_CLIENTES)

    def get_login_funcionario(self, login):
        return self._execute_query(queries.SELECT_FUNCIONARIOS_DETALHADOS, (login,))

    def get_car_availability(self):
        return self._execute_query(queries.SELECT_NOME_CARRO_OCUP)

    def get_all_clientes(self):
        return self._execute_query(queries.SELECT_CLIENTES)

    def get_all_funcionarios(self):
        return self._execute_query(queries.SELECT_FUNCIONARIOS_DETALHADOS)

    def get_all_carros(self):
        return self._execute_query(queries.SELECT_NOME_CARRO_OCUP)

    def get_user(self, login):
        return self._execute_query(queries.SELECT_FUNCIONARIOS_DETALHADOS, (login,))

    def insert_funcionario(self, nome, login, cargo, senha):
        return self._execute_query(queries.INSERT_FUNCIONARIO, (nome, login, cargo, senha))

    def insert_cliente(self, nome, cnh, nasc, end, tel):
        return self._execute_query(queries.INSERT_CLIENTE, (nome, cnh, nasc, end, tel))

    def update_cliente(self, nome, cnh, nasc, end, tel, old_nome, old_cnh, old_end, old_tel):
        return self._execute_query(queries.UPDATE_CLIENTE, (nome, cnh, nasc, end, tel, old_nome, old_cnh, old_end, old_tel))

    def update_funcionario(self, nome, login, cargo, senha, old_nome, old_login, old_cargo, old_senha):
        return self._execute_query(queries.UPDATE_FUNCIONARIO, (nome, login, cargo, senha, old_nome, old_login, old_cargo, old_senha))

    def delete_funcionario(self, nome, cargo, login, senha):
        return self._execute_query(queries.DELETE_FUNCIONARIO, (nome, cargo, login, senha))

    def delete_cliente(self, nome, cnh):
        return self._execute_query(queries.DELETE_CLIENTE, (nome, cnh))

    def update_carro(self, cliente, data_alug, data_dev, ocup, nome_carro):
        return self._execute_query(queries.UPDATE_CARRO, (cliente, data_alug, data_dev, ocup, nome_carro))

    def update_ocupacao_carro(self, ocup, nome_carro):
        return self._execute_query(queries.UPDATE_OCUPACAO_CARRO, (ocup, nome_carro))