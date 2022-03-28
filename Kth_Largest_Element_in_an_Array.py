# Resolve a questão Kth Largest Element in an Array, do juiz online LeetCode
# Nível: Médio
# Link: leetcode.com/problems/kth-largest-element-in-an-array

def mergeSort(arr):

    if len(arr) > 1:

        mid = len(arr)//2   # Encontra o meio do array, dividindo-o em dois

        L = arr[:mid]       # Seleciona a metade esquerda do array
        R = arr[mid:]       # Seleciona a metade direita do array

        # Chama a função recursivamente para as duas metades
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0       # Inicializa iteradores

        # Realiza o merge, rearmazenando os itens divididos no array original conforme sua ordenação
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Rearmazena os itens que sobraram, caso existam
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


class Solution(object):

    def findKthLargest(nums, k):

        # A ideia aqui é encontrar o k-ésimo maior elemento;
        # Para isso, primeiramente precisamos ordenar;
        # Faremos isso utilizando o algoritmo mergeSort, que exercita a ordenação por meio do paradigma Dividir e Conquistar.
        mergeSort(nums)

        # Então aqui
        tam = len(nums)
        kth = tam - k

        return nums[kth]


print(Solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(Solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
