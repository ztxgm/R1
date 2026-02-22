# № 1 "Делаем срезы"
print("№ 1")
s = input().strip()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

# № 2 "Две половинки"
print("\n№ 2")
s = input().strip()
n = (len(s) + 1) // 2
result = s[n:] + s[:n]
print(result)

# № 3 "Обращение фрагмента"
print("\n№ 3")
s = input().strip()
first = s.find('h')
last = s.rfind('h')
result = s[:first + 1] + s[last - 1:first:-1] + s[last:]
print(result)

# № 4 "Первое и последнее вхождения"
print("\n№ 4")
s = input().strip()
first = s.find('f')
last = s.rfind('f')
if first != -1:
    if first == last:
        print(first)
    else:
        print(first, last)

# № 5
print("\n№ 5")
x = input()
while True:
    y = x
    x = input()
    if x[0].lower() != y[-1].lower():
        print(y)
        break

# № 6
print("\n№ 6")
s = input().strip()
result = ''
for i, ch in enumerate(s):
    result += ch * (i + 1)
print(result)

# № 7
print("\n№ 7")
s = input()
a = s[1::].replace('V', '!V!').split('!')
c_pos = 0
k = 1 if len(s) == 1 or s[1] == 'V' else 0
for i in a:
    if i == '':
        continue
    elif i[0] == '<':
        c_pos -= len(i)
        print(c_pos * ' ' + s[0] + i.replace('<', s[0]))
        k = 0
    elif i[0] == '>':
        print(c_pos * ' ' + s[0] + i.replace('>', s[0]))
        c_pos += len(i)
        k = 0
    elif i[0] == 'V':
        if k:
            print(c_pos * ' ' + s[0])
        k = 1
if k:
    print(c_pos * ' ' + s[0])

# № 8
print("\n№ 8")
s = input().strip()
n = len(s)
if n % 2 == 1:
    center = n // 2
    rows = n // 2 + 1
    for i in range(rows):
        left = center - i
        right = center + i
        line = [' '] * n
        line[left] = s[left]
        if left != right:
            line[right] = s[right]
        print(''.join(line))
else:
    left_center = n // 2 - 1
    right_center = n // 2
    rows = n // 2
    for i in range(rows):
        left = left_center - i
        right = right_center + i
        line = [' '] * n
        line[left] = s[left]
        line[right] = s[right]
        print(''.join(line))

# № 9 "Больше предыдущего"
print("\n№ 9")
nums = list(map(int, input().split()))
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        print(nums[i], end=' ')
print()

# № 10 "Соседи одного знака"
print("\n№ 10")
nums = list(map(int, input().split()))
for i in range(1, len(nums)):
    if nums[i] * nums[i - 1] > 0:
        print(nums[i - 1], nums[i])
        break

# № 11 "Переставить соседние"
print("\n№ 11")
nums = list(map(int, input().split()))
for i in range(0, len(nums) - 1, 2):
    nums[i], nums[i + 1] = nums[i + 1], nums[i]
print(' '.join(map(str, nums)))

# № 12 "Уникальные элементы"
print("\n№ 12")
nums = list(map(int, input().split()))
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
unique = [x for x in nums if counts[x] == 1]
print(' '.join(map(str, unique)))

# № 13
print("\n№ 13")
indices = list(map(int, input().split()))
sentence = input().strip()
words = sentence.split()
result_words = [words[i - 1] for i in indices]
result = ' '.join(result_words)
if result:
    result = result[0].upper() + result[1:]
print(result)

# № 14 "Ферзи"
print("\n№ 14")
coords = []
for _ in range(8):
    x, y = map(int, input().split())
    coords.append((x, y))


def attack(a, b):
    return a[0] == b[0] or a[1] == b[1] or abs(a[0] - b[0]) == abs(a[1] - b[1])


danger = False
for i in range(8):
    for j in range(i + 1, 8):
        if attack(coords[i], coords[j]):
            danger = True
            break
    if danger:
        break
print("YES" if danger else "NO")

# № 15
print("\n№ 15")
n = int(input())
print("Форматы ввода:")
print("1 <фамилия>  — Кто последний?")
print("2 <фамилия>  — Я только спросить!")
print("3            — Следующий!")
print("(можно также вводить фразы как в условии)")

queue = []
for _ in range(n):
    line = input().strip()
    if not line:
        continue

    if line[0].isdigit():
        parts = line.split(maxsplit=1)
        code = parts[0]
        if code == '1':
            name = parts[1].rstrip('.')
            queue.append(name)
        elif code == '2':
            name = parts[1].rstrip('.')
            queue.insert(0, name)
        elif code == '3':
            if queue:
                print(f"Заходит {queue.pop(0)}!")
            else:
                print("В очереди никого нет.")
    else:
        if "Кто последний?" in line or "кто последний?" in line:
            name = line.split("Я - ")[-1].rstrip('.')
            queue.append(name)
        elif "Я только спросить!" in line or "я только спросить!" in line:
            name = line.split("Я - ")[-1].rstrip('.')
            queue.insert(0, name)
        elif "Следующий!" in line:
            if queue:
                print(f"Заходит {queue.pop(0)}!")
            else:
                print("В очереди никого нет.")