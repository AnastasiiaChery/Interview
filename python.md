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


# Troubleshooting in Python

## Типи профайлерів: статичні та динамічні

Серйозна розробка програмного забезпечення вимагає оптимізації продуктивності.
Коли ви починаєте оптимізувати продуктивність застосунку, неможливо уникнути використання профайлерів.

Вони застосовуються як для:

* моніторингу production-серверів
* відстеження частоти та тривалості викликів методів

---

## Модуль trace

Модуль `trace` дозволяє виконувати кілька корисних дій.

### Code coverage

Побачити, які рядки коду виконуються:

```bash
python3 -m trace --count trace_example/main.py
```

### Зв’язки між функціями

```bash
python3 -m trace --listfuncs trace_example/main.py | grep -v importlib
```

### Відстеження викликів

```bash
python3 -m trace --listfuncs --trackcalls trace_example/main.py | grep -v importlib
```

Якщо ви тільки починаєте працювати з трасуванням, варто почати з `trace`.

---

## Модуль faulthandler

`faulthandler` використовується для:

* виведення traceback при помилках
* дампу traceback після timeout
* обробки користувацьких сигналів

Він добре працює разом із системними fault-handler’ами (наприклад, Apport або Windows fault handler).

Разом модулі `trace` і `faulthandler` допомагають налагоджувати Python-код.

---

## APM-інструменти

Application Performance Monitoring (APM) інструменти.

Приклад:

* Datadog (production-моніторинг)

---

## Яку частину коду профілювати?

Профілювання — це аналіз продуктивності для пошуку **bottleneck-ів**.

Часто профілюють:

* методи або функції
* окремі рядки коду
* використання пам’яті

---

## Які метрики вимірювати?

* швидкість (час)
* кількість викликів
* використання пам’яті

---

## Профілювання функцій і рядків

У Python 3 доступні модулі:

* `cProfile`
* `profile`
* `pstats`

Приклад:

```python
import cProfile
import re

cProfile.run('re.compile("foo|bar")')
```

```
197 function calls (192 primitive calls) in 0.002 seconds
```

---

## Memory profiling

Профілювання пам’яті допомагає:

* знаходити memory leaks
* оптимізувати використання пам’яті

Рекомендовані бібліотеки:

* pympler
* objgraph

```python
from pympler import classtracker

tr = classtracker.ClassTracker()
tr.track_class(Document)
tr.create_snapshot()

create_documents()

tr.create_snapshot()
tr.stats.print_summary()
```

---

## Deterministic vs Statistical profiling

Профілювання потребує моніторингу виконання програми.

Є два підходи:

### Deterministic profiling

Відстежує всі виклики функцій і події винятків.
Точніший, але має більший overhead.

Приклад:

```
cProfile
```

### Statistical profiling

Використовує sampling.
Менший overhead, але нижча точність.

---

## pyinstrument

`pyinstrument` — open-source профайлер зі **statistical profiling**.

Він підкреслює, що deterministic profiling може:

* уповільнювати програму
* викривляти результати

Особливо якщо:

> "code that makes a lot of Python function calls invokes the profiler a lot, making it slower."

---

## resource module

Модуль `resource` дозволяє вимірювати системні ресурси, використані програмою.

```python
from resource import *
import time

time.sleep(3)
print(getrusage(RUSAGE_SELF))

for i in range(10 ** 8):
   _ = 1 + 1

print(getrusage(RUSAGE_SELF))
```

---

# Context managers

Контекстні менеджери допомагають керувати зовнішніми ресурсами.

`with` автоматично виконує:

* setup
* teardown

---

## Контекстний менеджер через клас

```python
class WritableFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file_obj = open(self.file_path, mode="w")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()
```

---

## contextlib decorator

```python
from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()

with writable_file("hello.txt") as file:
    file.write("Hello, World!")
```

---

## Async context manager example

```python
# site_checker_v1.py
import aiohttp
import asyncio

async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")
            html = await response.text()
            print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com"),
    )

asyncio.run(main())
```


````md
# Модульне тестування в Python

## Mock-об’єкти

