from DBConfig import DBConfiguration
from DataCreator import DataCreator
from DataChanger import DataChanger
from DataDeleter import DataDeleter
from DataFinder import DataFinder


class MenuManager:

    def hello(self):
        print('Здравствуйте! Вы вошли в сервис управления клиентами. Для начала работы авторизуйтесь!')
        db_config = DBConfiguration()
        db_config.authorize()
        return

    def get_client_id(self):
        client_id = int(input("Введите уникальный идентификатор клиента: "))
        return client_id

    def menu(self):
        data_creator = DataCreator()
        data_changer = DataChanger()
        data_deleter = DataDeleter()
        data_finder = DataFinder()
        while True:
            print('-------------------------------\nДля регистрации нового клиента введите 1. Чтобы добавить новый номер телефона клиента, нажмите 2.\n'
                  'Чтобы добавить новый email клиента, нажмите 3. Чтобы изменить данные клиента, нажмите 4.\n'
                  'Чтобы удалить клиента из сервиса, нажмите 5. Чтобы удалить номер телефона клиента, нажмите 6.\n'
                  'Чтобы узнать уникальный идентификатор клиента, нажмите 7. Чтобы узнать контакты клиента, нажмите 8.\n'
                  'Чтобы выйти из системы, нажмите q.\n-------------------------------'
                  )
            choice = input()
            if choice == '1':
                first_name = input('Введите имя нового клиента: ')
                surname = input('Введите фамилию нового клиента: ')
                phone_number = input('Введите номер телефона нового клиента. Если вы не хотите оставлять свой телефон, нажмите Enter. ')
                email = input('Введите email нового клиента. Если вы не хотите оставлять свой email, нажмите Enter. ')
                data_creator.create_new_client(first_name, surname, phone_number, email)
            elif choice == '2':
                client_id = self.get_client_id()
                data_creator.add_phone_number(client_id)
            elif choice == '3':
                client_id = self.get_client_id()
                data_creator.add_email(client_id)
            elif choice == '4':
                client_id = self.get_client_id()
                data_changer.change_client_details(client_id)
            elif choice == '5':
                client_id = self.get_client_id()
                data_deleter.delete_client(client_id)
            elif choice == '6':
                client_id = self.get_client_id()
                data_deleter.delete_phone_number(client_id)
            elif choice == '7':
                data_finder.find_client_id()
            elif choice == '8':
                client_id = self.get_client_id()
                data_finder.find_client_contacts(client_id)
            elif choice == 'q':
                break
        return
