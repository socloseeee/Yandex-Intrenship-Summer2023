def check_anagram(first_word, second_word):
    if len(first_word) != len(second_word):
        return 0
    else:
        first_count = [0] * 26  # создаем список счетчиков символов для первой строки
        second_count = [0] * 26  # создаем список счетчиков символов для второй строки
        for i in range(len(first_word)):
            first_count[ord(first_word[i]) - ord('a')] += 1  # увеличиваем счетчик для символа в первой строке
            second_count[ord(second_word[i]) - ord('a')] += 1  # увеличиваем счетчик для символа во второй строке
        return 1 if first_count == second_count else 0  # сравниваем списки счетчиков


print(check_anagram(input(), input()))
