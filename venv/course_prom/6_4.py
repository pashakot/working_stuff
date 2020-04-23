def find_most_frequent(text):
    # якщо текст порожній - нема чого шукати
    if text == '':
        return []
    # видаляємо розділові знаки, змінюємо регістр та перетворюємо рядок у список слів
    text_list = text.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace('-', ' ').lower().split()
    # створюємо словник, де для кожного унікального слова зберігатимемо кількість його входжень.
    counts = dict()
    word = ''
    # для кожного слова в списку
    for word in text_list:
        # якщо воно вже присутнє у словнику
        if word in counts:
            # збільшуємо його лічильник на 1
            counts[word] = counts[word] + 1
        else:
            # інакше додаємо у словник
            counts[word] = 1

    # беремо останнє оброблене слово і вважаємо його найчастіше вживаним
    max_word = [word]
    # перевіряємо слова условнику, шукаючи слово із найбільшим лічильником
    for word in counts:
        # якщо знаходиме частіше вживане слово, зберігаємо його як єдиний елемент списка "лідерів"
        if counts[word] > counts[max_word[0]]:
            max_word = [word]
        # якщо знаходимо слово з аналогічною вживаністю, додаємо у список
        elif counts[word] == counts[max_word[0]] and word != max_word[0]:
            max_word.append(word)
    # повертаємо список слів-"лідерів"
    return max_word


print(find_most_frequent(''))
