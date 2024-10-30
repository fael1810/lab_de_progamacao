ATIVIDADE 23

a) ent = input('escreva uma lista de numeros inteiros separados por uma virgula: ')

numeros = [int(num) for num in ent.split(",")]

soma = sum(numeros)

print('a soma da lista é', soma)

b) ent = input('escreva uma lista de numeros inteiros separados por uma virgula: ')

numeros = [int(num) for num in ent.split(",")]

numeros_pares = [num for num in numeros if num % 2 == 0]

print('os numeros pares da lista é: ', numeros_pares)

c) ent = input('escreva uma lista de numeros inteiros separados por uma virgula: ')

numeros = [int(num) for num in ent.split(",")]

maior_num = (max(numeros))

menor_num = (min(numeros))

print('O maior numero da lista é o: ', maior_num, '\nO menor numero da lista é o: ', menor_num)

d) ent = input('escreva uma lista de numeros inteiros, contendo alguns elementos repetidos, todos separados por uma virgula: ')

numeros = [int(num) for num in ent.split(",")]

numeros_semdupl = [list(set(numeros))]

print('lista sem elementos duplicados: ', numeros_semdupl)

e)
