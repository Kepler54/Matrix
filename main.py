import bext
from time import sleep
from threading import Thread
from matrix_for_linux import MatrixForLinux
from matrix_for_windows import MatrixForWindows

matrix_linux = MatrixForLinux()
matrix_windows = MatrixForWindows()

if __name__ == '__main__':
    matrix_windows.title()
    matrix_windows.fullscreen()
    sleep(0.1)
    matrix_windows.matrixmove(-1, bext.height() - 2)
    Thread(target=matrix_windows.breaker()).start()
