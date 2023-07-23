# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list_elements = ['яблоко', 'яблоко', 'банан', 'киви', 'апельсин', 'гранат', 'гранат']
list_final = []
dubl_list = []
for item in list_elements:
    if list_elements.count(item) > 1:
        dubl_list.append(item)
    else:
        list_final.append(item)

print(f'Список дублирующихся элементов {set(dubl_list)}\n'
      f'Финальный список {list_final}')

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

str_pyhton = 'Python — это язык программирования, который широко используется в ' \
             'интернет-приложениях, разработке программного обеспечения, ' \
             'науке о данных и машинном обучении (ML). Разработчики используют Python, ' \
             'потому что он эффективен, прост в изучении и работает на разных платформах. ' \
             'Программы на языке Python можно скачать бесплатно, они совместимы со всеми типами ' \
             'систем и повышают скорость разработки. и и и и и и б б б б б'

list_str = str_pyhton.split(' ')
list_word = []
srt_dict = {}

for item in list_str:
    if item.isalpha() == True:
        list_word.append(item)

for item in list_word:
    srt_dict[list_word.count(item)] = item

sort_list = sorted(srt_dict, reverse=True)

print('Чаше всего в тексте встречаются слова:')

for item in sort_list:
    if sort_list.index(item) < 10:
        print(f'{item} раз: слово "{srt_dict[item]}"')
    else:
        break
