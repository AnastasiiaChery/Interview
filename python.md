
Mutable and Immutable Objects
Mutable objects (call by reference):
list, dict, set, bytearray

Immutable objects (pass by value):
int, float, complex, string,
tuple (the "value" of an immutable object can't change, but its constituent objects can.),
frozenset [note: immutable version of set],
bytes
Features:
Python handles mutable and immutable objects differently.
Immutable are quicker to access than mutable objects.
Mutable objects are great to use when you need to change the size of the object, example list, dict etc.. Immutables are used when you need to ensure that the object you made will always stay the same.
Immutable objects are fundamentally expensive to "change", because doing so involves creating a copy. Changing mutable objects is cheap.
How objects are passed to Functions
Its important for us to know difference between mutable and immutable types and how they are treated when passed onto functions. Memory efficiency is highly affected when the proper objects are used.

For example if a mutable object is called by reference in a function, it can change the original variable itself.

Hence to avoid this, the original variable needs to be copied to another variable. Immutable objects can be called by reference because its value cannot be changed anyways.

Ways to execute Python code: exec, eval, ast, code, codeop, etc.
The exec(object, globals, locals) method executes the dynamically created program, which is either a string or a code object. Returns None. Only side effect matters!

Example 1:

program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
Sum = 15
Example 2:

globals_parameter = {'__builtins__' : None}
locals_parameter = {'print': print, 'dir': dir}
exec('print(dir())', globals_parameter, locals_parameter)
['dir', 'print']
The eval(expression, globals=None, locals=None) method parses the expression passed to this method and runs python expression (code) within the program. Returns the value of expression!

>>> a = 5
>>> eval('37 + a')   # it is an expression
42
>>> exec('37 + a')   # it is an expression statement; value is ignored (None is returned)
>>> exec('a = 47')   # modify a global variable as a side effect
>>> a
47
>>> eval('a = 47')  # you cannot evaluate a statement
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    a = 47
      ^
SyntaxError: invalid syntax
If a code object (which contains Python bytecode) is passed to exec or eval, they behave identically, excepting for the fact that exec ignores the return value, still returning None always. So it is possible use eval to execute something that has statements, if you just compiled it into bytecode before instead of passing it as a string:

>>> eval(compile('if 1: print("Hello")', '<string>', 'exec'))
Hello
>>>
Abstract Syntax Trees, ASTs, are a powerful feature of Python. You can write programs that inspect and modify Python code, after the syntax has been parsed, but before it gets compiled to byte code. That opens up a world of possibilities for introspection, testing, and mischief.

In addition to compiling source code to bytecode, compile supports compiling abstract syntax trees (parse trees of Python code) into code objects; and source code into abstract syntax trees (the ast.parse is written in Python and just calls compile(source, filename, mode, PyCF_ONLY_AST)); these are used for example for modifying source code on the fly, and also for dynamic code creation, as it is often easier to handle the code as a tree of nodes instead of lines of text in complex cases.

The code module provides facilities to implement read-eval-print loops in Python. Two classes and convenience functions are included which can be used to build applications which provide an interactive interpreter prompt.

The codeop module provides utilities upon which the Python read-eval-print loop can be emulated, as is done in the code module. As a result, you probably don't want to use the module directly; if you want to include such a loop in your program you probably want to use the code module instead.

Advanced differences between 2.x and 3.x in general
Division operator
If we are porting our code or executing python 3.x code in python 2.x, it can be dangerous if integer division changes go unnoticed (since it doesn't raise any error). It is preferred to use the floating value (like 7.0/5 or 7/5.0) to get the expected result when porting our code.

print function
This is the most well-known change. In this, the print keyword in Python 2.x is replaced by the print() function in Python 3.x. However, parentheses work in Python 2 if space is added after the print keyword because the interpreter evaluates it as an expression.

Unicode
In Python 2, an implicit str type is ASCII. But in Python 3.x implicit str type is Unicode.

xrange
xrange() of Python 2.x doesn't exist in Python 3.x. In Python 2.x, range returns a list i.e. range(3) returns [0, 1, 2] while xrange returns a xrange object i. e., xrange(3) returns iterator object which works similar to Java iterator and generates number when needed.

Error Handling
There is a small change in error handling in both versions. In python 3.x, 'as' keyword is required.

_future_ module
The idea of the future module is to help migrate to Python 3.x. If we are planning to have Python 3.x support in our 2.x code, we can use future imports in our code.

Six
Six is a Python 2 and 3 compatibility library. It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions. See the documentation for more information on what is provided.

deepcopy, method copy, slicing, etc.
The copy() returns a shallow copy of list and deepcopy() return a deep copy of list. Python slice() function returns a slice object.

A sequence of objects of any type(string, bytes, tuple, list or range) or the object which implements __getitem__() and __len__() method then this object can be sliced using slice() method.

OrderedDict, DefaultDict
An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted.

Important note for Python 3.7+: Since Python 3.7, regular dict objects are guaranteed to maintain insertion order as part of the language specification. However, OrderedDict still provides additional features:

Feature	dict	OrderedDict
Equality comparison	Order-independent	Order-sensitive (two OrderedDicts with same items but different order are not equal)
move_to_end(key, last=True/False)	Not available	Moves key to either end efficiently
popitem(last=True/False)	Only pops from the end (LIFO)	Can pop from either end (LIFO or FIFO)
Memory usage	Lower	Higher
Reordering performance	Not optimized	Optimized for frequent reordering
Use OrderedDict when you need order-sensitive equality checks, move_to_end(), or bidirectional popitem().

Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

from collections import defaultdict

def def_value():
    return "Not Present"

d = defaultdict(def_value) переведи это. Но оставь в том же формате что бы я могла добавить это в мд файл в гит

ChatGPT сказал:
Ок — я переведу, сохранив структуру и формат, чтобы ты могла просто вставить это в .md файл.

Профилирование памяти
Детерминированное профилирование vs статистическое профилирование

pyinstrument

resource module

context managers: contextlib decorator, with-enabled class

Unit testing в Python
Mock objects

Coverage

nosetests, doctests

Управление памятью в Python
3 поколения GC

module gc

Какие типы объектов отслеживаются

Рекомендации по использованию GC

Утечки памяти / проблемы с deleters

Threading и multiprocessing в Python
GIL
Определение

Алгоритмы в Python 2.x и 3.x

Потоки
modules: thread, threading

class Queue

locks

Процессы
multiprocessing

Process

Queue

Pipe

Value

Array

Pool

Manager

Как избежать ограничений GIL
C extensions

Распространение и документация Python-пакетов
distutils, setup.py

публикация кода

автогенерация документации:

sphinx

pydoc

Взаимодействие Python и C
C extension API

вызов C из Python

вызов Python из C

cffi, swig, SIP, boost-python

Boost

Python tools
Стандартная библиотека Python
Продвинутое знание стандартной библиотеки.

Mutable и Immutable объекты
Mutable objects (передача по ссылке)
list

dict

set

bytearray

Immutable objects (передача по значению)
int

float

complex

string

tuple

frozenset

bytes

Особенности
Python по-разному работает с mutable и immutable объектами.

Immutable объекты быстрее читаются.

Mutable объекты удобны, когда нужно менять размер структуры (list, dict).

Immutable объекты используются, когда значение не должно изменяться.

Изменение immutable объекта требует создания копии.

Изменение mutable объекта дешёвое.

Передача объектов в функции
Важно понимать разницу между mutable и immutable типами и как они передаются в функции.

Если mutable объект передаётся по ссылке — функция может изменить оригинальный объект.

Чтобы этого избежать — нужно сделать копию.

Immutable объекты можно передавать безопасно, потому что их значение нельзя изменить.

Способы выполнения Python-кода
exec

eval

ast

code

codeop

exec
exec(object, globals, locals)
Выполняет программу (строку или code object).
Возвращает None.

Example
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
Sum = 15
Example
globals_parameter = {'__builtins__' : None}
locals_parameter = {'print': print, 'dir': dir}
exec('print(dir())', globals_parameter, locals_parameter)
['dir', 'print']
eval
eval(expression, globals=None, locals=None)
Выполняет выражение и возвращает значение.

a = 5
eval('37 + a')
42
exec('37 + a')
exec('a = 47')
a
47
eval('a = 47')
SyntaxError
compile + eval
eval(compile('if 1: print("Hello")', '<string>', 'exec'))
Hello
AST (Abstract Syntax Trees)
AST позволяет:

анализировать код

изменять код до компиляции

делать introspection

генерировать код динамически

ast.parse(source)
code module
Позволяет создавать REPL-интерпретатор внутри программы.

codeop module
Утилиты для REPL (обычно используется через code).

Различия Python 2.x и 3.x
Деление
В Python 2:

7 / 5 = 1
В Python 3:

7 / 5 = 1.4
print
Python 2:

print "hello"
Python 3:

print("hello")
Unicode
Python 2 → str = ASCII
Python 3 → str = Unicode

xrange
Python 2:

range() → список

xrange() → iterator

Python 3:

только range()

Обработка ошибок
Python 3 требует as:

except Exception as e:
future
Помогает миграции на Python 3.

six
Библиотека совместимости Python 2 и 3.

Копирование объектов
copy() → shallow copy

deepcopy() → deep copy

slice()

OrderedDict и DefaultDict
OrderedDict
Сох


Вы сказали:
На Украинский  но для терминов в скобках дописываю англ перевод

ChatGPT сказал:
Ок — зроблю український переклад, зберігши структуру для Markdown, і додам англійські терміни в дужках там, де це важливо.

Профілювання пам’яті (Memory profiling)
Детерміноване профілювання vs статистичне профілювання (Deterministic vs statistical profiling)

pyinstrument

модуль resource (resource module)

контекстні менеджери (context managers): contextlib decorator, with-enabled class

Модульне тестування в Python (Unit testing in Python)
Mock-об’єкти (Mock objects)

Покриття коду (Coverage)

nosetests, doctests

Керування пам’яттю в Python (Memory management in Python)
3 покоління збирача сміття (3 generations of GC)

модуль gc (gc module)

Які типи об’єктів відстежуються (Which type of objects are tracked)

Рекомендації щодо використання GC (recommendations for GC usage)

Витоки пам’яті / проблеми з deleters (Memory leaks / deleter issues)

Threading і multiprocessing у Python
GIL (Global Interpreter Lock)
Визначення (Definition)

Алгоритми в Python 2.x і 3.x

Потоки (Threads)
модулі thread, threading

клас Queue

блокування (locks)

Процеси (Processes)
multiprocessing

Process

Queue

Pipe

Value

Array

Pool

Manager

Як обійти обмеження GIL
C-розширення (C extensions)

Дистрибуція і документація Python-проєктів (Distributing and documentation in Python)
distutils, setup.py

публікація коду (code publishing)

автогенерація документації (Documentation autogeneration):

sphinx

pydoc

Взаємодія Python і C (Python and C interaction)
API C-розширень (C extension API)

виклик C з Python (call C from Python)

виклик Python з C (call Python from C)

cffi, swig, SIP, boost-python

Boost

Mutable і Immutable об’єкти (Mutable and Immutable Objects)
Mutable-об’єкти (передача за посиланням / call by reference)
list

dict

set

bytearray

Immutable-об’єкти (передача за значенням / pass by value)
int

float

complex

string

tuple

frozenset

bytes

Особливості (Features)
Python по-різному працює з mutable і immutable об’єктами.

Immutable-об’єкти швидші для доступу.

Mutable-об’єкти зручно використовувати, коли потрібно змінювати розмір структури (list, dict).

Immutable-об’єкти використовуються, коли значення не повинно змінюватися.

Зміна immutable-об’єкта потребує створення копії.

Зміна mutable-об’єкта є дешевою операцією.

Передача об’єктів у функції (How objects are passed to functions)
Важливо розуміти різницю між mutable і immutable типами та як вони передаються у функції.

Якщо mutable-об’єкт передається за посиланням — функція може змінити оригінальний об’єкт.

Щоб цього уникнути — потрібно створити копію.

Immutable-об’єкти можна передавати безпечно, оскільки їх значення не може бути змінене.

Виконання Python-коду (Ways to execute Python code)
exec

eval

ast

code

codeop

exec
exec(object, globals, locals)
Виконує програму (рядок або code object).
Повертає None.

eval
eval(expression, globals=None, locals=None)
Виконує вираз (expression) і повертає значення.

AST (Abstract Syntax Trees)
AST дозволяє:

аналізувати код (inspect code)

змінювати код до компіляції (modify code before compilation)

виконувати інтроспекцію (introspection)

динамічно генерувати код (dynamic code generation)

code module
Дозволяє створювати інтерактивний інтерпретатор (REPL) у програмі.

codeop module
Утиліти для реалізації REPL.

Відмінності Python 2.x і 3.x (Advanced differences between 2.x and 3.x)
Ділення (Division operator)
Python 2:

7 / 5 = 1
Python 3:

7 / 5 = 1.4
print function
Python 2:

print "hello"
Python 3:

print("hello")
Unicode
Python 2 → str = ASCII
Python 3 → str = Unicode

xrange
Python 2:

range() → список

xrange() → ітератор

Python 3:

тільки range()

Error handling
Python 3 вимагає:

except Exception as e:
future module
Допомагає переходу на Python 3.

six
Бібліотека сумісності Python 2 і 3.

Копіювання об’єктів (Copying objects)
copy() — shallow copy

deepcopy() — deep copy

slice()

OrderedDict і DefaultDict
OrderedDict
OrderedDict — це підклас словника, який зберігає порядок вставки ключів.

Починаючи з Python 3.7, звичайний dict також зберігає порядок вставки, але OrderedDict має додаткові можливості:

order-sensitive equality

move_to_end()

popitem(last=True/False)

оптимізоване перевпорядкування

defaultdict
defaultdict — це підклас dict, який ніколи не викликає KeyError і повертає значення за замовчуванням.

from collections import defaultdict

def def_value():
    return "Not Present"

d = defaultdict(def_value)
Якщо хочеш, я можу:

перетворити це в гарно структурований README.md

зробити короткий конспект для співбесіди

або додати приклади коду для кожної теми.


Вы сказали:
Давай перетворити це в гарно структурований README.md. Но не все в начиная с типов данных
То что до этого пропусти 

ChatGPT сказал:
Добре — зробимо це як README.md, починаючи з типів даних (mutable / immutable) і далі.
Ти зможеш просто вставити це у файл README.md.

Python Notes — Data Types, Execution, and Collections
Mutable and Immutable Objects
Mutable objects (call by reference)
Mutable-об’єкти можна змінювати після створення.

Приклади:

list

dict

set

bytearray

a = [1, 2]
b = a
b.append(3)

print(a)  # [1, 2, 3]
Immutable objects (pass by value)
Immutable-об’єкти не можна змінити після створення.

Приклади:

int

float

complex

str

tuple

frozenset

bytes

x = 5
y = x
y += 1

print(x)  # 5
Key differences
Python по-різному працює з mutable та immutable об’єктами.

Immutable-об’єкти швидші для доступу.

Mutable-об’єкти зручно використовувати для структур змінного розміру.

Зміна immutable-об’єкта створює новий об’єкт.

Зміна mutable-об’єкта змінює існуючий.

Passing objects to functions
Mutable-об’єкти можуть змінюватися всередині функції.

def add_item(lst):
    lst.append(10)

numbers = [1, 2]
add_item(numbers)

print(numbers)  # [1, 2, 10]
Щоб уникнути цього:

def add_item(lst):
    lst = lst.copy()
    lst.append(10)
    return lst
Executing Python Code
exec()
exec(object, globals=None, locals=None)
Виконує Python-код зі строки або code object.
Повертає None.

program = 'a = 5\nb = 10\nprint(a + b)'
exec(program)
eval()
eval(expression, globals=None, locals=None)
Виконує вираз і повертає значення.

a = 5
result = eval("a + 10")
print(result)
compile()
Можна компілювати:

source → bytecode

AST → code object

code_obj = compile('print("Hello")', '<string>', 'exec')
exec(code_obj)
AST (Abstract Syntax Trees)
AST дозволяє:

аналізувати код

змінювати код до компіляції

генерувати код

import ast
tree = ast.parse("x = 5")
print(ast.dump(tree))
code module
Дозволяє створити REPL-інтерпретатор.

codeop module
Допоміжний модуль для реалізації REPL.

Copying Objects
Shallow copy
import copy
copy.copy(obj)
або

lst.copy()
Deep copy
copy.deepcopy(obj)
Slicing
new_list = old_list[:]
OrderedDict and defaultdict
OrderedDict
from collections import OrderedDict
Зберігає порядок вставки елементів.

Навіть якщо dict у Python 3.7+ зберігає порядок,
OrderedDict має додаткові можливості:

order-sensitive equality

move_to_end()

popitem(last=True/False)

ефективне перевпорядкування

defaultdict
from collections import defaultdict
Ніколи не викликає KeyError.

from collections import defaultdict

def def_value():
    return "Not Present"

d = defaultdict(def_value)
print(d["missing"])
slice()
Функція slice() створює slice-object.

Працює з:

string

list

tuple

bytes

range

об’єктами з __getitem__() і __len__()

s = slice(1, 5, 2)
print([0, 1, 2, 3, 4, 5][s])

