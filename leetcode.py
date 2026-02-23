
"""
REMOVE DUPLICATES FROM SORTED ARRAY
(26. Remove Duplicates from Sorted Array) +

Задача:
Дано відсортований у неспадному порядку масив цілих чисел nums.
Потрібно видалити дублікати "на місці" (in-place) так, щоб кожен
унікальний елемент з’являвся лише один раз.

Повернути кількість унікальних елементів k.
Перші k елементів масиву nums повинні містити унікальні значення.
Елементи після k можна ігнорувати.

Приклад:
nums = [1, 1, 2, 2, 3]
Результат:
k = 3
nums = [1, 2, 3, ...]

Ідея:
Оскільки масив відсортований, дублікати стоять поруч.
Використовуємо підхід "двох вказівників":

i — проходить по масиву
k — позиція для запису наступного унікального елемента

Алгоритм:
1. Перший елемент завжди унікальний → k = 1
2. Проходимо масив з другого елемента
3. Якщо nums[i] != nums[i - 1]:
      nums[k] = nums[i]
      k += 1
4. Повертаємо k

Складність:
Time: O(n)
Space: O(1)
"""


def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k



"""
(122. Best Time to Buy and Sell Stock II)  +
Дано масив цілих чисел prices, де prices[i] — це ціна акції в i-й день.

Кожного дня ви можете вирішити купити і/або продати акцію.
При цьому:
ви можете володіти не більше ніж однією акцією одночасно
можна купувати й продавати акцію багато разів
дозволяється продати і знову купити в той самий день, якщо ви не володієте більше ніж однією акцією

Потрібно знайти і повернути максимальний прибуток, який можна отримати.

Приклад 1
Input: prices = [7,1,5,3,6,4]
Output: 7

Приклад 2
Input: prices = [1,2,3,4,5]
Output: 4

Приклад 3
Input: prices = [7,6,4,3,1]
Output: 0

Як це працює
Приклад:
prices = [7,1,5,3,6,4]
Різниці між днями:
1 - 7 = -6
5 - 1 = +4
3 - 5 = -2
6 - 3 = +3
4 - 6 = -2
Беремо лише позитивні:
4+3=7
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
            


"""
(189. Rotate Array)
Дано масив цілих чисел nums. Потрібно зсунути масив вправо на k кроків, де k — невід’ємне число.

Елементи, які “виходять” за правий край масиву, повинні переноситися на початок.

Приклад 1
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Приклад 2
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]



"""
(217. Contains Duplicate)
Дано цілий масив nums. Поверніть True, якщо будь-яке значення з’являється в масиві щонайменше двічі, і поверніть Fals якщо всі елементи є різними.

 Приклад 1:
 Вхід: nums = [1, 2, 3, 1]
 Вихід: True

Пояснення:
Елемент 1 зустрічається за індексами 0 і 3.

Приклад 2:
Вхід: nums = [1, 2, 3, 4]
Вихід: False

Пояснення:
Усі елементи різні.

Приклад 3:
Вхід: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Вихід: True
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)



"""
(136. Single Number)   doublecheck
Дано непорожній масив цілих чисел nums, у якому кожен елемент з’являється двічі, окрім одного. Знайдіть цей єдиний елемент.
Потрібно реалізувати розв’язок із лінійною складністю часу та використовувати лише сталий обсяг додаткової пам’яті.

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result
            

"""
(350. Intersection of Two Arrays II)  check
Дано два масиви цілих чисел nums1 і nums2. Поверніть масив їхнього перетину.
Кожен елемент у результаті має з’являтися стільки разів, скільки він зустрічається в обох масивах.
Результат можна повертати в будь-якому порядку.

Приклад 1:
Вхід:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
Вихід:
[2, 2]

Приклад 2:
Вхід:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
Вихід:
[4, 9]

Пояснення:
[9, 4] також є правильним результатом.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        result = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if counts.get(num, 0) > 0:
                result.append(num)
                counts[num] -= 1

        return result



"""
(66. Plus One)  check
Вам дано велике ціле число, представлене у вигляді масиву цілих чисел digits, де digits[i] — це i-та цифра числа.
Цифри розташовані від найстаршого розряду до наймолодшого зліва направо.
Велике число не містить початкових нулів.

Збільште це число на один і поверніть отриманий масив цифр.

Приклад 1:

Вхід:
digits = [1, 2, 3]

Вихід:
[1, 2, 4]
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1

            if digits[i] < 10:
                return digits

            digits[i] = 0

        return [1] + digits



"""
(283. Move Zeroes)  check
Move Zeroes
Условие:
Дан массив nums. Нужно переместить все нули в конец массива сохранив порядок ненулевых элементов.
Решение должно быть in-place (без создания копии массива).
Идея решения:
Используем два указателя.
insert_pos — позиция, куда записываем следующий ненулевой элемент.

Алгоритм:
1. Проходим по массиву.
2. Если элемент != 0 → записываем его в nums[insert_pos].
3. Увеличиваем insert_pos.
4. После прохода заполняем оставшиеся элементы нулями.

"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        for i in range(insert_pos, len(nums)):
            nums[i] = 0


"""
(1. Two Sum)
Дано масив цілих чисел nums і ціле число target.
Поверніть індекси двох чисел так, щоб їх сума дорівнювала target.
Можна вважати, що для кожного вхідного набору даних існує рівно один розв’язок, і не можна використовувати один і той самий елемент двічі.
Відповідь можна повернути в будь-якому порядку.

Приклад:
Вхід:
nums = [2, 7, 11, 15], target = 9
Вихід:
[0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i


"""
(36. Valid Sudoku)

Визначте, чи є коректною дошка **Sudoku 9 × 9**.
Перевіряти потрібно **лише заповнені клітинки** відповідно до таких правил:

Кожен **рядок** має містити цифри **1–9 без повторень**.
Кожен **стовпець** має містити цифри **1–9 без повторень**.
Кожен із **дев’яти підквадратів 3 × 3** має містити цифри **1–9 без повторень**.

---
Примітка:**
Дошка Sudoku (частково заповнена) може бути коректною, але не обов’язково розв’язуваною.
Перевіряти потрібно лише заповнені клітинки відповідно до наведених правил.

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if value in rows[r]:
                    return False
                if value in cols[c]:
                    return False
                if value in boxes[box_index]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)

        return True


"""
(48. Rotate Image)

Дано квадратну двовимірну матрицю **n × n**, що представляє зображення.
Потрібно **повернути зображення на 90° за годинниковою стрілкою**.

Поворот потрібно виконати **in-place**, тобто змінити **вхідну матрицю без створення нової**.

**Не можна створювати іншу 2D-матрицю для повороту.**

---

### Приклад

**Вхід:**

```
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
```

**Вихід:**

```
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
]
```

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()










