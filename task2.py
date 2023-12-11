"""
Сашко і Оленка грають в гру. Сашко загадав натуральне число від 1 до n.
Оленка намагається вгадати це число, для цього вона називає деякі
послідовності натуральних чисел. Сашко відповідає Оленці YES, якщо серед
названих нею чисел є задумане або NO в іншому випадку. Після декількох
заданих питань Оленка заплуталася в тому, які питання вона задавала і
які відповіді отримала і просить вас допомогти їй визначити, які числа
міг задумати Сашко. Перший рядок вхідних даних містить число n -
найбільше число, яке міг загадати Сашко. Далі йдуть рядки, які містять
питання Оленки. Кожен рядок представляє собою набір чисел, розділених
пропусками. Після кожного рядка з питанням йде відповідь Сашка: YES або
NO. Нарешті, останній рядок вхідних даних містить одне слово HELP. Ви
повинні вивести (через пропуск, в порядку зростання) всі числа, які міг
задумати Сашко.

Автор: Савченко Валентина 31І група
"""
import random

n = int(input("Enter number(the largest number for the list): "))

num = str(random.randint(1, n))
print(num)
num_yes = set()
num_no = set()

while True:
    question = input("Enter your guesses:")
    if question == "HELP":
        break
    numbers = list(question.split())
    if num in numbers:
        print("YES")
        num_yes.update(numbers)
    else:
        print("NO")
        num_no.update(numbers)

guess_all = list(num_yes - num_no)
guess = [int(el) for el in guess_all]
guess.sort()
print(guess)


