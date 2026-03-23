import sys
import math
import functools

# №1 map, filter
def task1_1(lst):
    return list(filter(lambda x: x < 5, lst))

def task1_2(lst):
    return list(map(lambda x: x / 2, lst))

def task1_3(lst):
    return list(map(lambda x: x / 2, filter(lambda x: x > 17, lst)))

def task1_4():
    return sum(map(lambda x: x * x,
                   filter(lambda x: 10 <= x <= 99 and x % 9 == 0, range(10, 100))))

# №2–5 генераторы
def factorials(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f

def square_fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a * a
        a, b = b, a + b

def russian_letters_generator():
    for code in range(ord('а'), ord('я') + 1):
        yield chr(code)

def russian_letters_expression():
    return (chr(code) for code in range(ord('а'), ord('я') + 1))

# №6–9 функция как объект
def arithmetic_operation(operation):
    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operation]

def same_by(characteristic, objects):
    if not objects:
        return True
    first = characteristic(objects[0])
    return all(characteristic(obj) == first for obj in objects)

def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
        row = [str(operation(i, j)) for j in range(1, num_columns + 1)]
        print(' '.join(row))

def ask_password(login, password, success, failure):
    login = login.lower()
    password = password.lower()
    vowels = set('aeiouy')

    def consonants(s):
        return ''.join(ch for ch in s if ch not in vowels)

    login_cons = consonants(login)
    pass_cons = consonants(password)
    vowel_count = sum(1 for ch in password if ch in vowels)

    if vowel_count == 3 and login_cons == pass_cons:
        success(login)
    elif vowel_count != 3 and login_cons != pass_cons:
        failure(login, "Everything is wrong")
    elif vowel_count != 3:
        failure(login, "Wrong number of vowels")
    else:
        failure(login, "Wrong consonants")

def main_ask_password(login, password):
    def success(login):
        print(f"Привет, {login}!")
    def failure(login, err):
        print(f"Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {err.upper()}.")
    ask_password(login, password, success, failure)

# №10–16 стандартные функции для итераторов
def task10(s):
    words = s.split()
    return ' '.join(sorted(words, key=str.lower))

def task11(nums):
    return sorted(nums, key=abs, reverse=True)

def task12(points):
    return sorted(points, key=lambda p: (p[0]*p[0] + p[1]*p[1], p[0], p[1]))

def task13(table):
    return any(0 in row for row in table)

def task14():
    text = sys.stdin.read()
    raw_words = text.split()

    def clean(word):
        return ''.join(ch for ch in word if ch.isalpha())

    words = [clean(w) for w in raw_words if clean(w)]

    first = {}
    for idx, w in enumerate(words):
        if w not in first:
            first[w] = idx

    capitals = [w for w in first if w and w[0].isupper()]
    capitals.sort()
    for w in capitals:
        print(first[w], w)

def task15():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return None
    return functools.reduce(lambda a, b: a if a < b else b, lines)

def task16():
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return None
    return functools.reduce(math.gcd, nums)

# №17–19 декораторы
def check_password(func):
    def wrapper(*args, **kwargs):
        pwd = input("Введите пароль: ")
        if pwd == "secret":
            return func(*args, **kwargs)
        print("В доступе отказано")
        return None
    return wrapper

def check_password_factory(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            pwd = input("Введите пароль: ")
            if pwd == password:
                return func(*args, **kwargs)
            print("В доступе отказано")
            return None
        return wrapper
    return decorator

def cached(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# Демонстрация работы
if __name__ == "__main__":
    print("=== №1 ===")
    lst = [1, 3, 5, 7, 9, 15, 20, 25]
    print(task1_1(lst))
    print(task1_2(lst))
    print(task1_3(lst))
    print(task1_4())

    print("\n=== №2 ===")
    print(list(factorials(7)))

    print("\n=== №3 ===")
    print(list(square_fibonacci(7)))

    print("\n=== №4 ===")
    gen = russian_letters_generator()
    print(''.join(list(gen)[:5]))

    print("\n=== №5 ===")
    expr = russian_letters_expression()
    print(''.join(list(expr)[:5]))

    print("\n=== №6 ===")
    op = arithmetic_operation('+')
    print(op(1, 4))

    print("\n=== №7 ===")
    values = [0, 2, 10, 6]
    print(same_by(lambda x: x % 2, values))
    values = [1, 2, 3, 4]
    print(same_by(lambda x: x % 2, values))

    print("\n=== №8 ===")
    print_operation_table(lambda x, y: x * y, 5)

    print("\n=== №9 ===")
    main_ask_password("anastasia", "nysatos")
    main_ask_password("eugene", "aangi")

    print("\n=== №10 ===")
    print(task10("cats dog CAT DOGGY monkey"))

    print("\n=== №11 ===")
    print(task11([3, 6, -8, 2, -78, 1, 23, -45, 9]))

    print("\n=== №12 ===")
    points = [(1, 2), (0, 0), (2, 2), (1, 1), (2, 1)]
    print(task12(points))

    print("\n=== №13 ===")
    table = [[4, 33, 79], [96, 27, 8], [95, 28, 91]]
    print(task13(table))
    table2 = [[4, 0, 79], [96, 27, 8]]
    print(task13(table2))

    print("\n=== №14 ===")
    task14()
    
    print("\n=== №15 ===")
    print(task15())

    print("\n=== №16 ===")
    print(task16())

    print("\n=== №17 ===")
    @check_password
    def secret_func():
        return "Секретное сообщение"
    secret_func()

    print("\n=== №18 ===")
    @check_password_factory("mysecret")
    def another_secret():
        return "Другой секрет"
    another_secret()

    print("\n=== №19 ===")
    @cached
    def fib(n):
        if n <= 2:
            return 1
        return fib(n-1) + fib(n-2)
    print(fib(10))
    print(fib(10))