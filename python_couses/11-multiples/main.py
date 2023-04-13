#data = set('hello')

data = {'': 4} # Используем словарь
data = {5,7,4,5,3,3,5} # Используем множество
print(data) # Удаляет дублированные элементы и выводит в хаотичном порядке

# Не можем поменять элементы и не можем обратиться по индексу
# Можем удалять и добавлять элементы

data.add(32)
data.update(['32', True, 4, 6])
data.remove(True)
data.pop()

print(data)
data.clear()

print(data)

nums = [5,7,3,5,5]
new_nums = set(nums)
print(new_nums)

new_data = frozenset([5,7,4, '22', True, 4, 5, 6, 7, 4, 3, 5]) # замороженный кортеж
print(new_data)

#new_data.add() NO SE PUEDE