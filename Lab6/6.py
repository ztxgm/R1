import sys
import math
from collections import deque
from typing import List, Dict, Optional, Tuple, Any, Union

# №1 BigBell
class BigBell:
    def __init__(self):
        self.ring = True  # True for ding, False for dong

    def sound(self):
        if self.ring:
            print("ding")
        else:
            print("dong")
        self.ring = not self.ring


# №2 Balance
class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, weight: int):
        self.right += weight

    def add_left(self, weight: int):
        self.left += weight

    def result(self) -> str:
        if self.left == self.right:
            return "="
        elif self.left > self.right:
            return "L"
        else:
            return "R"


# №3 Selector
class Selector:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def get_odds(self) -> List[int]:
        return [x for x in self.numbers if x % 2 != 0]

    def get_evens(self) -> List[int]:
        return [x for x in self.numbers if x % 2 == 0]


# №4 Point
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)


# №5 ReversedList
class ReversedList:
    def __init__(self, lst: List):
        self.lst = lst

    def __len__(self) -> int:
        return len(self.lst)

    def __getitem__(self, index: int):
        if index < 0 or index >= len(self.lst):
            raise IndexError("Index out of range")
        return self.lst[-1 - index]


# №6 SparseArray
class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key: int, value: int):
        if value != 0:
            self.data[key] = value
        else:
            self.data.pop(key, None)

    def __getitem__(self, key: int) -> int:
        return self.data.get(key, 0)


# №7 Queue
class Queue:
    def __init__(self, *args):
        self.items = list(args)

    def append(self, *values):
        self.items.extend(values)

    def copy(self) -> 'Queue':
        new_q = Queue()
        new_q.items = self.items.copy()
        return new_q

    def pop(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def extend(self, queue: 'Queue'):
        self.items.extend(queue.items)

    def next(self) -> 'Queue':
        if len(self.items) <= 1:
            return Queue()
        return Queue(*self.items[1:])

    def __add__(self, other: 'Queue') -> 'Queue':
        new_q = self.copy()
        new_q.extend(other)
        return new_q

    def __iadd__(self, other: 'Queue') -> 'Queue':
        self.extend(other)
        return self

    def __eq__(self, other: 'Queue') -> bool:
        if not isinstance(other, Queue):
            return False
        return self.items == other.items

    def __rshift__(self, n: int) -> 'Queue':
        if n >= len(self.items):
            return Queue()
        return Queue(*self.items[n:])

    def __str__(self) -> str:
        if not self.items:
            return "[]"
        return "[" + " -> ".join(str(x) for x in self.items) + "]"

    def __next__(self):
        return self.next()


# №9 Triangle и EquilateralTriangle
class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> float:
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side: float):
        super().__init__(side, side, side)


# №10 Summarator (базовый)
class Summarator:
    def transform(self, n: int) -> int:
        return n

    def sum(self, N: int) -> int:
        return sum(self.transform(i) for i in range(1, N + 1))


# №11 PowerSummator, SquareSummarator, CubeSummarator (переопределены)
class PowerSummator(Summarator):
    def __init__(self, b: float):
        self.b = b

    def transform(self, n: int) -> float:
        return n ** self.b


class SquareSummarator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummarator(PowerSummator):
    def __init__(self):
        super().__init__(3)


# №12 Классы A, B, C, D
class A:
    def __str__(self):
        return 'A__str__method'

    def hello(self):
        print('Hello')


class B:
    def __str__(self):
        return 'B__str__method'

    def good_evening(self):
        print('Good evening')


class C(A, B):
    pass


class D(B, A):   # порядок B, A чтобы __str__ брался от B
    pass


# №13 Weapon, BaseCharacter, BaseEnemy, MainHero
class Weapon:
    def __init__(self, name: str, damage: int, range_: float):
        self.name = name
        self.damage = damage
        self.range = range_

    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
            return
        ax, ay = actor.get_coords()
        tx, ty = target.get_coords()
        dist = math.hypot(ax - tx, ay - ty)
        if dist > self.range:
            print(f"Враг слишком далеко для оружия «{self.name}»")
        else:
            print(f"Враг нанесен урон оружием «{self.name}» в размере {self.damage}")
            target.get_damage(self.damage)

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x: float, pos_y: float, hp: float):
        self.x = pos_x
        self.y = pos_y
        self.hp = hp
        self.alive = True

    def move(self, delta_x: float, delta_y: float):
        self.x += delta_x
        self.y += delta_y

    def is_alive(self) -> bool:
        return self.hp > 0

    def get_damage(self, amount: float):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def get_coords(self) -> Tuple[float, float]:
        return (self.x, self.y)


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x: float, pos_y: float, weapon: Weapon, hp: float):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if not isinstance(target, MainHero):
            print("Могу ударить только Главного героя")
            return
        self.weapon.hit(self, target)

    def __str__(self):
        return f"Враг на позиции ({self.x}, {self.y}) с оружием «{self.weapon}»"


