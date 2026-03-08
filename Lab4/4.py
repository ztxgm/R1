import math

# Задача №1: 1–6
def task1_1(my_list):
    """Элементы списка, меньшие 5."""
    return [x for x in my_list if x < 5]

def task1_2(my_list):
    """Элементы списка, делённые на 2."""
    return [x / 2 for x in my_list]

def task1_3(my_list):
    """Элементы > 17, умноженные на 2."""
    return [x * 2 for x in my_list if x > 17]

def task1_4(n):
    """Квадраты чисел от 0 до n включительно."""
    return [i ** 2 for i in range(n + 1)]

def task1_5(s):
    """Из строки чисел получить их квадраты в одной строке."""
    numbers = [int(x) for x in s.split()]
    squares = [str(x ** 2) for x in numbers]
    return ' '.join(squares)

def task1_6(s):
    """Квадраты нечётных чисел, не оканчивающихся на 9."""
    numbers = [int(x) for x in s.split()]
    result = [str(x ** 2) for x in numbers if x % 2 != 0 and (x ** 2) % 10 != 9]
    return ' '.join(result)

# Задача №2: Горизонтальные столбчатые диаграммы
def task2(data):
    for value in data:
        print('*' * value)

# Задача №3: Проверка треугольника
def task3(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Это треугольник")
    else:
        print("Это не треугольник")

# Задача №4: Расстояние между точками
def task4(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

# Задача №5: Число прописью (1–99)
def task5(n):
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
             "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
             "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

    if 1 <= n <= 19:
        return units[n]
    elif 20 <= n <= 99:
        d = n // 10
        u = n % 10
        return tens[d] + (" " + units[u] if u else "")
    else:
        raise ValueError("Число должно быть от 1 до 99")

# Задача №6: Правильная скобочная последовательность
def task6(s):
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
            if balance < 0:
                print("NO")
                return
    print("YES" if balance == 0 else "NO")

# Задача №7: Палиндром (с учётом регистра и пробелов)
def task7(s):
    cleaned = ''.join(s.split()).lower()
    if cleaned == cleaned[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"

# Задача №8: Крестики-нолики
def task8(field):
    lines = []
    lines.extend(field)
    for j in range(3):
        lines.append([field[i][j] for i in range(3)])
    # диагонали
    lines.append([field[i][i] for i in range(3)])
    lines.append([field[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != '-':
            print(f"{line[0]} win")
            return
    print("draw")

# Задача №9: Печать без дубликатов
_last_message = None

def task9(message):
    global _last_message
    if message != _last_message:
        print(message)
        _last_message = message

# Задача №10: Друзья
_friends_db = {}

def add_friends(name_of_person, list_of_friends):
    if name_of_person not in _friends_db:
        _friends_db[name_of_person] = set()
    _friends_db[name_of_person].update(list_of_friends)

def are_friends(name_of_person1, name_of_person2):
    return name_of_person2 in _friends_db.get(name_of_person1, set())

def print_friends(name_of_person):
    friends = sorted(_friends_db.get(name_of_person, []))
    print(' '.join(friends))

# Задача №11: Римские числа
one = 5
two = 4
three = None

def task11():
    global three
    three = one + two

    def to_roman(num):
        val = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        roman = ''
        for v, sym in val:
            while num >= v:
                roman += sym
                num -= v
        return roman

    print(f"{to_roman(one)} + {to_roman(two)} = {to_roman(three)}")

# Задача №12: Разница между += и обычным сложением
def task12():
    a = 5
    b = 5
    a = a + 2
    b += 2
    print(f"int: a = a+2 -> {a}, b += 2 -> {b} (одинаково)")

    lst1 = [1, 2]
    lst2 = [1, 2]
    print(f"До: lst1={lst1}, lst2={lst2}")
    lst1 = lst1 + [3]
    lst2 += [3]
    print(f"После: lst1 = lst1+[3] -> {lst1}, lst2 += [3] -> {lst2}")
    print("lst1 изменил ссылку, lst2 модифицировал исходный список.")

# Задача №13: sort() vs sorted()
def task13():
    arr = [3, 1, 2]
    print(f"Исходный список: {arr}")

    new_sorted = sorted(arr)
    print(f"sorted(arr) = {new_sorted}, исходный arr остался: {arr}")

    arr.sort()
    print(f"arr.sort() изменил arr: {arr}")

# Задача №14: Исправление ошибки с разделением чётных/нечётных
def task14():
    numbers = [2, 5, 7, 7, 8, 4, 1, 6]
    odd = []
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    print(f"Чётные: {even}")
    print(f"Нечётные: {odd}")

# Задача №15: Создание фрактального списка
fractal = None

def task15():
    global fractal
    fractal = [0, None, None, 2]
    fractal[1] = fractal
    fractal[2] = fractal

# Задача №16: Исправление продолжения последовательности Фибоначчи
def continue_fibonacci_sequence(sequence, n):
    for _ in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)

def task16():
    seq = [1, 1]
    continue_fibonacci_sequence(seq, 1)
    print(*seq)

# Задача №17: Исправление зеркального отражения списка
def mirror(arr):
    mirrored_part = arr[::-1]
    arr.extend(mirrored_part)

def task17():
    arr = [1, 2]
    mirror(arr)
    print(*arr)

# Задача №18: Из строки в список
def from_string_to_list(string, container):
    if string.strip():
        numbers = [int(x) for x in string.split()]
        container.extend(numbers)

def task18():
    """Тест для from_string_to_list."""
    a = [1, 2, 3]
    from_string_to_list("1 3 99 52", a)
    print(*a)

# Задача №19: Транспонирование матрицы
def transpose(matrix):
    """Транспонирует матрицу N x M (изменяет исходную)."""
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    matrix[:] = [[matrix[i][j] for i in range(n)] for j in range(m)]

def task19():
    """Тест для transpose."""
    matrix = [[1, 2], [3, 4]]
    transpose(matrix)
    for line in matrix:
        print(*line)

# Задача №20: Обмен содержимым двух списков
def swap(first, second):
    first[:], second[:] = second[:], first[:]

def task20():
    """Тест для swap."""
    first = [1, 2, 3]
    second = [4, 5, 6]
    first_content = first[:]
    second_content = second[:]
    swap(first, second)
    print(first, second_content, first == second_content)
    print(second, first_content, second == first_content)

# Задача №21: Дефрактализация
def defractalize(fractal):
    for i in range(len(fractal) - 1, -1, -1):
        if fractal[i] is fractal:
            del fractal[i]

def task21():
    """Тест для defractalize."""
    fractal = [2, 5]
    fractal.append(fractal)
    fractal.append(3)
    fractal.append(fractal)
    fractal.append(9)
    defractalize(fractal)
    print(fractal)  # [2, 5, 3, 9]

# Задача №22: Печать фрактала с двумя уровнями вложенности
def fractal_print(obj):
    def helper(item, seen):
        if isinstance(item, list):
            if id(item) in seen:
                return ['...']
            seen.add(id(item))
            res = [helper(x, seen) for x in item]
            seen.remove(id(item))
            return res
        else:
            return item
    def _print(item, seen, first_level=True):
        if isinstance(item, list):
            if id(item) in seen:
                print('[. . .]', end='')
                return
            seen.add(id(item))
            print('[', end='')
            for i, elem in enumerate(item):
                if i > 0:
                    print(', ', end='')
                _print(elem, seen, False)
            print(']', end='')
            seen.remove(id(item))
        else:
            print(repr(item) if isinstance(item, str) else item, end='')

    _print(obj, set())
    print()

def task22():
    """Тест для fractal_print."""
    fractal = [3]
    fractal.append(fractal)
    fractal.append(2)
    fractal_print(fractal)  # должно быть [3, [3, [. . .], 2], 2]

# Задача №23: Создание матрицы с аргументами по умолчанию
def matrix(n=1, m=None, a=0):
    if m is None:
        m = n
    return [[a for _ in range(m)] for _ in range(n)]

def task23():
    """Тест для matrix."""
    rows = matrix(2)
    for row in rows:
        print(*row)  # 0 0

# Задача №24: Частичные суммы
def partial_sums(*args):
    result = [0]
    total = 0
    for x in args:
        total += x
        result.append(total)
    return result

def task24():
    """Тест для partial_sums."""
    print(partial_sums(1, 0.5, 0.25, 0.125))  # [0, 1, 1.5, 1.75, 1.875]

# Задача №25: Решение уравнений (до второй степени)
def solve(*coefficients):
    if len(coefficients) == 0 or len(coefficients) > 3:
        return None
    if len(coefficients) == 1:
        # c = 0
        c = coefficients[0]
        if c == 0:
            return ["all"]
        else:
            return []
    if len(coefficients) == 2:
        b, c = coefficients
        if b == 0:
            if c == 0:
                return ["all"]
            else:
                return []
        else:
            return [-c / b]
    if len(coefficients) == 3:
        a, b, c = coefficients
        if a == 0:
            return solve(b, c)
        d = b**2 - 4*a*c
        if d < 0:
            return []
        elif d == 0:
            return [-b / (2*a)]
        else:
            sqrt_d = math.sqrt(d)
            return [(-b - sqrt_d) / (2*a), (-b + sqrt_d) / (2*a)]

def task25():
    """Тест для solve."""
    print(sorted(solve(1, 2, 1)))
    print(sorted(solve(1, -3, 2)))

def main():
    print("# Задача №1")
    my_list = [1, 3, 5, 7, 9, 15, 20, 25]
    print("1.1 <5:", task1_1(my_list))
    print("1.2 /2:", task1_2(my_list))
    print("1.3 >17*2:", task1_3(my_list))
    print("1.4 квадраты до 5:", task1_4(5))
    print("1.5 квадраты из строки '1 2 3 4':", task1_5("1 2 3 4"))
    print("1.6 нечётные квадраты не на 9 из '1 2 3 4 5 6 7':", task1_6("1 2 3 4 5 6 7"))

    print("\n# Задача №2")
    task2([3, 5, 1])

    print("\n# Задача №3")
    task3(7, 6, 10)
    task3(1, 1, 2)

    print("\n# Задача №4")
    print("Расстояние (0,0)-(3,4):", task4(0, 0, 3, 4))

    print("\n# Задача №5")
    print(task5(4))
    print(task5(13))

    print("\n# Задача №6")
    task6("()")
    task6("((()(")

    print("\n# Задача №7")
    print(task7("A роза упала на лапу Азора"))
    print(task7("Палиндром"))

    print("\n# Задача №8")
    field = [['-', '0', '-'],
             ['x', 'x', 'x'],
             ['0', '0', '-']]
    task8(field)      # x win

    print("\n# Задача №9")
    task9("Привет")
    task9("Не могу до тебя дозвониться")
    task9("Не могу до тебя дозвониться")
    task9("Когда доедешь до дома")
    task9("Ага, жду")
    task9("Ага, жду")

    print("\n# Задача №10")
    add_friends("Алла", ["Марина", "Иван"])
    print(are_friends("Алла", "Мария"))
    add_friends("Алла", ["Мария"])
    print(are_friends("Алла", "Мария"))
    print_friends("Алла")

    print("\n# Задача №11")
    global one, two
    one, two = 5, 4
    task11()

    print("\n# Задача №12")
    task12()

    print("\n# Задача №13")
    task13()

    print("\n# Задача №14")
    task14()

    print("\n# Задача №15")
    task15()
    print("fractal создан. Его repr:", fractal)

    print("\n# Задача №16")
    task16()

    print("\n# Задача №17")
    task17()

    print("\n# Задача №18")
    task18()

    print("\n# Задача №19")
    task19()

    print("\n# Задача №20")
    task20()

    print("\n# Задача №21")
    task21()

    print("\n# Задача №22")
    task22()

    print("\n# Задача №23")
    task23()

    print("\n# Задача №24")
    task24()

    print("\n# Задача №25")
    task25()


if __name__ == "__main__":
    main()