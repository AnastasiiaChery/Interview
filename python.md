# Mutable та Immutable об’єкти в Python

## Mutable об’єкти (передача за посиланням)

* `list`
* `dict`
* `set`
* `bytearray`

## Immutable об’єкти (передача за значенням)

* `int`
* `float`
* `complex`
* `string`
* `tuple`

  > «Значення» immutable-об’єкта не може змінюватися, але об’єкти всередині нього можуть.
* `frozenset` — immutable-версія `set`
* `bytes`

---

## Особливості

* Python по-різному працює з mutable та immutable об’єктами.
* Immutable-об’єкти швидше для доступу.
* Mutable-об’єкти зручно використовувати, коли потрібно змінювати розмір об’єкта (`list`, `dict`).
* Immutable-об’єкти використовуються, коли потрібно гарантувати незмінність.
* Immutable-об’єкти «дорого» змінювати, бо створюється копія.
* Зміна mutable-об’єктів — дешева операція.

---

# Передача об’єктів у функції

Різниця між mutable та immutable типами важлива для **ефективності використання пам’яті**.

Якщо mutable-об’єкт передається у функцію, він може змінити **оригінальну змінну**.

Щоб цього уникнути — створюйте копію.

Immutable-об’єкти можна передавати безпечно, оскільки їх значення не змінюється.

---

# Способи виконання Python-коду

* `exec`
* `eval`
* `ast`
* `code`
* `codeop`

---

## exec()

Метод `exec(object, globals, locals)` виконує динамічно створену програму
(рядок або code object).
Повертає `None` — важливі лише побічні ефекти.

### Приклад 1

```python
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
```

Результат:

```
Sum = 15
```

### Приклад 2

```python
globals_parameter = {'__builtins__': None}
locals_parameter = {'print': print, 'dir': dir}

exec('print(dir())', globals_parameter, locals_parameter)
```

```
['dir', 'print']
```

---

## eval()

Метод `eval(expression, globals=None, locals=None)` виконує **вираз**
і повертає його значення.

```python
a = 5
eval('37 + a')
```

```
42
```

### Різниця між exec і eval

```python
exec('37 + a')   # значення ігнорується
exec('a = 47')   # змінює глобальну змінну
a
```

```
47
```

```python
eval('a = 47')  # помилка
```

---

## Використання compile()

```python
eval(compile('if 1: print("Hello")', '<string>', 'exec'))
```

```
Hello
```

---

# AST (Abstract Syntax Trees)

AST дозволяє:

* аналізувати код
* змінювати код
* генерувати код
* виконувати інспекцію

```python
import ast
tree = ast.parse("x = 1")
```

---

# Модулі code та codeop

## code

Дозволяє створювати **інтерактивні інтерпретатори (REPL)**.

## codeop

Допоміжний модуль для REPL.
Зазвичай використовується через `code`.

---

# Різниця Python 2.x та 3.x

## Ділення

Рекомендується використовувати float:

```python
7.0 / 5
7 / 5.0
```

---

## print

Python 2:

```python
print "Hello"
```

Python 3:

```python
print("Hello")
```

---

## Unicode

* Python 2 → ASCII `str`
* Python 3 → Unicode `str`

---

## xrange

Python 2:

* `range()` → список
* `xrange()` → ітератор

Python 3:

* тільки `range()`

---

## Обробка помилок

Python 3 потребує `as`:

```python
except Exception as e:
    pass
```

---

## future

Модуль `_future_` допомагає мігрувати з Python 2 до Python 3.

---

## six

