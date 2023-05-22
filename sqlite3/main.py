from PyQt5 import uic, QtWidgets, QtCore
import sqlite3


banco = sqlite3.connect('banco.db')


#FUNCAO LOGIN
def logar():
    login = pt1.loginspace.text()
    senha = pt1.pinspace.text()
    if login == '' or senha == '':
        QtWidgets.QMessageBox.about(pt1, 'Erro',
                                    'Por favor preencha todos os campos para logar')
        return
    try:
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM funcionarios")
        resultado = cursor.fetchall()
        for check in resultado:
            if login == check[2]:
                if senha == check[4]:
                    if "Padrao" == check[3]:
                        pt1.close()
                        pt2.show()
                        pt2.funcionario.setEnabled(False)
                        print("padrao")
                    else:
                        pt1.close()
                        pt2.show()
                        print("gestor")
                else:
                    pt1.infoname.setText("Dados incorretos")
                    pt1.pinspace.setText("")
                    pt1.loginspace.setText("")
            else:
                pt1.infoname.setText("Dados incorretos")
                pt1.pinspace.setText("")
                pt1.loginspace.setText("")
    except:
        print("Erro ao validar os dados")



#FUNCOES LOGOUT
def logout():
    pt2.close()
    pt1.infoname.setText("")
    pt1.pinspace.setText("")
    pt1.loginspace.setText("")
    pt1.show()

def logout3():
    pt3.close()

def logout4():
    pt4.close()

def logout5():
    pt5.close()

def logout6():
    pt6.close()

def logout7():
    pt7.close()

def logout8():
    pt8.close()

def logout9():
    pt9.close()

def logout10():
    pt10.close()
    pt2.show()

def logout11():
    pt11.close()
    pt2.show()


def logout12():
    pt12.label_info.setText("")
    pt12.close()

def logout13():
    pt13.label_info.setText("")
    pt13.close()

def logout14():
    pt14.label.setText("")
    pt14.close()
    pt11.show()
    cursor = banco.cursor()
    cursor.execute("SELECT nome_funcio,cargo_funcio,login_funcio,senha_funcio FROM funcionarios")
    dados_lidos = cursor.fetchall()
    pt11.tabela_funcio.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            pt11.tabela_funcio.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def logout15():
    pt15.label.setText("")
    pt15.close()
    pt10.show()
    cursor = banco.cursor()
    cursor.execute("SELECT nome_cliente,cnh_cliente,nasc_cliente,end_cliente,tel_cliente FROM cliente")
    dados_lidos = cursor.fetchall()
    pt10.tabelacliente.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            pt10.tabelacliente.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))




#FUNCOES CHAMAR TELA

def chamar_tela_alugar():
    pt3.show()


def chamar_tela_kwid():
    pt4.show()


def chamar_tela_mobi():
    pt5.show()


def chamar_tela_argo():
    pt6.show()


def chamar_tela_gol():
    pt7.show()


def chamar_tela_compass():
    pt8.show()


def chamar_tela_hrv():
    pt9.show()

def chamar_tela_cliente():
    pt2.close()
    pt10.show()
    cursor = banco.cursor()
    cursor.execute("SELECT nome_cliente,cnh_cliente,nasc_cliente,end_cliente,tel_cliente FROM cliente")
    dados_lidos = cursor.fetchall()
    pt10.tabelacliente.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            pt10.tabelacliente.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def chamar_tela_funcio():
    pt2.close()
    pt11.show()
    cursor = banco.cursor()
    cursor.execute("SELECT nome_funcio,cargo_funcio,login_funcio,senha_funcio FROM funcionarios")
    dados_lidos = cursor.fetchall()
    pt11.tabela_funcio.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            pt11.tabela_funcio.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def chamar_tela_editar_cliente():
    row = pt10.tabelacliente.currentRow()
    nome = pt10.tabelacliente.item(row, 0).text()
    cnh = pt10.tabelacliente.item(row, 1).text()
    nasc = pt10.tabelacliente.item(row, 2).text()
    end = pt10.tabelacliente.item(row, 3).text()
    tel = pt10.tabelacliente.item(row, 4).text()
    
    pt15.clientes_name_2.setPlaceholderText(nome)
    pt15.clientes_cnh_2.setPlaceholderText(cnh)
    pt15.clientes_end_2.setPlaceholderText(end)
    pt15.clientes_tel_2.setPlaceholderText(tel)

    pt10.close()
    pt15.show()


def chamar_tela_cadastrar_cliente():
    pt12.show()

def chamar_tela_cadastrar_funcio():
    pt13.show()

