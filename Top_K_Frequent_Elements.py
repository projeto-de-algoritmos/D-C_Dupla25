# Find a Peak Element II, do LeetCode
# link: https://leetcode.com/problems/find-a-peak-element-ii/

from ast import operator
from operator import itemgetter
from typing import List
from urllib import response

# A resposta comeca aqui

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resposta = []
        frequencia = {}
        # contabiliza a frequencia de cada numero
        for x in nums:
            # caso ja tenha aparecido incrementa 1 naquela posicao
            if x in frequencia:
                frequencia[x] = frequencia[x] + 1
            # caso se a primeira vez que aparece inicializa
            else:
                frequencia[x] = 1

        # ordena de acordo com a frequencia
        sort = sorted(frequencia.items(), key = lambda elem:elem[1], reverse = True)
        count = 0

        # armazena os K numeros mais frequentes
        for i in sort:
            if count < k:
                resposta.append(i[0])
                count += 1
            else:
                break
        return resposta
        

# A resposta termina aqui

if __name__ == '__main__':
    nums = [1,1,1,2,2,3,1,3,2,4,2,3,1]
    k = 2
    x = Solution
    print(x.topKFrequent(x, nums, k))