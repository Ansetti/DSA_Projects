#!/usr/bin/env python
# coding: utf-8

# In[1]:


#jogo da forca
#palavra será definida de acordo com o tema
#será criada uma função para cada tema, que serão: nome, carro ou cidade
import random 
print('Bem vindo ao jogo da Forca de André Setti')


tema =  input("Escolha o tema do jogo entre: nome, carro ou cidade ")
def nome():
    nomes = ['rita','rafael', 'rosana', 'andre','julio','carol']
    palavra = random.choice(nomes)
    quant = len(palavra)
    word = []
    erro = []
    chances = 6
    print('o tema escolhido foi nome')
    print('a palavra tem',quant, 'letras')
    print('tente advinhar a palavra digitando uma letra por vêz, você  terá 6 tentativas')
    for i in range(len(palavra)):
        word.append("_")
    
    print(word)
    while chances>0:
        letra = input('digite sua letra').lower()
        if letra in palavra:
            for i in range(len(palavra)):
                
                if palavra[i] == letra:
                    word[i] = letra
            print(" ".join(word))  
        else:
            chances -= 1
            print('letra errada! Chances restantes',chances)
            
        if chances ==0:
            print('Sinto muito! você PERDEU, a palavra era', palavra)
            break 
    
        if "_" not in word:
            print('PARABÉNS, VOCÊ VENCEU')
            break

def carro():
    carros = ['gol','celta', 'fusion', 'polo','camaro','nivus']
    palavra = random.choice(carros)
    quant = len(palavra)
    word = []
    erro = []
    chances = 6
    print('o tema escolhido foi carros')
    print('a palavra tem',quant, 'letras')
    print('tente advinhar a palavra digitando uma letra por vêz, você  terá 6 tentativas')
    for i in range(len(palavra)):
        word.append("_")
    
    print(word)
    while chances>0:
        letra = input('digite sua letra').lower()
        if letra in palavra:
            for i in range(len(palavra)):
                
                if palavra[i] == letra:
                    word[i] = letra
            print(" ".join(word))  
        else:
            chances -= 1
            print('letra errada! Chances restantes',chances)
            
        if chances ==0:
            print('Sinto muito! você PERDEU, a palavra era', palavra)
            break 
    
        if "_" not in word:
            print('PARABÉNS, VOCÊ VENCEU')
            break

def cidade():
    cidades = ['palmas','salvador', 'curitiba', 'florianopolis','itabuna','vitoria']
    palavra = random.choice(cidades)
    quant = len(palavra)
    word = []
    erro = []
    chances = 6
    print('o tema escolhido foi cidade')
    print('a palavra tem',quant, 'letras')
    print('tente advinhar a palavra digitando uma letra por vêz, você  terá 6 tentativas')
    for i in range(len(palavra)):
        word.append("_")
    
    print(word)
    while chances>0:
        letra = input('digite sua letra').lower()
        if letra in palavra:
            for i in range(len(palavra)):
                
                if palavra[i] == letra:
                    word[i] = letra
            print(" ".join(word))  
        else:
            chances -= 1
            print('letra errada! Chances restantes',chances)
            
        if chances ==0:
            print('Sinto muito! você PERDEU, a palavra era', palavra)
            break 
    
        if "_" not in word:
            print('PARABÉNS, VOCÊ VENCEU')
            break

if tema == ('nome'):
    nome()
elif tema == ('carro'):
    carro()
elif tema == ('cidade'):
    cidade()
else:
    while tema:
        print("digite um tema dos 3 indicados")
        tema =  input("Escolha o tema do jogo entre: nome, carro ou cidade ")
        if tema == ('nome'):
            nome()
        elif tema == ('carro'):
            carro()
        elif tema == ('cidade'):
            cidade()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




