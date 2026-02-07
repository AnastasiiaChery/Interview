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


