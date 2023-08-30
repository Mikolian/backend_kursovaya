from datetime import datetime


class Change:

    def __init__(self, date='', from_operation='', to_operation=''):
        # Дата из последних 5 операций
        self.date = date
        # откуда операци
        self.from_operation = from_operation
        # куда операция
        self.to_operation = to_operation

    def __repr__(self):
        return f'{self.__class__.__name__}\n' \
               f'Дата = {self.date}\n' \
               f'Операция от кого = {self.from_operation}\n' \
               f'Операция кому = {self.to_operation}'

    def change_date(self):
        """Метод изменяет дату на нужную"""
        date_from_str = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        return date_from_str.strftime('%d.%m.%Y')

    def change_from_operation(self):
        """метод скрывает цифры карты или счета ОТ КОГО отправлено"""
        split_list = self.from_operation.split(' ')
        if len(split_list[-1]) == 16:
            split_number = split_list[-1][0:4] + ' ' + split_list[-1][4:6] +'XX XXXX ' + split_list[-1][-4:]

            return ' '.join(split_list[:-1]) + ' ' + str(split_number)
        else:
            split_from = 'XX' + split_list[-1][-4:]
            return ' '.join(split_list[:-1]) + ' ' + str(split_from)

    def change_to_operation(self):
        """метод скрывает цифры карты или счета КУДА отправлено"""
        split_list = self.to_operation.split(' ')
        if len(split_list[-1]) == 16:
            split_number = split_list[-1][0:4] + ' ' + split_list[-1][4:6] +'XX XXXX ' + split_list[-1][-4:]
            return ' '.join(split_list[:-1]) + ' ' + str(split_number)
        else:
            split_from = 'XX' + split_list[-1][-4:]
            return ' '.join(split_list[:-1]) + ' ' + str(split_from)