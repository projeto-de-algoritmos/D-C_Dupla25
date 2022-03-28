# Resolve a questão Super Pow, do juiz online LeetCode
# Nível: Médio
# Link: leetcode.com/problems/super-pow/

# Para resolver esta questão, o paradigma Dividir e Conquistar é essencial,
# visto que calcular exponenciações com valores de potência pequenos, como de 4
# casas já causam provavelmente overflow, pelo tamanho dos valores gerados. É fato
# que o problema tem noção disso, já que propõe um cálculo de A^B mod C. Entretanto
# o problema não explicita o meio do caminho do cálculo, e é aí que o overflow irá
# acontecer, já que antes de gerarmos o valor modular "pequeno", teoricamente
# necessitaria de gerar antes o A^B.
# Assim, uma solução para isso é utilizar uma propriedade da exponenciação modular,
# que diz:
# (m * n) % p =((m % p) * (n % p)) % p
# Usando de tal propriedade, podemos considerar a aplicação do DeC, no sentido que
# podemos dividir a exponenciação em pequenas partes já calculando o seu módulo antes
# de se tornar um valor muito grande, em que por exemplo:
# 2^90 mod 13 = (2^50 * 2^40) mod 13
# 2^90 mod 13 = (2^50 mod 13 * 2^40 mod 13) mod 13
# Logo, para este problema, podemos utilizar a seguinte lógica:
# Se o valor da potência (b) é par, então: (a^b) % c = ((a^(b/2))*(a^(b/2))) % c
# Se o valor da potência (b) é impar, então: (a^b) % c = (a*(a^(b-1)) % c

def powDC(a, b, mod):

    # Casos-base
    if a == 0:
        return 0
    if b == 0:
        return 1

    # variável auxiliar
    x = 0

    # Se b é par
    if b % 2 == 0:

        # (a^b) % c = ((a^(b/2))*(a^(b/2))) % c
        x = powDC(a, b/2, mod)

        return (x * x) % mod

    # Se b é ímpar
    else:

        # Há o módulo de a pela distributiva no 1º membro
        x = a % mod

        # (a^b) % c = (a*(a^(b-1)) % c
        return (x * powDC(a, b-1, mod) % mod) % mod


class Solution(object):

    def superPow(self, a, b):

        # Une os valores de entrada de b em um único int
        for i in range(len(b)):
            b[i] = str(b[i])
        b = ''.join(b)
        b = int(b)

        res = powDC(a, b, 1337)

        return res
