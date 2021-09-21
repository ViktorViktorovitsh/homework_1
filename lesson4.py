from pprint import pprint

#цикл while

x = 10
while x > 0:
  print(x)
  x -= 1 # x = x -1

# x = 10
# while x > 0:
#   if x % 2 == 0:
#     print(x, 'четное число')
#   else:
#     print(x, 'нечетное число')
#   x -= 1


# вечный цикл
x = [1, 3, 5, 55]
# x = 10
# while x > 0:
#   print(x)

# x = [1, 3, 5, 55]
# print(type(x))
# for i in x:
#   print(i)


# есть два списка, поэтов и произведений ими написанных,
# вывести последовательно имя поэта и произведения им написанные.

poets = ['Пушкин', 'Лермонтов', 'Некрасов']
poems = [['Евгений Онегин', 'Узник', 'Руслан и Людмила'], ['Мцыри', 'Прощай, немытая Россия', 'Бородино'], ['Есть женщины в русских селеньях', 'Крестьянские дети']]


# pprint(poems)

# pprint(list(zip(poets, poems)))
# print(type(list(zip(poets, poems))[0]))

# x , y = 5, 10

# print(x,y)

a, b = 3, 5

# for poet, poem in zip(poets, poems):
#   # print(poet)
#   # print(poem)
#   for title in poem:
#     print(title)
#   print()


poets = ['Пушкин', 'Лермонтов', 'Некрасов']
poems = [['Евгений Онегин', 'Узник', 'Руслан и Людмила'], ['Мцыри', 'Прощай, немытая Россия', 'Бородино'], ['Есть женщины в русских селеньях', 'Крестьянские дети']]

# print(poems[1][0])

# for num, poet in enumerate(poets):
#   # print(num, poet)
#   # print(poems[num])
#   for title in poems[num]:
#     print(title)
#   print()
    
# enumerate() — это встроенная функция в Python, которая позволяет вам иметь автоматический счетчик во время цикла по итерациям. 
# Функция enumerate() принимает следующий вид: enumerate(iterable, start=0)
#  Функция принимает два аргумента: iterable — объект, поддерживающий итерацию. start — число, с которого начинается счетчик (по умолчанию start = 0)
# возвращает индекс и элемент объекта

poems = [['Евгений Онегин', 'Узник', 'Руслан и Людмила'], ['Мцыри', 'Прощай, немытая Россия', 'Бородино'], ['Есть женщины в русских селеньях', 'Крестьянские дети']]

## еще пример вложенного цикла
# print('Золотая коллекция:')
# num = 1
# for i in poems:
#   # print(i)
#   for j in i:
#     # print(j)
#     print(f'{num}. "{j}"')
#     num += 1

# break, continue, pass

nekrasov = 'Однажды в студёную зимнюю пору, я из лесу вышел, был сильный мороз...'

for letter in nekrasov:
  pass

  # print(letter)
  # if letter == ' ':
  #   # break
  #   # continue
  #   pass
  # print(letter,  end = '')


# исправляем вечный цикл
# x = 100
# while True:
#   print(x)
#   x -= 1
#   if x < 0:
#     break





## функция range возвращает итерируемый объект, принимать может три параметра (int): старт, стоп, шаг
# по объекту типа range можно итерироваться как по списку

# print(range(10))
# print(type(range(10)))

# for num in range(1, 10, 2):
#   print(num, end = ' ')



## факториал 
# n = 10000
# fact = 1
# for i in range(1, n + 1):
#   fact = fact * i
#   # print(fact)
# print(fact)

# домашка:
# https://github.com/ViktorViktorovitsh/homework_1/blob/main/HW1.md
# https://replit.com/
# hhomework@list.ru