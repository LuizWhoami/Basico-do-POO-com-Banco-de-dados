import sqlite3

class funcionario:
    def __init__(self, nome=None, cargo=None, salario=None):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def armazenar(self):
        conn = sqlite3.connect('Funcionario.db')
        cursor = conn.cursor()
        funcionario = (self.nome, self.cargo, self.salario)
        inserir = 'INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)'
        cursor.execute(inserir, funcionario)
        conn.commit()
        conn.close

    @staticmethod
    def visualizar():
        conn = sqlite3.connect('Funcionario.db')
        cursor = conn.cursor()
        inserir = 'SELECT * FROM funcionarios'
        cursor.execute(inserir)
        dados = cursor.fetchall()
        print('\n ')
        print('=-'*20)
        print('Banco de dados')
        print('=-'*20)
        for data in dados:
            print(data)
        conn.commit()
        conn.close()

def infos():
    nome = str(input('Nome: '))
    cargo = str(input('Cargo: '))
    salario = float and int(input('Salario: '))
    pessoa = funcionario(nome, cargo, salario)
    pessoa.armazenar()

repete = '='
print(repete*50)
print('\n')
print("""
Sistema de Controle de Funcionarios
        [1] Armazenar
        [2] visualizar""")
print('\n')
print(repete*50)

escolha = int(input('Escolha: '))
    
if escolha == 1:
    infos()
elif escolha == 2:
    receber = funcionario()
    receber.visualizar()

else:
    print('Escolheu algo errado')

#database
conn = sqlite3.connect('Funcionario.db')
cursor = conn.cursor()

db = """
CREATE TABLE IF NOT EXISTS funcionarios
(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    cargo TEXT,
    salario REAL
);
"""
cursor.execute(db)
conn.commit()
conn.close()



#inserir

#conn = sqlite3.connect('Funcionario.db')
#cursor = conn.cursor()
#funcionario = ['Dvison', 'analista', 3000]
#insert = 'INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)'
#cursor.execute(insert, funcionario)
#conn.commit()
#conn.close()

#visualizar

#conn = sqlite3.connect('Funcionario.db')
#cursor = conn.cursor()
#visualizar = 'SELECT * FROM funcionarios'
#cursor.execute(visualizar)
#dados = cursor.fetchall()
#for func in dados:
#    print(func)
#conn.commit()
#conn.close()