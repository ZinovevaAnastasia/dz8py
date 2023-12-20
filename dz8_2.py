from dz8 import print_contacts, add_contacts, find_contact, delete_contact, change_contact, import_contact
file_with_contacts = 'contacts.txt'

def interface():
    while True:
        print('Выберите действие:\
            \n 1 - Добавить контакт \
            \n 2 - Вывести все контакты \
            \n 3 - Найти контакт \
            \n 4 - Удалить контакт\
            \n 5 - Изменить контакт\
            \n 6 - Импортировать данные\
            \n 0 - Выйти')
        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contacts(file_with_contacts)
            case 2:
                print_contacts(file_with_contacts)
            case 3:
                find_contact(file_with_contacts)
            case 4:
                delete_contact(file_with_contacts)
            case 5:
                change_contact(file_with_contacts)
            case 6:
                file_to_add = input('Введите название импортируемого файла: ')
                import_contact(file_to_add, file_with_contacts)
            case _:
                print('Ошибка')

if __name__ == '__main__' :
 
    interface()






