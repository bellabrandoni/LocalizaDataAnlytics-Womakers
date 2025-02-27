
#importando sqlite3
import sqlite3

#conectando ao banco de dados  exercicio
conexao = sqlite3.connect('exercicio.')

#criando tabela alunos
#cursor()`** – O método `.cursor()` é chamado sobre a conexão (`conexao`) para criar um objeto **cursor**. O cursor é utilizado para executar comandos SQL


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

#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Vinicius",22, "Engenharia" )')

#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (6, "Edson",28, "Engenharia" )')
    #3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
    #a) Selecionar todos os registros da tabela "alunos".

#dados = cursor.execute('SELECT nome FROM alunos')

#for aluno in dados: 
    #print(aluno)


    #b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#resultado = cursor.execute("SELECT nome, idade FROM alunos WHERE idade > 20 ")
#for aluno in resultado:
    #print(aluno)


    #c) Selecionar os alunos do curso de "Engenharia"
#resultado = cursor.execute("SELECT nome, curso FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")
#for aluno in resultado:
    #print(aluno)

    #d) Contar o número total de alunos na tabela
#resultado = cursor.execute("SELECT COUNT(id) FROM alunos")
#for aluno in resultado:
    #print(aluno)

#4. Atualização e Remoção
    #a) Atualize a idade de um aluno específico na tabela.

#cursor.execute('UPDATE alunos SET idade="32" WHERE nome = "Vinicius"')

#dados = cursor.execute('SELECT * FROM alunos')

#for aluno in dados: 
    #print(aluno)


    #b) Remova um aluno pelo seu ID.
#cursor.execute('DELETE FROM alunos WHERE id = "2"')



#5. Criar uma Tabela e Inserir Dados

    #Crie uma tabela chamada "clientes" com os campos: id (chaveprimária), nome (texto), idade (inteiro) e saldo (float). 
    # #Insira alguns registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), idade INT, saldo FLOAT)')

#Inserindo dados dentro da tabela 
#cursor.execute('INSERT INTO clientes ( nome, idade, saldo) VALUES ("Isabella",25, 1500.75 )')
#cursor.execute('INSERT INTO clientes ( nome, idade, saldo) VALUES ( "Carlos",28, 2500.55 )')
#cursor.execute('INSERT INTO clientes ( nome, idade, saldo) VALUES ("Vinicius",28, 3500.75 )')
#cursor.execute('INSERT INTO clientes ( nome, idade, saldo) VALUES ("Eduardo",38, 2300.00 )')
#cursor.execute('INSERT INTO clientes ( nome, idade, saldo) VALUES ("Marcia",33, 2300.00 )')

#cursor.execute('INSERT INTO clientes ( nome, idade, saldo) VALUES ("Carolina",22, 5000.00 )')
#cursor.execute('INSERT INTO clientes ( nome, idade, saldo) VALUES ("Hugo",18, 4500.55 )')

#6. Consultas e Funções Agregadas
    #Escreva consultas SQL para realizar as seguintes tarefas:
    #a) Selecione o nome e a idade dos clientes com idade superior a
    #30 anos.

#resultado = cursor.execute("SELECT nome, idade FROM clientes WHERE idade > 30 ")

#for cliente in resultado:
    #print(cliente)


    #b) Calcule o saldo médio dos clientes.
#resultado = cursor.execute("SELECT AVG(saldo) FROM clientes")
#for cliente in resultado:
    #print(cliente)

    #c) Encontre o cliente com o saldo máximo.

#resultado = cursor.execute("SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)")

#for cliente in resultado:
    #print(cliente)


    #d) Conte quantos clientes têm saldo acima de 1000.

#resultado = cursor.execute("SELECT COUNT(*) FROM clientes WHERE saldo > 1000")
#for cliente in resultado:
    #print(cliente)


#7. Atualização e Remoção com Condições
    #a) Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE alunos SET idade="32" WHERE nome = "Vinicius"')
#cursor.execute('UPDATE clientes SET saldo = "900" WHERE nome = "Isabella"')


#dados = cursor.execute('SELECT * FROM clientes ')

#for cliente in dados: 
    #print(cliente)


    #b) Remova um cliente pelo seu ID.
#resultado = cursor.execute('DELETE FROM clientes WHERE id = "3"')
#dados = cursor.execute('SELECT * FROM clientes ')

#for cliente in dados: 
    #print(cliente)


#8. Junção de Tabelas 
    # Crie uma segunda tabela chamada "compras" com os 
# campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 

#cursor.execute('CREATE TABLE compras(id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER, produto VARCHAR(100), valor FLOAT)')

    # Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.


#cursor.execute('INSERT INTO compras (cliente_id, produto, valor)  VALUES (1, "smartphone", 500.75 )')
#cursor.execute('INSERT INTO compras (cliente_id, produto, valor)  VALUES (2, "sofá", 200.75 )')
#cursor.execute('INSERT INTO compras (cliente_id, produto, valor)  VALUES (4, "TV 4k", 2000.500 )')



#dados =  cursor.execute('SELECT * FROM clientes INNER JOIN compras ON cliente_id = compras.cliente_id')

#for cliente in dados:
    #print(cliente) 










#finalizando - para enviar os commits
conexao.commit()
#para fechar o programa 
conexao.close