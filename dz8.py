def print_contacts(file_name):
    with open(file_name, 'r', encoding = 'utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                 print(line.strip(), end = '\n\n')
        else :
             print('Список контактов пустой')

def connect_with_user():
     print('Введите имя, фамилью и телефон')
     con_info = input()
     return con_info

def add_contacts(file_name):
    with open(file_name, 'r', encoding = 'utf8') as file:
            all_cont =  file.readlines()
    new_cont = connect_with_user()
    all_cont.append(new_cont)
    with open(file_name, 'w', encoding = 'utf8') as file:
         file.writelines(all_cont)

def users():
     print('Выберите параметр для поиска:\
           \n 1 - Имя \
           \n 2 - Фамилия \
           \n 3 - Телефон')
     con = int(input())
     if con == 1 :
          print('Введите имя:') 
          con1 = input()
     if con == 2 :
          print('Введите фамилию:')
          con1 = input()
     if con == 3 :
          print('Введите номер телефона')
          con1 = input()
     return [con, con1]


def find_contact(file_name) :
     with open(file_name, 'r', encoding = 'utf8') as file:
            all_cont =  file.readlines()
     print(*all_cont)
     list_users = users()
     n = list_users[0]
     data = list_users[1]
     print('Найденные контакты:')
     for cont in all_cont:
          cont_as_list = cont.strip().split()
          if cont_as_list[n-1] == data :
               print(*cont_as_list)
          
def delete_contact(file_name) :
     with open(file_name, 'r', encoding = 'utf8') as file:
            all_cont =  file.readlines()
     print(*all_cont)
     list_users = users()
     n = list_users[0]
     data = list_users[1]
     list_del = list()
     print('Найденные контакты:')
     for cont in all_cont:
          cont_as_list = cont.strip().split()
          if cont_as_list[n-1] == data :
               list_del.append(cont)
               print(*cont_as_list)
     print('Уточните контакт, который хотите удалить (введите номер строки)')
     a = int(input())
     for con in all_cont :
          if con == list_del[a-1] :
               all_cont.remove(con)
     print('Удалённый контакт:')
     print(con)
     with open(file_name, 'w', encoding = 'utf8') as file:
         file.writelines(all_cont)

def change_contact (file_name) :
     with open(file_name, 'r', encoding = 'utf8') as file:
            all_cont =  file.readlines()
     print(*all_cont)
     list_users = users()
     n = list_users[0]
     data = list_users[1]
     list_del = list()
     print('Найденные контакты:')
     for cont in all_cont:
          cont_as_list = cont.strip().split()
          if cont_as_list[n-1] == data :
               list_del.append(cont)
               print(*cont_as_list)
     print('Уточните контакт, который хотите изменить (введите номер строки)')
     a = int(input())
     for con in all_cont :
          if con == list_del[a-1] :
               d = all_cont.index(con)
               all_cont.remove(con)
     with open(file_name, 'w', encoding = 'utf8') as file:
         file.writelines(all_cont)
     print('Введите изменения')
     con = connect_with_user()
     all_cont.insert(d,con + '\n')
     with open(file_name, 'w', encoding = 'utf8') as file:
         file.writelines(all_cont)

def import_contact(file_to_add ,file_name):
     try:
        with open(file_to_add, 'r', encoding = 'utf8') as new_contacts, open(file_name, 'r', encoding = 'utf8') as file:
            contacts_to_add = new_contacts.readlines()
            for line in contacts_to_add :
                 print(line.strip(), end = '\n')
            all_cont = file.readlines()
            print('Какую строку вы хотите скопировать: ')
            n = int(input())
            all_cont.append('\n' + contacts_to_add[n-1])
        with  open(file_name, 'w', encoding = 'utf8') as file:
            file.writelines(all_cont)
     except FileNotFoundError:
        print(f'{file_to_add} не найден')
