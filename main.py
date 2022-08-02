'''
Resolva os problemas a seguir:

Mostrar na tela todos os números pares de 0 à 1000

Mostrar na tela todos os números ímpares de 5 à 55

Mostrar na tela somente números primos de 2 à 100;

'''


def mostrar_numeros(tipo, valor_inicial, valor_final):
    if tipo.lower() == 'pares':
        lista = []
        for i in range(valor_inicial, valor_final+1):
            if i % 2 == 0:
                lista.append(i)
        return lista

    if tipo.lower() == 'impares':
        lista = []
        for i in range(valor_inicial, valor_final+1):
            if i % 2 != 0:
                lista.append(i)
        return lista

    if tipo.lower() == 'primos':
        lista = []
        for i in range(valor_inicial, valor_final+1):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    lista.append(i)
        return lista


p = mostrar_numeros('pares', 0, 1000)
print(p)

i = mostrar_numeros('impares', 5, 55)
print(i)

pr = mostrar_numeros('primos', 2, 100)
print(pr)
