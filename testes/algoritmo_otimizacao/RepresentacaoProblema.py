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