Mock-об’єкт підміняє та імітує реальний об’єкт у середовищі тестування. Це універсальний і потужний інструмент для підвищення якості ваших тестів.

Одна з причин використовувати mock-об’єкти в Python — це контроль поведінки коду під час тестування.

Наприклад, якщо ваш код робить HTTP-запити до зовнішніх сервісів, то тести виконуються передбачувано лише настільки, наскільки ці сервіси поводяться очікувано. Іноді тимчасова зміна поведінки таких зовнішніх сервісів може спричиняти періодичні збої у вашому наборі тестів.

```python
>>> from unittest.mock import Mock
>>> mock = Mock()
>>> mock
<Mock id='4561344720'>
````

Mock повинен імітувати будь-який об’єкт, який він замінює. Для досягнення такої гнучкості він створює свої атрибути під час звернення до них.

```python
>>> from unittest.mock import Mock

>>> # Створення mock-об’єкта
... json = Mock()

>>> json.loads('{"key": "value"}')
<Mock name='mock.loads()' id='4550144184'>

>>> # Ви знаєте, що викликали loads(), тому можете
>>> # зробити перевірки (assertions)
... json.loads.assert_called()
>>> json.loads.assert_called_once()
>>> json.loads.assert_called_with('{"key": "value"}')
>>> json.loads.assert_called_once_with('{"key": "value"}')
```

```python
datetime = Mock()
datetime.datetime.today.return_value = "tuesday"

requests = Mock()
requests.get.side_effect = Timeout
```

```python
@patch('my_calendar.requests')
def test_get_holidays_timeout(self, mock_requests):
    mock_requests.get.side_effect = Timeout
```

або

```python
with patch('my_calendar.requests') as mock_requests:
    mock_requests.get.side_effect = Timeout
```

Також існують `MagicMock` і `AsyncMock`.

---

## Coverage

Coverage.py — один із найпопулярніших інструментів для вимірювання покриття коду в Python. Він використовує інструменти аналізу коду та механізми трасування зі стандартної бібліотеки Python для вимірювання покриття. Працює з основними версіями CPython, PyPy, Jython та IronPython. Coverage.py можна використовувати як з `unittest`, так і з `pytest`.

---

## Фреймворки тестування: pytest, unittest, doctest

Примітка: оригінальний проєкт **nose** більше не підтримується (останній реліз у 2015 році). **nose2** існує, але також не розвивається активно. **pytest** наразі є фактичним стандартом для тестування Python.

---

## pytest (Рекомендовано)

```python
# test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"
```

```bash
pytest test_example.py -v
```

### Основні можливості pytest

* Простий `assert` (без спеціальних методів перевірки)
* Потужні fixtures для setup/teardown
* Параметризовані тести
* Розвинена екосистема плагінів
* Кращий вивід і налагодження

---

## unittest (Стандартна бібліотека)

Вбудований у Python, використовує патерн xUnit:

```python
import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
```

---

## doctest

Модуль `doctest` шукає фрагменти тексту, які виглядають як інтерактивні сесії Python, а потім виконує їх, щоб перевірити, що вони працюють саме так, як показано.

Поширені способи використання `doctest`:

* Перевірка актуальності docstring-прикладів у модулі
* Регресійне тестування інтерактивних прикладів
* Написання навчальної документації з прикладами введення-виведення

Залежно від того, що підкреслюється — приклади чи пояснювальний текст — це може нагадувати **literate testing** або **виконувану документацію**.

```bash
python example.py -v
```

```
```


````md
# Керування пам’яттю в Python

## 3 покоління GC

Основний алгоритм збирання сміття, який використовується в CPython, — це **підрахунок посилань (reference counting)**. Основна ідея полягає в тому, що CPython підраховує, скільки різних місць мають посилання на об’єкт. Таким місцем може бути інший об’єкт, глобальна (або статична) C-змінна або локальна змінна в деякій C-функції.

Коли лічильник посилань об’єкта стає рівним нулю, об’єкт звільняється з пам’яті. Якщо він містить посилання на інші об’єкти, їхні лічильники посилань зменшуються. Ці об’єкти також можуть бути звільнені, якщо їхній лічильник стане рівним нулю, і так далі.

Поле лічильника посилань можна перевірити за допомогою функції `sys.getrefcount` (зверніть увагу, що значення, яке повертається, завжди на 1 більше, оскільки сама функція також має посилання на об’єкт під час виклику):

```python
x = object()
sys.getrefcount(x)
2
y = x
sys.getrefcount(x)
3
del y
sys.getrefcount(x)
2
````