Бібліотека сумісності Python 2 і 3:
[https://six.readthedocs.io](https://six.readthedocs.io)

---

# copy та slicing

```python
copy()
deepcopy()
slice()
```

* `copy()` — поверхнева копія
* `deepcopy()` — глибока копія
* `slice()` — створює slice-об’єкт

---

# OrderedDict та DefaultDict

## OrderedDict

Зберігає порядок вставки ключів.

З Python 3.7 `dict` також гарантує порядок, але `OrderedDict` має додаткові можливості:

* order-sensitive equality
* `move_to_end()`
* `popitem()` з обох боків

---

## DefaultDict

```python
from collections import defaultdict

def def_value():
    return "Not Present"

d = defaultdict(def_value)
```

Не викликає `KeyError`.

---

# Hashable об’єкти

Об’єкт є hashable, якщо:

* має незмінний hash
* має `__hash__()`
* має `__eq__()`

```python
from collections.abc import Hashable
isinstance(obj, Hashable)
```

Або:

```python
try:
    hash(obj)
except TypeError:
    pass
```

---

## Hashable типи

Immutable:

* `int`
* `str`
* `tuple`
* `frozenset`

Не hashable:

* `list`
* `dict`
* `set`

---

## Функції

* `lambda` — hashable
* user-defined functions — hashable

Хешування є **one-way функцією**.


# Strong та Weak Typing у Python

Python є **strongly typed** та **dynamically typed** мовою.

## Strong typing

Сильна типізація означає, що тип значення **не змінюється автоматично**.
Наприклад, рядок, який містить лише цифри, не перетворюється на число без явного приведення типу.

Кожна зміна типу потребує **явної конверсії**.

---

## Dynamic typing

Динамічна типізація означає, що **тип мають об’єкти під час виконання**, а не змінні.

```python
bob = 1
bob = "bob"
```

Це працює, тому що змінна **не має фіксованого типу** — вона лише посилається на об’єкт.

```python
type(bob)
```

Результат:

* після `bob = 1` → `int`
* після `bob = "bob"` → `str`

---

# Frozenset

Функція `frozenset()` повертає **immutable-об’єкт множини**, створений з ітерабельного об’єкта.

Frozen set — це **незмінна версія set**.

* елементи `set` можна змінювати
* елементи `frozenset` не можна змінити після створення

Завдяки цьому `frozenset` можна використовувати:

* як ключ у словнику
* як елемент іншої множини

Як і `set`, він **не є впорядкованим**.

```python
fs = frozenset([1, 2, 3])
```

---

# Weak references

У Python є модуль `weakref`, який дозволяє створювати **слабкі посилання на об’єкти**.

Якщо на об’єкт більше немає **сильних посилань**,
**garbage collector** може звільнити пам’ять.

Weak references використовуються для:

* кешів
* великих мапінгів
* структур даних з великою кількістю об’єктів

```python
import weakref
```

---

# Raw strings

Raw-рядок у Python створюється за допомогою префікса `r` або `R`.

У raw-рядку символ `\` сприймається **буквально**, а не як escape-послідовність.

Це особливо корисно для:

* регулярних виразів
* шляхів у файловій системі
* Windows-шляхів

```python
path = r"C:\Users\name\file.txt"
print(path)
```


# Unicode та ASCII-рядки в Python

**Unicode** — це міжнародний стандарт, який підтримує відповідність між символами та унікальними числовими значеннями.

Модуль Python `unicodedata` використовує **Unicode Character Database (UCD)**.
Починаючи з **Python 3.13+**, Python використовує **Unicode 16.0.0 (вересень 2024)**, який містить **154 000+ символів**, включаючи:

* латиницю
* індійські писемності
* китайсь


# Python Statements та Syntax

## Iteration Protocol

Ітератор у Python — це об’єкт, який реалізує **iterator protocol**:

* `__iter__()`
* `__next__()`

---

# Generators

Генератори — це ітератори, які можна пройти лише **один раз**.
Вони **не зберігають усі значення в пам’яті**, а генерують їх під час виконання.

---

## yield

`yield` працює подібно до `return`, але функція повертає **generator object**.

Коли функція з `yield` викликається — її код **не виконується одразу**,
а повертається генератор.

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

---

# Методи генератора

## send()

Надсилає значення у генератор.
`send(None)` потрібно викликати при ініціалізації.

```python
def double_number(number):
    while True:
        number *= 2
        number = yield number
```

---

## throw()

Дозволяє кинути виняток у генератор.

```python
def add_to_database(connection_string):
    db = mydatabaselibrary.connect(connection_string)
    cursor = db.cursor()
    try:
        while True:
            try:
                row = yield
                cursor.execute('INSERT INTO mytable VALUES(?, ?, ?)', row)
            except CommitException:
                cursor.execute('COMMIT')
            except AbortException:
                cursor.execute('ABORT')
    finally:
        cursor.execute('ABORT')
        db.close()
```

---

## Інші методи генератора

* `next()`
* `close()`

---

# Coroutines (async / await)

Рекомендований спосіб роботи з `asyncio`.

```python
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
```

Результат:

```
hello
world
```

---

# Pattern Matching (Python 3.10+)

Structural pattern matching з `match` і `case`.

## Особливості

* робота з послідовностями
* робота зі словниками
* guard-вирази
* capture patterns

```python
def process_command(command):
    match command.split():
        case ["go", direction]:
            return f"Moving {direction}"
        case ["pick", "up", item]:
            return f"Picking up {item}"
        case ["quit"]:
            return "Quitting"
        case _:
            return "Unknown command"
```

---

# Exception Groups (Python 3.11+)

Дозволяють обробляти **кілька винятків одночасно**.

```python
try:
    raise ExceptionGroup("group", [
        ValueError("invalid value"),
        TypeError("invalid type")
    ])
except* ValueError as e:
    print(f"Handled ValueError: {e}")
except* TypeError as e:
    print(f"Handled TypeError: {e}")
```

---

# Type Parameter Syntax (Python 3.12+)

Новий синтаксис для generic-типів.

```python
type List[T] = list[T]

def first[T](items: list[T]) -> T:
    return items[0]
```

---

# Per-Interpreter GIL (Python 3.12+)

Дозволяє кожному інтерпретатору мати **власний GIL**, що забезпечує паралелізм.

## Еволюція API

* Python 3.12 — тільки C-API
* Python 3.13 — базовий interpreters module
* Python 3.14 — `InterpreterPoolExecutor`

```python
from concurrent.futures import InterpreterPoolExecutor

def cpu_bound_task(n):
    return sum(i * i for i in range(n))

with InterpreterPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_bound_task, [10**6]*4))
```

---

# Free-Threaded Python (Python 3.13+, Experimental)

PEP 703 — режим Python **без GIL**.

## Особливості

* справжній паралелізм потоків
* fine-grained locking
* експериментальна функція

```python
import sys
print(sys._is_gil_enabled())
```

---

# JIT Compiler (Python 3.13+, Experimental)

Just-In-Time компілятор:

* вимкнений за замовчуванням
* невелике прискорення
* працює разом із adaptive interpreter

---

# Покращений REPL (Python 3.13+)

Новий інтерпретатор:

* багаторядкове редагування
* кольорові traceback
* історія команд
* F1 для довідки

---

# Підтримка платформ (Python 3.13+)

PEP 11:

* iOS — Tier 3
* Android — Tier 3

---
# Функції в Python

## Коли і скільки разів обчислюються аргументи за замовчуванням?

Один раз під час запуску програми.

---

## partial

```
functools.partial(func, /, *args, **keywords)
```

Повертає новий об’єкт partial, який при виклику поводиться так само, як `func`, викликана з позиційними аргументами `args` і ключовими аргументами `keywords`.
Якщо під час виклику передаються додаткові аргументи, вони додаються до `args`.
Якщо передаються додаткові ключові аргументи, вони розширюють і перевизначають `keywords`.

---

## Найкраща практика декораторів для функцій

Основна ідея — використовувати функцію, але повертати partial-об’єкт самої себе, якщо її викликають із параметрами перед використанням як декоратора:

```python
from functools import wraps, partial

