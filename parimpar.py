"""
Par ou Ímpar
20/08/2024
De Rafael para professor Berssa
"""

# --> Biblioteca
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption, displayHeaderT #Importa funções do arquivo "modules.py"
from random import randint


# --> Constantes (👁️‍🗨️), Variáveis e Listas
msgsInicio = ["Seja bem vinde ao",
               "Jogo do Par ou Ímpar", 
               "Boa sorte :⟭"] #define a msgsInicio com essa mensagem de bem vindo
msgs = []
playAgain = ""
playerScore = 0
computerScore = 0 

# --> Funções
def startPI(): #define a variavel startPI
  while (True): #confere se o startPI foi startado
    clrScreen() #Limpa a tela
    displayHeader(msgsInicio) #Define o cabeçalho como a msg de inicio q é as boas vindas
    playPI()

    #Funções start
    playAgain = getUserOption("Deseja jogar novamente? (s/n)") #atribui o play again
    while not validateUserOption(playAgain, ["s", "n", "S", "N", "y", "Y"]): #Identificas opções válidas
      playAgain = getUserOption("Deseja jogar novamente (s/n)") #Mostra msg de jogar de novo
    if playAgain.lower() != "s": #se for "s" (true), prossiga com o código. (lower=Transforma a respota do usuario em minusculo)
      break #Quebra o código


def displayMenu():
  msgs = ["Escolha:",
    "[1] ⇛ Ímpar",
    "[2] ⇛ Par"] 
  displayLine()
  for msg in msgs:
    displayMsg(msg)
  displayLine()

def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append(f"Player; {playerScore} --- PC: {computerScore}")
  displayHeaderT(msgs)

def determineWinner(playerChoice, computerChoice):
  play = ""
  result = ""
  choices = ["Par", "Ímpar"]
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  soma = playerChoice + computerChoice
  if soma % 2 == int(playerChoice == 2):
    result = "Você ganhou!!!"
  else:
    result = "Você perdeu!!!"

  displayHeaderT(msgs)
  return result

def playPI():
  playerScore = 0
  computerScore = 0 
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption("Sua escolha")
    while not validateUserOption(playerChoice, ["1", "2"]):
      displayMenu()
      playerChoice = getUserOption("Sua escolha")
    computerChoice = str(randint(0,9))
    result = determineWinner(playerChoice, computerChoice)
    if "ganhou" in result:
      playerScore += 1
    elif "perdeu" in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore("PLACAR", playerScore, computerScore)
  displayScore("PLACAR FINAL", playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(["Bravo! 🥀 ",
                  "Você ganhou"])
  else:
     displayHeader(["Você perdeu"])

# --> Main