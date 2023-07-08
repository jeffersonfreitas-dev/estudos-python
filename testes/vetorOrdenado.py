import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
      if self.ultima_posicao == -1:
         print("O vetor está vazio")
      else:
         for i in range(self.ultima_posicao + 1):
            print(i, " - ", self.valores[i])


    def insere(self, valor):
      if self.ultima_posicao == self.capacidade -1:
         print("Capacidade máxima atingida")
         return
      
      #Encontrando a posição para inserir no array. Se o valor no array for maior que o valor informado é feito um break para recuperar a posição
      posicao_para_inserir = 0
      for i in range(self.ultima_posicao + 1):
         posicao_para_inserir = i
         if self.valores[i] > valor:
            break
         if i == self.ultima_posicao:
            posicao_para_inserir = i+1
      
      #Após encontrar a posicao para inserir, deve remanejar os valores para abrir espaço para inclusão do novo valor
      ultima_posicao_array = self.ultima_posicao
      while ultima_posicao_array >= posicao_para_inserir:
         self.valores[ultima_posicao_array + 1] = self.valores[ultima_posicao_array]
         ultima_posicao_array -= 1
      
      self.valores[posicao_para_inserir] = valor
      self.ultima_posicao += 1


##### TESTANDO
vetor  = VetorOrdenado(10)
vetor.imprime()

vetor.insere(6)
vetor.imprime()

vetor.insere(4)
vetor.imprime()

vetor.insere(3)
vetor.imprime()

vetor.insere(5)
vetor.imprime()

vetor.insere(1)
vetor.imprime()