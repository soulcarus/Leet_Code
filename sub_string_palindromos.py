class Solution:
    def longestPalindrome(self, s: str) -> str:
        resposta = ''
        contador = 0
        tamanho = len(s)

        for i in range(tamanho):
            esquerda, direita = i, i
            while esquerda >= 0 and direita < tamanho and s[esquerda] == s[direita]:
                if (direita - esquerda + 1) > contador:
                    resposta = s[esquerda:direita+1]
                    contador = direita - esquerda + 1
                esquerda -= 1
                direita += 1
            
            esquerda, direita = i, i + 1
            while esquerda >= 0 and direita < tamanho and s[esquerda] == s[direita]:
                if (direita - esquerda + 1) > contador:
                    resposta = s[esquerda:direita+1]
                    contador = direita - esquerda + 1
                esquerda -= 1
                direita += 1
            
        return resposta


