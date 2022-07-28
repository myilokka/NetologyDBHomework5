import psycopg2


class DBConfiguration:

    def __init__(self):
        # self.database = input('Введите имя базы данных: ')
        # self.user = input('Введите имя пользователя БД: ')
        # self.password = input('Введите пароль пользователя БД: ')

        self.database = "client_managment_service"
        self.user = 'postgres'
        self.password = 'ratusha1'

    def authorize(self):
        self._create_tables()

    def _create_tables(self):
        conn = self.create_connection()
        with conn.cursor() as cur:
            # cur.execute("""
            #     DROP TABLE phone_numbers;
            #     DROP TABLE emails;
            #     DROP TABLE clients;
            # """)
            # conn.commit()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                id SERIAL PRIMARY KEY, 
                first_name VARCHAR(30) NOT NULL,
                surname VARCHAR(30) NOT NULL);
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phone_numbers (
                id SERIAL PRIMARY KEY, 
                phone_number VARCHAR(20),
                client_id INT,
                FOREIGN KEY (client_id) REFERENCES clients(id));
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS emails (
                id SERIAL PRIMARY KEY, 
                email VARCHAR(70),
                client_id INT,
                FOREIGN KEY (client_id) REFERENCES clients(id));
            """)
            conn.commit()
        conn.close()
        print("Таблицы успешно созданы!")
        return

    def create_connection(self):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        return conn
