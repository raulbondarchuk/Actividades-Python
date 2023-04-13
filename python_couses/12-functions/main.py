def test_func():
    #pass # Это аналог ничего не произойдет 
    print("Hello", end="")
    print("!")
    print(" ")
    
test_func()
test_func()


def test_func(word):
    print(word, end="")
    print("!")
    print(" ")
    
test_func("Hi")

# Функция не возвращает ничего
def summa(a,b):
    res = (a + b)
    print("Result:", res)
summa(5,1.6)
summa("P", "e")

def summa(a, b):
    res = a + b
    return res

res = summa(4,8.5)
print(res)