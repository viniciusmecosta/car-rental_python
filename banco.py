import sqlite3

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE cliente(id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,nome_cliente VARCHAR(255), cnh_cliente VARCHAR(255),nasc_cliente VARCHAR(255), tel_cliente VARCHAR(255), end_cliente VARCHAR(255))")
#cursor = banco.cursor()
#cursor.execute("CREATE TABLE funcionarios(id_funcio INTEGER PRIMARY KEY AUTOINCREMENT,nome_funcio VARCHAR(255), login_funcio VARCHAR(255),cargo_funcio VARCHAR(255), senha_funcio VARCHAR(255))")
#cursor = banco.cursor()
#cursor.execute(("INSERT INTO funcionarios(nome_funcio,login_funcio,cargo_funcio,senha_funcio) VALUES ('admin','admin','Gestor','admin')"))
#cursor.execute("CREATE TABLE carros(nome_carro VARCHAR(255), cliente VARCHAR(255),diarias VARCHAR(255), km VARCHAR(255), data_alug VARCHAR(255), data_dev VARCHAR(255), ocup VARCHAR(255))")
#cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Kwid')"))
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Mobi')"))
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Argo')"))
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Gol')"))
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Compass')"))
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Hrv')"))
#cursor = banco.cursor()
banco.commit()
banco.close()