class MainHero(BaseCharacter):
    def __init__(self, pos_x: float, pos_y: float, name: str, hp: float):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.current_weapon_index = -1

    def hit(self, target):
        if not self.weapons:
            print("Я безоружен")
            return
        if not isinstance(target, BaseEnemy):
            print("Могу ударить только Врага")
            return
        weapon = self.weapons[self.current_weapon_index]
        weapon.hit(self, target)

    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
            return
        self.weapons.append(weapon)
        if len(self.weapons) == 1:
            self.current_weapon_index = 0
        print(f"Подобрал «{weapon}»")

    def next_weapon(self):
        if not self.weapons:
            print("Я безоружен")
        elif len(self.weapons) == 1:
            print("У меня только одно оружие")
        else:
            self.current_weapon_index = (self.current_weapon_index + 1) % len(self.weapons)
            weapon = self.weapons[self.current_weapon_index]
            print(f"Сменил оружие на «{weapon}»")

    def heal(self, amount: float):
        self.hp = min(200, self.hp + amount)
        print(f"Попечился, теперь здоровья {self.hp}")


# №14 MailClient (почтовые серверы и клиенты)
class MailServer:
    def __init__(self, name: str):
        self.name = name
        self.mailbox = {}

    def register_user(self, user: str):
        if user not in self.mailbox:
            self.mailbox[user] = []

    def send_mail(self, to_user: str, message: str):
        if to_user in self.mailbox:
            self.mailbox[to_user].append(message)
        else:
            print(f"Пользователь {to_user} не зарегистрирован на сервере {self.name}")

    def receive_mail(self, user: str) -> List[str]:
        if user not in self.mailbox:
            return []
        messages = self.mailbox[user].copy()
        self.mailbox[user].clear()
        return messages


class MailClient:
    available_servers = {}

    @classmethod
    def add_server(cls, server: MailServer):
        cls.available_servers[server.name] = server

    def __init__(self, server: MailServer, user: str):
        self.server = server
        self.user = user
        server.register_user(user)

    def receive_mail(self) -> List[str]:
        return self.server.receive_mail(self.user)

    def send_mail(self, server_name: str, user: str, message: str):
        if server_name not in self.available_servers:
            print(f"Невозможно отправить письмо: сервер {server_name} не в списке доступных")
            return
        target_server = self.available_servers[server_name]
        target_server.send_mail(user, message)


# №15 Преобразование списка чисел
class Command:
    def __init__(self, condition, transformation):
        self.condition = condition
        self.transformation = transformation

    def apply(self, numbers: List[int]) -> List[int]:
        result = []
        for x in numbers:
            if self.condition(x):
                result.append(self.transformation(x))
            else:
                result.append(x)
        return result


make_negative = Command(lambda x: x > 0, lambda x: -x)
square = Command(lambda x: True, lambda x: x * x)
strange_command = Command(lambda x: x % 5 == 0, lambda x: x + 1)


def process_commands(numbers: List[int], commands: List[Command]) -> List[int]:
    result = numbers[:]
    for cmd in commands:
        result = cmd.apply(result)
    return result


# №16 Математические функции
class Function:
    def evaluate(self, x: float) -> float:
        raise NotImplementedError


class Constant(Function):
    def __init__(self, value: float):
        self.value = value

    def evaluate(self, x: float) -> float:
        return self.value


class Variable(Function):
    def evaluate(self, x: float) -> float:
        return x


class SqrtFun(Function):
    def evaluate(self, x: float) -> float:
        return math.sqrt(x)


class BinaryOperation(Function):
    def __init__(self, left: Union[Function, float], op: str, right: Union[Function, float]):
        self.left = left if isinstance(left, Function) else Constant(left)
        self.right = right if isinstance(right, Function) else Constant(right)
        self.op = op

    def evaluate(self, x: float) -> float:
        lv = self.left.evaluate(x)
        rv = self.right.evaluate(x)
        if self.op == '+':
            return lv + rv
        elif self.op == '-':
            return lv - rv
        elif self.op == '*':
            return lv * rv
        elif self.op == '/':
            return lv / rv
        else:
            raise ValueError(f"Unknown operator {self.op}")


