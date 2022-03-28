# Find a Peak Element II, do LeetCode
# link: https://leetcode.com/problems/find-a-peak-element-ii/

from typing import List

# A resposta comeca aqui

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        primeiraColuna = 0
        ultimaColuna = len(mat[0])-1

        while primeiraColuna <= ultimaColuna:
            auxColuna = int((primeiraColuna + ultimaColuna)/2)
            maiorColuna = 0

            for x in range(len(mat)):
                if mat[x][auxColuna] >= mat[maiorColuna][auxColuna]:
                    maiorColuna = x

            esquerdaMaior = False
            direitaMaior = False

            if auxColuna-1 >= primeiraColuna and mat[maiorColuna][auxColuna-1] > mat[maiorColuna][auxColuna]:
                esquerdaMaior = True
            if auxColuna+1 <= ultimaColuna and mat[maiorColuna][auxColuna+1] > mat[maiorColuna][auxColuna]:
                direitaMaior = True

            if not direitaMaior and not esquerdaMaior:
                return [maiorColuna,auxColuna]
            elif direitaMaior:
                ultimaColuna = auxColuna-1
            else:
                primeiraColuna = auxColuna+1
            
        return []

# A resposta termina aqui

if __name__ == '__main__':
    mat = [[41,8,2,48,18],[16,15,9,7,44],[48,35,6,38,28],[3,2,14,15,33],[39,36,13,46,42]]
    x = Solution
    print(x.findPeakGrid(x, mat))