def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result

        

params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)


# функция key_params должна обрабатывать kwargs и возвращать словарь, 
# где ключами являются значения kwargs, а значениями - соответствующие ключи. 
# Если значение не является одним из базовых типов(int, str, float, bool, tuple), 
# оно преобразуется в строку перед добавлением в словарь
