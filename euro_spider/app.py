import schedule
from time import sleep
import os

# Mudar uma vez para o diretório que contém o prejeto scrapy
print(os.getcwd())  # diz a pasta em que estou
os.chdir('euro_spider')
print(os.getcwd())  # verifica se mudou de pasta


# Criar uma função que será executada periodicamente
def rodar_botprecos():
    os.system('scrapy crawl eurobot')


# Agendar essa execução
schedule.every(1).minutes.do(rodar_botprecos)
print(str(schedule.next_run()))
# Colocar esse agendamento na fila
while True:
    schedule.run_pending()
    sleep(1)
