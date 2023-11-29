def anagram_of(string):
    # базовый случай
    if len(string) == 1:
        return [string[0]]
    collection = []  # создаем коллекцию для хранения вариантов
    substring_anagram = anagram_of(string[1:])  # рекурсивно вызываем функцию
    for substring in substring_anagram:  # перебираем варианты
        for i in range(len(substring) + 1):
            copy = list(substring)
            copy.insert(i, string[0])  # вставляем букву в позицию i
            new_string = "".join(copy)
            collection.append(new_string)  # добавляем вариант в коллекцию
    return collection


print(anagram_of(input()))
