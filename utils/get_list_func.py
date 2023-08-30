import json


def get_list_operation(path):
    """Функция возвращаения списка с успешными операциями EXECUTED"""
    with open(path, "r", encoding='utf-8') as file:
        list_operation = json.load(file)  # Загружаем файл операций

        list_exe_op = []  # пустой список для словарей EXECUTED

        for position in list_operation:
            # перебираем словари и складываем в пустой список словари операций со статусом EXECUTED
            try:
                if position['state'] == 'EXECUTED':
                    list_exe_op.append(position)

            except KeyError:
                continue

        return list_exe_op