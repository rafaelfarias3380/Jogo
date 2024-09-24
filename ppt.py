"""
pedra, papel e tesoura
13/08/2024
De Rafael para professor Berssa
"""

# --> Biblioteca
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption, displayHeaderT #Importa funções do arquivo "modules.py"
from random import randint


# --> Constantes (👁️‍🗨️), Variáveis e Listas
msgsInicio = ["Seja bem vinde ao",
               "Jogo do PEDRA-PAPEL-TESOURA", 
               "Boa sorte :⟭"] #define a msgsInicio com essa mensagem de bem vindo
msgs = []
playAgain = ""
playerScore = 0
computerScore = 0 
               
# --> Funções
def startPPT(): #define a variavel startPPT
  while (True): #confere se o startPPT foi startado
    clrScreen() #Limpa a tela
    displayHeader(msgsInicio) #Define o cabeçalho como a msg de inicio q é as boas vindas
    playPPT()
    
    #Funções start
    playAgain = getUserOption("Deseja jogar novamente? (s/n)") #atribui o play again
    while not validateUserOption(playAgain, ["s", "n", "S", "N", "y", "Y"]): #Identificas opções válidas
      playAgain = getUserOption("Deseja jogar novamente (s/n)") #Mostra msg de jogar de novo
    if playAgain.lower() != "s": #se for "s" (true), prossiga com o código. (lower=Transforma a respota do usuario em minusculo)
      break #Quebra o código


def displayMenu():
  msgs = ["Escolha:",
    "[0] ⇛ Pedra",
    "[1] ⇛ Pepel",
    "[2] ⇛ Tesoura"] 
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
  choices = ["Pedra", "Papel", "Tesoura"]
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  if playerChoice == computerChoice:
    result = "Empate!"
  elif (playerChoice == "0" and computerChoice == "2") or \
       (playerChoice == "1" and computerChoice == "0") or \
       (playerChoice == "2" and computerChoice == "1"):
    play = f"{playerChoiceStr} vence {computerChoiceStr}"
    result = "Você ganhou!!!"
  else:
    play = f"{computerChoiceStr} vence {playerChoiceStr}"
    result = "Você perdeu!!!"
  msgs = ["Jogada do Player: " + playerChoiceStr,
          "Jogada do PC: " + computerChoiceStr,
         play, result]

  displayHeaderT(msgs)
  return result
  
def playPPT():
  playerScore = 0
  computerScore = 0 
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption("Sua escolha")
    while not validateUserOption(playerChoice, ["0", "1", "2"]):
      displayMenu()
      playerChoice = getUserOption("Sua escolha")
    computerChoice = str(randint(0,2))
    result = determineWinner(playerChoice, computerChoice)
    if "ganhou" in result:
      playerScore += 1
    elif "perdeu" in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore("PLACAR", playerScore, computerScore)
  displayScore("PLACAR FINAL", playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(["Bravo! 🥀",
                  "Você ganhou"])
  else:
     displayHeader(["Você perdeu"])
    
# --> Main