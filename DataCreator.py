from DBConfig import DBConfiguration
from DataFinder import DataFinder
import re


class DataCreator:

    def create_new_client(self, first_name, surname, phone_number, email):
        db_config = DBConfiguration()
        conn = db_config.create_connection()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO clients(first_name, surname) VALUES (%s ,%s) returning id; 
                """, (first_name, surname))
            client_id = cur.fetchone()
            if phone_number:
                phone_match = re.fullmatch(r'[+]?\d{11}', phone_number)
                if not phone_match:
                    print('Неверно введен номер телефона!')
                    return
                cur.execute("""
                    INSERT INTO phone_numbers(phone_number, client_id) VALUES (%s, %s) returning id; 
                    """, (phone_number, client_id))
                # print(cur.fetchone())
            if email:
                email_match = re.fullmatch(r'[0-9a-zA-Z]+@[0-9a-zA-Z]+.[0-9a-zA-Z]+', email)
                if not email_match:
                    print('Неверно введен email!')
                    return
                cur.execute("""
                    INSERT INTO emails(email, client_id) VALUES (%s, %s) returning id; 
                    """, (email, client_id))
                # print(cur.fetchone())
            conn.commit()
        conn.close()
        print(f'Клиент успешно создан! Уникальный идентификатор клиента: {client_id[0]}')
        return

    def add_phone_number(self, client_id):
        db_config = DBConfiguration()
        conn = db_config.create_connection()
        with conn.cursor() as cur:
            data_finder = DataFinder()
            ids = data_finder.get_client_ids()
            k = 0
            for i in ids:
                if i[0] == client_id:
                    phone_number = input('Введите номер телефона, который хотите добавить клиенту: ')
                    phone_match = re.fullmatch(r'[+]?\d{11}', phone_number)
                    if not phone_match:
                        print('Неверно введен номер телефона!')
                        return
                    cur.execute("""
                        INSERT INTO phone_numbers(phone_number, client_id) VALUES (%s, %s) returning id;
                        """, (phone_number, client_id))
                    # print(cur.fetchone())
                    conn.commit()
                    print('Новый номер телефона успешно добавлен!')
                    k = 1
                    break
            if k != 1:
                print("Введен неверный идентификатор клиента!")
        conn.close()
        return

    def add_email(self, client_id):
        db_config = DBConfiguration()
        conn = db_config.create_connection()
        with conn.cursor() as cur:
            ids = DataFinder().get_client_ids()
            k = 0
            for i in ids:
                if i[0] == client_id:
                    email = input('Введите email, который хотите добавить клиенту: ')
                    email_match = re.fullmatch(r'[0-9a-zA-Z]+@[0-9a-zA-Z]+.[0-9a-zA-Z]+', email)
                    if not email_match:
                        print('Неверно введен email!')
                        return
                    cur.execute("""
                        INSERT INTO emails(email, client_id) VALUES (%s, %s) returning id;
                        """,(email, client_id))
                    # print(cur.fetchone())
                    conn.commit()
                    print('Новый email успешно добавлен!')
                    k = 1
                    break
            if k != 1:
                print("Введен неверный идентификатор клиента!")
        conn.close()
        return

