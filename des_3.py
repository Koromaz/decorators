import os
from dec_2 import logger


def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c

d = discriminant(2, 10,4)
print(d)

def test_3():
    paths = ('log_4.log', 'log_5.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def discriminant(a, b, c):
            """
            функция для нахождения дискриминанта
            """
            return b ** 2 - 4 * a * c





        result = discriminant(2, 10, 4)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 68, '10 ** 2 - 4 * 2 * 4'



    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'discriminant' in log_file_content, 'должно записаться имя функции'

        for item in (2, 10, 4):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_3()