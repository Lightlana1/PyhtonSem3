# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.


things_to_hike = {'Андрей': ['фонарик', 'спальник', 'сапоги', 'спички', 'веревка'],
                  'Иван': ['палатка', 'лодка', 'фонарик', 'сапоги', 'спички'],
                  'Алексей': ['спальник', 'насос', 'карта', 'сапоги', 'лопата', 'горелка']
                  }

count_friedns = len(things_to_hike)

# ✔ Какие вещи взяли все три друга
all_things = list(things_to_hike.values())
common_things = set(all_things[0])

for things in all_things:
    common_things = common_things.intersection(set(things))

print(f'У каждого из {count_friedns}-х друзей есть: \n{common_things}')

# ✔ Какие вещи уникальны, есть только у одного друга
unique_things = {}
things_list = []

for item in all_things:
    common_things = set(item)
    for item in common_things:
        things_list.append(item)

new_new_list = []

for name, things in things_to_hike.items():
    new_list = list(things)

    for item in new_list:
        if things_list.count(item) == 1:
            new_new_list.append(item)

    unique_things[name] = new_new_list
    new_new_list = []

print(f'Уникальные вещи, которые есть только у одного друга: \n{unique_things}')

# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
things_for_one = {}

for name, things in things_to_hike.items():
    new_list = list(things)

    for item in things_list:
        if item not in new_list and things_list.count(item) == count_friedns - 1:
            new_new_list.append(item)
    if len(new_new_list) > 0:
        things_for_one[name] = set(new_new_list)
    new_new_list = []

print(f'Эти вещи есть у всех, кроме этого друга: \n{things_for_one}')
