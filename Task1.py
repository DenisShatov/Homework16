documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people_name(ndoc):
    for nman in documents:
        if nman["number"] == ndoc:
            return nman["name"]
            break
    else:
        return False


def shelf_num(ndoc):
    for k, v in directories.items():
        if ndoc in v:
            return k
    return False


def list_doc():
    ldoc = []
    for doc in documents:
        ldoc.append(doc["name"])
    return ldoc


def add_doc(ndoc, tdoc, nman, ndir):
    if ndir in directories:
        documents.append({"type": tdoc, "number": ndoc, "name": nman})
        directories[ndir].append(ndoc)
        return ndir
    else:
        return False


def add_shelf(ndir):
    if ndir in directories:
        return False
    else:
        directories[ndir] = []
        return True


def del_doc(ndoc):
    for doc in documents:
        if doc['number'] == ndoc:
            documents.remove(doc)
    for docv in directories:
        if ndoc in directories[docv]:
            directories[docv].remove(ndoc)
            return True
    return False


def move_doc(ndoc, ndir):
    if ndir not in directories:
        return False

    for docv in directories.values():
        if ndoc in docv:
            docv.remove(ndoc)
            directories[ndir].append(ndoc)
            return True
            break
    else:
        return False


def main():
    while True:
        command = input('\nВведите команду из списка:'
                        '\np – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит'
                        '\ns – команда, которая спросит номер документа и выведет номер полки, на которой он находится'
                        '\nl – команда, которая выведет список всех документов'
                        '\na – команда, которая добавит новый документ в каталог и в перечень полок'
                        '\nd – команда, которая спросит номер документа и удалит его из каталога и из перечня полок'
                        '\nm – команда, которая спросит номер документа и целевую полку, и переместит его с текущей '
                        'полки на целевую'
                        '\nas – команда, которая спросит номер новой полки и добавит ее в перечень'
                        '\nexit - команда, которая закроет программу\n')
        if command == 'p':
            print(people_name(input('Введите № документа: ')))

        elif command == 's':
            print(shelf_num(input('Введите № документа: ')))

        elif command == 'l':
            print(list_doc())

        elif command == 'a':
            print(add_doc(input('Введите № документа: '), input('\nВведите Тип документа: '),
                          input('\nВведите Имя владельца: '), input('\nВведите № полки: ')))

        elif command == 'd':
            print(del_doc(input('Введите № документа: ')))

        elif command == 'm':
            print(move_doc(input('Введите № документа: '),
                           input('\nВведите № полки, на которую переместить документ: ')))

        elif command == 'as':
            print(add_shelf(input('Введите № новой полки: ')))

        elif command == 'exit':
            break

        else:
            print('Введена некорректная команда, введите команду из списка')


if __name__ == '__main__':
    main()
