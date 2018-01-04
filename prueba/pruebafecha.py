import datetime
import time

dia = time.strftime('%d')
mes = time.strftime('%m')
ano = time.strftime('%y')
fechahoy=datetime.datetime(int(ano),int(mes),int(dia))
print fechahoy
