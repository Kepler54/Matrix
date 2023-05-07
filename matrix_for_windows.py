import bext
from bext import goto
from bext import hide
from time import sleep
from colorama import Fore
from threading import Lock
from random import randint
from threading import Thread


class MatrixForWindows:
    v = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    w = ('Ω', 'λ', 'β', 'γ', 'θ', 'π', 'Σ', 'Ψ', '¥', 'ω')
    x = ('@', '№', '#', '%', '&', '§', '?', '₽', '€', '$')
    y = ('j', 'S', 'X', 'Y', 'Z', 'W', 'd', 'x', 'y', 'z')
    z = ('Ё', 'У', 'р', 'Ф', 'q', 'ё', 'R', 'й', 'Ь', 'ю')
    o = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

    locker = Lock()
    switch = False
    maincounter = 0
    horizcoordcounter = 1  # счетчик и начальная координата по горизонтали

    '''Выключатель матрицы'''

    @classmethod
    def breaker(cls):
        input()
        cls.switch = True

    '''Включатель матрицы'''

    @classmethod
    def runner(cls):
        cls.switch = False

    '''Формирующая случайный символ из картежа функция'''

    def matrixsymbol(self):
        f = (
            self.v[(randint(0, 9))],
            self.w[(randint(0, 9))],
            self.x[(randint(0, 9))],
            self.y[(randint(0, 9))],
            self.z[(randint(0, 9))],
            self.o[(randint(0, 9))]
        )
        return f[randint(0, 5)]

    '''Функция формирует пустоту'''

    def matrixvoid(self):
        f = (self.o[(randint(0, 9))], self.o[(randint(0, 9))])
        return f[randint(0, 1)]

    '''Формирующая каплю функция'''

    def matrixdrop(self, dropheight, horizcoord, coordofthedropbeginn):
        while not self.switch:  # общий цикл процесса
            for b in range(6):  # цикл жизни капли
                verticalcoordcounter = coordofthedropbeginn
                self.maincounter += 1  # счетчик главного цикла
                for c in range(randint(0, dropheight)):  # случайная координата конечной высоты капли
                    verticalcoordcounter += 1  # в каждом новом цикле высота капли умножается на 1
                    with self.locker:
                        goto(horizcoord, verticalcoordcounter)  # координаты ширины и высоты капли
                        if self.maincounter % 3 == 0:  # если число главного цикла делится на 0
                            print(f'{Fore.GREEN}{self.matrixvoid()}')  # выводится пустота
                        else:
                            print(f'{Fore.GREEN}{self.matrixsymbol()}')  # в противном случае генерируется капелька
                    sleep(float(f'{0.0}{randint(3, 6)}'))
            self.maincounter = 0

    '''Формирующая потоки капель функция'''

    def matrixmove(self, coordofthedropbeginn, dropheight, timesleep):
        hide()
        for q in range(bext.width() // 2):
            Thread(
                target=MatrixForWindows().matrixdrop,
                args=(dropheight, self.horizcoordcounter, coordofthedropbeginn, timesleep)
            ).start()
            self.horizcoordcounter += 2  # шаг между потоками капель
