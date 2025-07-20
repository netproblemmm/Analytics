'''
3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
 Не учитывать знаки препинания и регистр символов.
 За основу возьмите любую статью из википедии или из документации к языку.
'''
excluded_chars = [".", ",", "_", "—", "!", "?", "'"]

with open(r"d:\Projects\Analytics\22-03\simple_text.txt", encoding="utf-8") as text_file:
    text = text_file.read().lower()

for char in excluded_chars:
    text = text.replace(char, "")
text = text.split()

dict_frequent_words = {}

for i in text:
    if i.isdigit() == False:
       dict_frequent_words[i] = dict_frequent_words.get(i, 0) + 1 

sorted_dict = sorted(dict_frequent_words.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict[:10])