---

## Проблема циклічних посилань

Основна проблема схеми підрахунку посилань полягає в тому, що вона **не обробляє циклічні посилання**. Наприклад:

```python
container = []
container.append(container)
sys.getrefcount(container)
3
del container
```

У цьому прикладі `container` містить посилання на самого себе, тому навіть після видалення змінної `container` лічильник посилань не стає нулем. Об’єкт не буде очищений простим підрахунком посилань.

З цієї причини потрібен додатковий механізм для очищення циклічних посилань між об’єктами, коли вони стають недосяжними. Це **циклічний збирач сміття**, який зазвичай називають **Garbage Collector (GC)**, хоча підрахунок посилань також є формою збирання сміття.

---

## Покоління GC

Щоб обмежити час кожного проходу GC, використовується оптимізація — **покоління (generations)**.

Ідея полягає в припущенні, що більшість об’єктів мають короткий життєвий цикл і можуть бути зібрані невдовзі після створення. Це відповідає реальності багатьох Python-програм, де тимчасові об’єкти створюються і знищуються дуже швидко.

Чим старіший об’єкт, тим менша ймовірність, що він стане недосяжним.

Усі **container-об’єкти** поділяються на **три покоління**:

* **generation 0** — нові об’єкти
* **generation 1**
* **generation 2**

Кожен новий об’єкт починає в **generation 0**.
Якщо об’єкт переживає збірку свого покоління, він переміщується до наступного покоління, де перевіряється рідше.

---

## Пороги GC

Покоління збираються, коли кількість об’єктів досягає певного порогу. Ці пороги можна перевірити:

```python
import gc
gc.get_threshold()
(700, 10, 10)
```

```python
import gc
gc.get_count()
(596, 2, 1)
```

---

## Ручний запуск GC

Процес збирання сміття можна запустити вручну:

```python
gc.collect()
```

Приклад:

```python
import gc

class MyObj:
    pass

gc.collect()
0

x = MyObj()
x.self = x

gc.get_objects(generation=0)
[..., <__main__.MyObj object at 0x7fbcc12a3400>, ...]

gc.collect(generation=0)
0
gc.get_objects(generation=0)
[]
gc.get_objects(generation=1)
[..., <__main__.MyObj object at 0x7fbcc12a3400>, ...]
```

---

## Відстеження об’єктів

Модуль GC надає функцію:

```python
gc.is_tracked(obj)
```

Вона повертає статус відстеження об’єкта.

---

## Які об’єкти відстежуються?

Загальне правило:

* екземпляри **атомарних типів** не відстежуються
* екземпляри **неатомарних типів** (контейнери, користувацькі об’єкти) відстежуються

Деякі оптимізації:

* кортежі з незмінних об’єктів не відстежуються
* словники з незмінних об’єктів не відстежуються

---

## Рекомендації щодо використання GC

Загальне правило:
**не змінюйте поведінку garbage collector без необхідності.**

---

## Витоки пам’яті

Python-програми, як і програми іншими мовами, можуть мати **витоки пам’яті (memory leaks)**.

Витоки пам’яті в Python виникають, якщо garbage collector не очищає невикористані або недосяжні дані.

Розробники Python додали механізми автоматичного звільнення пам’яті, але деякі невикористані об’єкти все ще можуть залишатися в пам’яті, що призводить до витоків.

```
```


````md
# Threading і multiprocessing у Python

## GIL (визначення, алгоритми в 2.x і 3.x)

**GIL (Global Interpreter Lock)** — це механізм, який використовується інтерпретатором CPython для гарантування того, що **лише один потік виконує Python-байткод одночасно**.

