from apiconverter import APIConverter

class InputException(Exception):
    pass


value_code = {'рубль': 'RUB', 'доллар': 'USD', 'евро': 'EUR', 'фунт': 'GBP', 'биткоин': 'BTC'}


class IOConverter():

    @staticmethod                       # get value code
    def get_value_code(text: str):
        try:
            return value_code[text]
        except:
            raise InputException(f'Неизвестная валюта {text}')

    @staticmethod                        # parse value code
    def convert(line: str):

        # parse input
        elements = line.split(' ')

        # check input
        if len(elements) < 3:
            raise InputException('Недостаточно параметров')
        if len(elements) > 3:
            raise InputException('Слишком много параметров')

        amount_text, from_text, into_text = elements

        if from_text == into_text:
            raise InputException('Одинаковые валюты')

        try:
            amount = float(amount_text)
        except ValueError:
            raise InputException('Неправильно введено количество')

        # try to get value code
        from_code = IOConverter.get_value_code(from_text)
        into_code = IOConverter.get_value_code(into_text)

        # send request
        total = APIConverter.convert_values(amount, from_code, into_code)
        total = round(total, 5)
        return f'{amount_text} {from_text} стоит {total} {into_text}'

    @staticmethod                        # get list of values
    def get_list():
        text = 'Доступные валюты:'
        for name in value_code.keys():
            text += '\n' + name
        return text

    @staticmethod                        # get list of commands
    def get_help():
        text = 'Список доступных команд:\n'
        text += '<количество> <что превести> <во что перевести>\n'
        text += 'например: 10 евро рубль\n'
        text += '/help - подсказка\n'
        text += '/list - список валют'
        return text



