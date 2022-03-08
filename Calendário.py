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

ano = 2022
data = calendar.calendar(ano)
print(data)

input()
