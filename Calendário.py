# -*- coding: utf-8 -*-
#!/usr/bin/python
import calendar
from datetime import datetime
from pytz import timezone


data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%A, %d/%m/%Y %H:%M:%S')

print(data_e_hora_sao_paulo_em_texto)
print("")

cal = [0]*12
cal[0] = calendar.month(2020, 1)
cal[1] = calendar.month(2020, 2)
cal[2] = calendar.month(2020, 3)
cal[3] = calendar.month(2020, 4)
cal[4] = calendar.month(2020, 5)
cal[5] = calendar.month(2020, 6)
cal[6] = calendar.month(2020, 7)
cal[7] = calendar.month(2020, 8)
cal[8] = calendar.month(2020, 9)
cal[9] = calendar.month(2020, 10)
cal[10] = calendar.month(2020, 11)
cal[11] = calendar.month(2020, 12)
print ("Aqui está o calendário:")
print(cal[0])
print(cal[1])
print(cal[2])
print(cal[3])
print(cal[4])
print(cal[5])
print(cal[6])
print(cal[7])
print(cal[8])
print(cal[9])
print(cal[10])
print(cal[11])
