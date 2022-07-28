from DBConfig import DBConfiguration
from DataFinder import DataFinder


class DataChanger:

    def change_client_details(self, client_id):
        db_config = DBConfiguration()
        conn = db_config.create_connection()
        with conn.cursor() as cur:
            ids = DataFinder().get_client_ids()
            k = 0
            for i in ids:
                if i[0] == client_id:
                    choice = input('Какие данные вы хотите изменить? 1- Имя, 2- Фамилия: ')
                    k =+1
                    if choice == '1':
                        client_change = input('Введите новое имя: ')
                        cur.execute("""
                            UPDATE clients SET first_name = %s WHERE id = %s;
                            """,(client_change, client_id))
                        conn.commit()
                        cur.execute("""
                            SELECT first_name,surname FROM clients WHERE id = %s;
                            """,(client_id,))
                        print(*cur.fetchone())
                    if choice == '2':
                        client_change = input('Введите новую фамилию: ')
                        cur.execute("""
                            UPDATE clients SET surname = %s WHERE id = %s;
                            """,(client_change, client_id))
                        conn.commit()
                        cur.execute("""
                            SELECT first_name,surname FROM clients WHERE id = %s;
                            """,(client_id,))
                        print(*cur.fetchone())
            if k != 1:
                print("Введен неверный идентификатор клиента!")
        conn.close()
        return
