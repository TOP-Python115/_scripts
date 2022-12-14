s = """У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил."""

# составление списка, содержащего в качестве элементов строчки стиховторения
# перебор элементов списка с поиском нужного слова в каждой строке по-отдельности
# l = s.split('\n')
# while query := input():
    # for line in l:
        # if query in line:
            # print(line)
            # break


# выделяем подстроку со строчкой стиха с помощью поиска символа '\n' рядом с индексом найденного запроса
while query := input():
    if query.lower() in s.lower():
        query_position = s.lower().index(query.lower())
        
        line_stop = s.find('\n', query_position, query_position+35)
        # приближенный вид работы метода find()
        # line_stop = 0
        # for i in range(query_position, query_position+35):
            # if s[i] == '\n' or i == len(s)-1:
                # line_stop = i
                # break
        
        line_start = s.find('\n', query_position-35, query_position)
        # приближенный вид работы метода find()
        # line_start = 0
        # for i in range(query_position, query_position-35, -1):
            # if s[i] == '\n' or i == -1:
                # line_start = i
                # break
        
        print(s[ line_start+1 : line_stop ])