def chamar_tela_editar_funcio():
    row = pt11.tabela_funcio.currentRow()
    nome = pt11.tabela_funcio.item(row, 0).text()
    cargo = pt11.tabela_funcio.item(row, 1).text()
    login = pt11.tabela_funcio.item(row, 2).text()
    senha = pt11.tabela_funcio.item(row, 3).text()

    pt14.funci_name_2.setPlaceholderText(nome)
    pt14.funci_login_3.setPlaceholderText(login)
    pt14.funci_senha_2.setPlaceholderText(senha)
    pt14.funci_senha_3.setPlaceholderText(senha)

    if (cargo == "Gestor"):
        pt14.radio_gestor.setChecked(True)
    else:
        pt14.radio_padrao.setChecked(True)

    pt11.close()
    pt14.show()
    

#FUNCOES CADASTRAR

def cadastrar_funcionario():

    caracteres = "!@#$%¨&*()-=+[]"
    nome = pt13.funci_name_2.text()
    login = pt13.funci_login_3.text()
    senha = pt13.funci_senha_2.text()
    senha2 = pt13.funci_senha_3.text()

    if nome == '' or login == '' or senha == '' or senha2 == '':
        QtWidgets.QMessageBox.about(pt1, 'Erro',
                                    'Por favor preencha todos os campos antes de inserir')
        return

    for j in caracteres:
        if j in nome:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar o nome!')
            return

    for j in caracteres:
        if j in login:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar o login!')
            return

    for j in caracteres:
        if j in senha:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar a senha!')
            return

    for j in caracteres:
        if j in senha2:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para confirmar a senha!')
            return


    if pt13.radio_gestor.isChecked():
        opcao="Gestor"
    else:
        opcao="Padrão"

    if(senha==senha2):
        try:
            cursor = banco.cursor()
            cursor.execute(("INSERT INTO funcionarios(nome_funcio,login_funcio,cargo_funcio,senha_funcio) VALUES ('" + nome + "','" + login + "','" + opcao + "','" + senha + "')"))
            banco.commit()
            pt13.label_info.setText("Usuario cadastrado com sucesso")
            pt13.funci_name_2.setText("")
            pt13.funci_login_3.setText("")
            pt13.funci_senha_2.setText("")
            pt13.funci_senha_3.setText("")
        except:
            print("Erro ao inserir os dados: ")
    else:
        pt13.label_info.setText("As duas senhas não coincidem")
    cursor = banco.cursor()
    cursor.execute("SELECT nome_funcio,cargo_funcio,login_funcio,senha_funcio FROM funcionarios")
    dados_lidos = cursor.fetchall()
    pt11.tabela_funcio.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            pt11.tabela_funcio.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def cadastrar_cliente():

    caracteres = "!@#$%¨&*()-=+[]"
    nome = pt12.clientes_name_2.text()
    cnh = pt12.clientes_cnh_2.text()
    nasc = pt12.clientes_nasc_2.text()
    tel = pt12.clientes_tel_2.text()
    end = pt12.clientes_end_2.text()

    if nome == '' or cnh == '' or nasc == '' or tel == '' or end == '':
        QtWidgets.QMessageBox.about(pt1, 'Erro',
                                    'Por favor preencha todos os campos antes de inserir')
        return

    for j in caracteres:
        if j in nome:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar o nome!')
            return

    for j in caracteres:
        if j in cnh:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar o número da CNH!')
            return

    for j in caracteres:
        if j in nasc:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar a data de nascimento!')
            return

    for j in caracteres:
        if j in tel:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar o telefone!')
            return

    try:
        cursor = banco.cursor()
        cursor.execute(("INSERT INTO cliente(nome_cliente,cnh_cliente,nasc_cliente,tel_cliente,end_cliente) VALUES ('" + nome + "','" + cnh + "','" + nasc + "','" + tel + "','" + end + "')"))
        banco.commit()
        pt12.label_info.setText("Usuário cadastrado com sucesso")
        pt12.clientes_name_2.setText("")
        pt12.clientes_cnh_2.setText("")
        #pt12.clientes_nasc_2.setText("01/01/2000")
        pt12.clientes_tel_2.setText("")
        pt12.clientes_end_2.setText("")
    except:
        print("Erro ao inserir os dados: ")
    cursor = banco.cursor()
    cursor.execute("SELECT nome_cliente,cnh_cliente,nasc_cliente,tel_cliente,end_cliente FROM cliente")
    dados_lidos = cursor.fetchall()
    pt10.tabelacliente.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            pt10.tabelacliente.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

