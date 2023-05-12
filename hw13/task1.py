# Функция get_credentials_users из предыдущей задачи возвращает нам список строк
# username:password:
#
# ['andry:uyro18890D', 'steve:oppjM13LL9e']
# Реализуйте функцию encode_data_to_base64(data), которая принимает в параметре data
# указанный список, выполняет кодирование каждой пары username:password в формат Base64
# и возвращает список с закодированными парами username:password в виде:
#
# ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']

import base64


def encode_data_to_base64(data):
    result = []
    for item in data:
        encoded = base64.b64encode(item.encode('utf-8')).decode('utf-8')
        result.append(encoded)
    return result


if __name__ == '__main__':
    data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
    result = encode_data_to_base64(data)
    assert ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU='] == result