def decorator(func=None, parameter1=None, parameter2=None):

   if not func:
        # Єдиний недолік — для функцій немає
        # такого поняття, як "self" — доводиться покладатися
        # на ім’я функції-декоратора у просторі імен модуля
        return partial(decorator, parameter1=parameter1, parameter2=parameter2)

   @wraps(func)
   def wrapper(*args, **kwargs):
        # Код декоратора — parameter1 тощо
        # можна вільно використовувати тут
        return func(*args, **kwargs)
   return wrapper
```

І це все — декоратори, написані за цим шаблоном, можуть одразу декорувати функцію без попереднього "виклику":

```python
@decorator
def my_func():
    pass
```

Або бути налаштованими через параметри:

```python
@decorator(parameter1="example.com", ...)
def my_func():
    pass
```

---

## Decorator

```python
import functools

def require_authorization(f):
    @functools.wraps(f)
    def decorated(user, *args, **kwargs):
        if not is_authorized(user):
            raise UserIsNotAuthorized
        return f(user, *args, **kwargs)
    return decorated

@require_authorization
def check_email(user, etc):
    # etc.
```

---

## Фабрика декораторів (передача аргументів у декоратори)

```python
def require_authorization(action):
    def decorate(f):
        @functools.wraps(f)
        def decorated(user, *args, **kwargs):
            if not is_allowed_to(user, action):
                raise UserIsNotAuthorized(action, user)
            return f(user, *args, **kwargs)
        return decorated
    return decorate
