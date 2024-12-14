import time
from ._game import Sudoku

if __name__ == '__main__':
    model = [
        [0, 0, 8, 0, 1, 0, 0, 0, 9],
        [6, 0, 1, 0, 9, 0, 3, 2, 0],
        [0, 4, 0, 0, 3, 7, 0, 0, 5],
        [0, 3, 5, 0, 0, 8, 2, 0, 0],
        [0, 0, 2, 6, 5, 0, 8, 0, 0],
        [0, 0, 4, 0, 0, 1, 7, 5, 0],
        [5, 0, 0, 3, 4, 0, 0, 8, 0],
        [0, 9, 7, 0, 8, 0, 5, 0, 6],
        [1, 0, 0, 0, 6, 0, 9, 0, 0]
    ]

    start = time.time()
    s = Sudoku(model)
    
    print("Entrada: ")
    s.display()
    if s.solve():
        print("\nSolução: ")
        s.display()

    else:
        print('\nnão foi possível encontrar uma solução válida!')

    duration = time.time() - start

    print(f'Duração {duration:.4f}s')