Це спрощує реалізацію CPython, роблячи модель об’єктів (включно з критичними вбудованими типами, такими як `dict`) неявно безпечною для конкурентного доступу. Блокування всього інтерпретатора полегшує підтримку багатопотоковості, але зменшує рівень паралелізму на багатоядерних системах.

Деякі модулі-розширення (стандартні або сторонні) можуть **звільняти GIL** під час виконання обчислювально-інтенсивних задач, таких як стиснення або хешування. Також GIL завжди звільняється під час **операцій введення/виведення (I/O)**.

Спроби створити «вільно-потоковий» інтерпретатор (з блокуванням даних на більш дрібному рівні) не були успішними, оскільки продуктивність у типовому однопроцесорному випадку погіршувалася.

---

## Перемикання потоків

```python
import sys

sys.getswitchinterval()
0.005  # 5 мс — інтервал між перемиканнями потоків

sys.setswitchinterval(0.01)
````

Примітка:

* `sys.getcheckinterval()` і `sys.setcheckinterval()` були видалені у Python 3.2
* Python 2.x використовував перемикання за кількістю інструкцій
* Python 3.x використовує **часовий інтервал (за замовчуванням 5 мс)**

Раніше CPU-bound потік часто повторно захоплював GIL раніше за інші потоки.
Цю проблему було виправлено у Python 3.2 (Antoine Pitrou), додавши механізм врахування запитів інших потоків.

---

## Threads

(модулі `thread`, `threading`; клас `Queue`; locks)

### Простий приклад

```python
from time import sleep, perf_counter
from threading import Thread

def task():
    print('Starting a task...')
    sleep(1)
    print('done')

start_time = perf_counter()

t1 = Thread(target=task)
t2 = Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
```

---

### ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def cube(x):
    result = x * x * x
    print(f'Куб числа {x}: {result}')
    return result

if __name__ == '__main__':
    values = [3, 4, 5, 6]

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(cube, values))

    print("\nРезультати:")
    for value, result in zip(values, results):
        print(f"Куб числа {value}: {result}")
```

---

## queue.Queue

Операції:

* `maxsize` — максимальна кількість елементів
* `empty()` — перевірка, чи черга порожня
* `full()` — перевірка, чи черга заповнена
* `get()` — отримати елемент (з блокуванням)
* `get_nowait()` — отримати елемент без блокування
* `put(item)` — додати елемент
* `put_nowait(item)` — додати без блокування
* `qsize()` — кількість елементів

---

# Processes (multiprocessing)

`multiprocessing`, `Process`, `Queue`, `Pipe`, `Value`, `Array`, `Pool`, `Manager`

## Простий приклад

```python
from multiprocessing import Process
import time

def fun():
    print('starting fun')
    time.sleep(2)
    print('finishing fun')

def main():
    p = Process(target=fun)
    p.start()
    p.join()

if __name__ == '__main__':
    print('starting main')
    main()
    print('finishing main')
```

---

## Pool

```python
import time
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count

def square(n):
    time.sleep(2)
    return n * n

def main():
    start = timer()
    print(f'starting computations on {cpu_count()} cores')
    values = (2, 4, 6, 8)

    with Pool() as pool:
        res = pool.map(square, values)
        print(res)

    end = timer()
    print(f'elapsed time: {end - start}')

if __name__ == '__main__':
    main()
```

---

## pipes

Модуль `pipes` надає інтерфейс до shell-pipeline.
Він визначає клас для абстракції конвеєра — послідовності перетворень файлів.

---

# Як обійти обмеження GIL (C extensions)

## Лише C-потоки

```c
#include "Python.h"

PyObject *pyfunc(PyObject *self, PyObject *args)
{
    Py_BEGIN_ALLOW_THREADS

    /* Threaded C code (без Python API) */

    Py_END_ALLOW_THREADS

    return result;
}
```

---

## Змішування C і Python

Примітка:

* `PyEval_InitThreads()` застаріла з Python 3.9
* видалена у Python 3.13
* з Python 3.7 GIL ініціалізується автоматично

У сучасному Python достатньо використовувати:

