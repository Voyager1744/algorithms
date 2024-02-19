"""
Форматирование текста
Дан текст из строчных английских букв, пробелов и запятых. Пусть
l
e
n
len равно максимальной длине слова в тексте, умноженной на
3
3. Вам необходимо отформатировать текст следующим образом:

в каждой строке должно быть не более
l
e
n
len символов
запятая «приклеивается» к слову перед ней, то есть должна находиться на одной строке с ним
перед запятой пробел не ставится
после запятой пробел ставится, если она не является последним символом строки
если слово не входит на строку
i
i, строка
i
i заканчивается, а слово будет записано на строке
(
i
+
1
)
(i+1)
последним символом в любой строке должна быть буква или запятая

"""


def format_text(input_str):
    words_and_commas = input_str.replace(',', ' , ').split()
    max_word_length = max(len(word) for word in words_and_commas)
    max_line_length = max_word_length * 3

    output_lines = []
    current_line = ""

    for i in range(len(words_and_commas)):
        token = words_and_commas[i]
        next_token = words_and_commas[i + 1] if i + 1 < len(words_and_commas) else None
        if next_token == ',' and len(current_line) + 1 + len(token) + 1 > max_line_length:
            output_lines.append(current_line)
            current_line = token
        elif token == ',':
            current_line += ','

        elif len(current_line) == 0:
            current_line += token
        elif len(current_line) + len(
                token) + 1 > max_line_length:
            output_lines.append(current_line)
            current_line = token
        else:
            current_line += ' ' + token if token != ',' else token

    if current_line:
        output_lines.append(current_line)

    formatted_text = '\n'.join(output_lines)

    return formatted_text


input_str = input()
formatted_text = format_text(input_str)
print(formatted_text)

# a,b,c,d,e,few,g,h,i,j,k,l,m,n,o,p,yandex