#FUNCOES EDITAR
def editar_cliente():
    caracteres = "!@#$%¨&*()-=+[]"

    nome = pt15.clientes_name_2.placeholderText()
    cnh = pt15.clientes_cnh_2.placeholderText()
    tel = pt15.clientes_tel_2.placeholderText()
    end = pt15.clientes_end_2.placeholderText()

    nome_novo = pt15.clientes_name_2.text()
    cnh_novo = pt15.clientes_cnh_2.text()
    nasc_novo = pt15.clientes_nasc_2.text()
    tel_novo = pt15.clientes_tel_2.text()
    end_novo = pt15.clientes_end_2.text()

    if nome_novo == '':
        nome_novo = nome
    if cnh_novo == '':
        cnh_novo = cnh
    if nasc_novo == '':
        nasc_novo = "01/01/2000"
    if tel_novo == '':
        tel_novo = tel
    if end_novo == '':
        end_novo = end

    for j in caracteres:
        if j in nome_novo:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar o nome!')
            return

    for j in caracteres:
        if j in cnh_novo:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar a CNH!')
            return

    for j in caracteres:
        if j in nasc_novo:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar a data de nascimento!')
            return

    for j in caracteres:
        if j in tel_novo:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar o telefone!')
            return

    try:
        cursor = banco.cursor()
        cursor.execute("UPDATE cliente SET nome_cliente=?, cnh_cliente=?, nasc_cliente=?, tel_cliente=?, end_cliente=? WHERE nome_cliente=? AND cnh_cliente=? AND tel_cliente=? AND end_cliente=?",
        (nome_novo, cnh_novo, nasc_novo, tel_novo, end_novo, nome, cnh, tel, end,))
        banco.commit()
        pt15.label.setText("Usuário atualizado com sucesso")
        pt15.clientes_name_2.setText("")
        pt15.clientes_name_2.setPlaceholderText("")
        pt15.clientes_cnh_2.setText("")
        pt15.clientes_cnh_2.setPlaceholderText("")
        #pt15.clientes_nasc_2.setText("01/01/2000")
        pt15.clientes_tel_2.setText("")
        pt15.clientes_tel_2.setPlaceholderText("")
        pt15.clientes_end_2.setText("")
        pt15.clientes_end_2.setPlaceholderText("")
    except:
        print("Erro ao inserir os dados: ")

def editar_funcionario():
    caracteres = "!@#$%¨&*()-=+[]"

    nome = pt14.funci_name_2.placeholderText()
    login = pt14.funci_login_3.placeholderText()
    senha = pt14.funci_senha_2.placeholderText()
    senha2 = pt14.funci_senha_3.placeholderText()

    if pt14.radio_gestor.isChecked():
        cargo = "Gestor"
    else:
        cargo = "Padrão"

    nome_novo = pt14.funci_name_2.text()
    login_novo = pt14.funci_login_3.text()
    senha_novo = pt14.funci_senha_2.text()
    senha2_novo = pt14.funci_senha_3.text()

    if nome_novo == '':
        nome_novo = nome
    if login_novo == '':
        login_novo = login
    if senha_novo == '':
        senha_novo = senha
    if senha2_novo == '':
        senha2_novo = senha2

    for j in caracteres:
        if j in nome_novo:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar o nome!')
            return

    for j in caracteres:
        if j in login_novo:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar o login!')
            return

    for j in caracteres:
        if j in senha_novo:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para registrar a senha!')
            return

    for j in caracteres:
        if j in senha2_novo:
            QtWidgets.QMessageBox.about(pt1, 'Erro',
                                        'Por favor não use caractéres especiais para confirmar a senha!')
            return

    if pt14.radio_gestor.isChecked():
        opcao="Gestor"
    else:
        opcao="Padrão"

    if(senha_novo==senha2_novo):
        try:
            cursor = banco.cursor()
            cursor.execute("UPDATE funcionarios SET nome_funcio=?, login_funcio=?, cargo_funcio=?, senha_funcio=? WHERE nome_funcio=? AND login_funcio=? AND cargo_funcio=? AND senha_funcio=?", 
            (nome_novo, login_novo, opcao, senha_novo, nome, login, cargo, senha,))
            banco.commit()
            pt14.label.setText("Funcionário atualizado com sucesso")
            pt14.funci_name_2.setText("")
            pt14.funci_name_2.setPlaceholderText("")
            pt14.funci_login_3.setText("")
            pt14.funci_login_3.setPlaceholderText("")
            pt14.funci_senha_2.setText("")
            pt14.funci_senha_2.setPlaceholderText("")
            pt14.funci_senha_3.setText("")
            pt14.funci_senha_3.setPlaceholderText("")
        except:
            print("Erro ao inserir os dados: ")
    else:
        pt14.label.setText("As duas senhas não coincidem")
    
    
#FUNCOES EXCLUIR
def excluir_funcionario():
    try:
        row = pt11.tabela_funcio.currentRow()
        
        nome = pt11.tabela_funcio.item(row, 0).text()
        cargo = pt11.tabela_funcio.item(row, 1).text()
        login = pt11.tabela_funcio.item(row, 2).text()
        senha = pt11.tabela_funcio.item(row, 3).text()

        cursor = banco.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE nome_funcio = ? AND cargo_funcio = ? AND login_funcio = ? AND senha_funcio = ?", (nome, cargo, login, senha,))
        banco.commit()
        pt11.tabela_funcio.removeRow(row)

        print("Funcionário deletado")
    except:
        print("Um erro ocorreu ao deletar o funcionário")


