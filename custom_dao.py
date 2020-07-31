import sqlite3
from custom_classes import Configs as configs, colors

# QUERYS
insert_query = """INSERT INTO registros(topic, event_date, time_spent, brief_description, daily_percentage) VALUES(?, ?, ?, ?, ?);"""
create_script = """CREATE TABLE registros(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	topic VARCHAR(30),
	event_date DATE,
	time_spent SMALLINT,
	brief_description VARCHAR(50),
	daily_percentage DOUBLE(3)
);"""


# FUNC
def save_register(register):
    try:
        with sqlite3.connect(configs.db) as db_conn:
            db_conn.execute(
                insert_query,
                (register.topic, register.event_date, register.time_spent,
                 register.brief_description, register.daily_percentage)
            )
            db_conn.commit()
            print(colors.OKBLUE + 'Registro salvo com sucesso!' + colors.ENDC)
    except sqlite3.OperationalError:
        print(colors.FAIL + 'Erro ao salvar.' + colors.ENDC)


def create_table():
    with sqlite3.connect(configs.db) as db_conn:
        try:
            db_conn.execute(create_script)
            print('created table!')
        except sqlite3.OperationalError:
            pass
