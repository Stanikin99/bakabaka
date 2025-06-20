
list_of_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

'''
list_of_dict - список вводных данных
filter_by_state - функция, которая принимает список словарей и опционально значение для ключа
state(по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
 содержащий только те словари, у которых ключ
state соответствует указанному значению.
filtered_list-новый список, в который будут возвращаться словари.
'''


def filter_by_state(list_of_dict: list, state: str = 'EXECUTED') -> list:
    filtered_list = []
    for dict_item in list_of_dict:
        if dict_item.get('state') == state:
            filtered_list.append(dict_item)
    return filtered_list


result = filter_by_state(list_of_dict)


print(result)


'''
sort_by_date - функция, которая принимает список словарей и необязательный параметр,
 задающий порядок сортировки (по умолчанию — убывание).
  Функция должна возвращать новый список, отсортированный по дате (date).
'''


def sort_by_date(list_of_dict: list, reverse: bool = False) -> list:
    return sorted(list_of_dict, key=lambda x: x['date'], reverse=reverse)


print(sort_by_date(list_of_dict))
