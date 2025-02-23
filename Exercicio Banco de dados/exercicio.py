
#importando sqlite3
import sqlite3

#conectando ao banco de dados  exercicio
conexao = sqlite3.connect('exercicio')

#criando tabela alunos
#**`cursor()`** – O método `.cursor()` é chamado sobre a conexão (`conexao`) para criar um objeto **cursor**. O cursor é utilizado para executar comandos SQL
cursor = conexao.cursor()

#criando tabela alunos 
    #1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

    #2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#Inserindo dados dentro da tabela 
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Isabella",24, "relações internacionais" )')

#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Carolina",22, "relações públicas" )')

#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Beatriz",18, "Letras" )')

#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Hugo",28, "História" )')

#cursor.execute('DELETE from alunos (id, nome, idade, curso) VALUES (5, "Victor",22, "relações públicas" )')

cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Vinicius",22, "Engenharia" )')

    #3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".

#cursor.execute("SELECT * FROM alunos ")
#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#cursor.execute("SELECT * FROM alunos WHERE idade > 20 ")
#resultado = cursor.fetchall()
#for linha in resultado:
    #print(linha)

#c) Selecionar os alunos do curso de "Engenharia"
cursor.execute("SELECT * FROM alunos WHERE curso = ? ORDER BY nome", ("Engenharia",))
resultado = cursor.fetchall()

# Exibir os alunos encontrados
print("Alunos do curso de Engenharia em ordem alfabética:")
for aluno in resultado:
    print(aluno)

#finalizando - para enviar os commits
conexao.commit()
#para fechar o programa 
conexao.close