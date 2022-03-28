# Find a Peak Element II, do LeetCode
# link: https://leetcode.com/problems/find-a-peak-element-ii/

from typing import List

# A resposta comeca aqui

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # armazeno a primeira e a ultima coluna da matriz
        primeiraColuna = 0
        ultimaColuna = len(mat[0])-1

        while primeiraColuna <= ultimaColuna:
            # comeco a busca pela coluna do meio
            auxColuna = int((primeiraColuna + ultimaColuna)/2)
            maiorColuna = 0

            # armezena o maior valor da coluna
            for x in range(len(mat)):
                if mat[x][auxColuna] >= mat[maiorColuna][auxColuna]:
                    maiorColuna = x

            # declara o valor da direita e esquerda como menor
            esquerdaMaior = False
            direitaMaior = False

            # se nao é a primeira coluna e o valor da esquerda é maior, esquerdaMaior vira true
            if auxColuna-1 >= primeiraColuna and mat[maiorColuna][auxColuna-1] > mat[maiorColuna][auxColuna]:
                esquerdaMaior = True
            # se nao é a ultima coluna e o valor da direita é maior, direitaMaior vira true
            if auxColuna+1 <= ultimaColuna and mat[maiorColuna][auxColuna+1] > mat[maiorColuna][auxColuna]:
                direitaMaior = True

            # se o valor da esquerda e direita nao é maior, ja achamos o peak element
            if not direitaMaior and not esquerdaMaior:
                return [maiorColuna,auxColuna]
            # se o valor da esquerda é maior, atualiza a ultima coluna
            elif esquerdaMaior:
                ultimaColuna = auxColuna-1
            else:
            # se o valor da direita é maior, atualiza a primeira coluna
                primeiraColuna = auxColuna+1
            
        return []

# A resposta termina aqui

if __name__ == '__main__':
    mat = [[41,8,2,48,18],[16,15,9,7,44],[48,35,6,38,28],[3,2,14,15,33],[39,36,13,46,42]]
    x = Solution
    print(x.findPeakGrid(x, mat))