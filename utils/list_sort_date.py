def list_sort_operation(list_all):
    """Функция получения списка последних, подвержденных операций"""
    list_date = []  # пустой список для сбора дат операций# пустой список для сбора дат операций
    for date in list_all:
        list_date.append(date['date'])

    list_date.sort()
    five_list_date = (list_date[-5:])

    five_list_oprations = []  # пустой список для сбора пяти последних операций

    for date_key in list_all:
        # перебираем список операций и складываем нужные операции в список
        if date_key['date'] in five_list_date:
            five_list_oprations.append(date_key)

    return five_list_oprations