functions = {
    'x': Variable(),
    'sqrt_fun': SqrtFun()
}


def parse_define(tokens):
    name = tokens[1]
    left_str = tokens[2]
    op = tokens[3]
    right_str = tokens[4]

    def parse_operand(s: str) -> Function:
        try:
            return Constant(float(s))
        except ValueError:
            return functions[s]

    left_func = parse_operand(left_str)
    right_func = parse_operand(right_str)
    functions[name] = BinaryOperation(left_func, op, right_func)


def parse_calculate(tokens):
    name = tokens[1]
    func = functions[name]
    results = []
    for tok in tokens[2:]:
        x = float(tok)
        results.append(func.evaluate(x))
    print(' '.join(str(int(res)) if res.is_integer() else str(res) for res in results))


def process_math_expression(line: str):
    tokens = line.strip().split()
    if not tokens:
        return
    if tokens[0] == 'define':
        parse_define(tokens)
    elif tokens[0] == 'calculate':
        parse_calculate(tokens)


# №17 Конференция (доклады)
class Talk:
    def __init__(self, topic: str, start_time: float, duration: float):
        self.topic = topic
        self.start = start_time
        self.end = start_time + duration

    def overlaps(self, other: 'Talk') -> bool:
        return not (self.end <= other.start or self.start >= other.end)


class Conference:
    def __init__(self):
        self.talks = []

    def add_talk(self, talk: Talk) -> bool:
        for t in self.talks:
            if t.overlaps(talk):
                print(f"Ошибка: доклад «{talk.topic}» пересекается с докладом «{t.topic}»")
                return False
        self.talks.append(talk)
        self.talks.sort(key=lambda x: x.start)
        print(f"Доклад «{talk.topic}» добавлен")
        return True

    def total_time(self) -> float:
        return sum(t.end - t.start for t in self.talks)

    def longest_break(self) -> float:
        if len(self.talks) <= 1:
            return 0.0
        max_break = 0.0
        for i in range(1, len(self.talks)):
            gap = self.talks[i].start - self.talks[i-1].end
            if gap > max_break:
                max_break = gap
        return max_break

    def print_schedule(self):
        print("Расписание конференции:")
        for t in self.talks:
            print(f"  {t.start:.1f}-{t.end:.1f}: {t.topic}")


# №18 Файловая система
class FileSystemNode:
    pass


class Directory(FileSystemNode):
    def __init__(self, name: str):
        self.name = name
        self.subdirs = {}
        self.files = {}

    def get_or_create_dir(self, path: List[str]) -> 'Directory':
        if not path:
            return self
        first, rest = path[0], path[1:]
        if first not in self.subdirs:
            self.subdirs[first] = Directory(first)
        return self.subdirs[first].get_or_create_dir(rest)

    def get_dir(self, path: List[str]):
        if not path:
            return self
        first, rest = path[0], path[1:]
        if first in self.subdirs:
            return self.subdirs[first].get_dir(rest)
        return None

    def list(self):
        items = list(self.subdirs.keys()) + list(self.files.keys())
        return sorted(items)

    def create_file(self, name: str, content: str = ""):
        self.files[name] = content

    def read_file(self, name: str) -> Optional[str]:
        return self.files.get(name)

    def write_file(self, name: str, content: str):
        self.files[name] = content


class FileSystem:
    def __init__(self):
        self.root = Directory("")

    def _resolve_path(self, path: str) -> Tuple[Directory, str, List[str]]:
        parts = [p for p in path.split('/') if p]
        if not parts:
            return self.root, "", []
        *dir_parts, last = parts
        parent = self.root.get_dir(dir_parts)
        if parent is None:
            parent = self.root.get_or_create_dir(dir_parts)
        return parent, last, dir_parts

    def mkdir(self, path: str):
        parent, last, _ = self._resolve_path(path)
        if last in parent.subdirs:
            print(f"Директория {path} уже существует")
        else:
            parent.subdirs[last] = Directory(last)
            print(f"Создана директория {path}")

    def ls(self, path: str = ""):
        parent, _, _ = self._resolve_path(path)
        items = parent.list()
        print(' '.join(items) if items else "(пусто)")

    def write(self, path: str, content: str):
        parent, filename, _ = self._resolve_path(path)
        parent.write_file(filename, content)
        print(f"Записано в файл {path}")

    def read(self, path: str):
        parent, filename, _ = self._resolve_path(path)
        content = parent.read_file(filename)
        if content is None:
            print(f"Файл {path} не найден")
        else:
            print(content)


