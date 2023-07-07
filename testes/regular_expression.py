import re #regular expression

#SEARCH
frase1 = 'Olá, meu número é (85)99999-0000'
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase1))

frase2 = "A  placa do carro é ADB-8965"
print(re.search('[A-Z]{3}-\d{4}', frase2))

frase3 = "Entre em contato no e-mail contato@email.com"
print(re.search("\w+@\w+\.com", frase3))



#MATCH - Inicio do texto
frase1 = 'Olá, meu número é (85)99999-0000'
print(re.match('\(\d{2}\)\d{4,5}-\d{4}', frase1)) #NONE

frase2 = "ADB-8965 placa de carro"
print(re.match('[A-Z]{3}-\d{4}', frase2)) #retorna valor


#FIND ALL
frase5 = 'Meu número de telefone atual é (85)96969-0101. O número (85)98988-0202 é o antigo'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase5))