```

---

## wraps

Зберігає оригінальне ім’я функції.

---

## Декоратор для класу

### Просто використати наслідування

### Використати декоратор, що повертає клас

```python
def addID(original_class):
    orig_init = original_class.__init__
    # Робимо копію оригінального __init__, щоб уникнути рекурсії

    def __init__(self, id, *args, **kws):
        self.__id = id
        self.getId = getId
        orig_init(self, *args, **kws)  # Виклик оригінального __init__

    original_class.__init__ = __init__
    return original_class

@addID
class Foo:
    pass
```

---

## Використання метакласу

Насправді метакласи особливо корисні для "чорної магії" і складних речей.
Але самі по собі вони прості:

* перехопити створення класу
* змінити клас
* повернути змінений клас

```python
>>> class Foo(object):
...       bar = True

>>> Foo = type('Foo', (), {'bar':True})
```

```python
class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, attrs):
        uppercase_attrs = {
            attr if attr.startswith("__") else attr.upper(): v
            for attr, v in attrs.items()
        }
        return type(clsname, bases, uppercase_attrs)
```

Основний випадок використання метакласів — створення API.
Типовий приклад — Django ORM.

---

## Непрямі виклики функцій

* використовувати іншу змінну для функції
* використовувати partial
* передавати як параметр `def indirect(func, *args)`
* використовувати вкладену функцію та повертати її (функціональний підхід)

```python
eval("func_name()")   # повертає результат функції
exec("func_name()")   # повертає None
```

```python
# імпорт модуля (припустимо, модуль foo з методом bar)
module = __import__('foo')
func = getattr(module, 'bar')
func()
```

```python
locals()["myfunction"]()
globals()["myfunction"]()
```

```python
functions = {'myfoo': foo.bar}

mystring = 'myfoo'
if mystring in functions:
    functions[mystring]()
