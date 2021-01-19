### Числа Фибоначи

F1 = F2 = 1, Fn = Fn-1 + Fn-2, при n > 2


### Мячик на лесенке

На вершине лесенки, содержащей N ступенек, находится мячик, который начинает прыгать по ним вниз, к основанию. Мячик может прыгнуть на следующую ступеньку, на ступеньку через одну или через 2. (То есть, если мячик лежит на 8-ой ступеньке, то он может переместиться на 5-ую, 6-ую или 7-ую.) Определить число всевозможных "маршрутов" мячика с вершины на землю.


### Последовательность из 0 и 1

Требуется подсчитать количество последовательностей длины N, состоящих из 0 и 1, в которых никакие две единицы не стоят рядом.


### Калькулятор и Калькулятор с восстановлением ответа

Имеется калькулятор, который выполняет три операции:

Прибавить к числу X единицу.

Умножить число X на 2.

Умножить число X на 3.

Определите, какое наименьшее число операций необходимо для того, чтобы получить из числа 1 заданное число N.


### Cамый дешевый путь

В каждой клетке прямоугольной таблицы N×M записано некоторое число. Изначально игрок находится в левой верхней клетке. За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо вниз (влево и вверх перемещаться запрещено). При проходе через клетку с игрока берут столько килограммов еды, какое число записано в этой клетке (еду берут также за первую и последнюю клетки его пути).

Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.


### Ход конем

Дана прямоугольная доска N × M (N строк и M столбцов). В левом верхнем углу находится шахматный конь, которого необходимо переместить в правый нижний угол доски. При этом конь может ходить ТОЛЬКО на две клетки вниз и на одну клетку вправо, либо на две клетки вправо и на одну клетку вниз.

Необходимо определить, сколько существует различных маршрутов, ведущих из левого верхнего в правый нижний угол.


### Наибольшая общая подпоследовательность (НОП)

Даны две последовательности, требуется найти длину их наибольшей общей подпоследовательности.


### Скобки

Вывести все правильные скобочные выражения длиной N, состоящие из круглых и квадратных скобок.


### Построить из строки следующую анаграмму

Для данного слова (последовательности строчных латинских букв) выведите следующее за ним (в лексикографическом порядке) слово, которое может быть получено из данного перестановкой букв (анаграмму). Если данное слово уже является последним среди всех своих анаграмм, то необходимо вывести первую возможную (в лексикографическом порядке) анаграмму.


### Префикс-функция

Дана непустая строка S, длина которой N не превышает 106. Будем считать, что элементы строки нумеруются от 1 до N.

Для каждой позиции i символа в строке нас будет интересовать подстрока, заканчивающаяся в этой позиции, и совпадающая с некоторым началом всей строки. Вообще говоря, таких подстрок будет несколько, не меньше двух. Самая длинная из них имеет длину i, она нас интересовать не будет. А будет нас интересовать самая длинная из остальных таких подстрок (заметим, что такая подстрока всегда существует — в крайнем случае, если ничего больше не найдется, сгодится пустая подстрока).

Значением префикс-функции π[i] будем считать длину этой подстроки.

Префикс-функция используется в различных алгоритмах обработки строк. В частности, с её помощью можно быстро решать задачу о поиске вхождения одной строки в другую («поиск образца в тексте»).

Требуется для всех i от 1 до N вычислить π[i].


### Z-функция

Дана непустая строка s, длина которой N не превышает 106. Будем считать, что элементы строки нумеруются от 1 до N.

Для каждой позиции i символа в строке определим Z-блок как наибольшую подстроку, которая начинается в этой позиции и совпадает с некоторым началом всей строки s. Значением Z-функции Z(i) будем считать длину этого Z-блока. (Заметим, что для первой позиции строки  Z-блок совпадает со всей строкой, поэтому Z(1)=N. С другой стороны, если s[i]≠s[1], то Z(i)=0).

Z-функция используется в различных алгоритмах обработки строк. В частности, с её помощью можно быстро решать задачу о поиске вхождения одной строки в другую («поиск по образцу»).

Требуется для всех i от 1 до N вычислить Z(i).


### Поиск подстроки

Найти все вхождения строки T в строку S.


### Компоненты связности

Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их.


### Путь в графе

В неориентированном графе требуется найти минимальный путь между двумя вершинами.


### Дейкстра: восстановление пути

Дан ориентированный взвешенный граф. Найдите кратчайший путь от одной заданной вершины до другой.


### Есть ли цикл?

Дан ориентированный граф. Требуется определить, есть ли в нем цикл.


### Баобаб

Дан неориентированный невзвешенный граф. Необходимо определить, является ли он деревом.


### Обратная польская запись

В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B + C) * D.

Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.

Дано выражение в постфиксой записи, содержащее однозначные числа, операции +, –, \*. Вычислите значение записанного выражения.