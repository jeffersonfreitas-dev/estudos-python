import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
from RepresentacaoProblema import pessoas
from RepresentacaoProblema import voos
from RepresentacaoProblema import imprimir_voos

destino = 'FCO'
agenda = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3]

def fitness_fuction(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        origem = pessoas[i][1]
        id_voo +=1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
    return total_preco

fitness = mlrose.CustomFitness(fitness_fuction)


# length=12 : Quantidade iteração da agenda, 
# fitness_fn=fitness : função criada acima, 
# maximize=False: Não é o máximo e sim o menor valor (minimo), 
# max_val=10 : Quantidade voos por localidade Ex: 10 voos de Madri para Roma e vice-versa
problema = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)


print("HILL CLIMB--------------")
melhor_solucao, melhor_custo = mlrose.hill_climb(problema)
print(melhor_solucao, melhor_custo)
imprimir_voos(melhor_solucao)

print("SIMULATED ANNELING--------------")
melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema, schedule=mlrose.decay.GeomDecay(init_temp=10000), random_state=1)
print(melhor_solucao, melhor_custo)
imprimir_voos(melhor_solucao)

print("ALGORITMO GERNÉTICO--------------")
# pop_size=500 : Tamanho inicial da população, default 200, 
# mutation_prob=0.2 : 20% de dados que sofrerão mutações (troca), 
melhor_solucao, melhor_custo = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2, random_state=1)
print(melhor_solucao, melhor_custo)
imprimir_voos(melhor_solucao)
