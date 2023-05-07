from os import system
from random import randint
from threading import Thread
from matrix_for_linux import MatrixForLinux
from matrix_for_windows import MatrixForWindows

matrix_linux = MatrixForLinux()
matrix_windows = MatrixForWindows()

if __name__ == '__main__':
    system('cls')
    Thread(target=matrix_windows.runner).start()
    matrix_windows.matrixmove(-1, 30, float(f'{0.0}{randint(6, 9)}'))
    Thread(target=matrix_windows.breaker).start()
    input()
