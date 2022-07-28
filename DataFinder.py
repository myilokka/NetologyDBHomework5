from DBConfig import DBConfiguration


class DataFinder:

    def get_client_ids(self):
        db_config = DBConfiguration()
        conn = db_config.create_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id FROM clients;
                """)
            ids = cur.fetchall()
        conn.close()
        return ids

    def find_client_id(self):
        answer = int(input('Найти id клиента по: имени и фамилии - 1, номеру телефона - 2, email - 3. Введите нужную цифру: '))
        db_config = DBConfiguration()
        conn = db_config.create_connection()
        with conn.cursor() as cur:
            if answer == 1:
                first_name = input('Введите имя клиента: ')
                surname = input('Введите фамилию клиента: ')
                cur.execute("""
                    SELECT id FROM clients WHERE first_name=%s AND surname=%s;
                    """, (first_name, surname))
                client_id = cur.fetchall()
                if len(client_id) == 0:
                    print('В базе данных нет такого клиента!')
                if len(client_id) == 1:
                    print(f'Уникальный идентификатор клиента: {client_id[0][0]} ')
                if len(client_id) > 1:
                    print(f'Клиентов с таким именем и фамилией больше 1, их уникальные идентификаторы:{client_id} ')
            if answer == 2:
                phone_number = input('Введите номер телефона клиента. Если вы не осталявляли номер телефона, нажмите Enter. ')
                cur.execute("""
                    SELECT client_id FROM phone_numbers WHERE phone_number=%s;
                    """, (phone_number,))
                client_id = cur.fetchone()
                if client_id is None:
                    print('Такого номера телефона нет в базе данных!')
                else:
                    print(f'Уникальный идентификатор клиента: {client_id[0]}')
            if answer == 3:
                email = input('Введите email клиента. сли вы не осталявляли email, нажмите Enter. ')
                cur.execute("""
                    SELECT client_id FROM emails WHERE email=%s;
                    """, (email,))
                client_id = cur.fetchone()
                if client_id is None:
                    print('Такого email нет в базе данных!')
                else:
                    print(f'Уникальный идентификатор клиента: {client_id[0]}')
        conn.close()
        return

    def find_client_contacts(self, client_id):
        db_config = DBConfiguration()
        conn = db_config.create_connection()
        with conn.cursor() as cur:
            ids = self.get_client_ids()
            k = 0
            for i in ids:
                if i[0] == client_id:
                    k =+1
                    cur.execute("""
                        SELECT phone_number FROM phone_numbers WHERE client_id=%s;
                         """, (client_id, ))
                    phone_number = cur.fetchall()
                    print(f'Номера телефона клиента: {phone_number}')
                    cur.execute("""
                        SELECT email FROM emails WHERE client_id=%s;
                        """, (client_id, ))
                    email = cur.fetchall()
                    print(f'Email клиента: {email}')
            if k!=1:
                 print("Введен неверный идентификатор клиента!")
        conn.close()
        return
