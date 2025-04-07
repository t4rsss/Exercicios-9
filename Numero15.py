import os
import time
import datetime
import calendar

print("Diretório atual:", os.getcwd())
print("Data e hora atual:", datetime.datetime.now())

agora = datetime.datetime.now()
print("Calendário do mês atual:")
print(calendar.month(agora.year, agora.month))

print("Esperando 3 segundos...")
time.sleep(3)
print("Pronto!")
