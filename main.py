from custom_classes import Register, Configs as conf, colors
from custom_dao import save_register, create_table
import datetime as dt

print(colors.OKGREEN + conf.mini_logo + colors.ENDC)
print('Boa tarde ' + conf.user_name)
create_table()
topic_numbers = int(input('Com quantos tópicos você trabalhou hoje?'))
for topic_number in range(0, topic_numbers):
    topic_descr = str(input('Certo!, digite o nome do tópico'))  # melhorar
    time_spent = int(input('Quantas horas foram gastas?'))
    briefing_descr = str(input('Digite uma breve descrição do que foi feito:'))
    register = Register(topic_descr, dt.date.today(), time_spent, briefing_descr)
    save_register(register)