```c
Py_BEGIN_ALLOW_THREADS
Py_END_ALLOW_THREADS
```

```
```


````md
# Розповсюдження і документація в Python

## distutils, setup.py

`distutils` було видалено у Python 3.12. Він був застарілим з Python 3.10 і остаточно видалений. Див. **PEP 632** для деталей.

Більшість користувачів Python не використовують цей модуль безпосередньо, а застосовують інструменти Python Packaging Authority.  
Найважливіший із них — **setuptools**, розширена альтернатива distutils, що надає:

- підтримку оголошення залежностей проєкту
- механізми визначення файлів для source-релізів
- інтеграцію з системами контролю версій
- підтримку **entry points** (плагін-системи)
- автоматичне створення Windows CLI-виконуваних файлів під час інсталяції

Setuptools — це стабільна бібліотека з повним функціоналом для пакування Python-проєктів.

---

## Мінімальна конфігурація setuptools

### pyproject.toml
```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
````

Далі потрібен `setup.cfg` або `setup.py`.

```python
from setuptools import setup

setup(
    name='mypackage',
    version='0.0.1',
    packages=['mypackage'],
    install_requires=[
        'requests',
        'importlib; python_version == "2.6"',
    ],
)
```

Структура проєкту:

```
~/mypackage/
    pyproject.toml
    setup.cfg
    mypackage/__init__.py
```

```bash
python -m build
```

---

## Публікація коду

[https://packaging.python.org/en/latest/tutorials/packaging-projects/](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src/
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

---

# Автогенерація документації

Інструменти:

* sphinx
* pydoc
* autosummary
* autodoc
* pdoc
* pdoc3
* pydoctor
* Doxygen (+ Graphviz)

### autosummary

розширення Sphinx для автоматичного створення summary-документації.

### autodoc

обробляє docstring-и reST.

### pdoc

простий генератор API-документації.

### PyDoc

браузер документації зі стандартної бібліотеки.

### Doxygen

генерує HTML, PDF, LaTeX-документацію і діаграми.

---

# Взаємодія Python і C

## Python C API

### Проста C-функція

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    FILE *fp = fopen("write.txt", "w");
    fputs("Real Python!", fp);
    fclose(fp);
    return 1;
}
```

---

## Python-сумісна версія

```c
#include <Python.h>

static PyObject *method_fputs(PyObject *self, PyObject *args) {
    char *str, *filename = NULL;
    int bytes_copied = -1;

    if(!PyArg_ParseTuple(args, "ss", &str, &filename)) {
        return NULL;
    }

    FILE *fp = fopen(filename, "w");
    bytes_copied = fputs(str, fp);
    fclose(fp);

    return PyLong_FromLong(bytes_copied);
}
```

---

## Побудова через setuptools

### pyproject.toml

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "fputs"
version = "1.0.0"

[tool.setuptools]
ext-modules = [
    {name = "fputs", sources = ["fputsmodule.c"]}
]
```

### setup.py

```python
from setuptools import setup, Extension

setup(
    name="fputs",
    version="1.0.0",
    ext_modules=[Extension("fputs", ["fputsmodule.c"])]
)
```

```bash
pip install build
python -m build
pip install dist/*.whl
```

---

## Приклад використання

```python
import fputs
fputs.fputs("Real Python!", "write.txt")
```

---

# Інструменти інтеграції C і Python

## cffi

[https://cffi.readthedocs.io/en/latest/](https://cffi.readthedocs.io/en/latest/)

```python
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
    float pi_approx(int n);
""")
```

---

## SWIG

[http://www.swig.org/exec.html](http://www.swig.org/exec.html)

Інтерфейс-компілятор для C/C++ і Python.

---

## SIP

[https://www.riverbankcomputing.com/static/Docs/sip/examples.html](https://www.riverbankcomputing.com/static/Docs/sip/examples.html)

Інструменти для створення Python-binding-ів для C/C++.

---

## Boost.Python

```cpp
#include <boost/python.hpp>

BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
    def("greet", greet);
}
```

Python:

```python
import hello_ext
print(hello_ext.greet())
```

```
```




