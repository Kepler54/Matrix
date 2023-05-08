import bext
import threading
from time import sleep
from colorama import Fore
from random import randint
from threading import Thread
from keyboard import press_and_release


class MatrixForWindows:
    v = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    w = ('Ω', 'λ', 'β', 'γ', 'θ', 'π', 'Σ', 'Ψ', '¥', 'ω')
    x = ('@', '№', '#', '%', '&', '§', '?', '₽', '€', '$')
    y = ('j', 'S', 'X', 'Y', 'Z', 'W', 'd', 'x', 'y', 'z')
    z = ('Ё', 'У', 'р', 'Ф', 'q', 'ё', 'R', 'й', 'Ь', 'ю')
    o = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

    locker = threading.Lock()
    maincounter = 0
    stop = False
    horizcoordcounter = 1  # counter and initial horizontal coordinate

    '''Title'''

    @staticmethod
    def title():
        return bext.title("Matrix, version 1.0")

    '''Full screen mode'''

    @staticmethod
    def fullscreen():
        return press_and_release('alt+enter')

    '''Matrix switch'''

    @classmethod
    def breaker(cls):
        input()
        cls.stop = True

    '''Forming a random symbol from the map function'''

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

    '''The function forms a void'''

    def matrixvoid(self):
        f = (self.o[(randint(0, 9))], self.o[(randint(0, 9))])
        return f[randint(0, 1)]

    '''Drop shaping function'''

    def matrixdrop(self, dropheight, horizcoord, coordofthedropbeginn):
        while not self.stop:  # overall process cycle
            for b in range(6):  # drop life cycle
                verticalcoordcounter = coordofthedropbeginn
                self.maincounter += 1  # main cycle counter
                for c in range(randint(0, dropheight)):  # random coordinate of the final drop height
                    verticalcoordcounter += 1  # in each new cycle the drop height is multiplied by 1
                    with self.locker:
                        bext.goto(horizcoord, verticalcoordcounter)  # coordinates of drop width and drop height
                        if self.maincounter % 3 == 0:  # if the number of the main loop is divisible by 0
                            print(f'{Fore.GREEN}{self.matrixvoid()}')  # a void is output
                        else:
                            print(f'{Fore.GREEN}{self.matrixsymbol()}')  # otherwise a droplet is generated
                    sleep(float(f'{0.0}{randint(3, 6)}'))
            self.maincounter = 0

    '''Shaping droplet streams function'''

    def matrixmove(self, coordofthedropbeginn, dropheight):
        bext.hide()
        for q in range(bext.width() // 2):
            Thread(target=MatrixForWindows().matrixdrop,
                   args=(dropheight, self.horizcoordcounter, coordofthedropbeginn)).start()
            self.horizcoordcounter += 2  # pitch between droplet streams
