import numpy as np
import skfuzzy as fuzz #pip install scikit-fuzzy & pip install matplotlib
from skfuzzy import control as ctrl

#Antecedente
#Setando o universo de valores para o problema que vai de 0..10 (Notas dos clientes)
qualidade = ctrl.Antecedent(np.arange(0,11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')


#Consequencia
#Setando o universo de valores para o problema que vai de 0 a 20 (% das Gorjetas)
gorjeta = ctrl.Consequent(np.arange(0,21, 1), 'gorjeta')

#Membership functions
#Colocando os valores dos universos em grupos de nomes
qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitavel', 'otimo'])

#Setando as gorjetas onde é informado o inicio, o pico e o fim [x,x,x] no grafico (trimf)
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0,0,7])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [8,10,14])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [15,18,20])

#Definindo as regras
#Se a qualidade da comida for ruim ou o serviço for ruim a gorjeta será baixa e etc
regra01 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra02 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])
regra03 = ctrl.Rule(servico['otimo'] | qualidade['saborosa'], gorjeta['alta'])

#Sistema de controle
sistema_controle = ctrl.ControlSystem([regra01, regra02, regra03])
sistema = ctrl.ControlSystemSimulation(sistema_controle)
sistema.input['qualidade'] = 8.5
sistema.input['servico'] = 6.5

sistema.compute()
print(sistema.output['gorjeta'])
gorjeta.view(sim = sistema)