from get_list_func import get_list_operation
from list_sort_date import list_sort_operation
from change import Change

# Ссылка на файл
FILE_OPERATION = '../operations.json'


def main():
    # Основной код программы
    # получаем список операций EXECUTED через функцию
    all_list = get_list_operation(FILE_OPERATION)
    # Создаем список из 5 последних опреаций EXECUTED
    list_five_last_operation = list_sort_operation(all_list)
    # сортируем список по дате
    list_five_last_operation_sorty = sorted(list_five_last_operation, key=lambda x: x['date'])

    # перебираем список
    for list_t in reversed(list_five_last_operation_sorty):
        try:
            # Вызываем класс Change для изменения формата даты и обработки номеров карт и счетов
            work_class = Change(date=list_t['date'], from_operation=list_t['from'], to_operation=list_t['to'])

            print(work_class.change_date(), list_t['description'])
            print(work_class.change_from_operation(), '--->', work_class.change_to_operation())
            print(list_t['operationAmount']['amount'], list_t['operationAmount']['currency']['name'], '\n')
        # обработка ошибки
        except KeyError:
            work_class = Change(date=list_t['date'], to_operation=list_t['to'])
            print(work_class.change_date(), list_t['description'])
            print('none', '--->', work_class.change_to_operation())
            print(list_t['operationAmount']['amount'], list_t['operationAmount']['currency']['name'], '\n')


if __name__ == '__main__':

    main()