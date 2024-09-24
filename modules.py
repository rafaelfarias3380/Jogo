"""
Arquivo de Modulos
13/08/2024
De Rafael para professor Berssa
"""

# --> Biblioteca
from random import choice #impota
from time import sleep

# --> Constantes (👁️‍🗨️), Variáveis e Listas
TAM = 50 #Tamanho da tela
CAR = choice(["◙", "▨", "▥", "◧", "◘", "▮"]) #Caracter do desenho
MAR = 4 #Tamanho da margem

# --> Funções
def clrScreen(): #Função para "limpar" a tela
  print("\n"*TAM) #Imprime 77 linhas vazias na tela

def displayLine (): #Função para fazer uma linha de caracteres
  print(CAR*TAM)

def displayMsg(msg): #Motra umas msg alinha a esquerda entre os Caracteres (CAR)
  print(f"{CAR} {msg:<{TAM-MAR}} {CAR}") #Centraliza mensagem

def displayMsgCenter(msg): #define a variavel displayMsgCenter
  print(f"{CAR} {msg:^{TAM-MAR}} {CAR}") #poem as variaveis em seus devidos lugares

def displayHeader(msgs): #define a variavel displayHeader
  displayLine()
  for item in msgs: #ve se tem item em msgs
    displayMsgCenter(item) #se for true, poem o item em displayMsgCenter
  displayLine() #se for false, deixa displayLine vazio

def displayHeaderT(msgs): #define a variavel displayHeader
  displayLine()
  for item in msgs: #ve se tem item em msgs
    displayMsgCenter(item) #se for true, poem o item em displayMsgCenter
    displayLine() #se for false, deixa displayLine vazio
  sleep(1)

def getUserOption(msg):#define a variavel getUserOption
  option = input(f"{CAR} {msg}: ").strip() #Lugar para o usuario por um numero. alem disse, apaga espaços em branco na resposta da resposta
  return option #Retorna a opção pro começo

def validateUserOption(option, listaOptions ): #define as opções de resposta do usuario
  if option in listaOptions: #ve se as opcçoes são compativeis com as opções da lista
    return True #Valida a opção
  else: #vishhhhhh (false)
    msgsErro = ["Erro 734", "Escolha um numero correto ou tente mais tarde."] #define o texto ai na msgsErro
    displayHeader(msgsErro) #printa a msg de erro
    return False #recomeça
    
# --> Main