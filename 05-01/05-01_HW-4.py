# Lesson_01: HW_4

string_list = ['string with text 1', 'string with 2', 'string with text 3', 'string text 4']

def count_words(list) -> int:
    return sum(len(text.split()) for text in list)

print(count_words(string_list))