# Демонстрация работы
if __name__ == "__main__":
    print("=== №1 BigBell ===")
    bell = BigBell()
    bell.sound()
    bell.sound()
    bell.sound()
    print()

    print("=== №2 Balance ===")
    balance = Balance()
    balance.add_right(18)
    balance.add_left(5)
    balance.add_left(2)
    print(balance.result())
    balance.add_left(1)
    print(balance.result())
    print()

    print("=== №3 Selector ===")
    sel = Selector([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(sel.get_odds())
    print(sel.get_evens())
    print()

    print("=== №4 Point ===")
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)
    print(p1 == p2)
    print(p1 != p2)
    print(p1 == p3)
    print()

    print("=== №5 ReversedList ===")
    rl = ReversedList([10, 20, 30])
    for i in range(len(rl)):
        print(rl[i])
    print()

    print("=== №6 SparseArray ===")
    arr = SparseArray()
    arr[1] = 10
    arr[2] = 20
    for i in range(10):
        print(f"arr[{i}] = {arr[i]}")
    print()

    print("=== №7 Queue ===")
    q1 = Queue(1, 2, 3)
    print(q1)
    q1.append(4, 5)
    print(q1)
    q2 = q1.copy()
    print(q2)
    print(q1 == q2, id(q1) == id(q2))
    q3 = q1.next()
    print(q1, q2, q3, sep='\n')
    q3.extend(Queue(1, 2))
    print(q3)
    q4 = Queue(1, 2)
    q4 += q3 >> 4
    print(q4)
    q5 = next(q4)
    print(q5)
    print()

    print("=== №9 Triangle & EquilateralTriangle ===")
    t = Triangle(3, 4, 5)
    print(t.perimeter())
    et = EquilateralTriangle(6)
    print(et.perimeter())
    print()

    print("=== №10 Summarator (базовый) ===")
    s = Summarator()
    print(s.sum(5))
    print("=== №11 PowerSummator, SquareSummarator, CubeSummarator ===")
    p = PowerSummator(2.5)
    print(p.sum(4))
    sq = SquareSummarator()
    print(sq.sum(5))
    cb = CubeSummarator()
    print(cb.sum(5))
    print()

    print("=== №12 Классы A, B, C, D ===")
    c = C()
    c.hello()
    c.good_evening()
    print(c)
    d = D()
    d.hello()
    d.good_evening()
    print(d)
    print()

    print("=== №13 Weapon, BaseEnemy, MainHero ===")
    sword = Weapon("Меч", 20, 1.5)
    enemy = BaseEnemy(5, 5, sword, 50)
    hero = MainHero(0, 0, "Герой", 100)
    hero.add_weapon(sword)
    hero.hit(enemy)
    print(enemy.is_alive())
    hero.next_weapon()
    hero.heal(30)
    print()

    print("=== №14 Почтовые серверы ===")
    server1 = MailServer("mail.ru")
    server2 = MailServer("gmail.com")
    MailClient.add_server(server1)
    MailClient.add_server(server2)
    client = MailClient(server1, "alice")
    client.send_mail("gmail.com", "bob", "Hello, Bob!")
    client2 = MailClient(server2, "bob")
    print(client2.receive_mail())
    print()

    print("=== №15 Преобразование списка ===")
    nums = [1, 5, -2, 0, 30, -4]
    print(process_commands(nums, [make_negative]))
    print(process_commands(nums, [square, strange_command]))
    print(process_commands(nums, [square, strange_command, square]))
    print()

    print("=== №16 Математические функции ===")
    test_input = "define f1 x * x\ndefine f2 -1 * x\ndefine f3 f1 + f2\ncalculate f3 -5 -2 0 2 5"
    for line in test_input.split('\n'):
        process_math_expression(line)
    print()

    print("=== №17 Конференция ===")
    conf = Conference()
    conf.add_talk(Talk("Python", 9.0, 1.0))
    conf.add_talk(Talk("Java", 10.0, 0.5))
    conf.add_talk(Talk("C++", 10.5, 1.0))
    conf.add_talk(Talk("Go", 11.0, 1.0))
    print(f"Общее время: {conf.total_time()}")
    print(f"Самый длинный перерыв: {conf.longest_break()}")
    conf.print_schedule()
    print()

    print("=== №18 Файловая система ===")
    fs = FileSystem()
    fs.mkdir("aaa")
    fs.mkdir("aaa/bbb")
    fs.mkdir("aaa/ccc")
    fs.ls("aaa")
    fs.write("aaa/1.txt", "Hello world")
    fs.read("aaa/1.txt")
    fs.ls("aaa/bbb")
