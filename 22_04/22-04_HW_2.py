'''
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
 где ключ — значение переданного аргумента, а значение — имя аргумента.
   Если ключ не хешируем, используйте его строковое представление.
'''
def make_dict_keys(**kwargs):
  d = {}
  s = set()
  for key, value in kwargs.items():
    try:
      s.add(value)
    except:
      value = str(value)
    d[value] = key
  return d


print(make_dict_keys(a=5, b=6, c=[8, 9]))
