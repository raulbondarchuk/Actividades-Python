numbers = [5, 2, 7]

#numbers[3] = 100
numbers.append(100) # append добавляет в список еще один индекс
numbers.append(True)
print(numbers) # [5, 2, 7, 100, True]

numbers.insert(1, False) # Добавить в определенный элемент в указанную позицию списка 
print(numbers) #[5, False, 2, 7, 100, True] 

b = [123,227,212]
numbers.extend([2,2,8]) # Добавляет указанные элементы в списке добавляются к первоначальному списку
numbers.extend(b) 
print(numbers) # [5, False, 2, 7, 100, True]

numbers.sort() # Отсортировать 
print(numbers) # True -> 1 False = 0 [False, True, 2, 2, 2, 5, 7, 8, 100]
numbers.reverse() # От большего к меньшему 
print(numbers) # [100, 8, 7, 5, 2, 2, 2, True, False]

numbers.pop() # Последний элемент удаляетб если указать индекс, то удаляет элемент по индексу
numbers.remove(True) # Удаляет определенный элемент

# numbers.clear() # очищает весь список

print(numbers.count(5)) #считает сколько элементов = 5 (количество совпадений)

print(len(numbers)) # Количество элементов


