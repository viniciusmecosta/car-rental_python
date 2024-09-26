import sqlite3

def create_tables():
    banco = sqlite3.connect('banco.db')
    cursor = banco.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cliente TEXT NOT NULL,
            cnh_cliente TEXT,
            nasc_cliente TEXT,
            tel_cliente TEXT,
            end_cliente TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id_funcio INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_funcio TEXT NOT NULL,
            login_funcio TEXT NOT NULL,
            cargo_funcio TEXT NOT NULL,
            senha_funcio TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carros (
            id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_carro TEXT NOT NULL,
            cliente TEXT,
            diarias TEXT,
            km TEXT,
            data_alug TEXT,
            data_dev TEXT,
            ocup TEXT
        )
    ''')

    banco.commit()
    banco.close()

def insert_initial_data():
    banco = sqlite3.connect('banco.db')
    cursor = banco.cursor()

    carros = ['Kwid', 'Mobi', 'Argo', 'Gol', 'Compass', 'Hrv']
    for carro in carros:
        cursor.execute(f'''
            INSERT INTO carros (nome_carro)
            VALUES ('{carro}')
        ''')

    banco.commit()
    banco.close()

if __name__ == "__main__":
    insert_initial_data()