```

---

## Інтроспекція функцій

Інтроспекція — це здатність визначати тип об’єкта під час виконання.
У Python усе є об’єктом. Кожен об’єкт може мати атрибути та методи.
Інтроспекція дозволяє динамічно досліджувати об’єкти Python.

Вона використовується для аналізу класів, методів, об’єктів, модулів і ключових слів та отримання інформації про них.

Інтроспекція відкриває корисну інформацію про об’єкти програми.

### Функції інтроспекції

* `type()` — повертає тип об’єкта
* `dir()` — список методів і атрибутів об’єкта
* `id()` — повертає унікальний ідентифікатор об’єкта
* `help()` — показує довідку
* `hasattr()` — перевіряє наявність атрибута
* `getattr()` — повертає значення атрибута
* `repr()` — рядкове представлення об’єкта
* `callable()` — перевіряє, чи є об’єкт функцією
* `issubclass()` — перевіряє наслідування класів
* `isinstance()` — перевіряє тип екземпляра
* `sys()` — доступ до системних змінних і функцій
* `__doc__` — документація об’єкта
* `__name__` — ім’я об’єкта

---

## Деталі реалізації функціонального програмування: for vs map

Функціональне програмування — це парадигма, у якій основним способом обчислення є виконання чистих функцій.
Хоча Python не є суто функціональною мовою, корисно знати:

* `lambda`
* `map()`
* `filter()`
* `reduce()`

Вони допомагають писати короткий, високорівневий і паралелізований код.

```python
list(
     map(
         (lambda a, b, c: a + b + c),
         [1, 2, 3],
         [10, 20, 30],
         [100, 200, 300]
     )
)
```

```python
list(filter(lambda s: s.isupper(),
["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]))
```

```python
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100)
# (100 + 1 + 2 + 3 + 4 + 5), 100 — початкове значення
```

---

## Атрибути функції

```python
def func():
    pass

dir(func)
```

```
Out[3]:
['__annotations__',
 '__call__',
 ...
 '__str__',
 '__subclasshook__']
```

```python
func.a = 1
dir(func)
```

```
Out[5]:
['__annotations__',
 '__call__',
 ...
 '__str__',
 '__subclasshook__',
 'a']
```

```python
print(func.__dict__)
```

```
{'a': 1}
```

```python
func.__getattribute__("a")
```

```
Out[7]: 1
```


# Scopes in Python

## Правило LEGB

Python визначає імена за так званим **правилом LEGB**, яке назване за типами областей видимості в Python.
Абревіатура **LEGB** означає **Local, Enclosing, Global, Built-in**.

Ось короткий огляд цих понять.

---

### Local (локальна область видимості)

Локальна (або функціональна) область видимості — це тіло будь-якої функції Python або lambda-виразу.
Вона містить імена, які ви визначаєте всередині функції.

Ці імена видимі лише з коду функції.

Локальна область видимості створюється **під час виклику функції**, а не під час її визначення, тому кількість локальних областей дорівнює кількості викликів функції.

Це справедливо навіть якщо:

* функція викликається кілька разів
* функція викликається рекурсивно

Кожен виклик створює нову локальну область видимості.

---

### Enclosing (nonlocal)

Охоплююча (або nonlocal) область видимості існує лише для **вкладених функцій**.

Якщо локальна область належить внутрішній функції, то enclosing-область — це область зовнішньої функції.

Вона містить імена, визначені у зовнішній функції.
Ці імена доступні як у внутрішній, так і у зовнішній функції.

---

### Global (модульна область)

Глобальна область — це **найвища область видимості** в програмі, скрипті або модулі Python.

Вона містить усі імена, визначені на верхньому рівні програми або модуля.
Імена з цієї області доступні з будь-якого місця коду.

```
dir()
```

---

### Built-in (вбудована область)

Built-in область — це спеціальна область видимості, яка створюється під час запуску скрипта або відкриття інтерактивної сесії.

Вона містить:

* ключові слова
* функції
* винятки
* інші вбудовані об’єкти Python

Імена з цієї області також доступні з будь-якого місця коду.

Вона автоматично завантажується Python під час запуску програми.

```
dir(__builtins__)  # ~152 імені
```

---

## Порядок пошуку імен (LEGB)

Правило LEGB визначає порядок, у якому Python шукає імена:

1. Local
2. Enclosing
3. Global
4. Built-in

Якщо ім’я знайдено — використовується перше знайдене значення.
Якщо ні — виникає помилка.

Коли `dir()` викликається без аргументів, повертається список імен у **глобальній області Python**.

Якщо створити нову змінну на верхньому рівні модуля (наприклад, `var` у `__main__`), вона з’явиться у списку `dir()`.

---

## global і nonlocal

### Інструкція global

Інструкція складається з ключового слова `global` і одного або кількох імен, розділених комами.

Можна використовувати кілька інструкцій `global`.

Усі імена, зазначені в `global`, будуть прив’язані до **глобальної (модульної) області видимості**.

---

### Інструкція nonlocal

Подібно до глобальних імен, **nonlocal-імена** можна читати з внутрішніх функцій, але змінювати їх безпосередньо не можна.

Щоб змінювати їх, потрібно використовувати `nonlocal`.

Інструкція `nonlocal` складається з:

* ключового слова `nonlocal`
* одного або кількох імен

Ці імена посилаються на ті самі змінні в **enclosing-області**.

---

## Scopes, вкладені функції та closures

Техніка, за якою дані (у цьому прикладі `hello`) прив’язуються до коду, називається **closure** в Python.

```python
def print_msg(msg):
    # Це зовнішня функція
    def printer():
        # Це вкладена функція
        print(msg)
    return printer  # повертає вкладену функцію

another = print_msg("Hello")
another()

# Output: Hello
```

### Умови створення closure

* має існувати вкладена функція
* вкладена функція повинна використовувати змінну із зовнішньої функції
* зовнішня функція повинна повертати вкладену функцію

Декоратори Python широко використовують closures.

---

## globals() і locals()

```
globals() → словник простору імен модуля
locals() → словник поточного простору імен
vars() → словник простору імен або об’єкта
```

`vars()`:

* без аргументів повертає словник поточного простору імен
* з аргументом повертає словник атрибутів об’єкта

Важливо:

* словник `locals()` **не оновлюється автоматично** при присвоєнні змінних
* зміна словника не створює відповідні локальні змінні


# Modules in Python

## Перезавантаження модуля (importlib)

Перезавантажує раніше імпортований модуль. Аргументом має бути **об’єкт модуля**, тому він повинен бути попередньо успішно імпортований.

Це корисно, якщо ви змінили вихідний файл модуля у зовнішньому редакторі й хочете перевірити нову версію без перезапуску інтерпретатора Python.

Повертається об’єкт модуля (він може відрізнятися, якщо повторний імпорт створює інший об’єкт у `sys.modules`).

```python
from importlib import reload  # Python 3.4+
import foo

while True:
    # Робимо щось
    if is_changed(foo):
        foo = reload(foo)
```

---

# OOP in Python

## SOLID

У програмній інженерії **SOLID** — це мнемонічна абревіатура з п’яти принципів проєктування, які роблять програмні системи зрозумілішими, гнучкішими та простішими в підтримці.

Ці принципи є підмножиною ідей, популяризованих Робертом С. Мартіном (Robert C. Martin) у роботі *Design Principles and Design Patterns* (2000).

Абревіатуру **SOLID** пізніше (≈2004) запропонував Майкл Фезерс.

### Принципи SOLID

**Single Responsibility Principle**
Клас повинен мати лише одну причину для зміни.

**Open–Closed Principle**
Програмні сутності мають бути відкритими для розширення, але закритими для модифікації.

**Liskov Substitution Principle**
Об’єкти похідних класів повинні бути взаємозамінними з об’єктами базового класу.

**Interface Segregation Principle**
Краще багато спеціалізованих інтерфейсів, ніж один універсальний.

**Dependency Inversion Principle**
Залежати потрібно від абстракцій, а не від реалізацій.

---

## Чотири основи об’єктно-орієнтованого програмування

**Encapsulation (інкапсуляція)**
Об’єднання даних і функцій, що працюють із ними, у клас.

**Abstraction (абстракція)**
Робота із системою як із “чорною скринькою”.

**Inheritance (наслідування)**
Похідний клас отримує функціональність і властивості базового класу.

**Polymorphism (поліморфізм)**
Один інтерфейс — різна поведінка залежно від типу об’єкта.

---

## Abstract Base Class

Абстрактні базові класи гарантують, що підкласи реалізують потрібні методи та властивості.

Вони:

* відокремлюють інтерфейс від реалізації
* визначають загальні методи
* спрощують підтримку ієрархії класів
* допомагають уникати помилок

```python
from abc import ABCMeta, abstractmethod

class AbstactClassCSV(metaclass=ABCMeta):
    def __init__(self, path, file_name):
       self._path = path
       self._file_name = file_name
        
    @property
    @abstractmethod
    def path(self):
       pass
```

---

## getattr(), setattr(), hasattr()

### hasattr(object, name)

Перевіряє, чи має об’єкт атрибут або метод.

### getattr(object, name[, default])

Повертає атрибут або значення за замовчуванням.

### setattr(object, name, value)

Присвоює значення атрибуту.

---

## **getattr**, **setattr**, **delattr**

```python
class Frob:
    def __setattr__(self, name, value):
        self.__dict__[name] = value.upper()

f = Frob()
f.bamf = "bamf"
f.bamf
```

```
'BAMF'
```

`__getattr__()` викликається лише тоді, коли атрибут не знайдено стандартним способом.

```python
class Frob:
    def __init__(self, bamf):
        self.bamf = bamf

    def __getattr__(self, name):
        return 'Frob does not have `{}` attribute.'.format(str(name))

f = Frob("bamf")
f.bar
f.bamf
```

---

## **getattribute**

```python
class Frob(object):
    def __getattribute__(self, name):
        print(f"getting `{name}`")
        return object.__getattribute__(self, name)

f = Frob()
f.bamf = 10
f.bamf
```

---

## Name mangling

У процесі name mangling ідентифікатори з подвійним підкресленням перетворюються на:

```
_classname__identifier
```

```python
class Student:
    def __init__(self, name):
        self.__name = name
  
s1 = Student("Santhosh")
print(s1._Student__name)
```

---

## @property (getter, setter, deleter)

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
del p.name
```

---

## Спеціальні методи

### **init**

Ініціалізація об’єкта.

### repr()

Повертає представлення об’єкта для відладки.

### **str**

Рядкове представлення об’єкта.

### **new**

Викликається під час створення об’єкта.

```python
class A(object):
    def __new__(cls):
         print("Creating instance")
         return super(A, cls).__new__(cls)
  
    def __init__(self):
        print("Init is called")
```

---

### **del**

Деструктор — викликається під час garbage collection.

---

## **hash** і **eq**

```python
class A(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __eq__(self, othr):
        return (
            isinstance(othr, type(self)) and
            (self._a, self._b, self._c) ==
            (othr._a, othr._b, othr._c)
        )

    def __hash__(self):
        return hash((self._a, self._b, self._c))
```

---

## Rich comparison methods

```
__lt__  __gt__  __le__  __ge__  __eq__  __ne__
```

---

## **call**

```python
class Product:
    def __init__(self):
        print("Instance Created")

    def __call__(self, a, b):
        print(a * b)

ans = Product()
ans(10, 20)
```

---

## Multiple inheritance і MRO

Python 3 використовує алгоритм **C3 MRO**.

Порядок пошуку методів:

* знизу вгору
* зліва направо

Спочатку перевіряється клас об’єкта, потім базові класи.

---

## Mixins

Mixin — це форма множинного наслідування.

Використовується, коли:

* потрібно додати опціональну функціональність
* одну можливість використовують багато класів

---

## Metaclass definition

Метакласи — це класи, що створюють класи.

```python
MyClass = type('MyClass', (), {})
```

```
MyClass = MetaClass()
my_object = MyClass()
```

---

## type(), isinstance(), issubclass()

### type()

* з одним аргументом → тип об’єкта
* з трьома → створення класу

Параметри:

* name
* bases
* dict

### isinstance()

Перевіряє тип об’єкта.

### issubclass()

Перевіряє наслідування.

```
issubclass(class, classinfo)
```

---

## **slots**

`__slots__` дозволяє явно визначити атрибути екземпляра.

Переваги:

* швидший доступ до атрибутів
* економія пам’яті

Економія пам’яті досягається завдяки збереженню значень у slots замість `__dict__`.

```python
class Base:
    __slots__ = 'foo', 'bar'

class Right(Base):
    __slots__ = 'baz',
```




