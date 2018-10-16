#!/usr/bin/env python
# coding: utf-8


import random
resposta = [5,4,3,2,1]
lista = random.sample(range(1,8), 5)
pop_inicial = []
pop_fitness = []
pop_tamanho = 10
taxa_mutacao = 0.1
lista
taxa_cross = 0.2
for x in range (0, pop_tamanho):
    pop_inicial.append(random.sample(range(1,8), 5))

    
pop_inicial



def fit(individuo):
    fitness = 0
    i = 0        
    while i < 5:
        if individuo[i] == resposta[i]:
            fitness += 10
        elif individuo[i] in resposta:
            fitness += 1
        i += 1
    return fitness



for individuo in pop_inicial:
    pop_fitness.append(fit(individuo))
pop_fitness


def crossover(indi1, indi2):
    pos = int(random.random()*5)
    return (indi1[:pos]+indi2[pos:], indi2[:pos]+indi1[pos:])



def selecao():
    posicao = int(random.random()*pop_tamanho)
    return pop_inicial[posicao],posicao


for i in range(0, int(pop_tamanho*taxa_cross)):
    pai1, x = selecao()
    pai2, x = selecao()
    a,b = crossover(pai1, pai2)
    pop_inicial.append(a)
    pop_inicial.append(b)


def mutacao(individuo):
    individuo[int(random.random()*5)] = int(random.random()*8)
    return(individuo)


for i in range(0, int(pop_tamanho*taxa_mutacao)):
    print(pop_inicial)
    mutante, x = selecao()
    mutante = mutacao(mutante)
    print(mutante)
    print('')
    pop_inicial[x] = mutante
    print(pop_inicial)


pop_fitness = []
for individuo in pop_inicial:
    pop_fitness.append(fit(individuo))
len(pop_inicial)
ranking = pop_fitness.sort(reverse=True)
for item in ranking:
    



