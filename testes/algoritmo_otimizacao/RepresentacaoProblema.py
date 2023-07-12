pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destino = 'FCO'

voos = {}

for linha in open('algoritmo_otimizacao/flights.txt'):
    origem, destino, saida, chegada, preco = linha.split(",")
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida, chegada, int(preco)))

#print(voos)
#print(voos['FCO', 'DUB'])

agenda = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3]
#print(agenda[0])

def imprimir_voos(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        nome = pessoas[i][0]
        origem = pessoas[i][1]
        id_voo +=1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
        print("%10s%10s %5s-%5s %3s %5s-%5s %3s" % (nome, origem, ida[0], ida[1], ida[2], volta[0], volta[1], volta[2]))
    print("Preço total: ", total_preco)

imprimir_voos(agenda)

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