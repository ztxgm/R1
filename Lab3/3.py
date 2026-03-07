def task1(numbers):
    """Количество различных чисел"""
    return len(set(numbers))

def task2(list1, list2):
    """Количество совпадающих чисел"""
    return len(set(list1) & set(list2))

def task3(list1, list2):
    """Пересечение множеств (числа в порядке возрастания)"""
    return sorted(set(list1) & set(list2))

def task4(sequence):
    """Встречалось ли число раньше: список YES/NO"""
    seen = set()
    result = []
    for num in sequence.split():
        if num in seen:
            result.append("YES")
        else:
            result.append("NO")
            seen.add(num)
    return result

def task5(text_lines):
    """Количество различных слов в тексте (первая строка - число строк)"""
    n = int(text_lines[0].strip())
    text = " ".join(line.strip() for line in text_lines[1:1+n])
    return len(set(text.split()))

def task6(surname_lines):
    """Количество однофамильцев"""
    from collections import Counter
    n = int(surname_lines[0].strip())
    surnames = [line.strip() for line in surname_lines[1:1+n]]
    cnt = Counter(surnames)
    return sum(v for v in cnt.values() if v > 1)

def task7(text):
    """Номер появления слова (сколько раз встречалось ранее)"""
    words = text.split()
    counts = {}
    result = []
    for w in words:
        result.append(counts.get(w, 0))
        counts[w] = counts.get(w, 0) + 1
    return result

def task8(data_lines):
    """Синоним для последнего слова"""
    idx = 0
    n = int(data_lines[idx].strip())
    idx += 1
    synonyms = {}
    for _ in range(n):
        a, b = data_lines[idx].strip().split()
        synonyms[a] = b
        synonyms[b] = a
        idx += 1
    word = data_lines[idx].strip()
    return synonyms[word]

def task9(votes_lines):
    """Итоги выборов (список строк кандидат сумма)"""
    n = int(votes_lines[0].strip())
    total = {}
    for i in range(1, n+1):
        name, votes = votes_lines[i].strip().split()
        total[name] = total.get(name, 0) + int(votes)
    return [f"{name} {total[name]}" for name in sorted(total)]

def task10(access_lines):
    """Проверка прав доступа (список строк OK/Access denied)"""
    idx = 0
    n = int(access_lines[idx].strip())
    idx += 1
    file_perms = {}
    for _ in range(n):
        parts = access_lines[idx].strip().split()
        file_perms[parts[0]] = set(parts[1:])
        idx += 1
    m = int(access_lines[idx].strip())
    idx += 1
    results = []
    for _ in range(m):
        op, fname = access_lines[idx].strip().split()
        results.append("OK" if op in file_perms.get(fname, set()) else "Access denied")
        idx += 1
    return results

def main():
    print("#1 Количество различных чисел")
    print(task1([1, 2, 3, 2, 1, 5, 5, 5]))

    print("\n#2 Количество совпадающих чисел")
    print(task2([1, 2, 3, 4], [3, 4, 5, 6]))

    print("\n#3 Пересечение множеств")
    print(task3([1, 3, 5, 7], [3, 4, 5, 8, 9]))

    print("\n#4 Встречалось ли число раньше")
    for line in task4("1 2 3 2 3 4"):
        print(line)

    print("\n#5 Количество слов в тексте")
    text5 = ["34", "дада ненет", "привет пока", "хах ну ладно", "и опять"]
    print(task5(text5))

    print("\n#6 Однофамильцы")
    surnames6 = ["5", "Иванов", "Неиванов", "Иванов", "Неиванов", "УУУУУУ"]
    print(task6(surnames6))

    print("\n#7 Номер появления слова")
    print(task7("раз два раз три два раз"))

    print("\n#8 Словарь синонимов")
    data8 = ["3", "Hello Hi", "Bye Goodbye", "List Array", "Goodbye"]
    print(task8(data8))

    print("\n#9 Выборы в США")
    votes9 = ["5", "McCain 16", "McCain 10", "Obama 17", "McCain 5", "Obama 9"]
    for res in task9(votes9):
        print(res)

    print("\n#10 Права доступа")
    access10 = [
        "4",
        "helloworld.exe R X",
        "pinglog W R",
        "nya R",
        "goodluck X W R",
        "5",
        "read nya",
        "write helloworld.exe",
        "execute nya",
        "read pinglog",
        "write pinglog"
    ]
    for ans in task10(access10):
        print(ans)

if __name__ == "__main__":
    main()