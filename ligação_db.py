import sqlite3

with sqlite3.connect("MINHA_LISTA_TAREFAS.db") as conn:
  cursor = conn.cursor()

  cursor.execute(""" CREATE TABLE IF NOT EXISTS prioridade(
                   id INT PRIMARY KEY,
                   NOME TEXT NOT NULL
                    )""")
  
 
  
  cursor.execute(""" CREATE TABLE IF NOT EXISTS status(
                   id_status INTEGER,
                   nome TEXT)""")
  
  cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas(
                 id_tarefas INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT,
                 descricao TEXT,
                 id INTEGER,
                 id_status INTERGER,
                 FOREIGN KEY (id) REFERENCES prioridade(id), 
                 FOREIGN KEY (id_status) REFERENCES status(id_status))""")
  
  
  
  #cursor.execute("INSERT INTO prioridade (id,NOME) VALUES (?,?)",(1,"Alta"))
  #cursor.execute("INSERT INTO prioridade (id,NOME) VALUES (?,?)",(2,"Media"))
  #cursor.execute("INSERT INTO prioridade (id,NOME) VALUES (?,?)",(3,"Alta"))

  #cursor.execute("INSERT INTO status (id_status,nome) VALUES (?,?)",(1,"Não iniciada"))
  #cursor.execute("INSERT INTO status (id_status,nome) VALUES (?,?)",(2,"Em processo"))
  #cursor.execute("INSERT INTO status (id_status,nome) VALUES (?,?)",(3,"Concluida")) 
  