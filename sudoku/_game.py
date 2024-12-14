from typing import Iterable
import math

__all__ = ['Sudoku']

class Sudoku:
    def __init__(self, matriz:Iterable[Iterable[int]]):
        self.__matriz = matriz
        self.__ordem = len(matriz)
        ordem_bloco = math.sqrt(self.__ordem)

        # verificando se a matriz representa um sudoku valido
        if not ordem_bloco.is_integer():
            raise ValueError('esta matriz não representa um sudoku válido!')

        self.__ordem_bloco = int(ordem_bloco)
        self.__matriz_cols = [[None for _ in range(self.__ordem)] for _ in range(self.__ordem)]

        # dados para exibição da matriz
        self.__len_item = (self.__ordem // 10) + 3
        num_sep = self.__ordem_bloco - 1
        self.__line = '|' + ('-' * ((self.__len_item * self.__ordem) + num_sep)) + '|'

        self.__updateDependences()

    def __getGroupIndexByPosition(self, row:int, col:int):
        return (row - (row % self.__ordem_bloco)) + (col // self.__ordem_bloco)

    def __updateDependences(self):
        """ gera os valores de dependência utilizados nas verificações """
        
        self.__groups = [[] for _ in range(self.__ordem)]

        # armazenando grupos e colunas como lista
        for row, values in enumerate(self.__matriz):
            for col, item in enumerate(values):
                self.__matriz_cols[col][row] = item
                self.__groups[self.__getGroupIndexByPosition(row, col)].append(self.__matriz[row][col])
        

    def __updateMatriz(self, row:int, col:int, value:int):
        if value > self.__ordem:
            raise ValueError('O valor não deve ser superior a ordem da matriz')
        
        self.__matriz[row][col] = value
        self.__updateDependences()
        
    def solve(self) -> bool:
        """ calcula a solução da matriz """

        # analisando possibilidades
        while True:
            
            found = False

            # armazenando conjunto de possibilidades para cada item
            for row in range(self.__ordem):
                for col in range(self.__ordem):

                    # verificando se não é um campo em branco
                    if self.__matriz[row][col] != 0:
                        continue

                    possibilidades = self.getPossibilities(row, col)
                    
                    # caso haja apenas uma possibilidade
                    if len(possibilidades) == 1:
                        self.__updateMatriz(row, col, possibilidades[0])
                        found = True

            if not found:
                break
                
        # verificando se faltam campos
        for row in self.__matriz:
            if 0 in row:
                return False
        
        return True
    
    def display(self):
        print(self.__line)

        count_row = 0
        for row in range(self.__ordem):
            count_row += 1
            print('|', end='')

            count_col = 0
            for col in range(self.__ordem):
                val = self.__matriz[row][col]
                count_col += 1

                print(str(val).center(self.__len_item), end='')
                if count_col == self.__ordem_bloco:
                    print('|', end='')
                    count_col = 0

            print()

            if count_row == self.__ordem_bloco:
                print(self.__line)
                count_row = 0
            

    def getPossibilities(self, index_row:int, index_col:int):
        value = self.__matriz[index_row][index_col]
        if value != 0:
            return [value]

        row = self.__matriz[index_row]
        col =  self.__matriz_cols[index_col]
        group = self.__groups[self.__getGroupIndexByPosition(index_row, index_col)]

        return list(filter(lambda x: x not in row and x not in col and x not in group, range(1, self.__ordem+1)))
