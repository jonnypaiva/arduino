import mysql.connector
import time

conect = mysql.connector.connect(
    user = 'jonpsouza',
    passoword = '12345',
    host = '127.0.0.1',
    database = 'JP'
)

cursor = conect.cursor()

inserir_dados = "INSERT INTO sinais(sin_temp, sin_umid) VALUES (%s, %s)"
dados_sensor = ['33.50', '66.98']
x = 0
while True:
    cursor.execute(inserir_dados, inserir_dados)
    conect.commit()
    time.sleep(5)
    x += 1

cursor.close()
conexao.close()