def excluir_cliente():
    try:
        row = pt10.tabelacliente.currentRow()
        
        nome = pt10.tabelacliente.item(row, 0).text()
        cnh = pt10.tabelacliente.item(row, 1).text()
        nasc = pt10.tabelacliente.item(row, 2).text()
        tel = pt10.tabelacliente.item(row, 3).text()
        end = pt10.tabelacliente.item(row, 4).text()

        cursor = banco.cursor()
        cursor.execute("DELETE FROM cliente WHERE nome_cliente = ? AND cnh_cliente = ? AND nasc_cliente = ? AND tel_cliente = ? AND end_cliente = ?", (nome, cnh, nasc, tel, end,))
        banco.commit()
        pt10.tabelacliente.removeRow(row)

        print("Cliente deletado")
    except:
        print("Um erro ocorreu ao deletar o cliente")



app = QtWidgets.QApplication([])
#CRIAR TELAS
pt1 = uic.loadUi("tela/pt1(login).ui")
pt2 = uic.loadUi("tela/pt2(inicial).ui")
pt3 = uic.loadUi("tela/pt3(carros).ui")
pt4 = uic.loadUi("tela/pt4(kwid).ui")
pt5 = uic.loadUi("tela/pt5(mobi).ui")
pt6 = uic.loadUi("tela/pt6(argo).ui")
pt7 = uic.loadUi("tela/pt7(gol).ui")
pt8 = uic.loadUi("tela/pt8(compass).ui")
pt9 = uic.loadUi("tela/pt9(hrv).ui")
pt10 = uic.loadUi("tela/pt10(clientes).ui")
pt11 = uic.loadUi("tela/pt11(func).ui")
pt12 = uic.loadUi("tela/pt12(clientes_cadastro).ui")
pt13 = uic.loadUi("tela/pt13(func_cadastro).ui")
pt14 = uic.loadUi("tela/pt14(func_editar).ui")
pt15 = uic.loadUi("tela/pt15(clientes_editar).ui")


#BOTAO LOGIN
pt1.open.clicked.connect(logar)

#BOTOES CADASTRAR
pt12.salvar_cliente.clicked.connect(cadastrar_cliente)
pt13.salvar_funcio.clicked.connect(cadastrar_funcionario)

#BOTOES DELETAR
pt10.excluircliente.clicked.connect(excluir_cliente)
pt11.excluirfuncionario_3.clicked.connect(excluir_funcionario)

#BOTOES EDITAR
pt15.salvar_cliente.clicked.connect(editar_cliente)
pt14.salvar_funcio.clicked.connect(editar_funcionario)


#BOTOES CHAMAR TELA
pt2.funcionario.clicked.connect(chamar_tela_funcio)
pt2.cliente.clicked.connect(chamar_tela_cliente)
pt2.alugar.clicked.connect(chamar_tela_alugar)
pt3.kwid.clicked.connect(chamar_tela_kwid)
pt3.mobi.clicked.connect(chamar_tela_mobi)
pt3.argo.clicked.connect(chamar_tela_argo)
pt3.gol.clicked.connect(chamar_tela_gol)
pt3.compass.clicked.connect(chamar_tela_compass)
pt3.hrv.clicked.connect(chamar_tela_hrv)
pt10.cadastrarcliente.clicked.connect(chamar_tela_cadastrar_cliente)
pt10.editarcliente.clicked.connect(chamar_tela_editar_cliente)
pt11.cadastrarfuncionario_2.clicked.connect(chamar_tela_cadastrar_funcio)
pt11.editar_funcio.clicked.connect(chamar_tela_editar_funcio)


#BOTOES LOGOUT
pt2.exitbutton.clicked.connect(logout)
pt3.exitbutton.clicked.connect(logout3)
pt4.voltar_10.clicked.connect(logout4)
pt5.voltar_10.clicked.connect(logout5)
pt6.voltar_10.clicked.connect(logout6)
pt7.voltar_10.clicked.connect(logout7)
pt8.voltar_10.clicked.connect(logout8)
pt9.voltar_10.clicked.connect(logout9)
pt10.saircliente.clicked.connect(logout10)
pt11.sairfunc.clicked.connect(logout11)
pt12.voltar_10.clicked.connect(logout12)
pt13.voltar_10.clicked.connect(logout13)
pt14.voltar_10.clicked.connect(logout14)
pt15.voltar_10.clicked.connect(logout15)


pt1.show()
app.exec()
