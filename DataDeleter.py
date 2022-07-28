from DBConfig import DBConfiguration
from DataFinder import DataFinder


class DataDeleter:

     def delete_phone_number(self, client_id):
        db_config = DBConfiguration()
        conn = db_config.create_connection()
        with conn.cursor() as cur:
            ids = DataFinder().get_client_ids()
            k = 0
            for i in ids:
                if i[0] == client_id:
                    k =+ 1
                    cur.execute("""
                        SELECT phone_number FROM phone_numbers WHERE id = %s;
                        """, (client_id,))
                    list_numbers = cur.fetchall()
                    print(list_numbers)
                    if len(list_numbers) == 0:
                        print('У этого клиента нет номеров телефона в нашей базе!')
                    elif len(list_numbers) == 1:
                        cur.execute("""
                            DELETE FROM phone_numbers WHERE client_id=%s;
                            """, (client_id,))
                        conn.commit()
                        print('Номер телефона удален!')
                    elif len(list_numbers) > 1:
                        for c, j in enumerate(list_numbers):
                            print(f'{c}: {j[0]}')
                        answer = int(input('Какой именно номер вы хотите удалить? Введите цифру: '))
                        cur.execute("""
                            DELETE FROM phone_numbers WHERE phone_number=%s;
                            """, (list_numbers[answer][0],))
                        conn.commit()
                        print('Номер телефона удален!')
            if k != 1:
                print("Введен неверный идентификатор клиента!")
        conn.close()
        return

     def delete_client(self, client_id):
        db_config = DBConfiguration()
        conn = db_config.create_connection()
        with conn.cursor() as cur:
            ids = DataFinder().get_client_ids()
            k = 0
            for i in ids:
                if i[0] == client_id:
                    k =+1
                    cur.execute("""
                            DELETE FROM phone_numbers WHERE client_id=%s;
                            """, (client_id,))
                    cur.execute("""
                            DELETE FROM emails WHERE client_id=%s;
                            """, (client_id,))
                    conn.commit()
                    cur.execute("""
                            DELETE FROM clients WHERE id=%s;
                            """, (client_id,))
                    conn.commit()
                    print('Клиент удален!')
            if k != 1:
                print("Введен неверный идентификатор клиента!")
        conn.close()
        return
